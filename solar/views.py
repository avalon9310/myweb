from django.shortcuts import render, redirect
from  datetime import  datetime
from django.utils.safestring import mark_safe
import numpy as np
from G import G
def html(request):
    info = G.saveHistory(request, 'solar')
    request.session["currentPage"] = "/solar"
    if 'userAccount' not in request.session:
        return redirect("/login")
    if "year" in request.POST:
        now = int(request.POST["year"])
    else:
        now = int(datetime.now().strftime("%Y"))
    year_list = list(range(2000, 2051))
    #日期 = (Y * D + C)-L
    #Y : 西元年後二位
    #D : 0.2422
    #C : 常數
    #L : 閏年數
    D = 0.2422
    solar_dic = {
        '立春': 0, '雨水': 1, '驚蟄': 2, '春分': 3, '清明': 4, '穀雨': 5,
        '立夏': 6, '小滿': 7, '芒種': 8, '夏至': 9, '小暑': 10, '大暑': 11,
        '立秋': 12, '處暑': 13, '白露': 14, '秋分': 15, '寒露': 16, '霜降': 17,
        '立冬': 18, '小雪': 19, '大雪': 20, '冬至': 21, '小寒': 22, '大寒': 23
    }

    C0 = [3.87, 18.73, 5.63, 20.646, 4.81, 20.888,
          6.318, 21.86, 6.5, 22.2, 7.928, 23.65,
          8.35, 23.95, 8.44, 23.822, 9.098, 24.218,
          8.218, 23.08, 7.9, 22.6, 6.11, 20.84]

    C1 = np.array([3.8585, 18.689,
                   5.6085, 20.6475,
                   4.8069, 20.106,
                   5.526, 21.068,
                   5.6975, 21.398,
                   7.123, 22.85,
                   7.53, 23.1445,
                   7.652, 23.047,
                   8.396, 23.047,
                   7.4405, 22.338,
                   7.145, 21.896,
                   5.6155, 20.341], dtype=np.float64)

    if now >= 2000:
        C = C1
    else:
        C = C0
    year_last=now % 100

    terms = list(solar_dic.keys())

    html = "<table>"
    for row in range(12):
        html += "<tr>"
        for col in range(2):
            index = row * 2 + col
            yyyy = now
            month = int(index / 2) + 2
            if month == 13:
                month = 1
                yyyy += 1

            #閏年數
            leap = year_last
            if index<=1 or index >=22:leap -=1
            day = year_last * D +C[index] - int(leap / 4)
            if now == 2000 and (index <=1 or index >=22): day +=1

            hr = (day-int(day))*24
            min = (hr - int(hr)) * 60

            html += f'<td>{terms[index]}</td>'
            html += f'<td>{yyyy}-{month:02d}-{int(day):02.0f} {hr:02.0f}:{min:02.0f}</td>'
        html += "</tr>"
    html += "</table>"
    return render(request, 'solar.html',
          {
                'year_now':now,
                'year_list': year_list,
                'html':mark_safe(html),
                "info": info[1],
                "userAccount":G.userAccount(request)
          }
    )


