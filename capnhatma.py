# -*- coding: UTF-8 -*-
import requests as req
import json,sys,time

#files:	Files.Read.All、Files.ReadWrite.All、Sites.Read.All、Sites.ReadWrite.All
#user:	User.Read.All、User.ReadWrite.All、Directory.Read.All、Directory.ReadWrite.All
#mail:  Mail.Read、Mail.ReadWrite、MailboxSettings.Read、MailboxSettings.ReadWrite












path=sys.path[0]+r'/bkc.txt'

def gettoken(refresh_token):
    headers={'Content-Type':cont_type
            }
    data={'grant_type': 'refresh_token',
          'refresh_token': refresh_token,
          'client_id':id,
          'client_secret':secret,
          'redirect_uri':url_red
         }
    html = req.post(url_xt,data=data,headers=headers)
    jsontxt = json.loads(html.text)
    refresh_token = jsontxt['refresh_token']
    access_token = jsontxt['access_token']
    with open(path, 'w+') as f:
        f.write(refresh_token)
def main():
    fo = open(path, "r+")
    refresh_token = fo.read()
    fo.close()
    gettoken(refresh_token)
main()
