'''
Python创建 SMTP 对象语法如下：
import smtplib
smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
参数说明：
host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如:w3cschool.cc，这个是可选参数。
port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下SMTP端口号为25。
local_hostname: 如果SMTP在你的本机上，你只需要指定服务器地址为 localhost 即可。


Python SMTP对象使用sendmail方法发送邮件，语法如下：
SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]
参数说明：
from_addr: 邮件发送者地址。
to_addrs: 字符串列表，邮件发送地址。
msg: 发送消息
这里要注意一下第三个参数，msg是字符串，表示邮件。我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意msg的格式。这个格式就是smtp协议中定义的格式。

'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_server = 'smtp.exmail.qq.com' #借用qq SMTP服务
mail_user = 'zengzhixiong@zhizhangyi.com'
mail_pwd  = 'Zengzhx123'

From_mail = ['zengzhixiong@zhizhangyi.com']
To_mail   = ['250085705@qq.com']
# 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python STMP 测试...用代码给你发一个邮件....','plain', 'UTF-8')
message['From'] = Header('Zengzhx','UTF-8')
message['To']   = Header('Test','UTF-8')

subject = 'python 邮件功能测试'
message['Subject']=Header(subject,'UTF-8')
try:
    smtp=smtplib.SMTP()
    smtp.connect(mail_server, 25)
    smtp.login(mail_user, mail_pwd)
    smtp.sendmail(From_mail, To_mail, message.as_string())
    print('邮件发送成功！')
except smtplib.SMTPException:
    print("Error: 无法发送邮件")