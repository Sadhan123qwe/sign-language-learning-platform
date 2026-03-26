import math

def page_setup():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

        /* Global Font and Base Styles */
        html, body, [class*="css"], h1, h2, h3, h4, h5, h6, p, span, div, a {
            font-family: 'Outfit', sans-serif !important;
        }

        /* Bold all Streamlit markdown native headers */
        h1, h2, h3 {
            font-weight: 800 !important;
            color: #FFFFFF !important;
            margin-bottom: 1.5rem !important;
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #006666;
            border-left: 2px solid #000;
        }
        ::-webkit-scrollbar-thumb {
            background: #FFFFFF;
            border-radius: 0;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #b2d8d8;
        }


         /* Hide side toolbar buttons*/
        div[data-testid="stToolbar"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }

        /* deccrease upper padding */
        .st-emotion-cache-gh2jqd {
            width: 100%;
            padding: 0rem 1rem 10rem;
            max-width: 46rem;
        }

        /* hide header */
        header {
        visibility: hidden;
        height: 0%;
        }

        /* placing log out button */
        .st-emotion-cache-hc3laj {
        position: fixed;
        top: 10px;
        right: 32.5px;
        }

        /* Neobrutalist Streamlit Elements */
        .stButton>button {
            background-color: #b2d8d8 !important;
            border: 2px solid #000 !important;
            color: #000 !important; /* Keep button text black for contrast */
            font-weight: 800 !important;
            border-radius: 0.5rem !important;
            box-shadow: 4px 4px 0px 0px #000 !important;
            transition: all 0.2s ease !important;
        }
        .stButton>button:hover {
            transform: translate(-2px, -2px) !important;
            box-shadow: 6px 6px 0px 0px #000 !important;
            color: #000 !important;
        }
        
        [data-testid="stSidebar"] {
            border-right: 2px solid #000 !important;
            padding-top: 20px;
            background-color: #006666 !important;
        }

        .stTextInput>div>div>input, .stSelectbox>div>div>div {
            border: 2px solid #000 !important;
            border-radius: 0.5rem !important;
            box-shadow: 4px 4px 0px 0px #000 !important;
        }

        .st-emotion-cache-1u2dcfn {
        display:none;
        }

        [data-testid="stSidebarNavSeparator"]{
        display: none;
        }

       [data-testid="stSidebarNavItems"] {
            max-height: none;
        }
    </style>
    """

def hide_navbar():
    return """
    <style>
        .st-emotion-cache-j7qwjs {
            display:none;
        }
        </style>
    """

def unhide_nav_bar() :
    return """
    <style>
        .st-emotion-cache-j7qwjs {
            display:block;
        }
        </style>
    """

def page_with_webcam_video() :
    return """
        <style>

        /* Streamlit Native Images (Webcams) */
        img {
            border-radius: 1rem;
            height:450px;
            width:350px;
            border: 2px solid #000000 !important;
            box-shadow: 6px 6px 0px 0px #000000 !important;
        }

        .video-container {
            position: relative;
            width: 100%;
            display: flex; /* Use flexbox */
            justify-content: center; /* Center horizontally */
            align-items: center; /* Center vertically */
            padding: 2rem;
        }

        .video-wrapper {
        background: #FFFFFF;
        border: 2px solid #000000;
        display: inline-block;
        width: 350px;
        height: 450px;
        overflow: hidden;
        position: relative;
        border-radius: 1rem; 
        align-content : center;
        transform: scaleX(-1);
        box-shadow: 6px 6px 0px 0px #000000;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .video-wrapper:hover {
            transform: scaleX(-1) translate(-2px, -2px);
            box-shadow: 8px 8px 0px 0px #000000;
        }

        .video-wrapper video {
        width: 100%;
        z-index: 1; /* Ensure video is behind text */
        }


        .text-overlay {
            position: absolute; 
            left: 6%;
            bottom: -7%;
            color: #b2d8d8;
            text-shadow: 2px 2px 0px #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
            font-size:150px;
            font-weight: 800;
            z-index: 2;
            transform:scaleX(-1);
            text-align: center; /* center the text horizontally */
        }

        .video-wrapperquiz {
        background: #006666;
        border: 2px solid #000000;
        width: 250px;
        height: 250px;
        overflow: hidden;
        position: relative;
        border-radius: 1rem;
        display: flex; /* Use flexbox */
        justify-content: center; /* Center horizontally */
        align-items: center; /* Center vertically */
        box-shadow: 6px 6px 0px 0px #000000;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        
        .video-wrapperquiz:hover {
            transform: translate(-3px, -3px);
            box-shadow: 9px 9px 0px 0px #000000;
        }

        .letterToFind {
        font-size: 190px;
        color: #ffe090;
        max-height: 20rem;
        text-align : center;
        }

        .progress-text {
        margin-top: 10px;
        text-align: center;
        }

        .progress-container {
        width: 100%;
        height: 2rem; 
        background-color: #683aff;
        border-radius: 5rem;
        position: relative;
        }

        .progress-bar {
        background-color: #ffe090; 
        height: 100%;
        border-radius: 5rem;
        width: 0;
        transition: width 0.3s ease-in-out;
        text-align: center;
        color: #683aff;
        font-size: 20px;
        font-weight: bold;
        line-height: 2rem;
        box-shadow: 10px 0 5px rgba(0, 0, 0, 0.2); /* Adjust values as needed */
        }

        /* quiz question */
        .question-text {
        font-family: 'Arial', sans-serif;
        font-size: 18px;
        color: #ffffff;
        text-align: center;
        margin-bottom: 20px;
        }

        /* button */
        .st-emotion-cache-11to1yi {
        width: 100%;
        }   

        .st-emotion-cache-1gv5c5a p {
            word-break: break-word;
            margin-bottom: 0px;
            font-size: 25px;
        }
    
        </style>
    """

def profile():
    return """
<style>
* {
margin: 0px;
padding: 0px;
box-sizing: border-box;
font-family: 'Outfit', 'Manrope', sans-serif;
list-style-type: none;
text-decoration: none;
}

.my_courses_details{
  padding: 50px;
  border-right:2px solid #f0f0f0;
}
.welcome-content{
  color: #ffe090;
  font-size: 18px;
  font-weight: 400;
  line-height: normal;
  letter-spacing: 0.9px;
}
.my_course_title{
  padding-top: 30px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.my_course_title h1{
  color: #FFFFFF;
  font-size: 30px;
  font-weight: 800;
  line-height: normal;
}

</style>

"""

def letterprogress():
    return """
<style>
.my_course_details{
  width: 100%;
  display: grid;
  grid-template-columns: repeat(2, 400px);
  gap: 30px;
  padding-top: 30px;
  stroke
}
.my_course_details .course-container{
  width: 350px;
  height: 200px;
  border-radius: 1rem;
  padding: 15px;
  border: 2px solid #000000;
  box-shadow: 6px 6px 0px 0px #000000;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.my_course_details .course-container:hover{
  transform: translate(-3px, -3px);
  box-shadow: 9px 9px 0px 0px #000000;
}
.course-container.letter{
  background: #b2d8d8;
  background-image: url('https://freepngimg.com/save/130272-a-letter-download-hq/512x512');
  background-position: 90%;
  background-repeat: no-repeat;
}
.course-container.words{
  background: #006666;
  background-image: url('images/train.png');
  background-position: 90%;
  background-repeat: no-repeat;
}

.my_course_details .circle{
    stroke-dashoffset:"300";
}

.circular-progress-container {
  position: relative;
  width: 52px;
  height: 52px;
}

.circular-progress-container .circle{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.circular-progress-container .circle circle{
  cx: 26px;
  cy: 26px;
  r: 24px;
}

.circular-progress-container .progress-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: Arial, sans-serif;
  font-size: 12px;
  color: #ffffff;
}
</style>
"""
