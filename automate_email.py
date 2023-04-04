import smtplib

# Define the email parameters
from_address = "sender@example.com"
to_address = "recipient@example.com"
subject = "Automated email: Away for a while..."
body = "Hello, This is an automated message."

# Construct the email message
message = f"Subject: {subject}\n\n{body}"

# Connect to the SMTP server
smtp_server = smtplib.SMTP("smtp.example.com")

# Login to the SMTP server (if necessary)
smtp_server.login("username", "password")

# Send the email
smtp_server.sendmail(from_address, to_address, message)

# Disconnect from the SMTP server
smtp_server.quit()
