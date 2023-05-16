import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
# from utils.get_path import report_dir

class SendEmail():
    # def __init__(self,sender_email):
    #     self.sender_email = sender_email
    def __init__(self):
        self.sender_email = 'chenzanxu@unity-drive.com'
        self.sender_password = 'tHTECYEP9Lvdh4et'
        self.recipient_email = ['chenzanxu@unity-drive.com','']

    #发送用例执行后的邮件
    def send_email(self, subject, body,attachment_path=None):
        print(self.sender_email)
        # 创建邮件容器
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = ','.join(self.recipient_email)
        msg['Subject'] = subject
        smtp_server = 'smtp.exmail.qq.com'
        # 添加邮件正文
        msg.attach(MIMEText(body, 'html', 'utf-8'))

        # # 添加邮件附件
        with open(attachment_path, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype='html')
            attachment.add_header('Content-Disposition', 'attachment', filename='report.html')
            msg.attach(attachment)

        # 发送邮件
        try:
            server = smtplib.SMTP_SSL(smtp_server, '465')
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
            server.quit()
            print("send email successed!")
        except smtplib.SMTPException as e:
            print("Error: unable to send email, %s" % e)

send_case_result_email = SendEmail()

if __name__ == '__main__':
    send = SendEmail()
    send.send_email('Test Results', 'Please find attached the results of the pytest execution.',"E:/InterfaceAuto/ApiAuto/outputs/report/report.html")