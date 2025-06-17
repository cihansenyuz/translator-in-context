from PyQt6.QtCore import QObject, pyqtSignal
from src.core import Translator, ContextManager
import threading

class TranslationService(QObject):
    translation_ready = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.translator = Translator()
        self.context_manager = ContextManager()
        
    def translate_with_context(self, text: str, context_type: str):
        """
        Initiates translation in a separate thread
        """
        context_map = {
            "İngilizce Bülten": "european-partners",
            "Outsource Yazışma": "chinese-partners"
        }
        context = [context_map[context_type]]
        
        try:
            context_prompt = self.context_manager.getContextPrompt(context)
            threading.Thread(
                target=self._do_translate,
                args=(text, context_prompt),
                daemon=True
            ).start()
        except Exception as e:
            self.translation_ready.emit(f"Çeviri Hatası: {e}")
            
    def _do_translate(self, text: str, context_prompt: str):
        """
        Performs the actual translation
        """
        try:
            translation = self.translator.translate(text, context_prompt)
            self.translation_ready.emit(translation)
        except Exception as e:
            self.translation_ready.emit(f"Çeviri Hatası: {e}")
