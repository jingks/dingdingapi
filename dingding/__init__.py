__doc__ = """
钉钉自定义机器人类
"""

import time
import hmac
import hashlib
import base64
import json
import requests
import urllib.parse

class customRobot():

    secret = ''
    access_token = ''
    timestamp = ''
    sign = ''
    url = ''

    def __init__(self, access_token, secret):
        self.secret = secret
        self.access_token = access_token
        self._get_url()
        print(self.url)

    def _get_url(self):
        self.timestamp = str(round(time.time() * 1000))
        secret_enc = self.secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(self.timestamp, self.secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod = hashlib.sha256).digest()
        self.sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        self.url = "https://oapi.dingtalk.com/robot/send?access_token=%s&timestamp=%s&sign=%s" % (self.access_token, self.timestamp, self.sign)

    def _send_url(self, jsn):

        headers = {
            "Content-Type": "application/json ;charset=utf-8 "
        }

        r = requests.post(self.url, data = jsn, headers = headers)
        return r.text

    def _get_jsn(self, types, data, to = None):
        jsn = {}
        
        if to is not None:
            if type(to) is list and len(to) > 0:
                jsn["at"] = {}
                jsn["at"]["atMobiles"] = to
            elif to == 'all':
                jsn["at"] = {}
                jsn["at"]["isAtAll"] = "true"
        
        new_jsn = {
            "msgtype": types,
            types: data,
        }
        jsn.update(new_jsn)
        print(json.dumps(jsn))
        return json.dumps(jsn)
    

    def text(self, msg, to = None):
        data = {
            "content": msg
        }
        jsn = self._get_jsn("text", data, to)
        return self._send_url(jsn)

    def link(self, title, text, msg_url, pic_url = "", to = None):
        data = {
            "text": text,
            "title": title,
            "picUrl": pic_url,
            "messageUrl": msg_url
        }
        jsn = self._get_jsn("link", data, to)
        return self._send_url(jsn)


    def markdown(self, title, text, to = None):
        data = {
            "title": title,
            "text": text
        }
        jsn = self._get_jsn("markdown", data, to)
        return self._send_url(jsn)


    def action_card_single(self, title, text, single_title, single_url, to = None):
        data = {
            "title": title,
            "text": text,
            "btnOrientation": 0,
            "singleTitle": single_title,
            "singleURL": single_url
        }

        jsn = self._get_jsn("actionCard", data, to)
        return self._send_url(jsn)

    def action_card_button(self, title, text, btns:"dict", btn_type:"0:vertical 1:Horizontal" = 0, to = None):
        data = {
            "title": title,
            "text": text,
            "btnOrientation": btn_type,
        }
        button = []
        for k, v in btns.items():
            item = {
                "title": k,
                "actionURL": v
            }
            button.append(item)
        data["btns"] = button

        jsn = self._get_jsn("actionCard", data, to)
        return self._send_url(jsn)

    def feed_card(self, articles:"dict {'jump_url':['title', 'pic_url']}", to = None):
        links = []
        for k, v in articles.items():
            link = {
                "messageURL": k,
                "title": v[0],
                "picURL": v[1]
            }
            links.append(link)

        data = {
            "links": links
        }

        jsn = self._get_jsn("feedCard", data, to)
        return self._send_url(jsn)
