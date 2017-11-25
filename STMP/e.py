from STMP import Email

Email = Email.Email('smtp.exmail.qq.com', 'zengzhixiong@zhizhangyi.com', 'Zengzhx123')
#250085705
Email.setFrom_To(['zengzhixiong@zhizhangyi.com'],['250085705@qq.com'])

Email.setContext('Zengzhx', '牛逼', '小程序发送邮件','python.........')

while True:
    Email.sendEmail()