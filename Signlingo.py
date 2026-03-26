import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
from styles import page_setup,hide_navbar,unhide_nav_bar
import json
import sqlite3

conn = sqlite3.connect(
    "signlingo.db"
)

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Profile (
                    username TEXT PRIMARY KEY,
                    name TEXT,
                    email_id TEXT
                )''')

c.execute(
    """CREATE TABLE IF NOT EXISTS Alphabet (
                    username TEXT,
                    letter TEXT,
                    PRIMARY KEY (username, letter),
                    FOREIGN KEY(username) REFERENCES User(username)
                )"""
)

c.execute(
    """CREATE TABLE IF NOT EXISTS Words (
                    username TEXT,
                    word TEXT,
                    PRIMARY KEY (username, word),
                    FOREIGN KEY(username) REFERENCES User(username)
                )"""
)

conn.commit()

st.markdown(page_setup(), unsafe_allow_html=True)
st.markdown(hide_navbar(), unsafe_allow_html=True)

def get_username(self):
        if st.session_state['LOGOUT_BUTTON_HIT'] == False:
            fetched_cookies = self.cookies
            if '__streamlit_login_signup_ui_username__' in fetched_cookies.keys():
                username=fetched_cookies['__streamlit_login_signup_ui_username__']
                return username

def get_name(self):
        with open("_secret_auth_.json","r") as auth:
             user_data = json.load(auth)
             current_user = get_username(self)
             for user in user_data:
                  if user["username"] == current_user:
                    return user["name"]

def get_email(self):
    with open("_secret_auth_.json","r") as auth:
        user_data = json.load(auth)
        current_user = get_username(self)
        for user in user_data:
            if user["username"] == current_user:
                return user["email"]

def add_profile_to_database(current_user):
    try:
        conn = sqlite3.connect("signlingo.db")
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO Profile (username, name, email_id)
                                VALUES (?, ?, ?)""",
                (current_user["username"], current_user["name"], current_user["email"]),
            )
    except Exception as e:
        print(f"Error occurred: {e}")
        # Log the exception or handle it appropriately
    finally:
        if conn:
            conn.close()

login_obj = __login__(
    auth_token="courier_auth_token",
    company_name="signlingo",
    width=200,
    height=250,
    logout_button_name="Logout",
    hide_menu_bool=True,
    hide_footer_bool=True,
    lottie_url="https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json",
)


logged_in = login_obj.build_login_ui()

if logged_in:

    current_user = {
        "username": get_username(login_obj),
        "name": get_name(login_obj),
        "email": get_email(login_obj),
        "id": None,
    }

    if "current_user" not in st.session_state:
        st.session_state["current_user"] = current_user
    else:
        st.session_state["current_user"] = current_user

    add_profile_to_database(current_user)

    st.markdown(unhide_nav_bar(), unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        /* Base Dark Mode Inversions */
        body {
            background-color: #004c4c;
            color: #FFFFFF;
        }
        /* Hide default Streamlit padding on this page purely to act like a real landing page */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important; 
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        [data-testid="stMainBlockContainer"] {
            padding-top: 0rem !important;
            padding-left: 0rem !important; 
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        [data-testid="stHeader"] {
            display: none !important;
        }
        /* Collapse sidebar entirely on the main page */
        [data-testid="stSidebar"] {
            display: none !important;
        }
        /* Ensure top margin is 0 */
        .st-emotion-cache-12fmjuu {
            gap: 0px !important;
        }

        .top-navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.5rem 4rem;
            background: #004c4c;
            border-bottom: none;
            position: sticky;
            top: 0;
            z-index: 1000;
            margin-bottom: 2rem;
            margin-top: -7rem;
        }
        .nav-brand {
            font-size: 2rem;
            font-weight: 900;
            color: #FFFFFF;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .nav-links {
            display: flex;
            gap: 3rem;
            align-items: center;
        }
        .nav-links a {
            color: #FFFFFF;
            text-decoration: none;
            font-weight: 600;
            font-size: 1.1rem;
            transition: all 0.2s ease;
        }
        .nav-links a:hover {
            color: #b2d8d8;
            text-decoration: underline;
            text-decoration-thickness: 3px;
            text-underline-offset: 4px;
        }
        .btn-request {
            background: #004c4c;
            border: 2px solid #000;
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            font-weight: 800;
            color: #FFFFFF;
            text-decoration: none;
            box-shadow: 4px 4px 0px 0px #000;
            transition: all 0.2s ease;
        }
        .btn-request:hover {
            transform: translate(-2px, -2px);
            box-shadow: 6px 6px 0px 0px #000;
            color: #000 !important;
        }
        
        .container {
            max-width: 1400px;
            margin: -2rem auto 0 auto;
            padding: 0 4rem;
        }

        .hero {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 4rem;
            margin-bottom: 6rem;
            gap: 4rem;
            background: #006666;
            border-radius: 1rem;
            border: 2px solid #000;
            box-shadow: 8px 8px 0px 0px #000;
        }
        .hero-content {
            flex: 1;
            text-align: left;
        }
        .hero-content h1 {
            font-size: 4.5rem;
            font-weight: 900;
            color: #FFFFFF;
            margin-bottom: 1.5rem;
            line-height: 1.1;
        }
        .hero-content p {
            font-size: 1.25rem;
            color: #DDDDDD;
            margin-bottom: 2.5rem;
            line-height: 1.6;
            max-width: 600px;
        }
        .btn-primary {
            display: inline-block;
            background: #b2d8d8;
            border: 2px solid #000;
            padding: 1rem 2.5rem;
            border-radius: 0.5rem;
            font-weight: 800;
            font-size: 1.2rem;
            color: #000; /* keep primary btn text dark for contrast */
            text-decoration: none;
            box-shadow: 6px 6px 0px 0px #000;
            transition: all 0.2s ease;
        }
        .btn-primary:hover {
            transform: translate(-3px, -3px);
            box-shadow: 9px 9px 0px 0px #000;
            color: #000 !important;
        }
        .hero-image {
            flex: 0.8;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 400px;
            background: #FFFFFF;
            border: 2px solid #000;
            border-radius: 1rem;
            position: relative;
        }
        .floating-emoji {
            font-size: 8rem;
            position: absolute;
            animation: float 6s ease-in-out infinite;
        }
        .floating-emoji.small {
            font-size: 4rem;
            top: 10%;
            right: 20%;
            animation-delay: -2s;
        }
        .floating-emoji.outline {
            font-size: 5rem;
            bottom: 10%;
            left: 15%;
            animation-delay: -4s;
            filter: drop-shadow(4px 4px 0 #000);
        }
        @keyframes float {
            0% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(5deg); }
            100% { transform: translateY(0px) rotate(0deg); }
        }

        .section-header {
            display: inline-block;
            background: #b2d8d8;
            color: #000;
            padding: 0.5rem 1.5rem;
            border-radius: 0.5rem;
            font-weight: 900;
            font-size: 1.8rem;
            border: 2px solid #000;
            margin-bottom: 1rem;
            box-shadow: 4px 4px 0px 0px #000;
        }
        .section-desc {
            font-size: 1.2rem;
            max-width: 600px;
            margin-bottom: 3rem;
            color: #333;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 3rem;
            margin-bottom: 6rem;
        }
        .feature-card {
            background: #006666;
            border: 2px solid #000;
            border-radius: 1rem;
            padding: 3rem 2rem;
            text-align: left;
            transition: all 0.2s ease;
            box-shadow: 8px 8px 0px 0px #000;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .feature-card.red {
            background: #66b2b2;
        }
        .feature-card:hover {
            transform: translate(-5px, -5px);
            box-shadow: 13px 13px 0px 0px #000;
        }
        .feature-header {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            margin-bottom: 2rem;
        }
        .feature-card h3 {
            font-size: 2rem;
            font-weight: 800;
            color: #FFFFFF;
            background: #004c4c;
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            border: 2px solid #000;
            display: inline-block;
            margin: 0;
            line-height: 1.2;
        }
        .feature-icon {
            font-size: 3rem;
            background: #004c4c;
            border: 2px solid #000;
            border-radius: 50%;
            width: 80px;
            height: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 4px 4px 0px 0px #000;
        }
        .feature-link {
            display: inline-flex;
            align-items: center;
            gap: 1rem;
            color: #FFFFFF;
            text-decoration: none;
            font-weight: 800;
            font-size: 1.2rem;
            margin-top: auto;
        }
        .feature-link:hover {
            text-decoration: underline;
        }
        .icon-circle {
            background: #FFFFFF;
            color: #b2d8d8;
            width: 35px;
            height: 35px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 900;
        }
        .feature-card.red .icon-circle {
            color: #FFFFFF;
            background: #004c4c;
            border: 2px solid #000;
        }
        
        .about-section {
            background: #006666;
            border-radius: 1rem;
            padding: 5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: white;
            position: relative;
            overflow: hidden;
            margin-bottom: 0rem;
        }
        .about-content {
            max-width: 600px;
            z-index: 2;
        }
        .about-content h2 {
            font-size: 3.5rem;
            font-weight: 900;
            margin-bottom: 1.5rem;
            color: #FFF;
            line-height: 1.1;
        }
        .about-content p {
            font-size: 1.25rem;
            color: #CCC;
            margin-bottom: 2.5rem;
        }
        .about-decoration {
            position: absolute;
            right: 5%;
            top: 10%;
            width: 300px;
            height: 300px;
            background: #b2d8d8;
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.5;
            z-index: 1;
        }
        .btn-inverted {
            background: transparent;
            color: #FFFFFF;
            border-color: #000;
        }
        .btn-inverted:hover {
            background: #b2d8d8 !important;
            color: #000 !important;
        }
        
        .site-footer {
            background: #006666;
            color: white;
            padding: 2rem 4rem;
            margin-top: -1rem; /* Streamlit markdown block spacing fix */
            margin-left: -4rem;
            margin-right: -4rem;
            margin-bottom: -10rem;
            border-top: 2px solid #000;
        }
        .footer-content {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        </style>
        <!-- Navbar mapped from HTML -->
        <div class="top-navbar">
            <div class="nav-brand">
                <img src="https://i.imgur.com/eelyBU4.png"  style="height: 40px; margin-right: 10px;">
            </div>
            <div class="nav-links">
                <a href="#about">About us</a>
                <a href="#services">Services</a>
                <a href="#cases">Use Cases</a>
                <a href="#pricing">Pricing</a>
                <a href="Learn_Alphabets_📚" target="_self" class="btn-request">Start Learning</a>
            </div>
        </div>
        <div class="container">
            <div class="hero">
                <div class="hero-content">
                    <h1>Navigating the visual landscape for success</h1>
                    <p>Our sign language learning platform helps individuals communicate and connect seamlessly. Through a range of interactive lessons including ASL, real-time feedback, and accessible content.</p>
                    <a href="Learn_Alphabets_📚" target="_self" class="btn-primary">Book a consultation</a>
                </div>
                <div class="hero-image">
                    <div class="floating-emoji">✌️</div>
                    <div class="floating-emoji small">✨</div>
                    <div class="floating-emoji outline">💬</div>
                </div>
            </div>
            <div id="services" style="padding-top: 2rem;">
                <div class="section-header">Features</div>
                <p class="section-desc">At our interactive learning platform, we offer a range of tools to help you master sign language. These features include:</p>
            </div>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-header">
                        <h3>Interactive<br>Lessons</h3>
                        <div class="feature-icon">📚</div>
                    </div>
                    <a href="Learn_Alphabets_📚" target="_self" class="feature-link"><div class="icon-circle">↗</div> Learn more</a>
                </div>
                <div class="feature-card red">
                    <div class="feature-header">
                        <h3>Real-time<br>Feedback</h3>
                        <div class="feature-icon">🤖</div>
                    </div>
                    <a href="Practice_Zone_🎓" target="_self" class="feature-link"><div class="icon-circle">↗</div> Learn more</a>
                </div>
                <div class="feature-card red">
                    <div class="feature-header">
                        <h3>Practice<br>Sessions</h3>
                        <div class="feature-icon">🎓</div>
                    </div>
                    <a href="Quiz_Time_📝" target="_self" class="feature-link"><div class="icon-circle">↗</div> Learn more</a>
                </div>
                <div class="feature-card">
                    <div class="feature-header">
                        <h3>Progress<br>Tracking</h3>
                        <div class="feature-icon">📈</div>
                    </div>
                    <a href="Your_Profile_👨🏻‍💼" target="_self" class="feature-link"><div class="icon-circle">↗</div> Learn more</a>
                </div>
            </div>
            <div id="about" class="about-section">
                <div class="about-content">
                    <h2>Let's make things happen</h2>
                    <p>Contact us today to learn more about how our platform can help you grow your communication skills and connect with the world.</p>
                    <a href="mailto:info@signlingo.test" class="btn-primary btn-inverted">Get your free proposal</a>
                </div>
                <div class="about-decoration"></div>
            </div>
        </div>
        <footer class="site-footer">
            <div class="footer-content">
                <div class="nav-brand" style="color: white;">
                    <span>✖</span> SignLingo
                </div>
                <p style="color: #ccc; margin: 0;">© 2026 SignLingo. All rights reserved.</p>
            </div>
        </footer>
        """,
        unsafe_allow_html=True,
    )
