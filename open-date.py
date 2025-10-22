#網路連線
# import urllib.request as request

#src="https://www.im.tku.edu.tw/"
#with request.urlopen(src) as response:
    #data=response.read().decode("utf-8")
#print(data)

#串接、擷取公開資料
import urllib.request as request
import json
src="https://od.moi.gov.tw/api/v1/rest/datastore/301000000A-001489-022"
with request.urlopen(src) as response:
    data=json.load(response) #json.load()直接將JSON格式資料轉成Python資料結構
print(data)

#將公司名稱列表出來
clist = data["result"]["results"]
with open("company.txt","w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["CompanyName"]+"\n")
print("公司名稱已寫入company.txt檔案中")