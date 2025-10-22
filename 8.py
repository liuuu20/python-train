#抓取PTT八卦版的網頁原始碼(HTML)
import urllib.request as req

def getDate(url):
    url="https://www.ptt.cc/bbs/Gossiping/index.html"
    #建立一個Request物件，附加Request Headers的資訊
    request=req.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
        })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    

    #解析原始碼，取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="title") #尋找所有class="title"的div標籤
    for title in titles:
        if title.a != None:  #有些文章可能被刪除，沒有a標籤
            print(title.a.string)  #取得標題文字
    #取得上一頁的連結
    nextlink=root.find("a",string="‹ 上頁") #尋找內文是‹ 上頁的a標籤
    return nextlink["href"]

#抓取一個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<5:
    
    pageURL="https://www.ptt.cc"+getDate(pageURL)
    count+=1

