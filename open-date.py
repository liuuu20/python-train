#網路連線
import urllib.request as request

src="https://www.im.tku.edu.tw/"
with request.urlopen(src) as response:
    data=response.read().decode("utf-8")
print(data)
#串接、擷取公開資料