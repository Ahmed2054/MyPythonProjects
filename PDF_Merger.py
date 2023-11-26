import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel
import fitz  # PyMuPDF library for working with PDF files

class PDFMerger(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PDF Merger')

        self.layout = QVBoxLayout()

        self.label = QLabel('Select PDF files to merge:')
        self.layout.addWidget(self.label)

        self.merge_button = QPushButton('Merge PDFs')
        self.merge_button.clicked.connect(self.merge_pdfs)
        self.layout.addWidget(self.merge_button)

        self.setLayout(self.layout)

    def merge_pdfs(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter('PDF Files (*.pdf)')

        if file_dialog.exec_():
            files = file_dialog.selectedFiles()
            output_file, _ = QFileDialog.getSaveFileName(self, 'Save Merged PDF', '', 'PDF Files (*.pdf)')

            if output_file:
                self.merge_files(files, output_file)
                self.label.setText('PDFs merged successfully!')

    def merge_files(self, input_files, output_file):
        merger = fitz.open()

        for file in input_files:
            pdf = fitz.open(file)
            merger.insert_pdf(pdf)

        merger.save(output_file)
        merger.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pdf_merger = PDFMerger()
    pdf_merger.show()
    sys.exit(app.exec_())

