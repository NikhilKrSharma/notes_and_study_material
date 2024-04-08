from PyPDF2 import PdfReader, PdfWriter

def add_blank_pages(input_pdf_path, output_pdf_path):
    with open(input_pdf_path, "rb") as input_file:
        reader = PdfReader(input_file)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)
            blank_page = writer.add_blank_page()
            blank_page.merge_page(page)

        with open(output_pdf_path, "wb") as output_file:
            writer.write(output_file)


# Example usage:
input_pdf_path = '/Users/nikhil20.sharma/Downloads/cs224n-self-attention-transformers-2023_draft.pdf'  # Provide the path to your input PDF file
output_pdf_path = '/Users/nikhil20.sharma/Downloads/cs224n-self-attention-transformers-2023_draft_mod.pdf'  # Provide the desired path for the modified PDF file
add_blank_pages(input_pdf_path, output_pdf_path)
