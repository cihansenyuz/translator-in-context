from typing import List

class ContextManager:
    def __init__(self):
        self.m_context_templates = {
            'european-partners': """This is a translation task of a service bulletin about television software.
        - Do not use software terms heavily, be simple and clear for non-technical person.
        - The translation should be formal and suitable for communication with European Balkan partners.""",
            'chinese-partners': """This is a translation task of an email about television software project.
        - Use software terms properly even if it is not used in the text, be clear for technical person.
        - The translation should be culturally appropriate for Chinese partners.
        - Do not add any additional explanations and comment"""
        }
        self.default_context = """- Two capital letters in the text indicates the mainboard project name."
        - Alpha, Beta, Charlie, Delta and Echo are the cabinet names.
        - In Turkish, the mainboard is also reffered as şasi or şase.
        - In Turkish, USB refers to "USB bellek" or "USB flash bellek", not just "USB".
        - "servisler" or "servis" may mean "technical service personal".
        - "cell", "OC" refers to an opencell component of the panel of the television.
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
