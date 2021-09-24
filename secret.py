#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi
import cgitb
import os
from templates import secret_page

cgitb.enable()


class FollowingTheTAsInstructionsError(Exception):
    def __init__(self):
        Exception.__init__(
            self, ("You must edit secret.py to change the username, password, "
                   "and to delete this error!"))


# Delete this line:
#raise FollowingTheTAsInstructionsError

# Edit the following two lines:
# password = form.getvalue('password')

username = '12345'
password = '12345'

#if username == entered_username and password == entered_password:
#!/usr/bin/python
#print("Set-Cookie:UserID = %s;\r\n" % username)
#print("Set-Cookie:Password = %s;\r\n" % password)
#print('Set-Cookie:Expires = Tuesday, 31-Dec-2021 23:12:40 GMT;\r\n')
#print('Set-Cookie:Domain = localhost;\r\n')
#print('Set-Cookie:Path = /perl;\r\n')
#print('Content-type: text/html\r\n\r\n')
#print(secret_page(username, password))
#for query in os.environ.keys():
#if query == 'HTTP_COOKIE':
#print("<b>%20s</b>: %s<br>" % (query, os.environ[query]))
#print(os.environ)

#return True
