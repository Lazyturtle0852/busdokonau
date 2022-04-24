# -*- coding: unicode-escape -*- 
from http.server import BaseHTTPRequestHandler
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        from urllib import request 
        from bs4 import BeautifulSoup  
        url = 'http://real.kanachu.jp/pc/displayapproachinfo?uid=selectstop&fNM=%8F%C3%93%EC%91%E4%89w%90%BC%8C%FB&tNM=%8Cc%89%9E%91%E5%8Aw&fNO=24096&tNO=24200&x=71&y=25'
        response = request.urlopen(url)
        soup = BeautifulSoup(response)
        response.close()
        try:
          bustime1 = soup.select_one('#main > div.frameArea01 > div > div > div:nth-of-type(4) > div.col02 > div.frameBox03 > p').get_text(strip=True)
          buskind1 = soup.select_one('#main > div.frameArea01 > div > div > div:nth-of-type(4) > div.col01').get_text(strip=True)
          if "ツインライナー" in buskind1:
            buskind1 = "ツインライナー"
          else:
            buskind1 = "通常バス"
          businfo1 = "一本目:"+buskind1+"での運行です。"+bustime1.replace('予定通り発車します','')
        except AttributeError:
          businfo1 = '本日の運行は終了しました。'
        message= businfo1
        self.wfile.write(message.encode('unicode-escape'))
        try:
          bustime2 = soup.select_one('#main > div.frameArea01 > div > div > div:nth-of-type(6) > div.col02 > div.frameBox03 > p').get_text(strip=True)
          buskind2 = soup.select_one('#main > div.frameArea01 > div > div > div:nth-of-type(6) > div.col01 > table:nth-of-type(2) > tbody').get_text(strip=True)

          if "ツインライナー" in buskind2:
           buskind2 = "ツインライナー"
          else:
            buskind2 = "通常バス"
          businfo2 = "二本目:"+buskind2+"での運行です。"+bustime2.replace('予定通り発車します','') 
        except AttributeError:
          businfo2 = '本日の運行は終了しました。'
        message= businfo2
        self.wfile.write(message)

        try:
          bustime3 = soup.select_one('#main > div.frameArea01 > div > div > div:nth-of-type(8) > div.col02 > div.frameBox03 > p').get_text(strip=True)
          buskind3 = soup.select_one('#main > div.frameArea01 > div > div > div:nth-of-type(8) > div.col01 > table:nth-of-type(2) > tbody').get_text(strip=True)
          if "ツインライナー" in buskind3:
            buskind3 = "ツインライナー"
          else:
            buskind3 = "通常バス"
          businfo3 = "三本目:"+buskind3+"での運行です。"+bustime3.replace('予定通り発車します','')
        except AttributeError:
          businfo3 = '本日の運行は終了しました。'
        message= businfo3
        self.wfile.write(message)

