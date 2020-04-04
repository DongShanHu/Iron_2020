import smtplib
from email.mime.text import MIMEText

mail_host = "smtp.mail.yahoo.com.tw"  # SMTP服務器
mail_user = "your  yahoo account@yahoo.com.tw"  # 用户名
mail_pass = "zrslwmaeqvrlrtou"  # 打上系統給予的密码
sender = 'send@yahoo.com.tw'  # 寄件人
receivers = ['receive@gmail.com']  # 接收人
content = 'Send Mail !  Test'  # 內文
title = 'Python SMTP Mail Test'  # 主题
message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
message['From'] = "{}".format(sender)
message['To'] = ",".join(receivers)
message['Subject'] = title
try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 啟用SSL寄信, 端口一般是465
    smtpObj.login(mail_user, mail_pass)  # 登陸驗證
    smtpObj.sendmail(sender, receivers, message.as_string())  # 寄送
    print("mail has been send successfully.")
except smtplib.SMTPException as e:
    print(e)
