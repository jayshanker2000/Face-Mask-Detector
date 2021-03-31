import smtplib, ssl

def func():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "jayshankaree17@gmail.com"  # Enter your address
    receiver_email = "jayshankaree17@gmail.com"  # Enter receiver address
    password = "asdfghjkl@123"
    sub = "Alert!!"
    message = f"""\
Subject: {sub}

Someone is not wearing mask
    """
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except smtplib.SMTPServerDisconnected:
        print('Failed to connect to the server. Wrong user/password?')
    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))
    else:
        print('Someone is not wearing mask. Email Sent')