

import streamlit as st
import pandas as pd

# Page Config with custom icon
st.set_page_config(page_title="Women Safety Awareness", page_icon="🛡️", layout="wide")

# Custom CSS for advanced UI
st.markdown("""
    <style>
        /* Background Gradient */
        .stApp {
            background: linear-gradient(135deg, #ffe6eb, #fff);
        }

        /* Title Style */
        h1, h2, h3 {
            color: #d63384;
            font-family: 'Trebuchet MS', sans-serif;
        }

        /* Card Style */
        .card {
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }

        /* Sidebar Style */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #ff4d6d, #ff8095);
        }
        .css-1d391kg {color: white !important;}
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🛡️ Women Safety")
page = st.sidebar.radio("Navigate", ["🏠 Home", "✨ Safety Tips", "📞 Emergency", "📝 Report", "🗺️ Live Map"])

# Home Page
if page == "🏠 Home":
    st.markdown("<div class='card'><h1>🛡️ Women Safety Awareness</h1><p>Together for a safer tomorrow 🌍</p></div>", unsafe_allow_html=True)
    st.image("women.jpg",use_container_width=True)
    st.success("⚠️ If you are in danger, go to Emergency section NOW!")

# Safety Tips Page
elif page == "✨ Safety Tips":
    st.markdown("<div class='card'><h2>✨ Smart Safety Tips</h2></div>", unsafe_allow_html=True)
    tips = [
        "Share your live location with trusted friends.",
        "Avoid isolated areas at night.",
        "Save emergency numbers in speed dial.",
        "Carry a whistle or safety alarm.",
        "Trust your instincts in unsafe situations."
    ]
    for tip in tips:
        st.markdown(f"<div class='card'>✅ {tip}</div>", unsafe_allow_html=True)

# Emergency Page
elif page == "📞 Emergency":
    st.markdown("<div class='card'><h2>🚨 Emergency Help</h2></div>", unsafe_allow_html=True)
    st.error("⚠️ If you feel unsafe, use the emergency contacts below immediately!")

    if st.button("🚨 Send Emergency Alert"):
        st.warning("📢 Alert sent to your emergency contacts!")

    st.markdown("""
        <div class='card'>
        <h3>📞 Important Numbers (Pakistan):</h3>
        <ul>
            <li>🚓 Police: <b>15</b></li>
            <li>🚑 Rescue: <b>1122</b></li>
            <li>📞 Women Helpline: <b>1043</b></li>
        </ul>
        </div>
    """, unsafe_allow_html=True)

# Report Page
elif page == "📝 Report":
    st.markdown("<div class='card'><h2>📝 Report an Incident</h2><p>Your report will remain confidential.</p></div>", unsafe_allow_html=True)

    name = st.text_input("Your Name (optional)")
    details = st.text_area("Incident Details")
    city = st.text_input("Location (City/Area)")

    if st.button("Submit Report"):
        if details.strip() == "":
            st.error("⚠️ Please provide details before submitting.")
        else:
            st.success("✅ Report submitted successfully! Stay safe.")

# Live Map Page
elif page == "🗺️ Live Map":
    st.markdown("<div class='card'><h2>🗺️ Incident Map</h2><p>This map shows reported incident areas (demo).</p></div>", unsafe_allow_html=True)
    data = pd.DataFrame({
        'lat': [31.5204, 24.8607, 33.6844],  # Lahore, Karachi, Islamabad
        'lon': [74.3587, 67.0011, 73.0479]
    })
    st.map(data, zoom=5)