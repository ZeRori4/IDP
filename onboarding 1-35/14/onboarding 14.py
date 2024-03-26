# -*- coding: utf-8 -*-
'''
<parameters>
	<title>onboarding 14</title>
	<version>1.0</version>
    <parameter>
        <type>string</type>
        <name>email получателей:</name>
        <id>EMAIL_TO</id>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>путь к файлу:</name>
        <id>FILE_PATH</id>
        <value>C:/DSSL/Trassir-4.5.5.0-IPR/shots/hello_world.txt</value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>учётная запись email:</name>
        <id>EMAIL_FROM</id>
        <value>smart_07_08@mail.ru</value>
    </parameter>
</parameters>
'''
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

GLOBALS = globals()

EMAIL_FROM = GLOBALS.get("EMAIL_FROM", "")
# "smart_07_08@mail.ru"
EMAIL_PASSWORD = "JPbPBrE5tRJVpNrSpA6U"
EMAIL_SERVER = "smtp.mail.ru"
EMAIL_PORT = 587

EMAIL_TO = GLOBALS.get("EMAIL_TO", "")
# "smart_07_08@mail.ru, smart_test_dssl@mail.ru"
SUBJECT = "Тестовое сообщение"
MESSAGE = "Текст сообщения"

FILE_PATH = GLOBALS.get("FILE_PATH", "")
# "C:/DSSL/Trassir-4.5.5.0-IPR/shots/hello_world.txt"


def send_email_with_attachment(
    email_from,
    email_password,
    email_server,
    email_port,
    to_addresses,
    subject,
    message_text,
    file_path
):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = email_from
    msg["To"] = ", ".join(to_addresses)

    msg_text = MIMEText(message_text, "plain")
    msg.attach(msg_text)

    with open(FILE_PATH, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment; filename={}".format(
            os.path.basename(FILE_PATH)))
        msg.attach(part)

    session = smtplib.SMTP(email_server, email_port)
    session.starttls()
    session.login(email_from, email_password)
    session.sendmail(msg['From'], msg['To'], msg.as_string())
    session.quit()


send_email_with_attachment(
    EMAIL_FROM,
    EMAIL_PASSWORD,
    EMAIL_SERVER,
    EMAIL_PORT,
    EMAIL_TO.split(", "),
    SUBJECT,
    MESSAGE,
    FILE_PATH
)
