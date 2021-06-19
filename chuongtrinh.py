#bkcom
import requests as req
import json,sys,time,random































path=sys.path[0]+r'/bkc.txt'
num1 = 0

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
    return access_token
def main():
    fo = open(path, "r+")
    refresh_token = fo.read()
    fo.close()
    global num1
    localtime = time.asctime( time.localtime(time.time()) )
    access_token=gettoken(refresh_token)
    headers={
    'Authorization':access_token,
    'Content-Type':'application/json'
    }
    print('Thoi gian bat dau chuong trinh :', localtime)
    for i in ar_url:
        try:
            if req.get(ar_url[i],headers=headers).status_code == 200:
                num1+=1
                print("Goi=> OK: "+str(num1)+' lan')
                time.sleep(random.randint(2,5))
        except:
            print("pass")
            pass
for _ in range(10):
    time.sleep(random.randint(864,1296))
    main()
