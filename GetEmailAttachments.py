#coding=utf-8

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from types import *
from myParsingEmail import *




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

'''
resp, header, octets = server.top(messageCount,0)

print '\tEmail header fields name\t\t\tfields value'
print '--------------------------------------------------------------------------'
i = 0
while i < len(header):
    print '%s\t\t\tNull' % (header[i])
    i +=1
'''

# Secondly,(maybe thirdly) choose specific emails and download their attachments
# According to emails' sender and attachments' name, choose the right emails
while (messageCount - 1):
    # Choose a message, messageCount as index,and retrive
    # the whole multipal-lines contained in this message.
    resp, lines, octets = server.retr(messageCount)
    # Then make the multipal lines into a whole line, 
    # seperating by \r\n
    msg_content = '\r\n'.join(lines)
    #Create an message instance from text msg_content
    msg = Parser().parsestr(msg_content)
    
    #print_structure(msg)
    #download_attachment(msg)
    #print getFrom(msg)
    #print getTo(msg)
    #print getSubject(msg)
    arrivalDate = getDate(msg)
    now = time.localtime()
    if ((arrivalDate.tm_year==now.tm_year) & 
        (arrivalDate.tm_mon==now.tm_mon) & 
       (now.tm_mday - arrivalDate.tm_mday<1) &
       (msg.get_content_type()=='multipart/mixed')):
        download_attachment(msg)
            
        #download_attachment(msg)

    messageCount -=1

server.quit()






