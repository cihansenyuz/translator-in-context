# Translator-in-Context

## Project Overview
A desktop application that allows users to translate text while considering specific context, powered by the Mixtral LLM running locally through Ollama.

### Primary Goals
- Context-aware translation using local LLM execution
- User-friendly interface for text translation
- Support for multiple context combinations

## Technology Stack
- Programming Language: Python
- GUI Framework: PyQt6
- LLM: Gemma
- LLM Runtime: Ollama
- Development Pattern: Desktop Application

## Prerequisites
- Python 3.x
- Ollama installed with Gemma model
- PyQt6 (for GUI version)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/translator-in-context.git
cd translator-in-context
```

2. Create and activate virtual environment:
```bash
sudo apt install python3.12-venv
python3 -m venv .venv
source .venv/bin/activate
```

3. Install required packages in the virtual environment:
```bash
pip install -r requirements.txt
```

4. Install Ollama:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
Then restart the terminal. Activate again virtual environment.

Download the model and test it:
```bash
ollama pull gemma
ollama run gemma
```

Use it in Python:
```bash
pip install ollama
```

## Development
Always make sure to activate the virtual environment before running the project:
```bash
source .venv/bin/activate
```

Ensure that the Ollama backend is running:
```bash
ollama serve
```

To deactivate when you're done:
```bash
deactivate
```

## Usage

### CLI Mode
```bash
# Basic translation with default context
python main.py --text "Text to translate"

# Translation with specific context
python main.py --text "Text to translate" --context chinese-partners

# Save translation to file
python main.py --text "Text to translate" --context formal --output translation.txt
```

### Available Context Options
- european-partners: formal and suitable for communication with European
- chinese-partners: clear and culturally appropriate

## Project Structure
```
translator-in-context/
├── docs/           # Documentation files
├── src/
│   ├── core/      # Core functionality
│   └── gui/       # GUI components (Phase 2)
├── main.py        # CLI entry point
└── requirements.txt
```

## Future Features
- GUI interface with PyQt6
- Custom context definition
- Translation history management
- Context templates
