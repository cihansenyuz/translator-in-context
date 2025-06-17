from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QComboBox, QFileDialog, QMessageBox
from PyQt6.QtCore import Qt
from src.core import Translator, ContextManager, FileHandler
import sys

class TranslatorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Translator in Context")
        self.setMinimumWidth(500)
        self.m_translator = Translator()
        self.m_context_manager = ContextManager()
        self.m_file_handler = FileHandler()
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
        self.context_combo.addItems(["Avrupa Ortakları", "Çinli Ortaklar"])
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
        context_map = {
            "Avrupa Ortakları": "european-partners",
            "Çinli Ortaklar": "chinese-partners"
        }
        context = [context_map[self.context_combo.currentText()]]
        if not text:
            QMessageBox.warning(self, "Girdi Gerekli", "Lütfen çevrilecek metni girin.")
            return
        try:
            context_prompt = self.m_context_manager.getContextPrompt(context)
            translation = self.m_translator.translate(text, context_prompt)
            self.output_text.setPlainText(translation)
        except Exception as e:
            QMessageBox.critical(self, "Çeviri Hatası", str(e))

    def onSave(self):
        translation = self.output_text.toPlainText().strip()
        if not translation:
            QMessageBox.warning(self, "Çeviri Yok", "Kaydedilecek bir çeviri yok.")
            return
        file_path, _ = QFileDialog.getSaveFileName(self, "Çeviriyi Kaydet", "ceviri.txt", "Metin Dosyaları (*.txt)")
        if file_path:
            try:
                self.m_file_handler.saveTranslation(translation, file_path)
                QMessageBox.information(self, "Kaydedildi", f"Çeviri {file_path} dosyasına kaydedildi.")
            except Exception as e:
                QMessageBox.critical(self, "Kaydetme Hatası", str(e))

def run_gui():
    app = QApplication(sys.argv)
    window = TranslatorGUI()
    window.show()
    sys.exit(app.exec())
