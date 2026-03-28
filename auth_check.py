import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
import json

def get_current_user():
    # If already authenticated in this session, return immediately
    if "current_user" in st.session_state:
        return st.session_state["current_user"]

    login_obj = __login__(
        auth_token="courier_auth_token", 
        company_name="signlingo",
        width=200, height=250, logout_button_name="Logout",
        hide_menu_bool=True, hide_footer_bool=True, 
        lottie_url="https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json"
    )

    try:
        logged_in = login_obj.build_login_ui()
    except Exception as e:
        err_msg = str(e)
        # extra-streamlit-components race condition on first load — rerun to fix
        if "SessionInfo" in err_msg or "Bad message" in err_msg or "not initialized" in err_msg:
            st.rerun()
        else:
            st.error(f"Login component error: {err_msg}")
            st.stop()
        return None

    if logged_in:
        try:
            fetched_cookies = login_obj.cookies
            if '__streamlit_login_signup_ui_username__' in fetched_cookies:
                username = fetched_cookies['__streamlit_login_signup_ui_username__']
                name = username
                email = ""
                try:
                    with open("_secret_auth_.json", "r") as f:
                        user_data = json.load(f)
                        for u in user_data:
                            if u["username"] == username:
                                name = u["name"]
                                email = u["email"]
                except Exception:
                    pass

                st.session_state["current_user"] = {
                    "username": username,
                    "name": name,
                    "email": email,
                    "id": None
                }
                return st.session_state["current_user"]
        except Exception as e:
            err_msg = str(e)
            if "SessionInfo" in err_msg or "Bad message" in err_msg or "not initialized" in err_msg:
                st.rerun()
            else:
                print(f"Auth check hit an exception: {e}")

    # Not logged in — show helpful message and stop
    st.error("Authentication required! Please click on 'Signlingo' in the sidebar or go to the Home Page to log in.")
    st.stop()
