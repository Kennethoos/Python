#coding=utf-8

import os
import base64, quopri
import time
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import *



def _decode_str(s):
    _is_multipalLines = s.find('\n')
    # single line
    if _is_multipalLines < 0:
        return _decode_single_line(s)
    #multipal lines
    else:
        return _decode_multipal_line(s)



def _decode_single_line(s):
    if s[0] == '=':
            _charset=s.split('?')[1]
            _code=s.split('?')[2]
            _str=s.split('?')[3]
            #print '_charset is:%s, _code is:%s, _str is:%s' % (_charset, _code, _str)
            if _code=='B':
                _decodedStr=base64.decodestring(_str)
            elif _code=='Q':
                _decodedStr=quopri.decodestring(_str)
            return _decodedStr
    else:
        return s

def _decode_multipal_line(s):
    _stripedLines=''
    _multipal_lines = s.split('\n')
    _lineCount = len(_multipal_lines)
    _index = 0
    #print 'LINE COUNT IS : %d' % _lineCount
    while _index < _lineCount:
        _stripedLines.join(_decode_single_line(_multipal_lines[_index]))
        _index +=1
    return _stripedLines

def _saveFile(fileName,msgPart):
    wd = 'c:\\tmp'
    os.chdir(wd)
    _dFilename=_decode_str(fileName)
    print _dFilename
    '''
    f = open(_dFilename, 'wb') # use wb
        #print 'The file: %s exists!' % _dFilename
        #f = open('another name','wb')
    f.write(msgPart)
    f.close()
    '''
    

# Get 'from' header
def getFrom(msg):
    _from = msg.__getitem__('From')
    print _from
    #if _from:
        #return _from#base64.decodestring(_from)
    #else:
        #print 'Named header is missing!'

def getTo(msg):
    _to = msg.get('To')
    if _to:
        return _to
    else:
        print 'Named header is missing!'

def getSubject(msg):
    _subject = msg.get('Subject')
    if _subject:
        return _subject
    else:
        print 'Named header is missing!'

# return struct time
def getDate(msg):
    _date = msg.get('Date')
    _timeStamp = time.mktime(parsedate(_date))
    if _timeStamp:
        return time.localtime(_timeStamp)
    else:
        print 'Named header is missing!'

def print_structure(msg):
    for part in msg.walk():
        print part.get_boundary()
    print '-------END-------'



# Provide download attachment function
def download_attachment(msg, indent=0):
    
    for part in msg.walk():
        if part.get_content_maintype()=='application':
            _nameValue = part.get_param('name')
            data = part.get_payload(decode=True) # decoding attachment content, save it to data
            #print _nameValue
            _saveFile(_nameValue,data)



