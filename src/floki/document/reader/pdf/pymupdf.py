from floki.document.reader.base import ReaderBase
from floki.types.document import Document
from typing import List
from pathlib import Path

class PyMuPDFReader(ReaderBase):
    """
    Reader for PDF documents using PyMuPDF.
    """

    def load(self, file_path: Path) -> List[Document]:
        """
        Load content from a PDF file using PyMuPDF.

        Args:
            file_path (Path): Path to the PDF file.

        Returns:
            List[Document]: A list of Document objects.
        """
        try:
            import pymupdf
        except ImportError:
            raise ImportError(
                "PyMuPDF library is not installed. Install it using `pip install pymupdf`."
            )

        file_path = str(file_path)
        doc = pymupdf.open(file_path)
        total_pages = len(doc)
        documents = []

        for page_num, page in enumerate(doc.pages):
            text = page.get_text()
            metadata = {
                "file_path": file_path,
                "page_number": page_num + 1,
                "total_pages": total_pages,
            }
            documents.append(Document(text=text.strip(), metadata=metadata))

        doc.close()
        return documents