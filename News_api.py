import requests
import json
import os
import speech_recognition as sr
import pyttsx3
from datetime import datetime, timedelta

# API Keys (Replace with your keys)
NEWS_API_KEY = "add your API key here"

# Text-to-Speech Engine Setup
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # Speed of speech
engine.setProperty("volume", 1.0)  # Volume

# Recognizer for speech input
recognizer = sr.Recognizer()

def speak(text):
    """Convert text to speech"""
    print(f"🔊 Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def get_voice_input():
    """Get user input through voice"""
    with sr.Microphone() as source:
        print("🎤 Listening for your news topic...")
        speak("What type of news are you interested in?")
        recognizer.adjust_for_ambient_noise(source)
        try:
            query = recognizer.listen(source)
            text = recognizer.recognize_google(query)
            print(f"✅ You said: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ Sorry, I couldn't understand. Try again.")
            speak("Sorry, I couldn't understand. Try again.")
            return get_voice_input()
        except sr.RequestError:
            print("❌ Could not request results. Check your internet connection.")
            speak("Could not request results. Check your internet connection.")
            return None

# Set date range (last 7 days)
today_date = datetime.today().strftime('%Y-%m-%d')
seven_days_ago = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')

def fetch_news(query):
    """Fetch latest news articles"""
    news_url = f"https://newsapi.org/v2/everything?q={query}&from={seven_days_ago}&to={today_date}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    }

    try:
        r = requests.get(news_url, headers=headers)
        r.raise_for_status()
        news = r.json()

        if news.get("status") != "ok":
            print("Error fetching news:", news.get("message", "Unknown error"))
            speak("Error fetching news. Please try again later.")
            return []

        articles = news.get("articles", [])
        if not articles:
            print(f"No news articles found for '{query}' in the last 7 days.")
            speak(f"No news articles found for {query}.")
            return []

        return articles[:5]  # Limit to 5 articles

    except requests.exceptions.RequestException as e:
        print("Error connecting to News API:", e)
        speak("Error connecting to News API.")
        return []

def summarize_text_basic(text):
    """Simple summary function that shortens the text by trimming excess details."""
    # Let's keep the first 200 characters for a basic summary
    if len(text) > 200:
        return text[:200] + "..."
    return text

def main():
    query = get_voice_input()
    if not query:
        return

    articles = fetch_news(query)
    if not articles:
        return

    speak(f"Here are the top {len(articles)} news articles about {query}.")
    print(f"\n🔍 Top {len(articles)} news articles on '{query}':\n")

    for i, article in enumerate(articles, 1):
        title = article.get("title", "No Title")
        description = article.get("description", "No Description")
        url = article.get("url", "No URL")

        # Generate simple summary
        summary = summarize_text_basic(description or title)

        print(f"{i}. \033[1m{title}\033[0m")  # Bold title
        print(f"   {summary}")
        print(f"   🔗 Read more: {url}")
        print("-" * 50)

        # Speak the news headline and summary
        speak(f"News {i}: {title}. {summary}")

if __name__ == "__main__":
    main()


