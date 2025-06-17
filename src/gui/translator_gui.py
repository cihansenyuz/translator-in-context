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

        self.input_label = QLabel("Text to translate:")
        layout.addWidget(self.input_label)

        self.input_text = QTextEdit()
        layout.addWidget(self.input_text)

        self.context_label = QLabel("Select context:")
        layout.addWidget(self.context_label)

        self.context_combo = QComboBox()
        self.context_combo.addItems(["european-partners", "chinese-partners"])
        layout.addWidget(self.context_combo)

        self.translate_button = QPushButton("Translate")
        self.translate_button.clicked.connect(self.onTranslate)
        layout.addWidget(self.translate_button)

        self.output_label = QLabel("Translation:")
        layout.addWidget(self.output_label)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        self.save_button = QPushButton("Save Translation")
        self.save_button.clicked.connect(self.onSave)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def onTranslate(self):
        text = self.input_text.toPlainText().strip()
        context = [self.context_combo.currentText()]
        if not text:
            QMessageBox.warning(self, "Input Required", "Please enter text to translate.")
            return
        try:
            context_prompt = self.m_context_manager.getContextPrompt(context)
            translation = self.m_translator.translate(text, context_prompt)
            self.output_text.setPlainText(translation)
        except Exception as e:
            QMessageBox.critical(self, "Translation Error", str(e))

    def onSave(self):
        translation = self.output_text.toPlainText().strip()
        if not translation:
            QMessageBox.warning(self, "No Translation", "There is no translation to save.")
            return
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Translation", "translation.txt", "Text Files (*.txt)")
        if file_path:
            try:
                self.m_file_handler.saveTranslation(translation, file_path)
                QMessageBox.information(self, "Saved", f"Translation saved to {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Save Error", str(e))

def run_gui():
    app = QApplication(sys.argv)
    window = TranslatorGUI()
    window.show()
    sys.exit(app.exec())
