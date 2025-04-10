from datetime import datetime

import requests
from django.utils.safestring import mark_safe


class G():
    dbHost="localhost"
    dbAccount="avalon"
    dbPassword="cious104534233"
    db="cloud"
    @staticmethod
    def saveHistory(request, page):
        x = request.META.get("HTTP_X_FORWARDED_FOR")
        if x:
            ip = x.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")

        #查詢地區及經緯度
        city=""
        country=""
        lat=0
        lng=0
        url = "http://ip-api.com/batch?"
        param={'fileds':'status, message, country, countryCode, region, regionName, city, query, lon, lat',
               'lang':'en-US'}
        ip_list = [ip]
        res=requests.post(url=url, params=param, json=ip_list)
        info=res.json()[0]
        if 'country' in info:
            country = info['country']
            city = info['city']
            lat = info['lat']
            lng = info['lon']

        #儲存到資料庫
        t = datetime.now()
        eventDay = t.strftime("%Y-%m-%d")
        evenTime = t.strftime("%H:%M:%S")


        return ip,mark_safe(
        f"""
            <p class='info'>{ip}</p>
            <p class='info'>{country} {city}</p>
            <p class='info'>{lng:.5f} {lat:.5f}</p>
        """
        )
    @staticmethod
    def userAccount(request):
        userAccount=""
        if "userAccount" in request.session:
            userAccount=request.session["userAccount"]
        return userAccount
