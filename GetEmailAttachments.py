#coding=utf-8

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from types import *
from myParsingEmail import download_attachment




# Firstly, log in mailbox, NEED A CLASS OR METHOD HERE.
# GIVEN email address, password, server name, RETURN a pop3 instance.

###
emailAddr = 'custody@cmbc.com.cn'
password = 'passw0rd!'
pop3_server = 'pop3.cmbc.com.cn'

server = poplib.POP3(pop3_server)

print(server.getwelcome())
server.user(emailAddr)
server.pass_(password)
###

messageCount, messageSize=server.stat()
print('Messages: %s' % messageCount)


# Secondly,(maybe thirdly) choose specific emails and download their attachments
# According to emails' sender and attachments' name, choose the right emails
while messageCount > 600:
    # Choose a message, messageCount as index,and retrive
    # the whole multipal-lines contained in this message.
    resp, lines, octets = server.retr(messageCount)
    # Then make the multipal lines into a whole line, 
    # seperating by \r\n
    msg_content = '\r\n'.join(lines)
    #Create an message instance from text msg_content
    msg = Parser().parsestr(msg_content)
    download_attachment(msg)

    messageCount -=1


server.quit()
