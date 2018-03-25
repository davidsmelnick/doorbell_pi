import smtplib

emailAddress = '921WinonaDoorbell@gmail.com'

def login():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    password = 'o4GQnNoVUTTacudH'
    server.login(emailAddress,password)
    return server
    