import cgi, cgitb, os, re
from templates import after_login_incorrect, secret_page
from secret import username, password


#!/usr/bin/python
def return_cookie(username, password):
    for query in os.environ.keys():
        if query == 'HTTP_COOKIE':
            http_cookie = os.environ[query]
            #print("<b>%s</b>" % http_cookie)
            values = http_cookie.split(';')
            for value in values:

                if value.split('=')[0] == 'UserID':
                    print("<b>Return cookie username: %s</b>" % username)
                if value.split('=')[0] == ' Password':
                    print("<b>Return cookie password: %s</b>" % password)


form = cgi.FieldStorage()

entered_username = form.getvalue('username')
entered_password = form.getvalue('password')

if entered_password == password and entered_username == username:

    print("Set-Cookie:UserID = %s" % username)
    print("Set-Cookie:Password = %s" % password)
    print('Set-Cookie:Expires = Tuesday, 31-Dec-2021 23:12:40 GMT')
    print('Set-Cookie:Domain = localhost')
    print('Set-Cookie:Path = /perl')
    print("Content-type:text/html\r\n\r\n")
    print('<html>')
    print('<head>')
    print('<title>Hello World</title>')
    print('</head>')
    print('<body>')

    print(secret_page(username, password))
    for query in os.environ.keys():
        if query == 'HTTP_COOKIE':
            if username in os.environ[query]:
                print('<h2>secret message: the user has logged in</h2>')
    return_cookie(username, password)

    print("<h1>hello world</h1>")
    print('</body>')
    print('</html>')
    #print(os.environ)

else:
    #print("Content-type:text/html\r\n\r\n")
    print(after_login_incorrect())
