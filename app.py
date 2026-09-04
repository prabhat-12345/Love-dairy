import streamlit as st
import os
import time

# 1. पेज की पूरी सेटिंग
st.set_page_config(page_title="Happy Birthday My Love!", page_icon="❤️", layout="wide")

# 2. सीक्रेट पासवर्ड लॉक स्क्रीन
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

# म्यूजिक प्लेयर स्टेट लॉजिक
if 'active_track' not in st.session_state:
    st.session_state.active_track = "https://soundhelix.com"

# ऑटोमैटिक इमेज लोडिंग सिस्टम
all_files = os.listdir(".")
all_images = [f for f in all_files if f.lower().endswith((".jpeg", ".jpg", ".png", ".webp")) and f.lower() != "app.py"]

main_photo = all_images if len(all_images) > 0 else None
album_photos = all_images if len(all_images) > 0 else ["https://unsplash.com"]

# डायरी के अलग-अलग पन्ने (Tabs System)
panna1, panna2, panna3 = st.tabs(["🏠 मुख्य पन्ना", "🎵 म्यूजिक रूम", "📸 फोटो एल्बम"])

# ----------------- पन्ना 1: होम और पूरे 20 कोट्स -----------------
with panna1:
    st.markdown("### 🎉 PRABHAT Wishes Happy Birthday To His Lifeline LAXMI 💖")
    st.subheader("Happy Birthday My Love 🎂")
    
    # इमेज लेआउट (गिटहब फोल्डर की पहली इमेज अपने आप उठाएगा)
    if main_photo:
        st.image(main_photo, use_container_width=True)
    else:
        st.image("https://unsplash.com", use_container_width=True)
        
    st.info("❤️ 11 YRS OF LOVE | MY WIFE | MY BABU | MY JAAN | MY LIFE ❤️")

    # पूरे 20 कोट्स बिना किसी बड़े कोडिंग ब्रैकेट के (बिल्कुल सेफ)
    st.success("🌹 1. 11 Years Of Love: ग्यारह साल का ये सफर सिर्फ वक्त नहीं, मेरी जिंदगी की सबसे हसीन यादें हैं।")
    st.success("💖 2. Forever Mine: तुम कल भी मेरी लाइफलाइन थीं, आज भी हो और हमेशा रहोगी।")
    st.success("💍 3. To My Soulmate: भगवान से हर जन्म में सिर्फ तुम्हें ही अपनी हमसफर के रूप में मांगूंगा।")
    st.success("🌸 4. Adhoori Zindagi Poori Hui: तुम्हारे आने से मेरी जिंदगी में खुशियों के सारे रंग भर गए।")
    st.success("🏹 5. Deepest Love: दुनिया की कोई भी ताकत तुम्हारे लिए मेरे प्यार को कम नहीं कर सकती।")
    st.success("👑 6. Meri Manzil: तुम्हारे साथ बिताया हर एक पल मेरे लिए किसी त्योहार से कम नहीं है।")
    st.success("🤍 7. Queen of My Heart: तुम मेरे दिल की वो रानी हो जिसका राज इस दिल पर हमेशा रहेगा।")
    st.success("♾️ 8. Rooh Ka Rishta: हमारा रिश्ता सिर्फ जिस्म का नहीं, बल्कि रूह से रूह का जुड़ाव है।")
    st.success("🥰 9. My Lifeline: तुम्हारे चेहरे की मुस्कान ही मेरे जीने की सबसे बड़ी वजह है।")
    st.success("🌟 10. Aakhiri Wada: हाथ थाम के कहता हूँ, आखिरी सांस तक सिर्फ तुमसे ही बेइंतहा मोहब्बत करूँगा।")
    st.success("🌹 11. Togetherness Power: हमारा यह सफर मेरी पूरी जिंदगी की सबसे खूबसूरत सच्चाई है।")
    st.success("🧎 12. Eternal Glow: चेहरे पर आपके रहे हमेशा नूर, खुदा कभी न करे हमसे आपको दूर... Happy Birthday Jaan!")
    st.success("🏹 13. Heartbeat Track: You are the beat of my heart, the smile on my face, and the spark in my life. I love you endlessly.")
    st.success("🌸 14. Completeness: तुम्हारे बिना मेरी सुबह और मेरी शाम अधूरी है, सच कहूँ तो लक्ष्मी, तुम्हारे बिना मेरी पूरी जान अधूरी है!")
    st.success("🌟 15. Unmatched Bond: In all the world, there is no heart for me like yours. In all the world, there is no love for you like mine.")
    st.success("🎂 16. Meri Mannat Dua: खुदा से जब भी मैंने कोई दुआ मांगी है, हर दुआ में सिर्फ और सिर्फ तुम्हारी लंबी उम्र और खुशी मांगी है।")
    st.success("🤍 17. Queen of My World: You are my today, my tomorrow, and my forever. Happy Birthday to the queen of my world!")
    st.success("♾️ 18. Unchanged Devotion: 11 साल में वक्त बदला, दुनिया बदली, पर इस दिल में लक्ष्मी के लिए धड़कन और मोहब्बत कभी नहीं बदली।")
    st.success("💍 19. Lifetime Commitment: सात फेरों के वो वादे और हाथ थामने का वो पल... मेरी आखिरी सांस तक मैं सिर्फ तुम्हारा बनकर रहूँगा।")
    st.success("🥰 20. Ultimate Smile Joy: जब तुम मुस्कुराती हो तो ऐसा लगता है जैसे पूरी दुनिया की खुशियां मेरे आँगन में सिमट आई हों।")
    st.snow()

# ----------------- पन्ना 2: म्यूजिक रूम -----------------
with panna2:
    st.markdown("#### 🎵 बैकग्राउंड गाना")
    st.audio(st.session_state.active_track, format="audio/mp3")
    
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        if st.button("🎵 धुन 1 चालू करें"):
            st.session_state.active_track = "https://soundhelix.com"
            st.rerun()
        if st.button("🎵 धुन 2 चालू करें"):
            st.session_state.active_track = "https://soundhelix.com"
            st.rerun()
    with col_m2:
        if st.button("🎵 धुन 3 चालू करें"):
            st.session_state.active_track = "https://soundhelix.com"
            st.rerun()
        if st.button("🤫 संगीत बंद करें"):
            st.session_state.active_track = ""
            st.rerun()

# ----------------- पन्ना 3: फोटो एल्बम -----------------
with panna3:
    st.markdown("#### 📸 यादों का एल्बम (आगे-पीछे बटन दबाकर देखें)")
    if 'current_slide' not in st.session_state:
        st.session_state.current_slide = 0
        
    total_pics = len(album_photos)
    current_img = album_photos[st.session_state.current_slide % total_pics]
    st.image(current_img, use_container_width=True)
    
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        if st.button("⬅️ पीछे"):
            st.session_state.current_slide = (st.session_state.current_slide - 1) % total_pics
            st.rerun()
    with col_b2:
        if st.button("आगे ➡️"):
            st.session_state.current_slide = (st.session_state.current_slide + 1) % total_pics
            st.rerun()
            
