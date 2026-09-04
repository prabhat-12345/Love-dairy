import streamlit as st
import os
import time

# 1. पेज की पूरी सेटिंग
st.set_page_config(page_title="Happy Birthday My Love!", page_icon="❤️", layout="wide")

# 2. लक्ज़री नियॉन थीम और तैरते हुए बलून्स का प्रीमियम CSS
custom_css = """
<style>
    .stApp {
        background: linear-gradient(135deg, #0d0003 0%, #1a0507 50%, #2b000a 100%);
        color: #ffffff;
        position: relative;
        overflow-x: hidden;
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
    
    /* 🌟 नियॉन शाइन विश बॉक्स डिज़ाइन */
    .wishes-container { margin-top: 25px; padding: 5px; }
    .premium-wish-box {
        background: rgba(15, 0, 5, 0.75); border: 2px solid #ff0055; padding: 16px; border-radius: 16px; margin-bottom: 20px;
        box-shadow: 0 0 15px #ff0055, inset 0 0 10px rgba(255, 0, 85, 0.3);
        animation: pulseNeon 3s ease-in-out infinite alternate;
    }
    @keyframes pulseNeon {
        0% { box-shadow: 0 0 10px #ff0055, inset 0 0 5px rgba(255, 0, 85, 0.2); border-color: #ff0055; }
        100% { box-shadow: 0 0 22px #ff3385, inset 0 0 15px rgba(255, 51, 133, 0.5); border-color: #ff3385; }
    }
    .wish-heading {
        font-family: 'Georgia', serif; font-weight: bold; color: #ffd700; font-size: 1.15rem;
        text-shadow: 0 0 10px #ffd700, 0 0 5px #ff0055; margin-bottom: 6px; display: block;
    }
    .wish-body { font-size: 1.02rem; line-height: 1.6; color: #ffffff; text-shadow: 0 0 2px rgba(255,255,255,0.5); }
    
    /* 🎈 तैरते बलून्स का बैकग्राउंड एरिया */
    .balloon-area { position: fixed; bottom: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none; }
    
    /* प्रीमियम स्लाइड बटन्स */
    .stButton>button {
        width: 100% !important;
        background: linear-gradient(45deg, #ff0055, #ff3377) !important;
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

# 🎈 बैकग्राउंड में तैरते हुए बलून इंजेक्ट करने का स्क्रिप्ट
balloons_html = """
<div class="balloon-area">
    <script>
        function createBalloon() {
            const colors = ['#ff0055', '#ff3385', '#ff66a3', '#ff00aa'];
            const balloon = document.createElement('div');
            balloon.style.position = 'fixed'; balloon.style.bottom = '-100px';
            balloon.style.width = Math.random() * 30 + 20 + 'px'; balloon.style.height = balloon.style.width;
            balloon.style.borderRadius = '50% 50% 50% 50% / 40% 40% 60% 60%';
            balloon.style.background = colors[Math.floor(Math.random() * colors.length)];
            balloon.style.boxShadow = 'inset -5px -5px 10px rgba(0,0,0,0.2), 0 0 10px ' + balloon.style.background;
            balloon.style.left = Math.random() * 100 + 'vw'; balloon.style.opacity = Math.random() * 0.5 + 0.4;
            balloon.style.zIndex = '-1'; balloon.style.transition = 'transform ' + (Math.random() * 4 + 6) + 's linear, opacity 2s';
            document.body.appendChild(balloon);
            setTimeout(() => { balloon.style.transform = 'translateY(-120vh) translateX(' + (Math.random() * 100 - 50) + 'px)'; }, 50);
            setTimeout(() => { balloon.remove(); }, 10000);
        }
        setInterval(createBalloon, 800);
    </script>
</div>
"""
st.markdown(balloons_html, unsafe_allow_html=True)

# म्यूजिक ट्रैक सिलेक्शन लॉजिक
if 'active_track' not in st.session_state:
    st.session_state.active_track = "https://soundhelix.com"

st.components.v1.html(f"""
<audio id="bg-audio" loop autoplay src="{st.session_state.active_track}"></audio>
<script>
    var audio = window.parent.document.getElementById('bg-audio') || document.getElementById('bg-audio');
    function triggerPlay() {{
        if (audio && audio.paused) {{
            audio.play().catch(e => console.log("Interaction required"));
        }}
    }}
    window.parent.document.addEventListener('click', triggerPlay, {{ once: true }});
    window.parent.document.addEventListener('touchstart', triggerPlay, {{ once: true }});
    if(audio) {{ audio.play(); }}
</script>
""", height=0)

# ऑटोमैटिक इमेज डिटेक्शन सिस्टम
all_files = os.listdir(".")
all_images = [f for f in all_files if f.lower().endswith((".jpeg", ".jpg", ".png", ".webp")) and f.lower() != "app.py"]
main_photo = all_images if len(all_images) > 0 else None
album_photos = all_images if len(all_images) > 0 else ["https://unsplash.com"]

panna1, panna2, panna3 = st.tabs(["🏠 मुख्य पन्ना", "🎵 म्यूजिक रूम", "📸 फोटो एल्बम"])

# ----------------- पन्ना 1: होम और पूरे 20 नियॉन कोट्स -----------------
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
        st.markdown('<div style="display: flex; flex-direction: column; justify-content: center; align-items: center; border: 2px solid #ff0055; border-radius: 50%; width: 140px; height: 140px; margin: 30px auto 0 auto; background: rgba(255,0,85,0.1); box-shadow: 0 0 20px #ff0055; font-family: \'Georgia\', serif; font-size: 0.8rem; font-weight: bold; color: #ffffff; text-align: center; line-height: 1.4; transform: rotate(-15deg);">11 💖 YRS<br>OF 🌹 LOVE<br>MY 💍 WIFE<br>MY BABU<br>MY 💞 JAAN<br>MY 🚼 LIFE</div>', unsafe_allow_html=True)

    st.markdown('<div class="romantic-badge badge-right">💝 YOU ARE MY EVERYTHING 🧸</div>', unsafe_allow_html=True)

    # 🌟 सुरक्षित डायरेक्ट रेंडरर - यहाँ पूरे 20 कोट्स को बिना किसी कोडिंग एरर के नियॉन बॉक्स में लॉक कर दिया है
