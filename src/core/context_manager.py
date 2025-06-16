from typing import List

class ContextManager:
    def __init__(self):
        self.m_context_templates = {
            'technical': "The translation should maintain technical terminology and professional tone.",
            'casual': "The translation should be conversational and friendly."
        }

    def getContextPrompt(self, contexts: List[str]) -> str:
        """
        Generate a context prompt based on selected contexts
        
        Args:
            contexts: List of context identifiers
            
        Returns:
            str: Combined context prompt
        """
        prompts = [self.m_context_templates[ctx] for ctx in contexts if ctx in self.m_context_templates]
        return " ".join(prompts)
