import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile
import os

st.set_page_config(
    page_title="Language Translator",
    page_icon="🌐"
)

st.title("🌐 Language Translation Tool")
st.caption("Powered by Google Translate")

# Language options
languages = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Bengali": "bn",
    "Portuguese": "pt",
    "Russian": "ru",
    "Korean": "ko",
    "Italian": "it",
    "Dutch": "nl",
    "Turkish": "tr",
    "Urdu": "ur",
    "Gujarati": "gu"
}

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        options=list(languages.keys()),
        index=0
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        options=list(languages.keys()),
        index=1
    )

input_text = st.text_area(
    "Enter text to translate",
    placeholder="Type or paste your text here...",
    height=150
)

if st.button("Translate 🚀", type="primary"):
    if input_text.strip():
        with st.spinner("Translating..."):
            try:
                translated = GoogleTranslator(
                    source=languages[source_lang],
                    target=languages[target_lang]
                ).translate(input_text)
                
                st.success("Translation Complete!")
                
                st.text_area(
                    "Translated Text",
                    value=translated,
                    height=150
                )
                
                # Copy button
                st.code(translated)
                st.caption("👆 Click to copy")
                
                # Text to speech
                if st.button("🔊 Listen to Translation"):
                    tts = gTTS(
                        text=translated,
                        lang=languages[target_lang]
                    )
                    with tempfile.NamedTemporaryFile(
                        delete=False, 
                        suffix='.mp3'
                    ) as f:
                        tts.save(f.name)
                        st.audio(f.name)
                        
            except Exception as e:
                st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter some text first")

st.divider()
st.caption("Built by Arjun Kanukuntla | CodeAlpha AI Internship")