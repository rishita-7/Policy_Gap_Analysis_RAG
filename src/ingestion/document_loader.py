import fitz


def load_pdf(file_path):
    document = fitz.open(file_path)

    pages = []

    for page_number, page in enumerate(document):

        text = page.get_text("text")

        if text.strip():

            pages.append({
                "text": text,
                "metadata": {
                    "source": file_path,
                    "page": page_number + 1
                }
            })

    document.close()

    return pages