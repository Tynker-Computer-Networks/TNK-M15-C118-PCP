# Import smtplib, MIMEText, MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create class SecretSanta App
class SecretSanta():
    def __init__(self):
        super().__init__()
        
    # Define meethod to send single email
    def send_email(self):
        try:
            sender_email = input("Enter Sender Email\n")
            password = input("Enter Sender Password\n")
            recipient_name = input("Enter Recipient Name\n")
            recipient_email = input("Enter Recipient Email\n")
            wishlist = input("Enter Comma Seperated Wihslist\n")
            assigned_to = input("Enter Participent Name to assign\n")

            # Send mail using SMTP server
            smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
            smtp_server.starttls()
            smtp_server.login(sender_email, password)

            subject = "Your Secret Santa Assignment"
            msg_body = f"Hello {recipient_name},\n\nYour Secret Santa assignment is: {assigned_to}\n\nWishlist: {wishlist}"

            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = subject
            message.attach(MIMEText(msg_body, "plain"))

            smtp_server.sendmail(sender_email, recipient_email, message.as_string())
            smtp_server.quit()

            print("Email Sent", "Email sent successfully!")


        except Exception as e:
            print("Error",f"An error occurred:{str(e)}")


# Define function main and call class EmailSenderApp()
def main():
    app = SecretSanta()
    app.send_email()

# Call main() function
if __name__ == "__main__":
    main()