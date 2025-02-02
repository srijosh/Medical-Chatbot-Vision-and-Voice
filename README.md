# Medical Chatbot Vision and Voice

This repository contains an **AI-powered Medical Chatbot** that processes **speech and images** to assist with medical inquiries. The chatbot leverages **Groq for text analysis, ElevenLabs for speech synthesis, and Gradio for an interactive UI**. It can transcribe audio, analyze medical images, and respond with AI-generated medical insights.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Tools and Technologies](#tools-and-technologies)

## Introduction

The **Medical-Chatbot_Vision-and-Voice** is designed to provide AI-powered **medical assistance** through speech and image analysis. Users can **speak their symptoms**, upload **medical images**, and receive AI-generated responses in **text and speech format**.

## Features

- **Audio Capture**: Captures user audio using `speech_recognition` or `Gradio Microphone Input`.
- **Speech-to-Text**: Converts user speech into text using **Whisper-large-v3**.
- **Image Analysis**: Processes medical images to provide AI-generated insights.
- **AI-Powered Responses**: Uses **Groq** for generating responses based on text and image inputs.
- **Text-to-Speech (TTS)**: Converts AI responses into speech using **ElevenLabs**.
- **Interactive Gradio Interface**: Provides a seamless web-based UI.

## Installation

1. Clone the repository to your local machine:

```
   git clone https://github.com/srijosh/Medical-Chatbot-Vision-and-Voice.git
```

2. Navigate to the project directory:

```
   cd Medical-Chatbot-Vision-and-Voice
```

3. Install the required dependencies:

```
   pip install -r requirements.txt
```

4. Set up environment variables by creating a .env file (Use .env.sample as a reference for setting up your .env file.)

## Usage

1. Run the Gradio interface:

```
   python gradio_app.py

```

### How It Works:

- Speak into the microphone: The chatbot transcribes and processes your query.
- Upload a medical image (X-ray, MRI, etc.): The AI analyzes it.
- AI Doctor Response: Get an AI-generated medical response.
- Text-to-Speech Output: Hear the AI’s response as speech.

## Tools and Technologies

- **Groq API**: AI-based text and image analysis.
- **ElevenLabs**: Text-to-speech synthesis for generating realistic voice responses.
- **Gradio**: Web-based UI for user interaction.
