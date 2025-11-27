import requests
import re
import time
urls = ["https://www.baidu.com/",
        "https://www.google.com/",
        "https://news.qq.com/",
        "https://www.bbc.com/news",
        "https://www.cnn.com/",
        "https://www.nytimes.com/",
        "https://www.theguardian.com/international",
        "https://www.aljazeera.com/",
        "https://www.reuters.com/"]

def getTitle(url: str) -> str | None:
    headers ={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
    }
    response = requests.get(url=url,headers=headers)
    #正则表达式筛选标题
    parr = re.findall(r"<title[^>]*>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
    title = re.sub(r"\s+", " ", parr[0]).strip()
    return title

#将标题及网址输出至log文件
def write_to_log(title: str, url: str) -> None:
    with open("log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"Title: {title}\tURL: {url}\tTime: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

if __name__ == "__main__":
    for url in urls:
        title = getTitle(url)
        if title:
            print(f"Title: {title}\nURL: {url}\n")
            write_to_log(title, url)
        else:
            print(f"Failed to retrieve title for URL: {url}\n")