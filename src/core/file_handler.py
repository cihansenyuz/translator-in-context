class FileHandler:
    def saveTranslation(self, translation: str, filepath: str) -> None:
        """
        Save translation to a file
        
        Args:
            translation: Translated text
            filepath: Path to save the file
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(translation)
        except Exception as e:
            raise Exception(f"Failed to save translation: {str(e)}")
