import cv2
import streamlit as st
import time
from model import general_prediction
from autocorrect import Speller
from styles import page_setup, page_with_webcam_video
import os
from auth_check import get_current_user

get_current_user()

if "page" not in st.session_state or st.session_state["page"] != "sentence_page":
    cv2.destroyAllWindows()
    st.session_state["page"] = "sentence_page"
    st.session_state.recorded = False

st.markdown(page_setup(), unsafe_allow_html=True)
st.markdown(page_with_webcam_video(), unsafe_allow_html=True)

st.title("Live Sentence Formation 📝")
st.markdown("""
Form sentences seamlessly using sign language!
1. Hold a sign steady to add a letter.
2. Drop your hands, wait for a moment, and the system will auto-insert a space, correct the word spelling, and add it to your sentence.
""")

target_words = st.slider("Target Number of Words to Record", min_value=1, max_value=20, value=3)

spell = Speller()

if st.button("Start Recording Session 🔴", type="primary"):
    cap = cv2.VideoCapture(0)
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out_video_path = "temp_sentence_video.avi"
    # Match the (450, 350) resolution outputted by general_prediction
    out = cv2.VideoWriter(out_video_path, fourcc, 10.0, (450, 350))
    
    col1, col2 = st.columns([0.6, 0.4])
    with col1:
        webcam_placeholder = st.empty()
    with col2:
        st.subheader("Live Transcription")
        word_placeholder = st.empty()
        sentence_placeholder = st.empty()
        status_placeholder = st.empty()

    current_word = ""
    sentence = []
    
    sustain_count = 0
    empty_frames = 0
    last_pred = None
    cooldown = 0
    
    status_placeholder.info("Recording started. Please begin signing.")
    
    while True and st.session_state["page"] == "sentence_page":
        if cap is not None and cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
                
            frame, best_pred, max_prob = general_prediction(frame)
            
            if cooldown > 0:
                cooldown -= 1
            else:
                if best_pred is not None and max_prob > 0.7:
                    empty_frames = 0  # reset empty hand counter
                    if best_pred == last_pred:
                        sustain_count += 1
                        if sustain_count > 10:  # threshold to confirm a letter
                            current_word += str(best_pred)
                            sustain_count = 0
                            cooldown = 15  # cooldown before next letter detection
                    else:
                        last_pred = best_pred
                        sustain_count = 1
                else:
                    # No confident prediction (hand dropped or unclear)
                    empty_frames += 1
                    sustain_count = 0
                    
                    if empty_frames > 20 and len(current_word) > 0: 
                        # Auto-correct and append word
                        corrected = spell(current_word.lower()).upper()
                        sentence.append(corrected)
                        current_word = ""
                        empty_frames = 0
            
            # Overlay visual data on the frame to be recorded
            # Streamlit is BGR natively when we use cv2
            overlay_text1 = f"Word: {current_word}"
            overlay_text2 = f"Sent: {' '.join(sentence)}"
            cv2.putText(frame, overlay_text1, (10, 310), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
            cv2.putText(frame, overlay_text2, (10, 340), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
            # Save frame to video
            out.write(frame)
            
            # Show in frontend
            webcam_placeholder.image(frame, channels="BGR")
            
            word_placeholder.markdown(f"**Current Word:** {current_word}")
            sentence_placeholder.markdown(f"**Sentence:** {' '.join(sentence)}")
            
            if len(sentence) >= target_words:
                break
        else:
            break
            
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    
    st.session_state.recorded = True
    status_placeholder.success("Recording Complete!")
    
    # Export the final text
    with open("temp_sentence.txt", "w") as f:
        final_sentence = ' '.join(sentence)
        if len(current_word) > 0:
            final_sentence += " " + current_word
        f.write(final_sentence.strip())

# Provide download links
if st.session_state.get("recorded", False):
    st.success("🎉 Your files are ready!")
    
    colA, colB = st.columns(2)
    with colA:
        if os.path.exists("temp_sentence_video.avi"):
            with open("temp_sentence_video.avi", "rb") as file:
                st.download_button(
                    label="Download Video Demo 🎥",
                    data=file,
                    file_name="sign_sentence_video.avi",
                    mime="video/avi"
                )
    with colB:
        if os.path.exists("temp_sentence.txt"):
            with open("temp_sentence.txt", "rb") as file:
                st.download_button(
                    label="Download Sentence Text 📄",
                    data=file,
                    file_name="sign_sentence.txt",
                    mime="text/plain"
                )
