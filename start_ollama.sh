#!/bin/bash

OLLAMA_PATH="$HOME/Downloads/Ollama.app/Contents/Resources/ollama"

if [ ! -f "$OLLAMA_PATH" ]; then
    echo "Error: Ollama not found at $OLLAMA_PATH"
    exit 1
fi

if ! pgrep -f "ollama serve" > /dev/null; then
    echo "Starting Ollama server..."
    "$OLLAMA_PATH" serve > /dev/null 2>&1 &
    sleep 2
    echo "Ollama server started!"
else
    echo "Ollama server is already running"
fi

echo "Available models:"
"$OLLAMA_PATH" list

echo ""
echo "You can now run: python3 main.py"

