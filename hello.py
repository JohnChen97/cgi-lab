import os, sys, json, socket
from templates import login_page

#!/usr/bin/env python3

print('Content-type: text/html\r\n\r\n')

print('<html>')
print('<head>')
print('<title>Hello World</title>')
print('</head>')
print('<body>')
print('<h2>Again, hello world</h2>')
print('</body>')
print('</html>')

#print("Content-type: text/html\r\n\r\n")

for query in os.environ.keys():
    if query == 'QUERY_STRING':

        print("<b>%20s</b>: %s<br>" % (query, os.environ[query]))
    if query == 'HTTP_USER_AGENT':
        print("<b>%20s</b>: %s<br>" % (query, os.environ[query]))

print('<form>')
print('<h3>This is the third heading</h3>')
print('<p>Type something in this box</p>')

print(
    "<input type='text' placeholder='this is a test. Do not enter anything here.' />"
)
print(
    "<input type='text' placeholder='another test. Do not enter anything here.' />"
)
print('<button> OK</button>')
print('</form>')

print(login_page())
