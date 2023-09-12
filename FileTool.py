import requests

class SpamMsgFacebook:
    def __init__(self,Cookies_FB) -> None:
        cookie = Cookies_FB.split(';')
        title = []
        value = []
        for i in range(len(cookie) - 1):
            title.append(cookie[i].split('=')[0].strip())
            value.append(cookie[i].split('=')[1].strip())
        self.cookies = dict(zip(title, value))
        
        self.headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'dpr': '1',
        'referer': 'https://mbasic.facebook.com/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.180", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.180"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"7.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'viewport-width': '670',
        }
        self.uid = self.cookies['c_user']
    def GetUserName(self):
        facebook = requests.get(f"https://mbasic.facebook.com/{self.uid}/", headers=self.headers, cookies=self.cookies).text
        self.UserName = facebook.split('<title>')[1].split('</')[0]
    def run(self, id):
        Profile_Target = requests.get(f"https://mbasic.facebook.com/{id}/", headers=self.headers, cookies=self.cookies).text
        Url_Mess_Target = "https://mbasic.facebook.com/messages/thread/"+Profile_Target.split('"/messages/thread/')[1].split('"')[0].replace("amp;", "")
        Mess_Target = requests.get(Url_Mess_Target,headers=self.headers,cookies=self.cookies).text
        icm = "https://mbasic.facebook.com/messages/send/?icm=" + Mess_Target.split('action="/messages/send/?icm=')[1].split('"')[0].replace("amp;","")
        fb_dtsg = Mess_Target.split('name="fb_dtsg" value="')[1].split('"')[0]

ApiFB = SpamMsgFacebook("sb=eGmAZPUCSjQrLBYA3sabl7Cr;datr=eGmAZOc8IE8tbGfQI6YDg3bP;c_user=100049621511685;m_page_voice=100049621511685;xs=47%3APDuvkXgi3fOygQ%3A2%3A1687658876%3A-1%3A6276%3A%3AAcWEISwCWryUvOwx_Xg6DFW-z7w-gpvKpyNhfgO01Oyc;fr=0SinOWDM24032Dv76.AWXtD6ZZZuK1arcB9PCsa8lbnCA.Bk__v0.vS.AAA.0.0.Bk__wa.AWX2z7V-nAQ;wd=1280x907;presence=C%7B%22lm3%22%3A%22u.100091741684428%22%2C%22t3%22%3A%5B%5D%2C%22utc3%22%3A1694498035084%2C%22v%22%3A1%7D;")
ApiFB.run("100076657214923")
https://mbasic.facebook.com/messages/send/?icm=1&eav=Afam6ILUDqLAz6atQzWboXM0DJAATnv6zoatq37l6JPLU6qY4GubHwNeJZM-h1I_6_E&paipv=0&refid=12
