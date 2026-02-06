import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta

# 1. Page Config
st.set_page_config(page_title="Booking Manager", layout="centered")

# 2. Hiding the standard Streamlit top-bar/hamburger to keep it clean
hide_st_style = """
            <style>
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 3. THE BOTTOM NAVIGATION BAR
# We place this at the bottom using a container
with st.container():
    st.write("---") # Visual separator
    selected = option_menu(
        menu_title=None,  # No title needed for bottom nav
        options=["Dashboard", "Guests", "Beds", "Bookings"], 
        icons=["speedometer2", "people", "house-door", "calendar-event"], 
        menu_icon="cast", 
        default_index=0, 
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#000000"},
            "icon": {"color": "#4ec3ad", "font-size": "20px"}, 
            "nav-link": {"font-size": "14px", "text-align": "center", "margin":"0px", "--hover-color": "#262730"},
            "nav-link-selected": {"background-color": "#262730"},
        }
    )

# 4. PAGE LOGIC
if selected == "Dashboard":
    st.title("Dashboard")
    
    # Your Date Switcher Logic
    if 'view_date' not in st.session_state:
        st.session_state.view_date = datetime.now().date()
        
    col1, col2 = st.columns([3, 2])
    with col1:
        st.subheader(st.session_state.view_date.strftime("%B %d, %Y"))
    
    with col2:
        # Mini column layout for the three buttons in your screenshot
        btn_col1, btn_col2, btn_col3 = st.columns(3)
        with btn_col1:
            if st.button("⬅️"):
                st.session_state.view_date -= timedelta(days=1)
                st.rerun()
        with btn_col2:
            if st.button("🏠"):
                st.session_state.view_date = datetime.now().date()
                st.rerun()
        with btn_col3:
            if st.button("➡️"):
                st.session_state.view_date += timedelta(days=1)
                st.rerun()

elif selected == "Guests":
    st.title("Guest Directory")
    st.write("Manage your guest list here.")

elif selected == "Beds":
    st.title("Room/Bed Status")
    st.write("View room availability.")

elif selected == "Bookings":
    st.title("All Bookings")
    st.write("Complete history of reservations.")