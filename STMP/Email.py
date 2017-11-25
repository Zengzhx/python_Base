import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Email:
    stmp_server, login_User, login_Pwd = '', '', ''

    From_Email, To_Email = [], []

    From_name, To_name, subject, context = '', '', '',''


    def __init__(self, stmp_server, login_User, login_Pwd):
        self.stmp_server = stmp_server
        self.login_User  = login_User
        self.login_Pwd   = login_Pwd

    def setFrom_To(self, From_Email, To_Email):
        self.From_Email = self.From_Email+From_Email
        self.To_Email   = self.To_Email+To_Email


    def setContext(self,From_name,To_name,subject,context):
        self.From_name = From_name
        self.To_name   = To_name
        self.subject   = subject
        self.context   = context

    def sendEmail(self):
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText(self.context, 'plain', 'UTF-8')
        message['From'] = Header(self.From_name, 'UTF-8')
        message['To'] = Header(self.To_name, 'UTF-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.stmp_server, 25)
            smtpObj.login(self.login_User, self.login_Pwd)
            smtpObj.sendmail(self.From_Email, self.To_Email, message.as_string())
            print("邮件发送成功   发送至：%s" % (self.To_Email))
        except:
            print("Error:失败")