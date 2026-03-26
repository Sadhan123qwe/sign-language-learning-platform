import streamlit as st
import pyttsx3
from gtts import gTTS
import os
from styles import page_setup
from auth_check import get_current_user

get_current_user()

if "page" not in st.session_state or st.session_state["page"] != "tts_page":
    st.session_state["page"] = "tts_page"

st.markdown(page_setup(), unsafe_allow_html=True)
st.title("Text-to-Speech Conversion 🗣️")

st.markdown("""
Convert your predicted text or typed text into voice seamlessly.
Choose between offline mode (English) or API-based integration (Tamil, Hindi).
""")

text_input = st.text_area("Enter text to convert to speech:", height=150)
language = st.selectbox("Select Language", ["English", "Tamil", "Hindi"])

if st.button("Generate Speech", type="primary"):
    if text_input.strip() == "":
        st.warning("Please enter some text to generate speech.")
    else:
        with st.spinner("Generating audio..."):
            try:
                temp_file = "temp_audio.mp3"
                if language == "English":
                    # Use pyttsx3 for English (Offline approach)
                    engine = pyttsx3.init()
                    engine.save_to_file(text_input, "temp_audio.wav")
                    engine.runAndWait()
                    
                    if os.path.exists("temp_audio.wav"):
                        audio_file = open("temp_audio.wav", "rb")
                        audio_bytes = audio_file.read()
                        st.audio(audio_bytes, format="audio/wav")
                else:
                    # Use gTTS for Tamil and Hindi (API approach)
                    lang_code = 'ta' if language == "Tamil" else 'hi'
                    tts = gTTS(text=text_input, lang=lang_code)
                    tts.save(temp_file)
                    
                    if os.path.exists(temp_file):
                        audio_file = open(temp_file, "rb")
                        audio_bytes = audio_file.read()
                        st.audio(audio_bytes, format="audio/mp3")
                        
                st.success("Audio generated successfully!")
            except Exception as e:
                st.error(f"An error occurred during speech generation: {e}")
