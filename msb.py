
import hashlib
import requests
import json
import base64
import random
import string
import base64
import json
import os
import hashlib
import time
import uuid
class MSB:
    def __init__(self, username, password, account_number):
        self.authToken = ""
        self.clientIp = ""
        self.guid = ""
        self.uuid = ""
        self.is_login = False
        self.key_captcha = "CAP-6C2884061D70C08F10D6257F2CA9518C"
        self.file = f"data/{username}.txt"
        self.url = {
    "getCaptcha": "https://ebank.msb.com.vn/IBS-API-Gateway/corporate/captcha?guid=",
    "login": "https://ebank.msb.com.vn/IBS-API-Gateway/login",
    "getHistories": "https://ebank.msb.com.vn/IBS-API-Gateway/corporate/mono/excute-api",
    "getlistAccount": "https://ebank.msb.com.vn/IBS-API-Gateway/corporate/mono/excute-api",
}
        self.lang = 'VN'
        self._timeout = 60
        self.appVersion = ""
        self.clientOsVersion = "WINDOWS"
        self.browserVersion = "126.0.0.0"
        self.browserName = "Edge"
        self.deviceCode = ""
        self.deviceName = "" 
        self.checkAcctPkg = "1"
        self.captcha1st = ""
        self.challenge = ""
        self.defaultPublicKey = "-----BEGIN PUBLIC KEY-----\n\
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAikqQrIzZJkUvHisjfu5Z\n\
CN+TLy//43CIc5hJE709TIK3HbcC9vuc2+PPEtI6peSUGqOnFoYOwl3i8rRdSaK1\n\
7G2RZN01MIqRIJ/6ac9H4L11dtfQtR7KHqF7KD0fj6vU4kb5+0cwR3RumBvDeMlB\n\
OaYEpKwuEY9EGqy9bcb5EhNGbxxNfbUaogutVwG5C1eKYItzaYd6tao3gq7swNH7\n\
p6UdltrCpxSwFEvc7douE2sKrPDp807ZG2dFslKxxmR4WHDHWfH0OpzrB5KKWQNy\n\
zXxTBXelqrWZECLRypNq7P+1CyfgTSdQ35fdO7M1MniSBT1V33LdhXo73/9qD5e5\n\
VQIDAQAB\n\
-----END PUBLIC KEY-----"
        self.clientPublicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCg+aN5HEhfrHXCI/pLcv2Mg01gNzuAlqNhL8ojO8KwzrnEIEuqmrobjMFFPkrMXUnmY5cWsm0jxaflAtoqTf9dy1+LL5ddqNOvaPsNhSEMmIUsrppvh1ZbUZGGW6OUNeXBEDXhEF8tAjl3KuBiQFLEECUmCDiusnFoZ2w/1iOZJwIDAQAB"
        self.clientPrivateKey = "-----BEGIN RSA PRIVATE KEY-----\n\
MIICXQIBAAKBgQCg+aN5HEhfrHXCI/pLcv2Mg01gNzuAlqNhL8ojO8KwzrnEIEuq\n\
mrobjMFFPkrMXUnmY5cWsm0jxaflAtoqTf9dy1+LL5ddqNOvaPsNhSEMmIUsrppv\n\
h1ZbUZGGW6OUNeXBEDXhEF8tAjl3KuBiQFLEECUmCDiusnFoZ2w/1iOZJwIDAQAB\n\
AoGAEGDV7SCfjHxzjskyUjLk8UL6wGteNnsdLGo8WtFdwbeG1xmiGT2c6eisUWtB\n\
GQH03ugLG1gUGqulpXtgzyUYcj0spHPiUiPDAPY24DleR7lGZHMfsnu20dyu6Llp\n\
Xup07OZdlqDGUm9u2uC0/I8RET0XWCbtOSr4VgdHFpMN+MECQQDbN5JOAIr+px7w\n\
uhBqOnWJbnL+VZjcq39XQ6zJQK01MWkbz0f9IKfMepMiYrldaOwYwVxoeb67uz/4\n\
fau4aCR5AkEAu/xLydU/dyUqTKV7owVDEtjFTTYIwLs7DmRe247207b6nJ3/kZhj\n\
gsm0mNnoAFYZJoNgCONUY/7CBHcvI4wCnwJBAIADmLViTcjd0QykqzdNghvKWu65\n\
D7Y1k/xiscEour0oaIfr6M8hxbt8DPX0jujEf7MJH6yHA+HfPEEhKila74kCQE/9\n\
oIZG3pWlU+V/eSe6QntPkE01k+3m/c82+II2yGL4dpWUSb67eISbreRovOb/u/3+\n\
YywFB9DxA8AAsydOGYMCQQDYDDLAlytyG7EefQtDPRlGbFOOJrNRyQG+2KMEl/ti\n\
Yr4ZPChxNrik1CFLxfkesoReXN8kU/8918D0GLNeVt/C\n\
-----END RSA PRIVATE KEY-----"
        self.init_guid()
        if not os.path.exists(self.file):
            self.username = username
            self.password = password
            self.account_number = account_number
            self.sessionId = ""
            self.mobileId = ""
            self.clientId = ""
            self.cif = ""
            self.res = ""
            self.browserToken = ""
            self.browserId = ""
            self.E = ""
            self.tranId = ""
            self.browserId = hashlib.md5(self.username.encode()).hexdigest()
            self.save_data()
            
        else:
            self.parse_data()
    def save_data(self):
        data = {
            'username': self.username,
            'password': self.password,
            'account_number': self.account_number,
            'sessionId': getattr(self, 'sessionId', ''),
            'mobileId': getattr(self, 'mobileId', ''),
            'clientId': self.clientId,
            'cif': getattr(self, 'cif', ''),
            'E': getattr(self, 'E', ''),
            'res': getattr(self, 'res', ''),
            'tranId': getattr(self, 'tranId', ''),
            'browserToken': getattr(self, 'browserToken', ''),
            'browserId': self.browserId,
        }
        with open(self.file, 'w') as f:
            json.dump(data, f)

    def parse_data(self):
        with open(self.file, 'r') as f:
            data = json.load(f)
        self.username = data.get('username', '')
        self.password = data.get('password', '')
        self.account_number = data.get('account_number', '')
        self.sessionId = data.get('sessionId', '')
        self.mobileId = data.get('mobileId', '')
        self.clientId = data.get('clientId', '')
        self.token = data.get('token', '')
        self.accessToken = data.get('accessToken', '')
        self.authToken = data.get('authToken', '')
        self.cif = data.get('cif', '')
        self.res = data.get('res', '')
        self.tranId = data.get('tranId', '')
        self.browserToken = data.get('browserToken', '')
        self.browserId = data.get('browserId', '')
        self.E = data.get('E', '')
    def init_guid(self):
        timestamp = str(int(time.time()))
        self.uuid = str(uuid.uuid4())
        combined_string = f"{timestamp}{self.uuid}"
        self.guid = hashlib.md5(combined_string.encode()).hexdigest()
        
        
    def createTaskCaptcha(self, base64_img):
        url_1 = 'https://captcha.pay2world.vip//ibscorp'
        url_2 = 'https://captcha1.pay2world.vip//ibscorp'
        url_3 = 'https://captcha2.pay2world.vip//ibscorp'
        
        payload = json.dumps({
        "image_base64": base64_img
        })
        headers = {
        'Content-Type': 'application/json'
        }
        
        for _url in [url_1, url_2, url_3]:
            try:
                response = requests.request("POST", _url, headers=headers, data=payload, timeout=10)
                if response.status_code in [404, 502]:
                    continue
                return json.loads(response.text)
            except:
                continue
        return {}
    def solveCaptcha(self):
        url = self.url['getCaptcha'] + self.guid
        response = requests.get(url)
        base64_captcha_img = base64.b64encode(response.content).decode('utf-8')
        result = self.createTaskCaptcha(base64_captcha_img)
        # captchaText = self.checkProgressCaptcha(json.loads(task)['taskId'])
        if 'prediction' in result and result['prediction']:
            captcha_value = result['prediction']
            return {"status": True, "key": self.guid, "captcha": captcha_value}
        else:
            return {"status": False, "msg": "Error solve captcha", "data": result}

    def curlPost(self, url, data,Servicename=None):
        headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJjb3JwSWQiOjU0MjM3MTM5LCJyb2xlSWQiOjMsInNlY3VyaXR5VHlwZSI6IlNPIiwiY3VycmVudFRyYW5TbiI6IiIsImxvZ2luRmxhZyI6IklCIiwibWVudVBlcm1pc3Npb24iOiIzMTAxLDMxMDEwNiwzMTAyMTEsMzEwMjExMDEsMzEwMjExMDIsMzEwMTA1LDMxMDEwNTAxLDMxMDEwNTAyLDMxMDQsMzEwNjAzLDMyMDEsMzIwMTAxLDMyMDExMiwzMjAxMTgsMzIwMjAxLDMyMDIwNCwzMjAyMDYiLCJleHAiOjE3MTg5Mjk1OTQsInVzZXJJZCI6NTAwODExNjcsImlhdCI6MTcxODkyMjM5NCwidXNlcm5hbWUiOiJDSEVDS0VSLUFOVklFVCJ9.5eUTpxjOZb0MlMF_2wbDwtxm71OpA_ztd29zrUM-_g4',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'f5avraaaaaaaaaaaaaaaa_session_=OPBGNPCDNGKOMHLBLBIKHCNEBBHHKKDPLGPPFNNEEOKBOAIDFLFJNFJIEMEJCPMGFGJDKNGHPMBJONEFJANADJAFEKKDOLCOGPCMMAAAOKCMKKBEMKCJAMCFIGOLFKHL; f5avraaaaaaaaaaaaaaaa_session_=GPJLDNELCPEKLCMPCNPJJMFFKLFLNKEHCMAGFEHKHDGOMAIFGPBINOMAMHGIONFGKHLDNPAALMOMFLNPCNMAKAEFDKHMIPFPCKPHOGBGJHEFINMBFDBCBODOFJHEGMBE; f5avraaaaaaaaaaaaaaaa_session_=CPMPLDEGHJANEMICHJOPDLOJHDABJCLAEKBPOKBGNBJKPHFHNHPGAHIMLGNAKOMJCAIDINOPKMIMLIIIGGFAAKEHDKOBMPACPNNNIODFANAPEFAMMGLNODKKKHLEGHCN; GUEST_LANGUAGE_ID=vi_VN; _hjSessionUser_3481884=eyJpZCI6IjhmMTgwZDg5LTkxMWItNWQ1OC1hMWY2LTJmYmVhYTUzOTgxOCIsImNyZWF0ZWQiOjE3MTgwMzY3NDAzNzUsImV4aXN0aW5nIjp0cnVlfQ==; BIGipServer~DC_RD_DMZ_10_PARTITION~ibsretail_for_web=rd10o00000000000000000000ffff0a014962o9081; BIGipServer~DC_RD_DMZ_10_PARTITION~ibsretail_foward_to_waf=rd10o00000000000000000000ffff0a012164o80; JSESSIONID=0000Fw4Ksw_87NAIwuJm4wAl248:1gr331l1d; TS01abae3f028=01d8bece9143d3c659e8fa9c0ef407baaae91b7cb357f9df557898f1354f083691d0fcd05bb0bf681b1185ffe56f90c6312934f642; __zi=3000.SSZzejyD5SqfnFE-q0q0p6R6fw2U0nYFEjIjlun12fajbFBvYaH1rIcJyFwE24JLAjhp-8W4JjStDJW.1; _gcl_au=1.1.1364469651.1718919831; _hjSession_3481884=eyJpZCI6IjYyNjkxNzU4LWEyN2EtNDMzMi1iOTI1LTEwYTQxNDBiMDdkYiIsImMiOjE3MTg5MTk4MzEyMzUsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _ga=GA1.1.1245939408.1718919831; _clck=15xyxam%7C2%7Cfms%7C0%7C1632; _tt_enable_cookie=1; _ttp=buK1wHNQ1lwNXlDtMlxG8uZI6k_; _clsk=4bu1j%7C1718919832725%7C1%7C1%7Cq.clarity.ms%2Fcollect; _ga_9D114M3P4Z=GS1.1.1718919831.1.0.1718919833.58.0.0; BIGipServer~DC_RD_DMZ_10_PARTITION~ebank.msb.com.vn-CORP_New=rd10o00000000000000000000ffff0a012117o80; BIGipServer~DC_RD_DMZ_10_PARTITION~ibscorp_foward_to_waf=rd10o00000000000000000000ffff0a0121cbo80; TS01abae3f=01fdc98cc0255b533dc9579f9ad1640cae7240505f81f51f16ebfd54649077b4383b3bc6c8c69b6a3bac56de2fb9db01143805b2498a31c9b8a95445daa4ccdb5665e87a84053c4b7ec8afd4c7bd2e4e1d5b1a732f; BIGipServer~DC_RD_DMZ_10_PARTITION~ibscorp=rd10o00000000000000000000ffff0a0121cco80; TS0650e699027=088feac562ab20005b7c7514c64de017d6999fc55a1a1a0337fee1aa01b8478c2c7129f6e28d32bf08159120a811300019117e751174bd349523bcd59aff9dcd85f2f38710e8a159f220cf199f082acc82e63342c3a52e56022a79a981958478; _ga_G7ZPDJH0EE=GS1.1.1718919837.1.1.1718922480.0.0.0; f5avraaaaaaaaaaaaaaaa_session_=FMOPOMFJJKIODJNMOJLMAANJKGOCNOOAIHKHJCJPOLOOJNMKCPFFKCELEILHABPGEFLDNIDGHLADKMGKKCHADEIONKGOBKOBIMEBONAMIPKBMGEEPONKABGFKBNLDNDO; BIGipServer~DC_RD_DMZ_10_PARTITION~ibscorp=rd10o00000000000000000000ffff0a01492fo9080',
        'Origin': 'https://ebank.msb.com.vn',
        'Referer': 'https://ebank.msb.com.vn/IBSCorp/account/payment',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'authenKey': '',
        'clientId': 'IB',
        'clientTime': '',
        'lang': 'VN',
        'requestId': '',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'signature': 'signature'
        }
        if self.authToken:
            headers['Authorization'] = 'Bearer ' + self.authToken
        if Servicename:
            headers['Servicename'] = Servicename
        response = requests.post(url, headers=headers, data=json.dumps(data))
        result = response.json()
        return result

    def checkBrowser(self, type=1):
        param = {
            "clientOsVersion": self.clientOsVersion,
            "browserVersion": self.browserVersion,
            "browserName": self.browserName,
            "E": self.getE() or "",
            "browserId": self.browserId,
            "lang": self.lang,
            "mid": 3008,
            "cif": "",
            "clientId": "",
            "mobileId": "",
            "sessionId": "",
            "browserToken": self.browserToken,
            "user": self.username
        }
        result = self.curlPost(self.url['authen-service'] + "3008", param)
        if "tranId" in result["transaction"]:
            return self.chooseOtpType(result["transaction"]["tranId"], type)
        else:
            return {
                'code': 400,
                'success': True,
                'message': "checkBrowser failed",
                "param": param,
                'data': result or ""
            }

    def chooseOtpType(self, tranID, type=1):
        param = {
            "clientOsVersion": self.clientOsVersion,
            "browserVersion": self.browserVersion,
            "browserName": self.browserName,
            "E": self.getE() or "",
            "browserId": self.browserId,
            "lang": self.lang,
            "mid": 3010,
            "cif": "",
            "clientId": "",
            "mobileId": "",
            "sessionId": "",
            "browserToken": self.browserToken,
            "tranId": tranID,
            "type": type,  # 1 la sms,5 la smart
            "user": self.username
        }
        result = self.curlPost(self.url['authen-service'] + "3010", param)
        if result["code"] == "00":
            self.tranId = tranID
            self.saveData()
            self.challenge = result.get("challenge", "")
            return {
                    'code': 200,
                    'success': True,
                    'message': 'Thành công',
                "result": {
                    "browserToken": self.browserToken,
                    "tranId": result.get("tranId", ""),
                    "challenge": result.get("challenge", "")
                },
                "param": param,
                'data': result or ""
            }
        else:
            return {
                'code': 400,
                'success': False,
                'message': result["des"],
                "param": param,
                'data': result or ""
            }

    def submitOtpLogin(self, otp):
        param = {
            "clientOsVersion": self.clientOsVersion,
            "browserVersion": self.browserVersion,
            "browserName": self.browserName,
            "E": self.getE() or "",
            "browserId": self.browserId,
            "lang": self.lang,
            "mid": 3011,
            "cif": "",
            "clientId": "",
            "mobileId": "",
            "sessionId": "",
            "browserToken": self.browserToken,
            "tranId": self.tranId,
            "otp": otp,
            "challenge": self.challenge,
            "user": self.username
        }
        result = self.curlPost(self.url['authen-service'] + "3011", param)
        if result["data"]["code"] == "00":
            self.sessionId = result["sessionId"]
            self.mobileId = result["userInfo"]["mobileId"]
            self.clientId = result["userInfo"]["clientId"]
            self.cif = result["userInfo"]["cif"]
            session = {"sessionId": self.sessionId, "mobileId": self.mobileId, "clientId": self.clientId, "cif": self.cif}
            self.res = result
            self.saveData()
            
            if result["allowSave"]:
                sv = self.saveBrowser()
                if sv["code"] == "00":
                    self.is_login = True
                    return {
                        'code': 200,
                        'success': True,
                        'message': 'Thành công',
                        'saved_browser': True,
                        "d": sv,
                        'session': session,
                        'data': result or ""
                    }
                else:
                    return {
                        'code': 400,
                        'success': False,
                        'message': sv["des"],
                        "param": param,
                        'data': sv or ""
                    }
            else:
                return {
                        'code': 200,
                        'success': True,
                        'message': 'Thành công',
                        'saved_browser': False,
                        'session': session,
                        'data': result or ""
                    }
        else:
            return {
                'code': 500,
                'success': False,
                'message': result["des"],
                "param": param,
                'data': result or ""
            }

    def saveBrowser(self):
        param = {
            "clientOsVersion": self.clientOsVersion,
            "browserVersion": self.browserVersion,
            "browserName": self.browserName,
            "E": self.getE() or "",
            "browserId": self.browserId,
            "browserName": "Microsoft Edge 125.0.0.0",
            "lang": self.lang,
            "mid": 3009,
            "cif": self.cif,
            "clientId": self.clientId,
            "mobileId": self.mobileId,
            "sessionId": self.sessionId,
            "user": self.username
        }
        result = self.curlPost(self.url['authen-service'] + "3009", param)
        return result

    def doLogin(self):
        solveCaptcha = self.solveCaptcha()
        if not solveCaptcha["status"]:
            return solveCaptcha

        param = {
            
            "browserVersion": self.browserVersion,
            "browserName": self.browserName,
            
            "clientIp": self.clientIp,
            "guid": self.guid,
            "captcha": solveCaptcha["captcha"],
            
            "clientOsVersion": self.clientOsVersion,
            
            "deviceCode": self.deviceCode,
            "deviceName": self.deviceName,
            "lang": self.lang,
            
            "password": hashlib.md5(self.password.encode()).hexdigest(),
            "username": self.username,
        }
        result = self.curlPost(self.url['login'], param)
        if result['errorCode'] == "000" and 'jwt' in result:
            self.deviceCode = result['data']['userInfo']['deviceCode']
            self.authToken = result['jwt']
            self.userInfo = result['data']['userInfo']
            session = {
                "authToken": self.authToken,
            }
            self.save_data()
            self.is_login = True
            return {
                'code': 200,
                'success': True,
                'message': "success",
                'session': session,
                'userInfo': self.userInfo,
                'data': result if result else ""
            }
        else:
            return {
                'code': 500,
                'success': False,
                'message': result['message'],
                "param": param,
                'data': result if result else ""
            }

    def saveData(self):
        data = {
            'username': self.username,
            'password': self.password,
            'account_number': self.account_number,
            'sessionId': self.sessionId,
            'mobileId': self.mobileId,
            'clientId': self.clientId,
            'cif': self.cif,
            'E': self.E,
            'res': self.res,
            'tranId': self.tranId,
            'browserToken': self.browserToken,
            'browserId': self.browserId,
        }
        with open(f"data/{self.username}.txt", "w") as file:
            json.dump(data, file)

    def parseData(self):
        with open(f"data/{self.username}.txt", "r") as file:
            data = json.load(file)
            self.username = data["username"]
            self.password = data["password"]
            self.account_number = data.get("account_number", "")
            self.sessionId = data.get("sessionId", "")
            self.mobileId = data.get("mobileId", "")
            self.clientId = data.get("clientId", "")
            self.token = data.get("token", "")
            self.accessToken = data.get("accessToken", "")
            self.authToken = data.get("authToken", "")
            self.cif = data.get("cif", "")
            self.res = data.get("res", "")
            self.tranId = data.get("tranId", "")
            self.browserToken = data.get("browserToken", "")
            self.browserId = data.get("browserId", "")
            self.E = data.get("E", "")

    def getE(self):
        ahash = hashlib.md5(self.username.encode()).hexdigest()
        imei = '-'.join([ahash[i:i+4] for i in range(0, len(ahash), 4)])
        return imei.upper()

    def getCaptcha(self):
        captchaToken = ''.join(random.choices(string.ascii_uppercase + string.digits, k=30))
        url = self.url['getCaptcha'] + captchaToken
        response = requests.get(url)
        result = base64.b64encode(response.content).decode('utf-8')
        return result

    def getlistAccount(self):
        if not self.is_login:
            login = self.doLogin()
            if not login['success']:
                return login
        param = {}
        result = self.curlPost(self.url['getlistAccount'], param,"GetAccountInfo")
        if 'data' in result and 'errorCode' in result and result['errorCode'] == '000':
            for account in result['data']:
                if self.account_number == account['acctNo']:
                    if float(account['availableBalance']) < 0:
                        return {'code':448,'success': False, 'message': 'Blocked account with negative balances!',
                                'data': {
                                    'balance':float(account['availableBalance'])
                                }
                                }
                    else:
                        return {'code':200,'success': True, 'message': 'Thành công',
                                'data':{
                                    'account_number':self.account_number,
                                    'balance':float(account['availableBalance'])
                        }}
            return {'code':404,'success': False, 'message': 'account_number not found!'} 
        else: 
            return {'code':520 ,'success': False, 'message': 'Unknown Error!'} 

    def getlistDDAccount(self):
        param = {
            "clientOsVersion": self.clientOsVersion,
            "browserVersion": self.browserVersion,
            "browserName": self.browserName,
            "browserId": self.browserId,
            "E": self.getE() or "",
            "mid": 35,
            "cif": self.cif,
            "serviceCode": "0551",
            "user": self.username,
            "mobileId": self.mobileId,
            "clientId": self.clientId,
            "sessionId": self.sessionId
        }
        result = self.curlPost(self.url['getlistDDAccount'], param)
        return result

    def getAccountDeltail(self):
        param = {
            "clientOsVersion": self.clientOsVersion,
            "browserVersion": self.browserVersion,
            "browserName": self.browserName,
            "E": self.getE() or "",
            "browserId": self.browserId,
            "accountNo": self.account_number,
            "accountType": "D",
            "mid": 13,
            "cif": self.cif,
            "user": self.username,
            "mobileId": self.mobileId,
            "clientId": self.clientId,
            "sessionId": self.sessionId
        }
        result = self.curlPost(self.url['getAccountDeltail'], param)
        return result

    def getHistories(self, fromDate="16/06/2023", toDate="16/06/2023", account_number='', page=1,limit = 100):
        if not self.is_login:
                login = self.doLogin()
                if not login['success']:
                    return login
        param = {
            "acctNo": account_number if account_number else self.account_number,
            "fromDate": fromDate,
            "historyType": "CORE",
            "toDate": toDate,
            "page": page,
            "pageSize": limit
        }
        result = self.curlPost(self.url['getHistories'], param,"AccountHistory")
        if 'errorCode' in result and result['errorCode'] == '000' and 'data' in result and 'coreHistoryList' in result['data']:
            return {'code':200,'success': True, 'message': 'Thành công',
                            'data':{
                                'transactions':result['data']['coreHistoryList'],
                    }}
        else:
            return  {
                    "success": False,
                    "code": 503,
                    "message": "Service Unavailable!"
                }

    def getBanks(self):
        param = {
            "clientOsVersion": self.clientOsVersion,
            "browserVersion": self.browserVersion,
            "browserName": self.browserName,
            "E": self.getE() or "",
            "browserId": self.browserId,
            "lang": self.lang,
            "fastTransfer": "1",
            "mid": 23,
            "cif": self.cif,
            "user": self.username,
            "mobileId": self.mobileId,
            "clientId": self.clientId,
            "sessionId": self.sessionId
        }
        result = self.curlPost(self.url['getBanks'], param)
        return result

    def createTranferOutMSB(self, bankCode, account_number, amount, message):
        param = {
            "clientOsVersion": self.clientOsVersion,
            "browserVersion": self.browserVersion,
            "browserName": self.browserName,
            "E": self.getE() or "",
            "browserId": self.browserId,
            "lang": self.lang,
            "debitAccountNo": self.account_number,
            "creditAccountNo": account_number,
            "creditBankCode": bankCode,
            "amount": amount,
            "feeType": 1,
            "content": message,
            "ccyType": "1",
            "mid": 62,
            "cif": self.cif,
            "user": self.username,
            "mobileId": self.mobileId,
            "clientId": self.clientId,
            "sessionId": self.sessionId
        }
        result = self.curlPost(self.url['tranferOut'], param)
        return result

    def createTranferInMSB(self, account_number, amount, message):
        param = {
            "clientOsVersion": self.clientOsVersion,
            "browserVersion": self.browserVersion,
            "browserName": self.browserName,
            "E": "",
            "browserId": self.browserId,
            "lang": self.lang,
            "debitAccountNo": self.account_number,
            "creditAccountNo": account_number,
            "amount": amount,
            "activeTouch": 0,
            "feeType": 1,
            "content": message,
            "ccyType": "",
            "mid": 16,
            "cif": self.cif,
            "user": self.username,
            "mobileId": self.mobileId,
            "clientId": self.clientId,
            "sessionId": self.sessionId
        }
        result = self.curlPost(self.url['tranferIn'], param)
        return result

    def genOtpTranFer(self, tranId, type="OUT", otpType=5):
        if otpType == 1:
            solveCaptcha = self.solveCaptcha()
            if not solveCaptcha["status"]:
                return solveCaptcha
            param = {
                "clientOsVersion": self.clientOsVersion,
                "browserVersion": self.browserVersion,
                "browserName": self.browserName,
                "E": self.getE() or "",
                "lang": self.lang,
                "tranId": tranId,
                "type": otpType,  # 1 là SMS,5 là smart otp
                "captchaToken": solveCaptcha["key"],
                "captchaValue": solveCaptcha["captcha"],
                "browserId": self.browserId,
                "mid": 17,
                "cif": self.cif,
                "user": self.username,
                "mobileId": self.mobileId,
                "clientId": self.clientId,
                "sessionId": self.sessionId
            }
        else:
            param = {
                "clientOsVersion": self.clientOsVersion,
                "browserVersion": self.browserVersion,
                "browserName": self.browserName,
                "E": self.getE() or "",
                "lang": self.lang,
                "tranId": tranId,
                "type": otpType,  # 1 là SMS,5 là smart otp
                "mid": 17,
                "browserId": self.browserId,
                "cif": self.cif,
                "user": self.username,
                "mobileId": self.mobileId,
                "clientId": self.clientId,
                "sessionId": self.sessionId
            }

        if type == "IN":
            result = self.curlPost(self.url['genOtpIn'], param)
        else:
            result = self.curlPost(self.url['genOtpOut'], param)
        return result

    def confirmTranfer(self, tranId, challenge, otp, type="OUT", otpType=5):
        if otpType == 5:
            param = {
                "clientOsVersion": self.clientOsVersion,
                "browserVersion": self.browserVersion,
                "browserName": self.browserName,
                "E": self.getE() or "",
                "lang": self.lang,
                "tranId": tranId,
                "otp": otp,
                "challenge": challenge,
                "mid": 18,
                "cif": self.cif,
                "user": self.username,
                "browserId": self.browserId,
                "mobileId": self.mobileId,
                "clientId": self.clientId,
                "sessionId": self.sessionId
            }
        else:
            param = {
                "clientOsVersion": self.clientOsVersion,
                "browserVersion": self.browserVersion,
                "browserName": self.browserName,
                "E": self.getE() or "",
                "browserId": self.browserId,
                "lang": self.lang,
                "tranId": tranId,
                "otp": otp,
                "challenge": challenge,
                "mid": 18,
                "cif": self.cif,
                "user": self.username,
                "mobileId": self.mobileId,
                "clientId": self.clientId,
                "sessionId": self.sessionId
            }

        if type == "IN":
            result = self.curlPost(self.url['confirmTranferIn'], param)
        else:
            result = self.curlPost(self.url['confirmTranferOut'], param)
        return result