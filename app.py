import streamlit as st
import time
from PIL import Image

# Load invitation image
image_path = 'demo.jpg'
invit_image = Image.open(image_path)

# Custom CSS for curtain animation
st.markdown(
    """
    <style>
        @keyframes openCurtain {
            0% { width: 100%; }
            100% { width: 0%; }
        }
        .curtain-left, .curtain-right {
            position: fixed;
            top: 0;
            width: 50%;
            height: 100%;
            background: #800000;
            z-index: 9999;
        }
        .curtain-left { left: 0; animation: openCurtain 2s forwards; }
        .curtain-right { right: 0; animation: openCurtain 2s forwards; }
    </style>
    <div class="curtain-left"></div>
    <div class="curtain-right"></div>
    """,
    unsafe_allow_html=True
)

# Display image after animation delay
time.sleep(2)
st.image(invit_image, caption='Grand Opening Invitation', use_column_width=True)

# Add a Stay Tuned message
st.markdown("""
    <div style="text-align: center; margin-top: 20px; font-size: 24px; font-weight: bold; color: green;">
        🎉 Stay tuned for updates on our new pharmacy website! 🎉
    </div>
""", unsafe_allow_html=True)
