import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Function to send a scheduled email
def send_scheduled_email():
    # Ask the user for the recipient's email
    recipient_email = input("Enter the recipient's email address: ")

    # Ask the user for the date and time to send the email
    send_date = input("Enter the date (YYYY-MM-DD): ")
    send_time = input("Enter the time (HH:MM): ")

    # Combine the date and time
    send_datetime = datetime.strptime(f"{send_date} {send_time}", "%Y-%m-%d %H:%M")

    # Calculate the delay in seconds until the scheduled time
    delay_seconds = (send_datetime - datetime.now()).total_seconds()

    # Ensure that the scheduled time is in the future
    if delay_seconds <= 0:
        print("Please select a future date and time.")
        return

    # Ask the user for the email subject and message
    subject = input("Enter the email subject: ")
    message_body = input("Enter the email message: ")

    # Sender's email and password (use an App Password or an application-specific password for security)
    sender_email = "hgod61683"
    sender_password = "tnoi plcb pblj nhcy"  # Replace with your application-specific password

    # Create an SMTP connection and send the email after the delay
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        # Attach the message body
        message.attach(MIMEText(message_body, "plain"))

        # Schedule the email
        print(f"Scheduling email for {send_datetime}...")
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()

        print("Email scheduled successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    send_scheduled_email()
