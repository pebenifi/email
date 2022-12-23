import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
msg = MIMEMultipart()

e = pd.read_excel("email.xlsx")
recipients = e['Emails'].values

msg['From'] = '000000@yandex.ru' #сюда пишем почту свою
msg['To'] = ''.join(recipients)
msg['Subject'] = 'Тест' # тема письма
message = 'Это тестовое сообщение и отвечать на него не нужно' # само письмо
msg.attach(MIMEText(message))

try:
    mailserver = smtplib.SMTP('smtp.yandex.ru',587)
    mailserver.set_debuglevel(True)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('0000000@yandex.ru', '1111111') # пишем свою почту и одноразовый пароль полученный в яндексе
    mailserver.sendmail('00000000@yandex.ru',recipients,msg.as_string()) # еще раз пишем свою почту
    mailserver.quit()
    print("Письмо успешно отправлено")
except smtplib.SMTPException:
    print("Ошибка: Невозможно отправить сообщение")