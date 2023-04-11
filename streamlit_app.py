def merge_pdf (pdfFiles):
    merger = PdfFileMerger()
    
    for file in pdfFiles: 
        merger.append(file, 'rb')
        
    _byteIo = BytesIO()
    merger.write(_byteIo)    
    _byteIo.seek(0)
    
    return _byteIo
