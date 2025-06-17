from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel

class TranslateProgressDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Çeviri")
        self.setModal(True)
        layout = QVBoxLayout()
        label = QLabel("Çeviri yapılıyor...")
        layout.addWidget(label)
        self.setLayout(layout)
        self.setFixedSize(200, 50)
