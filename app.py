import streamlit as st
import pandas as pd
import base64
import webbrowser
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
def open_link(url):
    webbrowser.open_new_tab(url)

# Custom futuristic CSS
def set_style():
    st.markdown(
        """
        <style>
        body {
            background-color: #0d1117;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background: linear-gradient(135deg, #1e90ff, #00bfff);
            color: white;
            border-radius: 10px;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
        }
        .stDataFrame {
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Sidebar Navigation
st.sidebar.title("Maxicure Pharma")
menu = ["Home", "Services", "Products", "Contact Us", "Review Box", "Blogs"]
choice = st.sidebar.radio("Menu", menu)

# Home Section
if choice == "Home":
    set_style()
    st.title("Welcome to Maxicure Pharma")
    col1, col2, col3 = st.columns(3)
    col1.metric("Customers Served", "5,000+")
    col2.metric("Orders Processed", "10,000+")
    col3.metric("Satisfied Clients", "98.5%")

# Services Section
elif choice == "Services":
    set_style()
    st.title("Our Services")
    
    import streamlit as st
    
    st.subheader("🛒 Order Online")
    
    order_link = "https://vyaparapp.in/store/maxicurepharma1"
    
    if st.button("Order Now"):
        st.markdown(f'<meta http-equiv="refresh" content="0; url={order_link}">', unsafe_allow_html=True)

    
    st.subheader("📲 Order via WhatsApp")
    if st.button("Chat on WhatsApp"):
        open_link("https://wa.me/918709290845")

    
    import streamlit as st
    from twilio.rest import Client
    import smtplib
    import os
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    # Twilio Credentials
    TWILIO_ACCOUNT_SID = TWILIO_ACCOUNT_SID
    TWILIO_AUTH_TOKEN = TWILIO_AUTH_TOKEN
    TWILIO_WHATSAPP_NUMBER = "+15392811447"  # Twilio WhatsApp sender number

    # Email Credentials
    EMAIL_RECEIVER = "your_email@gmail.com"
    EMAIL_PASSWORD = "koirvpslnvewsdpf"
    EMAIL_SENDER = "m22ma002@alumni.iitj.ac.in"  # Owner's Email

    # WhatsApp Owner Number
    # OWNER_WHATSAPP_NUMBER = "whatsapp:+917085758803"

    # Function to Send WhatsApp Message
    def send_whatsapp_message(receiver_number, message_body):
        try:
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            message = client.messages.create(
                from_=TWILIO_WHATSAPP_NUMBER,
                to=receiver_number,
                body=message_body
            )
            return True
        except Exception as e:
            st.error(f"❌ WhatsApp message failed: {str(e)}")
            return False

    # Function to Send Email with Attachment
    def send_email(subject, body, attachment_path, user_email):
        try:
            msg = MIMEMultipart()
            msg["From"] = EMAIL_SENDER  # Your business email
            msg["To"] = user_email  # Owner's email
            msg["Subject"] = subject
            msg["Reply-To"] = EMAIL_SENDER  # User's email for replies

            msg.attach(MIMEText(body, "plain"))

            # Attach File
            if attachment_path:
                with open(attachment_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment_path)}")
                    msg.attach(part)

            # Send Email via Business Email
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)  # Your email credentials
            server.sendmail(EMAIL_SENDER, user_email, msg.as_string())
            server.sendmail(EMAIL_SENDER, EMAIL_SENDER, msg.as_string())
            server.quit()

            return True
        except Exception as e:
            st.error(f"❌ Email failed: {str(e)}")
            return False


    # Streamlit App
    st.subheader("📜 Upload Prescription")

    user_phone = st.text_input("Enter Your WhatsApp Number (With Country Code)", "+91")
    user_email = st.text_input("Enter Your Email ID")

    uploaded_file = st.file_uploader("Upload your prescription", type=["png", "jpg", "pdf"])

    if uploaded_file and st.button("Submit"):
        # Save File Locally
        file_path = os.path.join("uploads", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # WhatsApp Message
        message_body = f"Hello! Your prescription has been received. Our team will process it soon."
        send_whatsapp_message(user_phone, message_body)  # To User
        # send_whatsapp_message(TWILIO_WHATSAPP_NUMBER, f"New Prescription Received from {user_phone}")  # To Owner

        # Send Email
        email_subject = "New Prescription Uploaded"
        email_body = f"Prescription received from: {user_email} ({user_phone})"
        send_email(email_subject, email_body, file_path, user_email)

        st.success("✅ Prescription sent to WhatsApp & Email successfully!")

    
    st.subheader("⚖️ BMI Calculator")
    height = st.number_input("Enter Height (cm)", min_value=100, max_value=250, step=1)
    weight = st.number_input("Enter Weight (kg)", min_value=20, max_value=200, step=1)
    if st.button("Calculate BMI"):
        bmi = round(weight / ((height / 100) ** 2), 2)
        st.metric("Your BMI", bmi)
        st.success("BMI sent to WhatsApp!")
        # Send BMI result via WhatsApp API

    st.subheader("📅 Book Slot for BP/Glucometer")
    name = st.text_input("Name")
    mobile = st.text_input("Mobile Number")
    date = st.date_input("Select Date")
    time = st.time_input("Select Time")
    if st.button("Book Now"):
        # send_email(email_subject, email_body, file_path, user_email)
        st.success("Slot booked successfully!")
        # Send booking details via WhatsApp & Email

# Products Section
elif choice == "Products":
    set_style()
    st.title("Our Products")
    categories = ["OTC Products", "Diabetes Care", "Veterinary Meds", "Other Products"]
    category = st.selectbox("Select a Category", categories)
    st.write(f"### {category} Available:")
    # Display products dynamically (fetch from database)

# Contact Us Section
elif choice == "Contact Us":
    set_style()
    st.title("Contact Us")
    st.write("📍 **Location:** Maxicure Pharma, Mumbai, India")
    st.write("📞 **Phone:** +91 99999 99999")
    st.write("📧 **Email:** contact@maxicurepharma.com")
    st.markdown("[View on Google Maps](https://goo.gl/maps/example)")

# Review Box Section
elif choice == "Review Box":
    set_style()
    st.title("Customer Reviews")
    st.write("Fetching reviews from Google Business...")
    # Fetch & display real-time reviews (API integration required)

# Blogs Section
elif choice == "Blogs":
    set_style()
    st.title("Maxicure Pharma Blog")
    blog_title = st.text_input("Blog Title")
    blog_content = st.text_area("Write your blog here...")
    if st.button("Publish Blog"):
        st.success("Blog published successfully!")
        # Store blog in a database

st.sidebar.write("Powered by Maxicure Pharma 🚀")
