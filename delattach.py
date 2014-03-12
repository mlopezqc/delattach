#!/usr/bin/env python
import email
import sys
import smtplib

def remove_attachments(rootmsg):
    """Remove all attachments that are not text/plain"""
    payloads = rootmsg.get_payload()
    to_remove = []
    for payload in payloads:
        content_type = payload.get_content_type()
        if content_type!='text/plain':
            to_remove.append(payload)
    for item in to_remove:
        payloads.remove(item)
    return rootmsg

if __name__ == '__main__':
    sender, recipient = sys.argv[1:3]
    print sender,recipient
    incontent=sys.stdin.read()
    try:
        rootmsg=email.message_from_string(incontent)
    except:
        sys.stderr.write('Message could not be parsed')
        sys.exit(1)
    if rootmsg.is_multipart():
        src=remove_attachments(rootmsg).as_string()
    else:
        src=rootmsg.as_string()
    if src!=None:
        message = src
    else:
        message = incontent
    server = smtplib.SMTP('localhost',10025)
    server.sendmail(sender, recipient, message)
