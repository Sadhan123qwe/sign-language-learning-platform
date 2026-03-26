import streamlit as st
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
Supports English, Tamil, and Hindi.
""")

text_input = st.text_area("Enter text to convert to speech:", height=150)
language = st.selectbox("Select Language", ["English", "Tamil", "Hindi"])

if st.button("Generate Speech", type="primary"):
    if text_input.strip() == "":
        st.warning("Please enter some text to generate speech.")
    else:
        with st.spinner("Generating audio..."):
            try:
                lang_code = {"English": "en", "Tamil": "ta", "Hindi": "hi"}[language]
                tts = gTTS(text=text_input, lang=lang_code)
                temp_file = "temp_audio.mp3"
                tts.save(temp_file)

                if os.path.exists(temp_file):
                    with open(temp_file, "rb") as audio_file:
                        audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format="audio/mp3")
                    st.success("Audio generated successfully!")
            except Exception as e:
                st.error(f"An error occurred during speech generation: {e}")
