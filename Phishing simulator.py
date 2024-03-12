from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Function to simulate sending the phishing email
def send_phishing_email():
    email_subject = "Urgent: Unusual Sign-in Activity Detected!"
    email_body = """\
Dear User,

We've detected an unusual sign-in attempt to your account from a new device. For your security, please verify your identity by clicking on the link below:

http://127.0.0.1:5000/

If you did not make this attempt, please change your password immediately.

Best,
Your Security Team
"""

    print("Sending phishing simulation email...")
    print(f"Subject: {email_subject}\n")
    print(email_body)
    # Here you would use smtplib to send an email if doing so for real, but we're just printing for this simulation.

# Define a route for the fake login page
@app.route('/')
def fake_login():
    # In a real educational setup, you would serve a page that looks like a login but doesn't actually collect data.
    return "This is a simulated phishing page. In a real scenario, this page would look like a legitimate login page to trick users into entering their credentials."

# Main function to run the Flask app and simulate email sending
if __name__ == '__main__':
    send_phishing_email()  # Simulate sending the phishing email at startup
    app.run(debug=True)  # Start the Flask app