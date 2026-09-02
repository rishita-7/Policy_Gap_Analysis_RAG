from src.ingestion.document_loader import load_pdf


PDF_PATH = "data/raw/framework/nist_csf_2.0.pdf"


pages = load_pdf(PDF_PATH)

print(f"Total pages extracted: {len(pages)}")

print("\n--- FIRST PAGE ---")
print(pages[0]["text"][:1000])

print("\n--- METADATA ---")
print(pages[0]["metadata"])