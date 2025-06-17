from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, 
                            QPushButton, QComboBox, QMessageBox)
from PyQt6.QtCore import Qt
from src.gui.progress_dialog import TranslateProgressDialog
from src.gui.translation_service import TranslationService
from src.gui.file_operations import FileOperations
import sys

class TranslatorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Translator in Context")
        self.setMinimumWidth(500)
        
        # Initialize services
        self.translation_service = TranslationService()
        self.file_operations = FileOperations()
        self.progress_dialog = None
        
        # Connect signals
        self.translation_service.translation_ready.connect(self.onTranslationComplete)
        
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.input_label = QLabel("Çevrilecek Metin:")
        layout.addWidget(self.input_label)

        self.input_text = QTextEdit()
        layout.addWidget(self.input_text)

        self.context_label = QLabel("Bağlam Seçin:")
        layout.addWidget(self.context_label)

        self.context_combo = QComboBox()
        self.context_combo.addItems(["İngilizce Bülten", "Outsource Yazışma"])
        layout.addWidget(self.context_combo)

        self.translate_button = QPushButton("Çevir")
        self.translate_button.clicked.connect(self.onTranslate)
        layout.addWidget(self.translate_button)

        self.output_label = QLabel("Çeviri:")
        layout.addWidget(self.output_label)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        self.save_button = QPushButton("Çeviriyi Kaydet")
        self.save_button.clicked.connect(self.onSave)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def onTranslate(self):
        text = self.input_text.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, "Girdi Gerekli", "Lütfen çevrilecek metni girin.")
            return

        self.progress_dialog = TranslateProgressDialog(self)
        self.progress_dialog.show()
        
        self.translation_service.translate_with_context(
            text,
            self.context_combo.currentText()
        )

    def onTranslationComplete(self, translation):
        if self.progress_dialog:
            self.progress_dialog.close()
        self.output_text.setPlainText(translation)

    def onSave(self):
        self.file_operations.save_translation(
            self,
            self.output_text.toPlainText()
        )

def run_gui():
    app = QApplication(sys.argv)
    window = TranslatorGUI()
    window.show()
    sys.exit(app.exec())
