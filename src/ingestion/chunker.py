import re


FUNCTION_REGEX = re.compile(
    r"^(GOVERN|IDENTIFY|PROTECT|DETECT|RESPOND|RECOVER)\s+\(([A-Z]{2})\):"
)

CATEGORY_REGEX = re.compile(
    r"^•\s*(.*?)\s+\(([A-Z]{2}\.[A-Z]{2})\):"
)

SUBCATEGORY_REGEX = re.compile(
    r"^o\s*([A-Z]{2}\.[A-Z]{2}-\d{2}):\s*(.*)"
)


def clean_line(line):
    """
    Clean a line extracted from the PDF.
    """

    line = line.strip()

    # Remove common PDF bullet characters
    line = line.replace("• ", "• ")
    line = line.replace("o ", "o ", 1)

    return line


def create_chunks(pages):
    """
    Create structure-aware chunks for the NIST CSF 2.0 Core.

    Each Subcategory becomes one semantic chunk while preserving
    Function, Category, Subcategory, and page metadata.
    """

    chunks = []

    current_function = None
    current_function_id = None

    current_category = None
    current_category_id = None

    current_subcategory = None
    current_subcategory_text = ""
    current_pages = []

    source = pages[0]["metadata"]["source"] if pages else None

    def save_subcategory():
        """
        Save the currently accumulated Subcategory.
        """

        if not current_subcategory:
            return

        chunks.append({
            "text": current_subcategory_text.strip(),

            "metadata": {
                "source": source,
                "pages": current_pages.copy(),

                "framework": "NIST CSF 2.0",

                "function": current_function,
                "function_id": current_function_id,

                "category": current_category,
                "category_id": current_category_id,

                "subcategory_id": current_subcategory,

                "chunk_id": len(chunks)
            }
        })

    for page in pages:

        page_number = page["metadata"]["page"]

        for raw_line in page["text"].splitlines():

            line = clean_line(raw_line)

            if not line:
                continue

            # -----------------------------------------
            # Detect Function
            # -----------------------------------------

            function_match = FUNCTION_REGEX.match(line)

            if function_match:

                save_subcategory()

                current_subcategory = None
                current_subcategory_text = ""
                current_pages = []

                current_function = function_match.group(1)
                current_function_id = function_match.group(2)

                current_category = None
                current_category_id = None

                continue

            # -----------------------------------------
            # Detect Category
            # -----------------------------------------

            category_match = CATEGORY_REGEX.match(line)

            if category_match:

                save_subcategory()

                current_subcategory = None
                current_subcategory_text = ""
                current_pages = []

                current_category = category_match.group(1)
                current_category_id = category_match.group(2)

                continue

            # -----------------------------------------
            # Detect Subcategory
            # -----------------------------------------

            subcategory_match = SUBCATEGORY_REGEX.match(line)

            if subcategory_match:

                save_subcategory()

                current_subcategory = subcategory_match.group(1)

                current_subcategory_text = (
                    f"{current_subcategory}: "
                    f"{subcategory_match.group(2)}"
                )

                current_pages = [page_number]

                continue

            # -----------------------------------------
            # Continue Subcategory text
            # -----------------------------------------

            if current_subcategory:

                current_subcategory_text += " " + line

                if page_number not in current_pages:
                    current_pages.append(page_number)

    # Save final subcategory
    save_subcategory()

    return chunks