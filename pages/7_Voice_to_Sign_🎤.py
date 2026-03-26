import streamlit as st
import speech_recognition as sr
from components import update_video
from styles import page_setup
import time
from auth_check import get_current_user

get_current_user()

if "page" not in st.session_state or st.session_state["page"] != "voice_page":
    st.session_state["page"] = "voice_page"

st.markdown(page_setup(), unsafe_allow_html=True)
st.title("Voice-to-Sign 🎤")

st.markdown("""
Speak into your microphone, and the system will convert your speech to text and instantly show you the corresponding sign language representation.
""")

language = st.selectbox("Select Input Language", ["English", "Tamil", "Hindi"])
lang_code_map = {"English": "en-US", "Tamil": "ta-IN", "Hindi": "hi-IN"}

def sign_language_output(text):
    clean_text = ''.join(e for e in text if e.isalnum() or e.isspace()).upper()
    words = clean_text.split()
    
    for word in words:
        st.markdown(f"#### {word}")
        all_letters = [char for char in word if char.isalpha()]
        
        if all_letters:
            cols = st.columns(min(len(all_letters), 6))
            for i, letter in enumerate(all_letters):
                with cols[i % 6]:
                    st.markdown(f'<div style="text-align: center; font-size: 24px;"><b>{letter}</b></div>', unsafe_allow_html=True)
                    st.markdown(update_video(letter), unsafe_allow_html=True)
            time.sleep(1) # Small pause between words to simulate pacing

if st.button("Start Recording", type="primary"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening... Please speak now.")
        try:
            # Adjust for ambient noise and listen
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio_text = r.listen(source, timeout=8, phrase_time_limit=15)
            
            st.info("⏳ Processing your speech...")
            text = r.recognize_google(audio_text, language=lang_code_map[language])
            
            st.success(f"**Recognized Text:** {text}")
            
            if language == "English":
                st.markdown("### 🤲 Sign Language Translation:")
                sign_language_output(text)
            else:
                st.warning("Sign language visual translation is currently supported mainly for English Alphabets. Only the recognized text in your selected language is displayed above.")
                
        except sr.WaitTimeoutError:
            st.error("Operation timed out. No speech detected.")
        except sr.UnknownValueError:
            st.error("Sorry, could not understand the audio. Please try speaking clearly.")
        except sr.RequestError as e:
            st.error(f"Could not request results from Speech Recognition service; {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
