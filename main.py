#!/usr/bin/env python3

from src.core import Translator, ContextManager
#from src.core import FileHandler
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Translate text with context using local LLM')
    parser.add_argument('--text', '-t', type=str, help='Text to translate')
    parser.add_argument('--context', '-c', type=str, nargs='+', 
                       choices=['european-partners', 'chinese-partners'],
                       help='Context for translation')
    parser.add_argument('--output', '-o', type=str, help='Output file path')

    args = parser.parse_args()
    text = args.text

    # Initialize components
    context_manager = ContextManager()
    translator = Translator()
    #file_handler = FileHandler()

    if not text:
        print("No text provided. Use --text or -t")
        sys.exit(1)

    # Process context
    if not args.context:
        context = ['european-partners']
    else:
        context = args.context

    try:
        # Apply context and get translation
        context_prompt = context_manager.getContextPrompt(context)
        translation = translator.translate(text, context_prompt)

        # Handle output
        '''if args.output:
            file_handler.saveTranslation(translation, args.output)
            print(f"Translation saved to {args.output}")
        else:'''
        print("\nTranslation:")
        print("-----------")
        print(translation)

    except Exception as e:
        print(f"Error during translation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
