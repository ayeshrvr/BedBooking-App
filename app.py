import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.bottom_container import bottom
from datetime import datetime, timedelta

# 1. Setup Page
st.set_page_config(page_title="Dashboard", layout="centered")

# 2. Custom CSS to match your screenshot (Dark theme, circular buttons)
st.markdown("""
    <style>
    /* Hide top bar and footer */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Style the dashboard buttons to be circular and hollow */
    div.stButton > button {
        border-radius: 50%;
        width: 45px;
        height: 45px;
        background-color: transparent;
        border: 1.5px solid #4ec3ad;
        color: #4ec3ad;
        padding: 0;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    div.stButton > button:hover {
        border-color: #ffffff;
        color: #ffffff;
        background-color: transparent;
    }

    /* Adjusting container padding for mobile */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 5rem; /* Space for bottom nav */
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Bottom Navigation
with bottom():
    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Guests", "Beds", "Bookings"],
        icons=["speedometer2", "people", "house-door", "calendar-event"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#000000"},
            "icon": {"color": "#4ec3ad", "font-size": "18px"},
            "nav-link": {"font-size": "12px", "text-align": "center", "margin":"0px", "color": "#7a7a7a"},
            "nav-link-selected": {"background-color": "transparent", "color": "#4ec3ad"},
        }
    )

# 4. Page Content Logic
if selected == "Dashboard":
    st.markdown("<h2 style='text-align: center; color: white;'>Dashboard</h2>", unsafe_allow_html=True)
    
    # Date Switcher Logic
    if 'view_date' not in st.session_state:
        st.session_state.view_date = datetime.now().date()
        
    # Layout for Date and Buttons
    col_date, col_btns = st.columns([2, 1])
    
    with col_date:
        st.write(f"### {st.session_state.view_date.strftime('%B %d, %Y')}")
        
    with col_btns:
        b_col1, b_col2, b_col3 = st.columns(3)
        with b_col1:
            if st.button("˂"):
                st.session_state.view_date -= timedelta(days=1)
                st.rerun()
        with b_col2:
            if st.button("⌂"):
                st.session_state.view_date = datetime.now().date()
                st.rerun()
        with b_col3:
            if st.button("˃"):
                st.session_state.view_date += timedelta(days=1)
                st.rerun()

    # Place your main dashboard data here
    st.info("Your main content goes here...")

elif selected == "Guests":
    st.title("Guests")