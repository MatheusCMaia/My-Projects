import smtplib


email_from = 'Your Email'
email_to = 'Destiny Email'
smtp = 'smtp.gmail.com'
server = smtplib.SMTP(smtp, 587)
server.starttls()
server.login(email_from, 'Password From Your Email')
msg = ''' Mensage '''
server.sendmail(email_from, email_to, msg)
server.quit()
print("Code Finished")
