#!/usr/bin/env python3

from src.core import Translator, ContextManager
#from src.core import FileHandler
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Translate text with context using local LLM')
    parser.add_argument('--text', '-t', type=str, help='Text to translate')
    parser.add_argument('--context', '-c', type=str, nargs='+', 
                       choices=['technical', 'casual'],
                       help='Context for translation')
    parser.add_argument('--output', '-o', type=str, help='Output file path')
    parser.add_argument('--clipboard', action='store_true', 
                       help='Use text from clipboard')

    args = parser.parse_args()

    # Initialize components
    context_manager = ContextManager()
    translator = Translator()
    #file_handler = FileHandler()

    # Get text from clipboard if specified
    if args.clipboard:
        try:
            import pyperclip
            text = pyperclip.paste()
        except Exception as e:
            print(f"Error reading from clipboard: {e}")
            sys.exit(1)
    else:
        text = args.text

    if not text:
        print("No text provided. Use --text or --clipboard option.")
        sys.exit(1)

    # Process context
    if not args.context:
        print("No context provided. Using default context.")
        context = ['casual']
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
