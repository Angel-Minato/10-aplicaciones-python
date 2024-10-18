from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email = "angel14game@gmail.com"
    from_password = "yfcr wukp kqbh gzxa"
    to_email = email

    subject = "Datos de altura"
    message = "Hola, tu altura es <strong>%s</strong>. <br> La altura promedio de todos es <strong>%s</strong> y se ha calculado a partir de <strong>%s</strong> personas. <br> ¡Gracias!" % (height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
