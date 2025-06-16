from typing import List

class ContextManager:
    def __init__(self):
        self.m_context_templates = {
            'european-partners': "The translation should be formal and suitable for communication with European Balkan partners.",
            'chinese-partners': "The translation should be clear and culturally appropriate for Chinese partners."
        }
        self.default_context = """- This is a translation task of a Turkish service bulletin about television software.
        - Do not use software terms heavily, be simple and clear for non-technical person.
        - Two capital letters in the text indicates the mainboard project name. In Turkish, they are also reffered as şasi/şase"
        - Alpha, Beta, Charlie, Delta and Echo are the cabinet names.
        -"""

    def getContextPrompt(self, contexts: List[str]) -> str:
        """
        Generate a context prompt based on selected contexts
        
        Args:
            contexts: List of context identifiers
            
        Returns:
            str: Combined context prompt
        """
        prompts = [self.m_context_templates[ctx] for ctx in contexts if ctx in self.m_context_templates]
        return f"{self.default_context} {' '.join(prompts)}"
