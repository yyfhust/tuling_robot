# -*- coding: utf-8 -*-  
 
import json  
import sys, locale
import requests

    



if __name__ == '__main__':  
    Key = '2cb29e5c4ad2430080bbb316f05e6cdb'  
    url = 'http://www.tuling123.com/openapi/api'
    while True:  
        info=raw_input('input:').strip().decode(sys.stdin.encoding or locale.getpreferredencoding(True))

        info.encode('utf-8')
        
        query={'key':Key,'info':info}
        headers={'Content-type':'text/html','charset':'utf-8'}
        
        r=requests.get(url,params=query,headers=headers)
        res=r.text
        print '答案'
        print json.loads(res).get('text').replace('<br>','\n')+'\n'
        