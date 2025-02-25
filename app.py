import streamlit as st
import time
from PIL import Image
import base64

# Load invitation image
image_path = 'demo.jpg'
invit_image = Image.open(image_path)

# Load and encode sound file
sound_path = 'crowd-cheer-in-school-auditorium-236699.mp3'
def get_base64_sound(sound_path):
    with open(sound_path, "rb") as sound_file:
        sound_base64 = base64.b64encode(sound_file.read()).decode()
    return f"data:audio/mp3;base64,{sound_base64}"
sound_base64 = get_base64_sound(sound_path)

# Custom CSS for curtain animation with image
st.markdown(
    """
    <style>
        @keyframes openCurtain {
            0% { width: 50%; }
            100% { width: 0%; }
        }
        .curtain-left, .curtain-right {
            position: fixed;
            top: 0;
            width: 50%;
            height: 100%;
            background-image: url('https://www.publicdomainpictures.net/pictures/300000/nahled/red-theater-curtain.jpg');
            background-size: cover;
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

# Play sound effect
st.markdown(
    f"""
    <audio autoplay>
        <source src="{sound_base64}" type="audio/mp3">
    </audio>
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
