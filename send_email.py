import smtplib
import config
from email.message import EmailMessage
import imghdr

password = config.password


def send_email(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = 'New object detected'
    email_message.set_content('Something enter the roo. Check the image attached')

    with open(image_path, 'rb') as file:
        content = file.read()

    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(config.sender, password)
    gmail.sendmail(config.sender, config.reiciver, email_message.as_string())
    gmail.quit()


if __name__ == '__main__':
    send_email("images/19.png")
