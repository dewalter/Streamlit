import streamlit as st
import PyPDF2

def split_pdf(input_file, start_page, end_page):
    """
    Splits a PDF file into a new file containing the specified pages.
    """
    # Open the input PDF file
    with open(input_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        # Create a new PDF writer object
        pdf_writer = PyPDF2.PdfFileWriter()
        # Add the specified pages to the new PDF
        for i in range(start_page - 1, end_page):
            pdf_writer.addPage(pdf_reader.getPage(i))
        # Create a new file for the output PDF
        output_file = f"{input_file.split('.pdf')[0]}_{start_page}-{end_page}.pdf"
        with open(output_file, 'wb') as out_f:
            pdf_writer.write(out_f)
    st.success(f"PDF successfully split into {output_file}")

def combine_pdfs(input_files):
    """
    Combines multiple PDF files into a single file.
    """
    # Create a new PDF writer object
    pdf_writer = PyPDF2.PdfFileWriter()
    # Loop through the input files and add each page to the new PDF
    for file in input_files:
        with open(file, 'rb') as f:
            pdf_reader = PyPDF2.PdfFileReader(f)
            for i in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(i))
    # Create a new file for the output PDF
    output_file = "combined.pdf"
    with open(output_file, 'wb') as out_f:
        pdf_writer.write(out_f)
    st.success(f"PDF files successfully combined into {output_file}")

def downsample_pdf(input_file, resolution):
    """
    Downsamples a PDF file to the specified resolution.
    """
    # Open the input PDF file
    with open(input_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        # Create a new PDF writer object
        pdf_writer = PyPDF2.PdfFileWriter()
        # Loop through each page in the input PDF and downsample it
        for i in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(i)
            page.scaleBy(resolution / 72)
            pdf_writer.addPage(page)
        # Create a new file for the output PDF
        output_file = f"{input_file.split('.pdf')[0]}_{resolution}dpi.pdf"
        with open(output_file, 'wb') as out_f:
            pdf_writer.write(out_f)
    st.success(f"PDF successfully downsampled to {resolution}dpi and saved as {output_file}")

# Define the Streamlit app
st.title("PDF Operations")

# Define the operation to perform
operation = st.selectbox("Select an operation", ["Split", "Combine", "Downsample"])

# Split PDF operation
if operation == "Split":
    input_file = st.file_uploader("Upload a PDF file", type="pdf")
    if input_file is not None:
        start_page = st.number_input("Enter the start page", min_value=1)
        end_page = st.number_input("Enter the end page", min_value=start_page, max_value=PyPDF2.PdfFileReader(input_file).getNumPages())
        if st.button("Split PDF"):
            split
