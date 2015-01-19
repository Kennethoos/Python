
import os
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

def download_attachment(msg, indent=0):
    wd = 'c:\\tmp'
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            # if value has a string containing the value of 'From', 'To', or 'Subject'
            if value:
                # if in this time of loop header is subject
                if header=='Subject':
                    value = decode_str(value)
                else:
                    #parseaddr(address) returns a tuple of realname and email address
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    for part in msg.walk():
        if not part.is_multipart():
            _nameValue = part.get_param('name')
            if _nameValue:
                _attachmentName = decode_str(email.Header.Header(_nameValue))
                print _attachmentName
                data = part.get_payload(decode=True) # decoding attachment content, save it to data 
                os.chdir(wd)
                try:
                    f = open(_attachmentName, 'wb') # use wb
                except:
                    print 'other name'
                    f = open('aaaa', 'wb')
                f.write(data)
                f.close()
        else:
            continue
        print '\n'

def decode_str(s):
    value, charset = decode_header(s)[0]
    # if charset!= None
    if charset:
        value = value.decode(charset)
    return value

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

