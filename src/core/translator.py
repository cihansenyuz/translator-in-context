from typing import List
import ollama

class Translator:
    def __init__(self):
        self.m_model = "mistral"
        self.m_ollama = ollama

    def translate(self, text: str, context_prompt: str) -> str:
        """
        Translate text using the local LLM with given context
        
        Args:
            text: Text to translate
            context_prompt: Context information for translation
            
        Returns:
            str: Translated text
        """
        # Construct the prompt
        prompt = f"""Context: {context_prompt}
        
Translate the following text to English keeping the provided context in mind.
Do not add any additional information, explanations and comment.:

{text}

Translation:"""

        try:
            response = self.m_ollama.generate(model=self.m_model, prompt=prompt)
            return response['response'].strip()
        except Exception as e:
            raise Exception(f"Translation failed: {str(e)}")
