import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方SMTP服务, 如163, qq, sina
mail_host = "smtp.163.com"  # 设置服务器
mail_port = 25  # 端口号
mail_user = "feng667298@163.com"  # 用户名
mail_pass = "VDJQLAIWPFWGDRNU"  # 163授权码

sender = "feng667298@163.com"  # 发送方


def send_163_email(receivers, code):
    try:
        ''' 发送纯文本邮件, text: 邮件内容 '''
        # 三个参数：第一个为文本内容，第二个plain设置文本格式，第三个utf-8设置编码
        message = MIMEText(f"您好，欢迎使用tracer企业bug管理系统，登录验证码为{code}，有效期5分钟，请您尽快完成验证。",
                           'plain',
                           'utf-8')  # 邮件内容
        message['From'] = Header(sender, 'utf-8')  # 发送者
        message['To'] = Header(receivers, 'utf-8')  # 接收者
        subject = 'tracer注册邮件'  # 邮件主题
        message['Subject'] = Header(subject, 'utf-8')

        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, mail_port)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        return {'message': '发送成功请查看邮箱'}
    except:
        return {'message': '发送失败请稍后再试'}
