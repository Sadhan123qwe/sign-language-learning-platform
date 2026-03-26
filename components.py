import streamlit as st
from urls import video_urls


def progress_bar(prog):
    if(prog > 0):
        return f"""
            <div class="progress-container" style="background: #006666; border: 2px solid #000000; border-radius: 2rem; height: 1.5rem; overflow: hidden; box-shadow: 4px 4px 0px 0px #000;">
                <div class="progress-bar" style="width: {prog}%; background: #b2d8d8; border-right: 2px solid #000; height: 100%; display: flex; align-items: center; justify-content: center; color: #000; font-weight: 800; font-size: 0.8rem; transition: width 0.3s ease-out;">{prog}%</div>
            </div>
            """
    else:
        return f"""
            <div class="progress-container" style="background: #006666; border: 2px solid #000000; border-radius: 2rem; height: 1.5rem; overflow: hidden; box-shadow: 4px 4px 0px 0px #000;">
                <div class="progress-bar" style="width: {prog}%; height: 100%;"></div>
            </div>
            """


def update_video(charachter):
    if st.session_state["page"]=="learnpage":
        return f"""
        <div class="video-wrapper">
        <div class="text-overlay">
            {charachter}
        </div>
        <video width="350" height="290" autoplay controlsList="nodownload" loop style="transform: scale(1.75);">
            <source src="{video_urls[charachter]}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        </div> 
        """
    else:
        return f"""
        <div class="video-wrapper">
        <video width="350" height="290" autoplay controlsList="nodownload" loop style="transform: scale(1.75);">
            <source src="{video_urls[charachter]}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        </div>
        """


def detected_word(WORD, detected_index):
    markdown_str = f'<div style="font-weight: 800; text-align: center; font-size: 3rem; background: #006666; border: 2px solid #000; border-radius: 1rem; padding: 1rem; margin-top: 1rem; display: inline-block; box-shadow: 6px 6px 0px 0px #000; color: #FFFFFF;">'
    # Loop through each letter in the word
    for i, letter in enumerate(WORD):
        # Check if the current letter index is less than or equal to the detected index
        if i <= detected_index:
            # If yes, add the letter with a solid pop of color and text shadow
            markdown_str += f'<span style="color: #b2d8d8; text-shadow: 2px 2px 0px #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;">{letter}</span>'
        else:
            # If no, add the letter in subdued teal
            markdown_str += f'<span style="color: #66b2b2;">{letter}</span>'
    markdown_str += "</div>"
    return markdown_str

