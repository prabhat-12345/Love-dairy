import streamlit as st
import os
import time

# 1. पेज की सेटिंग
st.set_page_config(page_title="Happy Birthday My Love!", page_icon="❤️", layout="wide")

# 2. प्रीमियम कस्टमाइज CSS थीम
custom_css = """
<style>
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
    .love-sender-box {
        text-align: center;
        margin-top: 5px;
        margin-bottom: 12px;
        line-height: 1.4;
    }
    .love-name {
        font-family: 'Georgia', serif;
        font-size: 2rem;
        font-weight: bold;
        text-transform: uppercase;
        background: linear-gradient(45deg, #ffd700, #ff00b3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 15px rgba(255, 128, 179, 0.6);
        display: inline-block;
    }
    .love-receiver-name {
        font-family: 'Georgia', serif;
        font-size: 2.2rem;
        font-weight: bold;
        text-transform: uppercase;
        background: linear-gradient(45deg, #ff0055, #ff00b3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 20px #ff0055, 0px 0px 10px #ff00b3;
        display: inline-block;
    }
    .romantic-badge {
        font-family: 'Georgia', serif;
        font-size: 1.2rem;
        font-weight: bold;
        text-align: center;
        margin: 10px auto;
        padding: 5px 15px;
        border-radius: 50px;
        background: rgba(255, 0, 85, 0.1);
        border: 1px solid rgba(255, 0, 85, 0.3);
        width: fit-content;
    }
    .badge-left { color: #ff0055; text-shadow: 0 0 8px #ff0055; }
    .badge-right { color: #ffd700; text-shadow: 0 0 8px #ffd700; }
    .stImage img {
        border-radius: 20px !important;
        border: 2px solid rgba(255, 0, 85, 0.5) !important;
        box-shadow: 0 0 25px rgba(255, 0, 85, 0.7) !important;
    }
    .wishes-container {
        margin-top: 25px;
        padding: 5px;
    }
    .premium-wish-box {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 0, 85, 0.2);
        border-left: 4px solid #ff0055;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .wish-heading {
        font-family: 'Georgia', serif;
        font-weight: bold;
        color: #ffd700;
        font-size: 1.1rem;
        text-shadow: 0 0 8px rgba(255, 215, 0, 0.4);
        margin-bottom: 5px;
        display: block;
    }
    .wish-body {
        font-size: 1rem;
        line-height: 1.5;
        color: #ffe6ed;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 51, 119, 0.1) !important;
        border: 1px solid rgba(255, 51, 119, 0.3) !important;
        border-radius: 15px !important;
        padding: 6px 12px !important;
        color: #ffb3cc !important;
        font-weight: bold !important;
        font-size: 0.9rem !important;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(45deg, #ff0055, #ff3377) !important;
        color: white !important;
        border: 1px solid #ffd700 !important;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.5) !important;
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

# ऑटोमैटिक इमेज डिटेक्शन
all_files = os.listdir(".")
all_images = [f for f in all_files if f.lower().endswith((".jpeg", ".jpg", ".png", ".webp")) and f.lower() != "app.py"]

main_photo = all_images if len(all_images) > 0 else None
album_photos = all_images if len(all_images) > 0 else ["https://unsplash.com"]

# 4. डायरी के अलग-अलग पन्ने (Tabs System)
panna1, panna2, panna3 = st.tabs(["🏠 मुख्य पन्ना", "🎵 म्यूजिक रूम", "📸 फोटो एल्बम"])

# ----------------- पन्ना 1: होम और पूरे 20 प्रीमियम कोट्स -----------------
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
        circle_html = """
        <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; border: 2px solid #ff0055; border-radius: 50%; width: 140px; height: 140px; margin: 30px auto 0 auto; background: rgba(255,0,85,0.1); box-shadow: 0 0 20px #ff0055; font-family: 'Georgia', serif; font-size: 0.8rem; font-weight: bold; color: #ffffff; text-align: center; line-height: 1.4; transform: rotate(-15deg);">
            11 💖 YRS<br>OF 🌹 LOVE<br>MY 💍 WIFE<br>MY BABU<br>MY 💞 JAAN<br>MY 🚼 LIFE
        </div>
        """
        st.markdown(circle_html, unsafe_allow_html=True)

    st.markdown('<div class="romantic-badge badge-right">💝 YOU ARE MY EVERYTHING 🧸</div>', unsafe_allow_html=True)

    # पूरे 20 प्रीमियम कोट्स बिना किसी पायथन डिक्शनरी या लिस्ट ब्रैकेट के (डायरेक्ट रेंडर)
    st.markdown('<div class="wishes-container">', unsafe_allow_html=True)
    
    st.markdown('<div class="premium-wish-box"><span class="wish-heading">🌹 1. 11 Years Of Love</span><p class="wish-body">ग्यारह साल का ये सफर सिर्फ वक्त नहीं, मेरी जिंदगी की सबसे हसीन यादें हैं।</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="premium-wish-box"><span class="wish-heading">💖 2. Forever Mine</span><p class="wish-body">तुम कल भी मेरी लाइफलाइन थीं, आज भी हो और हमेशा रहोगी।</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="premium-wish-box"><span class="wish-heading">💍 3. To My Soulmate</span><p class="wish-body">भगवान से हर जन्म में सिर्फ तुम्हें ही अपनी हमसफर के रूप में मांगूंगा।</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="premium-wish-box"><span class="wish-heading">🌸 4. Adhoori Zindagi Poori Hui</span><p class="wish-body">तुम्हारे आने से मेरी जिंदगी में खुशियों के सारे रंग भर गए।</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="premium-wish-box"><span class="wish-heading">🏹 5. Deepest Love</span><p class="wish-body">दुनिया की कोई भी ताकत तुम्हारे लिए मेरे प्यार को कम नहीं कर सकती।</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="premium-wish-box"><span class="wish-heading">👑 6. Meri Manzil</span><p class="wish-body">तुम्हारे साथ बिताया हर एक पल मेरे लिए किसी त्योहार से कम नहीं है।</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="premium-wish-box"><span class="wish-heading">🤍 7. Queen of My Heart</span><p class="wish-body">तुम मेरे दिल की वो रानी हो जिसका राज इस दिल पर हमेशा रहेगा।</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="premium-wish-box"><span class="wish-heading">♾️ 8. Rooh Ka Rishta</span><p class="wish-body">हमारी रिश्ता सिर्फ जिस्म का नहीं, बल्कि रู้ से रूह का जुड़ाव है।</p></div>', unsafe_allow_html=True)
    
