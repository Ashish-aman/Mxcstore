import streamlit as st
import time
from PIL import Image
import base64

# Load and encode invitation image
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

image_path = 'demo.jpg'
invit_image_base64 = get_base64_image(image_path)

# Load and encode sound file
sound_path = 'crowd-cheer-in-school-auditorium-236699.mp3'
def get_base64_sound(sound_path):
    with open(sound_path, "rb") as sound_file:
        return base64.b64encode(sound_file.read()).decode()

sound_base64 = get_base64_sound(sound_path)

# Custom CSS for curtain animation with image and heavy styling for the invitation
st.markdown(
    f"""
    <style>
        @keyframes openCurtain {{
            0% {{ width: 50%; }}
            100% {{ width: 0%; opacity: 0; }}
        }}
        .curtain-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: space-between;
            z-index: 9999;
            pointer-events: none;
        }}
        .curtain-left, .curtain-right {{
            width: 50%;
            height: 100%;
            background-image: url('https://www.publicdomainpictures.net/pictures/300000/nahled/red-theater-curtain.jpg');
            background-size: cover;
            animation: openCurtain 2s forwards;
        }}
        .curtain-left {{ animation-delay: 0s; }}
        .curtain-right {{ animation-delay: 0s; }}
        .invitation-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
            padding: 20px;
            background: linear-gradient(to right, #ffefba, #ffffff);
            border-radius: 15px;
            box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);
        }}
        .invitation-container img {{
            border: 8px solid #800000;
            border-radius: 15px;
            transition: transform 0.5s ease-in-out;
        }}
        .invitation-container img:hover {{
            transform: scale(1.05);
        }}
    </style>
    <div class="curtain-container">
        <div class="curtain-left"></div>
        <div class="curtain-right"></div>
    </div>
    """,
    unsafe_allow_html=True
)

# Play sound effect
st.markdown(
    f"""
    <audio autoplay>
        <source src="data:audio/mp3;base64,{sound_base64}" type="audio/mp3">
    </audio>
    """,
    unsafe_allow_html=True
)

# Display image after animation delay
time.sleep(2)
st.markdown(
    f"""
    <div class="invitation-container">
        <img src="data:image/jpeg;base64,{invit_image_base64}" alt="Grand Opening Invitation" width="80%">
    </div>
    """,
    unsafe_allow_html=True
)

# Add a Stay Tuned message
st.markdown(
    """
    <div style="text-align: center; margin-top: 20px; font-size: 24px; font-weight: bold; color: green;">
        🎉 Stay tuned for updates on our new pharmacy website! 🎉
    </div>
    """,
    unsafe_allow_html=True
)
