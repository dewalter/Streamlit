import io
import os
import streamlit as st
import PyPDF2

st.title("PDF Compressor")

# Allow user to upload a PDF file
uploaded_file = st.file_uploader("Choose a PDF file to compress", type=["pdf"])

if uploaded_file is not None:
    # Load PDF file into PyPDF2
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    # Create an empty output PDF file
    output_pdf = PyPDF2.PdfWriter()

    # Loop over each page in the input PDF file
    for page_num in range(pdf_reader.numPages):
        # Get the current page and its contents
        page = pdf_reader.pages[page_num]
        content = io.BytesIO()

        # Compress the page and write it to the output PDF file
        page.compress()
        output_pdf.addPage(page)

    # Create a temporary file to hold the compressed PDF
    temp_file = io.BytesIO()
    output_pdf.write(temp_file)

    # Display download link for compressed PDF
    st.download_button(
        label="Download Compressed PDF",
        data=temp_file.getvalue(),
        file_name=os.path.splitext(uploaded_file.name)[0] + "_compressed.pdf",
        mime="application/pdf",
    )
