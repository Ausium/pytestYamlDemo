import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(sender_email, sender_password, recipient_email, subject, body,attachment_path=None):
    # 创建邮件容器
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    smtp_server = 'smtp.exmail.qq.com'
    # 添加邮件正文
    msg.attach(MIMEText(body, 'plain'))

    # 添加邮件附件
    with open(attachment_path, 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype='html')
        attachment.add_header('Content-Disposition', 'attachment', filename='report.html')
        msg.attach(attachment)

    # 发送邮件
    try:
        server = smtplib.SMTP_SSL(smtp_server, '465')
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("send email successed!")
    except smtplib.SMTPException as e:
        print("Error: unable to send email, %s" % e)

if __name__ == '__main__':
    send_email('chenzanxu@unity-drive.com', 'tHTECYEP9Lvdh4et', 'chenzanxu@unity-drive.com', 'Test Results', 'Please find attached the results of the pytest execution.',"E:/InterfaceAuto/ApiAuto/output/report.html")