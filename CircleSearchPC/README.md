# CircleSearchPC

## Description

CircleSearchPC is a desktop application that allows users to perform quick searches and other actions using a configurable hotkey. It integrates AI and translation features to enhance productivity. The application uses OCR to capture text from the screen, making it a versatile tool for various tasks.

## Features

*   **Hotkey-activated Searching:** Press a configurable hotkey (`ctrl+alt+s` by default) to initiate a search.
*   **AI Integration:** Leverage AI models like Gemini or OpenAI for advanced search capabilities.
*   **Translation:** On-the-fly text translation.
*   **OCR Support:** Uses Tesseract OCR to extract text from images or screen captures.
*   **Configurable:** Easily configure features and settings through the `config.py` file.

## Tech Stack

*   **Backend:** Python
*   **OCR Engine:** Tesseract

## Directory Structure

```
CircleSearchPC/
├── assets/
├── config.py
└── README.md
```

## Configuration

The main configuration is done in the `config.py` file:

*   `HOTKEY`: The key combination to trigger the application. Default: `"ctrl+alt+s"`
*   `LANGUAGE`: The language for translation and other features. Default: `"en"`
*   `USE_AI`: Enable or disable AI features. Default: `True`
*   `USE_TRANSLATE`: Enable or disable translation features. Default: `True`
*   `AI_MODEL`: Choose the AI model to use (`"gemini"` or `"openai"`). Default: `"gemini"`
*   `TESSERACT_PATH`: The installation path for Tesseract OCR. Default: `"C:/Program Files/Tesseract-OCR/tesseract.exe"`

## Future Features

*   Support for more AI models.
*   Customizable UI themes.
*   Plugin system for additional functionality.
*   Expanded language support.