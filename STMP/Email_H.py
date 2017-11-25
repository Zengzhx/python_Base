'''
Python 发送带附件的邮件
发送带附件的邮件，首先要创建MIMEMultipart()实例，然后构造附件，如果有多个附件，可依次构造，最后利用smtplib.smtp发送。
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_server = 'smtp.exmail.qq.com' #借用qq SMTP服务
mail_user = 'zengzhixiong@zhizhangyi.com'
mail_pwd  = 'Zengzhx123'

From_mail = ['zengzhixiong@zhizhangyi.com']
To_mail   = ['1109496192@qq.com']

message = MIMEMultipart()
message['From'] = Header('Zengzhx', 'UTF-8')
message['To']   = Header('辣肌肉', 'UTF-8')
subject = 'Python'
message['Subject'] = Header(subject, 'UTF-8')

#邮件正文内容
message.attach(MIMEText('邮件发送测试……', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_server, 25)
    smtpObj.login(mail_user, mail_pwd)
    smtpObj.sendmail(From_mail, To_mail, message.as_string())
    print ("邮件发送成功   发送至：%s"%(To_mail))
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")