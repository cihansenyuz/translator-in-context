from PyQt6.QtWidgets import QFileDialog, QMessageBox
from src.core import FileHandler

class FileOperations:
    def __init__(self):
        self.file_handler = FileHandler()
        
    def save_translation(self, parent, translation: str) -> bool:
        """
        Handles the file saving operation with proper error handling
        """
        if not translation.strip():
            QMessageBox.warning(parent, "Çeviri Yok", "Kaydedilecek bir çeviri yok.")
            return False
            
        file_path, _ = QFileDialog.getSaveFileName(
            parent,
            "Çeviriyi Kaydet",
            "ceviri.txt",
            "Metin Dosyaları (*.txt)"
        )
        
        if not file_path:
            return False
            
        try:
            self.file_handler.saveTranslation(translation, file_path)
            QMessageBox.information(
                parent,
                "Kaydedildi",
                f"Çeviri {file_path} dosyasına kaydedildi."
            )
            return True
        except Exception as e:
            QMessageBox.critical(parent, "Kaydetme Hatası", str(e))
            return False
