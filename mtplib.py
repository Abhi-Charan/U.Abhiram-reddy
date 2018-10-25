import smtplib
 
server = smtplib.SMTP('abhi08082000@gmail.com', 587)
server.starttls()
server.login("abhi08082000@gmail.com", "08A46")
 
msg = "hiii i am abhiram"
server.sendmail("abhi08082000@gmail.com", "charan.uravakonda@gmail.com", msg)
server.quit()