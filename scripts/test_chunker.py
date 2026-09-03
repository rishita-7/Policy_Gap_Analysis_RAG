from src.ingestion.document_loader import load_pdf
from src.ingestion.chunker import create_chunks


PDF_PATH = "data/raw/framework/nist_csf_2.0.pdf"


pages = load_pdf(PDF_PATH)

chunks = create_chunks(pages)


print(f"Total pages: {len(pages)}")
print(f"Total chunks: {len(chunks)}")


print("\n--- Sample CHUNKS ---")

for chunk in chunks[:106:26]:

    print("\n==============================")
    print("CHUNK ID:", chunk["metadata"]["chunk_id"])
    print("PAGES:", chunk["metadata"]["pages"])
    print("==============================")

    print(chunk["text"])