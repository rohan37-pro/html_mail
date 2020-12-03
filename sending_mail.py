import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

print('modules are import complete......')


print('loading variables....')
time.sleep(1)


user = 'example@gmail.com'
password = 'password'
to = 'example_2_@gmail.com'

sub= 'hey brooo whatsup whatsup'
text= 'this is a text message'

html_text = """

<html>
<head>
<title>
</title>
</head>
<body style='background-color: cyan'>
<p>
<div><h1 style=color: green''>hello rid....</h1></div>
<h2 style='color: red'>yooo broo whats up whats up kya bolte public malum hai na</h2>
<h1 style='color: blue'>we are going to have a fun</h1>
</p>
</body>
</html>

"""

print('..variables are loaded....')
print('intitialize the funtion.....//')

def send_mail():

    msg  = MIMEMultipart('alternative')
    msg['from'] = user
    msg['to'] = to
    msg['subject'] = sub

    #txt_part = MIMEText(text,'plain')
    #msg.attach(txt_part)

    html_part = MIMEText(html_text,'html')
    msg.attach(html_part)

    print('html part is attached to msg ')
    
    msg_str = msg.as_string()
    print('massage is successfully converted as string')

    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    print('connected to the server')
    time.sleep(2)
    
    server.login(user,password)
    print('account login successfully')
    time.sleep(1)

    server.sendmail(user,to,msg_str)
    print('message sent')
    time.sleep(1)
    
    server.quit()
    print('quit from the server')

send_mail()

print('thanks.......//')

