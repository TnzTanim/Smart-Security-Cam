def email(term):
    import smtplib         #The package to access to your email
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    email_user = 'Your Email'
    email_password = 'Your email password'
    email_send = 'The email you want to send the video.'
    
    #example 
    #email_user = 'myemail@gmail.com'
    #email_password = '123.....'
    #email_send = 'mysecondemail@gmail.com'
    
    subject = 'Security alart'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'Hi there, looks like someone entered your house!'
    msg.attach(MIMEText(body, 'plain'))


    filename = term +'.mp4'
    print(filename)
    attachment = open(filename, 'rb')
    print("started email func")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, 'TANZIBUL')

    server.sendmail(email_user, email_send, text)
    print("mail sent")
    server.quit()




