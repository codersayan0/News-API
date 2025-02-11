# Voice-Activated News Summarizer

This project allows you to get news articles related to a topic through **voice input** and hear the summarized headlines and descriptions through **voice output**. It fetches the latest news using the **NewsAPI** and generates basic summaries by truncating the article descriptions.

## Features
- **Voice Input:** Speak the topic you want news about (e.g., "Technology news").
- **Voice Output:** Hear the top 5 news headlines and their summaries.
- **News Fetching:** Fetches news from the last 7 days using the **NewsAPI**.
- **Basic Summarization:** Summarizes the news articles by truncating the descriptions to the first 200 characters.
- **Error Handling:** Graceful handling of internet issues, API failures, and voice recognition errors.

## Technologies Used
- **NewsAPI** – For fetching the latest news articles.
- **SpeechRecognition** – For converting voice input to text.
- **pyttsx3** – For converting text to speech (Voice output).
- **Python 3.x** – The programming language used.

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/voice-news-summarizer.git
    cd voice-news-summarizer
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Make sure you have `pyaudio` installed for speech recognition:
    ```bash
    pip install pipwin
    pipwin install pyaudio
    ```

4. Replace the **NewsAPI** key in the script with your own API key.

## Usage

1. Run the script:
    ```bash
    python voice_news_summarizer.py
    ```

2. When prompted, **speak your news topic** (e.g., "Sports news").

3. The program will fetch the latest 5 news articles and summarize them for you. It will **read the headlines and summaries aloud**.

## API Keys
- **NewsAPI Key**: Sign up at [NewsAPI](https://newsapi.org/) and get your free API key. Replace the placeholder in the script.
  
- **OpenAI API Key** (if used in the future): This project currently uses a basic summarization method, but if you plan to integrate AI-powered summaries, replace this with your OpenAI API key.

## Example
```plaintext
🎤 Listening for your news topic...
You said: "Technology news"

🔍 Top 5 news articles on 'Technology news':

1. **Article Title 1**
   A brief summary of the article. The description is truncated to 200 characters...
   🔗 Read more: https://newslink.com

2. **Article Title 2**
   A brief summary of the article. The description is truncated to 200 characters...
   🔗 Read more: https://newslink.com
   ...
```
## Acknowledgments
- [NewsAPI](https://newsapi.org/) for providing access to news articles.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) and [pyttsx3](https://pypi.org/project/pyttsx3/) for enabling voice input and output.

---

### **Important Notes:**
- **Replace the API keys** in the script before running.
- Ensure you have a working **microphone** for voice input.
- **Run the script** in an environment where audio output is available (e.g., your computer's speakers).

---
