#網路連線
# import urllib.request as request

#src="https://www.im.tku.edu.tw/"
#with request.urlopen(src) as response:
    #data=response.read().decode("utf-8")
#print(data)

#串接、擷取公開資料
import urllib.request as request

src="https://data.moa.gov.tw/Service/OpenData/TraceBeefData.aspx?IsTransData=1&UnitId=369"
with request.urlopen(src) as response:
    data=json.load(response) #json.load()直接將JSON格式資料轉成Python資料結構
print(data)