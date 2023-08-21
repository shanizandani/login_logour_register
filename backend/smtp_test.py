# import smtplib
# from email.mime.text import MIMEText
# from email.utils import formataddr

# def send_test_email():
#     sender_email = 'shanilevi88761234@gmail.com'
#     sender_password = 'Shanilevi8876'
#     recipient_email = 'nurielyosef123@gmail.com'
    
#     try:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(sender_email, sender_password)
        
#         subject = 'SMTP Test Email'
#         message = 'This is a test email sent using smtplib.'
#         msg = MIMEText(message)
#         msg['From'] = formataddr(('Sender Name', sender_email))
#         msg['To'] = recipient_email
#         msg['Subject'] = subject
        
#         server.sendmail(sender_email, [recipient_email], msg.as_string())
#         print('Test email sent successfully.')
#     except Exception as e:
#         print('Error:', e)
#     finally:
#         server.quit()

# if __name__ == '__main__':
#     send_test_email()
