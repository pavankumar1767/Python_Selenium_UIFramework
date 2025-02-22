# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
# from email.mime.text import MIMEText
#
#
# def send_email(subject, body, to_email, attachment_path):
#     from_email = "automationcds@gmail.com"
#     from_password = "sblz jdic xzao hfty"
#
#     msg = MIMEMultipart()
#     msg['From'] = from_email
#     msg['To'] = to_email
#     msg['Subject'] = subject
#
#     msg.attach(MIMEText(body, 'plain'))
#
#     with open(attachment_path, "rb") as attachment:
#         part = MIMEBase('application', 'octet-stream')
#         part.set_payload(attachment.read())
#         encoders.encode_base64(part)
#         part.add_header('Content-Disposition', f"attachment; filename= {attachment_path}")
#         msg.attach(part)
#
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(from_email, from_password)
#     text = msg.as_string()
#     server.sendmail(from_email, to_email, text)
#     server.quit()
#
# # # Example usage
# # send_email(
# #     subject="Allure Test Report",
# #     body="Please find the attached Allure test report.",
# #     to_email="stakeholder@example.com",
# #     attachment_path="allure-report.zip"
# # )






import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

def send_email(subject, body, to_email, attachment_path):
    from_email = "sigmastreamautomation@gmail.com"
    from_password = "yque cesi nyqn pylv"


    msg = MIMEMultipart()
    msg['From'] = from_email
    # msg['To'] = to_email
    msg['To'] = ', '.join(to_email)  # Display all recipients in To field
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with open(attachment_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {attachment_path}")
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully!")
    except smtplib.SMTPDataError as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
















# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
# from email.mime.text import MIMEText
#
# def send_email(subject, body, to_email, attachment_path):
#     from_email = "sigmastreamautomation@gmail.com"  # Replace with your email
#     from_password = "yque cesi nyqn pylv"           # Replace with your email password or app password
#
#     # Create the email
#     msg = MIMEMultipart()
#     msg['From'] = from_email
#     msg['To'] = to_email
#     msg['Subject'] = subject
#
#     # Add the email body
#     msg.attach(MIMEText(body, 'plain'))
#
#     # Attach the file
#     with open(attachment_path, "rb") as attachment:
#         part = MIMEBase('application', 'octet-stream')
#         part.set_payload(attachment.read())
#         encoders.encode_base64(part)
#         part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
#         msg.attach(part)
#
#     try:
#         # Send the email using Gmail's SMTP server
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()  # Secure the connection
#         server.login(from_email, from_password)
#         text = msg.as_string()
#         server.sendmail(from_email, to_email, text)
#         server.quit()
#         print("Email sent successfully!")
#     except smtplib.SMTPDataError as e:
#         print(f"Failed to send email: {e}")
#     except Exception as e:
#         print(f"An error occurred: {e}")