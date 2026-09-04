import streamlit as st
import os
import time

# 1. पेज की पूरी सेटिंग
st.set_page_config(page_title="Happy Birthday My Love!", page_icon="❤️", layout="wide")

# 2. प्रीमियम कस्टमाइज नियॉन थीम और धड़कते दिल का CSS
custom_css = """
<style>
    @import url('https://googleapis.com');

    .stApp {
        background: linear-gradient(135deg, #0f0003 0%, #2a0a07 50%, #4d0011 100%);
        color: #ffffff;
    }
    .block-container {
        padding-top: 2.2rem !important;
        padding-bottom: 2rem !important;
        max-width: 450px !important;
    }
    .main-title {
        font-family: 'Georgia', serif;
        text-align: center;
        font-size: 2.4rem;
        font-weight: bold;
        letter-spacing: 1px;
        margin-top: 0px;
        margin-bottom: 10px;
        background: linear-gradient(to right, #ff0055, #ffd700, #ff00ab);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 4s linear infinite;
    }
    @keyframes textShine {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }
    .love-sender-box { text-align: center; margin-top: 5px; margin-bottom: 12px; line-height: 1.4; }
    .love-name {
        font-family: 'Georgia', serif; font-size: 2rem; font-weight: bold; text-transform: uppercase;
        background: linear-gradient(45deg, #ffd700, #ff00b3); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 15px rgba(255, 128, 179, 0.6); display: inline-block;
    }
    .love-receiver-name {
        font-family: 'Georgia', serif; font-size: 2.2rem; font-weight: bold; text-transform: uppercase;
        background: linear-gradient(45deg, #ff0055, #ff00b3); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 20px #ff0055, 0px 0px 10px #ff00b3; display: inline-block;
    }
    .romantic-badge {
        font-family: 'Georgia', serif; font-size: 1.2rem; font-weight: bold; text-align: center;
        margin: 10px auto; padding: 5px 15px; border-radius: 50px; background: rgba(255, 0, 85, 0.1);
        border: 1px solid rgba(255, 0, 85, 0.3); width: fit-content;
    }
    .badge-left { color: #ff0055; text-shadow: 0 0 8px #ff0055; }
    .badge-right { color: #ffd700; text-shadow: 0 0 8px #ffd700; }
    
    .stImage img {
        border-radius: 20px !important; border: 2px solid rgba(255, 0, 85, 0.5) !important;
        box-shadow: 0 0 25px rgba(255, 0, 85, 0.7) !important;
    }
    
    /* ❤️ धड़कता हुआ मोटा नियॉन दिल (Beating Heart Box) */
    .beating-heart-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 25px auto;
        position: relative;
        width: 170px;
        height: 170px;
        background: #ff0055;
        border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
        clip-path: path('M 85,30 C 50,0 0,20 0,75 C 0,120 50,150 85,170 C 120,150 170,120 170,75 C 170,20 120,0 85,30 Z');
        box-shadow: 0 0 30px #ff0055;
        animation: heartBeat 1.2s infinite;
    }
    @keyframes heartBeat {
        0% { transform: scale(0.95); box-shadow: 0 0 20px #ff0055; }
        50% { transform: scale(1.08); box-shadow: 0 0 40px #ff3385, 0 0 20px #ffd700; }
        100% { transform: scale(0.95); box-shadow: 0 0 20px #ff0055; }
    }
    .heart-text {
        font-family: 'Dancing Script', cursive, serif;
        font-size: 0.95rem;
        font-weight: 900 !important;
        color: #ffffff;
        text-align: center;
        line-height: 1.3;
        text-shadow: 0px 2px 5px rgba(0, 0, 0, 0.8), 0 0 10px #ffd700;
        z-index: 10;
        padding: 10px;
        margin-top: 10px;
    }
    
    /* 🌟 स्टाइलिश नियॉन कोट्स टेक्स्ट बॉक्स */
    .wishes-container { margin-top: 25px; padding: 5px; }
    .premium-wish-box {
        background: rgba(15, 0, 5, 0.8); 
        border: 2px solid #ff0055; 
        padding: 16px; 
        border-radius: 16px; 
        margin-bottom: 20px;
        box-shadow: 0 0 15px #ff0055, inset 0 0 10px rgba(255, 0, 85, 0.3);
    }
    .wish-heading {
        font-family: 'Georgia', serif; font-weight: bold; color: #ffd700; font-size: 1.15rem;
        text-shadow: 0 0 10px #ffd700; margin-bottom: 6px; display: block;
    }
    .wish-body { 
        font-family: 'Caveat', 'Dancing Script', cursive; 
        font-size: 1.3rem; 
        line-height: 1.5; 
        color: #ffccdb;
        text-shadow: 0 0 8px rgba(255, 51, 119, 0.6);
    }
    
    /* बटन स्टाइल */
    .stButton>button {
        width: 100% !important; background: linear-gradient(45deg, #ff0055, #ff3377) !important;
        color: white !important; font-weight: bold !important; border-radius: 20px !important;
        border: 1px solid #ffd700 !important; box-shadow: 0 4px 15px rgba(255, 0, 85, 0.4) !important;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; justify-content: center; }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 51, 119, 0.1) !important; border: 1px solid rgba(255, 51, 119, 0.3) !important;
        border-radius: 15px !important; padding: 6px 12px !important; color: #ffb3cc !important; font-weight: bold !important; font-size: 0.9rem !important;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(45deg, #ff0055, #ff3377) !important; color: white !important;
        border: 1px solid #ffd700 !important; box-shadow: 0 0 15px rgba(255, 0, 85, 0.5) !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. पासवर्ड लॉक स्क्रीन
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("<h2 style='text-align:center; font-family:Georgia; color:#ff0055; margin-top:50px;'>🔒 Our Private Space</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ffb3cc;'>यह डायरी सिर्फ तुम्हारे और मेरे लिए लॉक्ड है।</p>", unsafe_allow_html=True)
    
    password = st.text_input("सीक्रेट कोड (Password) दर्ज करें:", type="password")
    if st.button("डायरी खोलें 📖"):
        if password == "1122":  
            st.session_state.authenticated = True
            st.success("अनलॉक हो रहा है... ❤️")
            time.sleep(1)
            st.rerun()
        else:
            st.error("गलत पासवर्ड! सही कोड दर्ज करें।")
    st.stop()

# --- अनलॉक होने के बाद का मुख्य ऐप ---

if 'active_track' not in st.session_state:
    st.session_state.active_track = "https://soundhelix.com"

# गिटहब फोल्डर इमेज डिटेक्शन
all_files = os.listdir(".")
all_images = [f for f in all_files if f.lower().endswith((".jpeg", ".jpg", ".png", ".webp")) and f.lower() != "app.py"]
main_photo = all_images if len(all_images) > 0 else None
album_photos = all_images if len(all_images) > 0 else ["https://unsplash.com"]

panna1, panna2, panna3 = st.tabs(["🏠 मुख्य पन्ना", "🎵 म्यूजिक रूम", "📸 फोटो एल्बम"])

# ----------------- पन्ना 1: होम और पूरे 20 मिक्स्ड स्टाइलिश कोट्स -----------------
with panna1:
    st.markdown('<div class="love-sender-box"><span class="love-name">🎉 PRABHAT 🎉</span><br><span style="color:#ffb3cc; font-size:0.9rem; font-weight:bold;">Wishes Happy Birthday To His Lifeline</span><br><span class="love-receiver-name">💖 LAXMI 💖</span></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">Happy Birthday<br>My Love 🎂</h1>', unsafe_allow_html=True)
    st.markdown('<div class="romantic-badge badge-left">❤️ YOU ARE MY LIFE 🌹</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if main_photo:
            st.image(main_photo, use_container_width=True)
        else:
            st.image("https://unsplash.com", use_container_width=True)

    with col2:
        # ❤️ धड़कता हुआ शानदार मोटा दिल लेआउट
        st.markdown('<div class="beating-heart-container"><div class="heart-text">11 💖 YRS<br>OF 🌹 LOVE<br>MY 💍 WIFE<br>MY BABU<br>MY 💞 JAAN<br>MY 🚼 LIFE</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="romantic-badge badge-right">💝 YOU ARE MY EVERYTHING 🧸</div>', unsafe_allow_html=True)

    st.markdown('<div class="wishes-container">', unsafe_allow_html=True)
    
    # 20 मिक्स्ड हिंदी-इंग्लिश स्टाइलिश नियॉन कोट्स
    st.markdown('<div class="premium-wish-box"><span class="wish-heading">🌹 1. 11 Years Of Love</span><p class="wish-body">ग्यारह साल का ये सफर सिर्फ वक्त नहीं, It is the most beautiful journey of my life with you. 🌹</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="premium-wish-box"><span class="wish-heading">💖 2. Forever Mine</span><p class="wish-body">चेहरे पर आपके रहे हमेशा नूर, You are my forever love, no one can take you away from me. 💖</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="premium-wish-box"><span class="wish-heading">💍 3. To My Soulmate</span><p class="wish-body">भगवान से हर जन्म में सिर्फ तुम्हें ही मांगूंगा, You are my ultimate soulmate now and forever. 💍</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="premium-wish-box"><span class="wish-heading">🌸 4. Life Completed</span><p class="wish-body">तुम्हारे आने से खुशियों के सारे रंग भर गए, You completed my incomplete world so beautifully. 🌸</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="premium-wish-box"><span class="wish-heading">🏹 5. Deepest Love</span><p class="wish-body">दुनिया की कोई भी ताकत हमारे प्यार को कम नहीं कर सकती, My love for you grows deeper every single day. 🏹</p></div>', unsafe_allow_html=True)
    
