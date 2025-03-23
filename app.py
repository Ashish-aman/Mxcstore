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
    
    # Use a clickable Markdown button to open in a new tab
    st.markdown(f'<a href="{order_link}" target="_blank"><button style="background-color:green; color:white; padding:10px; font-size:16px;">Order Now</button></a>', unsafe_allow_html=True)

    
    # if st.button("Order Now"):
    #     st.markdown(f'<meta http-equiv="refresh" content="0; url={order_link}">', unsafe_allow_html=True)

    
    st.subheader("📲 Order via WhatsApp")
    whatsapp_link = "https://wa.me/918709290845"
    
    # Use a clickable Markdown button to open in a new tab
    st.markdown(f'<a href="{whatsapp_link}" target="_blank"><button style="background-color:green; color:white; padding:10px; font-size:16px;"> Order via WhatsApp</button></a>', unsafe_allow_html=True)

    # if st.button("Chat on WhatsApp"):

        
    #     open_link("")

    
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

    
    import streamlit as st
    import plotly.graph_objects as go
    import os
    import smtplib
    from email.message import EmailMessage
    from twilio.rest import Client
    import matplotlib.pyplot as plt
    

    
    # Email Credentials
    EMAIL_RECEIVER = "your_email@gmail.com"
    EMAIL_PASSWORD = "koirvpslnvewsdpf"
    EMAIL_SENDER = "m22ma002@alumni.iitj.ac.in" 
    
    # Function to send WhatsApp Message
    def send_whatsapp_message(phone_number, message):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=message,
            to=f"whatsapp:{phone_number}"
        )
        return message.sid
    
    # Function to send Email with Attachment
    def send_email(subject, body, recipient_email, attachment_path):
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_SENDER
        msg["To"] = recipient_email
        msg.set_content(body)
    
        # Attach Image
        with open(attachment_path, "rb") as f:
            msg.add_attachment(f.read(), maintype="image", subtype="png", filename="BMI_Graph.png")
    
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
    
    # Function to Create and Save BMI Graph
    def create_bmi_graph(bmi, category):
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.barh(["Underweight", "Normal", "Overweight", "Obese"], [18.5, 24.9, 29.9, 40], color=["blue", "green", "orange", "red"])
        ax.axvline(bmi, color="black", linestyle="--", linewidth=2)
        ax.set_title(f"BMI: {bmi} ({category})")
        ax.set_xlabel("BMI Value")
        
        graph_path = "bmi_graph.png"
        plt.savefig(graph_path)
        return graph_path
    
    # Streamlit UI
    st.title("⚖️ BMI Calculator")
    
    # User Input
    user_phone = st.text_input("Enter Your WhatsApp Number (With Country Code)")
    user_email = st.text_input("Enter Your Email Address")
    height_cm = st.number_input("Enter Height (cm)", min_value=100, max_value=250, step=1)
    weight_kg = st.number_input("Enter Weight (kg)", min_value=20, max_value=200, step=1)
    
    if st.button("📊 Calculate BMI & Send Results"):
        if user_phone and user_email:
            height_m = height_cm / 100  # Convert cm to meters
            bmi = round(weight_kg / (height_m ** 2), 2)
            st.metric("Your BMI", bmi)
    
            # Determine BMI Category
            if bmi < 18.5:
                category, color = "Underweight", "blue"
            elif 18.5 <= bmi < 25:
                category, color = "Normal Weight", "green"
            elif 25 <= bmi < 30:
                category, color = "Overweight", "orange"
            else:
                category, color = "Obese", "red"
    
            st.success(f"**Category:** {category}")
    
            # BMI Gauge Chart
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=bmi,
                title={"text": "BMI Indicator"},
                gauge={
                    "axis": {"range": [10, 40]},
                    "steps": [
                        {"range": [10, 18.5], "color": "blue"},
                        {"range": [18.5, 25], "color": "green"},
                        {"range": [25, 30], "color": "orange"},
                        {"range": [30, 40], "color": "red"},
                    ],
                    "bar": {"color": color}
                }
            ))
    
            st.plotly_chart(fig)
    
            # Generate and Save BMI Graph
            graph_path = create_bmi_graph(bmi, category)
    
            # WhatsApp Message
            message_body = f"Hello! Your BMI result is **{bmi} ({category})**."
            try:
                send_whatsapp_message(user_phone, message_body)
                st.success("✅ BMI result sent to WhatsApp!")
            except Exception as e:
                st.error(f"❌ WhatsApp Message Failed: {e}")
    
            # Email with Attachment
            email_subject = "Your BMI Result"
            email_body = f"Your BMI is {bmi}, which falls under the category '{category}'. Check the attached BMI graph."
            try:
                send_email(email_subject, email_body, user_email, graph_path)
                st.success("✅ BMI result sent via Email with graph attached!")
            except Exception as e:
                st.error(f"❌ Email Sending Failed: {e}")
    
        else:
            st.warning("⚠️ Please enter both your WhatsApp number and Email before submitting!")
    

    import streamlit as st
    import smtplib
    from email.message import EmailMessage
    
    # Email Credentials (Replace with your email credentials)
    EMAIL_PASSWORD = "koirvpslnvewsdpf"
    EMAIL_SENDER = "m22ma002@alumni.iitj.ac.in"
    
    # Function to send Email
    def send_email(subject, body, recipient_email):
        try:
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = EMAIL_SENDER
            msg["To"] = recipient_email
            msg["Reply-To"] = EMAIL_SENDER
            msg.set_content(body)

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                server.send_message(msg)
            return "Email Sent Successfully!"
        except Exception as e:
            return f"Email sending failed: {e}"
    
    # Streamlit UI
    st.subheader("📅 Book Slot for BP/Sugar/diabetes testing")
    
    # User Input
    name = st.text_input("Name")
    email = st.text_input("Email Address")
    date = st.date_input("Select Date")
    time = st.time_input("Select Time")
    
    if st.button("📩 Book Now & Send Email Confirmation"):
        if name and email:
            booking_details = f"""
            Hello {name}, 
            Your test slot is confirmed. 
            
            📅 Date: {date}  
            ⏰ Time: {time}  
            
            Thank you for booking!
            """
    
            # Send Email Confirmation
            email_status = send_email("Slot Booking Confirmation", booking_details, email)
            if "failed" not in email_status:
                st.success("✅ Email Confirmation Sent!")
            else:
                st.error(email_status)
    
            st.success("🎉 Slot booked successfully!")
        else:
            st.warning("⚠️ Please fill all details (Name & Email) before booking!")


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
    st.write("📞 **Phone:** +91 9939135365")
    st.write("📧 **Email:** contact@maxicurepharma.com")
    st.markdown("[View on Google Maps](https://maps.app.goo.gl/BMbeGKBMJ8gpDNA8A)")
    # Google Maps Embed
    map_html = """
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3608.815428920425!2d86.98605377538331!3d25.243140877681476!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39f049726e7f9489%3A0x41e3a05da0e7ce15!2sMaxicure%20Pharma%20Pvt.%20Ltd.!5e0!3m2!1sen!2sin!4v1742763130395!5m2!1sen!2sin"
    width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    """
    
    st.components.v1.html(map_html, height=450)

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
