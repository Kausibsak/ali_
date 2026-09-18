
import streamlit as st

st.set_page_config(page_title="My Mama ❤️", page_icon="❤️")

st.markdown("""
<style>
.stApp {
    background-color: #fff0f0;
}
h1, h2, h3 {
    color: #c00000;
}
</style>
""", unsafe_allow_html=True)

st.title("❤️ My Beautiful Mama ❤️")
st.subheader("Welcome to Mama's Special Website 🌹")

st.write("""
Mama meri zindagi ki sab se pyari aur special shakhsiyat hain.
Unki mohabbat aur care mere liye bohat qeemti hai. ❤️
""")

st.divider()

st.header("❤️ About My Mama")
st.write("""
Meri Mama bohat caring, loving aur kind hain.
Woh hamesha apni family ka khayal rakhti hain. 🌹
""")

st.header("🌹 Mama Ki Khoobiyan")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("❤️ Loving")

with col2:
    st.info("🌹 Caring")

with col3:
    st.warning("✨ Kind")

st.divider()

st.header("💌 A Special Message")
st.success("Mama, I Love You So Much! ❤️🌹")

st.divider()

st.caption("🌸 Made with love for my Mama 🌸")
