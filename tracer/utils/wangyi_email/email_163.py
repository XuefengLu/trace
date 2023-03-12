import smtplib
from email.mime.text import MIMEText
from email.header import Header
from tracer.local_settings import MAIL_HOST, MAIL_PORT, MAIL_USER, MAIL_PASS, SENDER, EMAIL_FORMAT


def send_163_email(receivers, code, template):
    message = None
    subject = None
    try:
        if template == "登录":
            ''' 发送纯文本邮件, text: 邮件内容 '''
            # 三个参数：第一个为文本内容，第二个plain设置文本格式，第三个utf-8设置编码
            message = MIMEText(f"{EMAIL_FORMAT['login']},您好，欢迎使用tracer企业bug管理系统，登录验证码为{code}，有效期5分钟，请您尽快完成验证。",
                               'plain',
                               'utf-8')  # 邮件内容
            subject = 'tracer登录邮件'  # 邮件主题
            message['From'] = Header(SENDER, 'utf-8')  # 发送者
            message['To'] = Header(receivers, 'utf-8')  # 接收者
            message['Subject'] = Header(subject, 'utf-8')
            smtpObj = smtplib.SMTP()
            smtpObj.connect(MAIL_HOST, MAIL_PORT)
            smtpObj.login(MAIL_USER, MAIL_PASS)
            smtpObj.sendmail(SENDER, receivers, message.as_string())
            return {'message': '发送成功请查看邮箱'}

        elif template == "注册":
            ''' 发送纯文本邮件, text: 邮件内容 '''
            # 三个参数：第一个为文本内容，第二个plain设置文本格式，第三个utf-8设置编码
            message = MIMEText(f"{EMAIL_FORMAT['register']},欢迎来到tracer企业bug管理系统，注册验证码为{code}，有效期5分钟，请您尽快完成验证。",
                               'plain',
                               'utf-8')  # 邮件内容
            subject = 'tracer注册邮件'  # 邮件主题

            message['From'] = Header(SENDER, 'utf-8')  # 发送者
            message['To'] = Header(receivers, 'utf-8')  # 接收者
            message['Subject'] = Header(subject, 'utf-8')
            smtpObj = smtplib.SMTP()
            smtpObj.connect(MAIL_HOST, MAIL_PORT)
            smtpObj.login(MAIL_USER, MAIL_PASS)
            smtpObj.sendmail(SENDER, receivers, message.as_string())
            return {'message': '发送成功请查看邮箱'}
    except:
        return {'message': '发送失败请稍后再试'}
