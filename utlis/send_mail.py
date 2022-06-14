import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import config


def smtp_object(sender_email, receiver_email, message):
    email_port = config.EMAIL_CONFIG["EMAIL_PORT"]
    host = config.EMAIL_CONFIG["EMAIL_SERVER"]
    try:
        smtp_obj = smtplib.SMTP(host, port=email_port)  # creates SMTP session
        # identify ourselves to smtp client
        smtp_obj.ehlo()
        # secure our email with tsl encryption
        smtp_obj.starttls()
        # re-identify ourselves as an encrypted connection
        smtp_obj.ehlo()

        smtp_obj.sendmail(sender_email, receiver_email, message.as_string())
        # terminating the session
        smtp_obj.quit()

    except Exception as e:
        print("ERROR Raised")
        print(str(e))
        return 1


def write_message(sender_email, receiver_email, subject, body, attachment=None):
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    print("From: ", message["from"])
    print("To: ", message["To"])
    print("Subject: ", message["Subject"])

    part_one = MIMEText(body, "plain")
    if attachment is not None:
        # Open PDF file in binary mode
        message.attach(part_one)
        with open(attachment, "rb") as attachment_file:
            part_two = MIMEBase("application", "octet-stream")
            part_two.set_payload(attachment_file.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part_two)

        # Add header as key/value pair to attachment part_two
        part_two.add_header(
            "Content-Disposition",
            f"attachment; filename= {attachment}",
        )
        # Add attachment to message and convert message to string
        message.attach(part_two)
        print("Sending message with attachment")

    else:
        message.attach(part_one)
        print("Sending message without attachment")

    return message


def send_mail():
    sender = config.EMAIL_INFO["EMAIL_FROM"]
    receiver = config.EMAIL_INFO["EMAIL_TO"]
    # Plain-text of the message
    text = """\
    Hi,
    How are you?
    This email is sent from python.
    Thankyou.
            """
    # With attachment

    filename = "document.pdf"  # In same directory as script

    message = write_message(sender, receiver, "Email from Python", text)
    message_with_attachment = write_message(sender, receiver, "Email from Python with attachment", text, filename)

    smtp_object(sender, receiver, message)
    print("Email sent successfully!!")
    smtp_object(sender, receiver, message_with_attachment)
    print("Email with attachment Sent Successfully!!!")


def main():
    send_mail()


if __name__ == '__main__':
    main()
