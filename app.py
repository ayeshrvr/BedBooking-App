import streamlit as st
from datetime import datetime, timedelta
from supabase import create_client, Client

# --- HIDE STREAMLIT BRANDING ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            #stDecoration {display:none;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- 1. CONFIGURATION ---
URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]

# We use st.cache_resource so we don't reconnect on every button click
@st.cache_resource
def init_connection():
    return create_client(URL, KEY)

supabase = init_connection()

# --- 2. STATE MANAGEMENT ---
if 'view_date' not in st.session_state:
    st.session_state.view_date = datetime.now().date()

# --- 3. UI LAYOUT ---
st.title("📅 Booking Manager")

# The Switcher
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Previous"):
        st.session_state.view_date -= timedelta(days=1)

with col2:
    st.markdown(f"<h3 style='text-align: center;'>{st.session_state.view_date}</h3>", unsafe_allow_html=True)

with col3:
    if st.button("Next ➡️"):
        st.session_state.view_date += timedelta(days=1)

# --- 4. DATA FETCHING ---
st.divider()
st.write(f"Showing results for: **{st.session_state.view_date}**")

# Replace 'bookings' with your actual table name
try:
    response = supabase.table("bookings").select("*").eq("checkin_date", str(st.session_state.view_date)).execute()
    data = response.data

    if data:
        st.table(data)
    else:
        st.info("No bookings found for this date.")
except Exception as e:
    st.error(f"Connect your table to see data! Error: {e}")