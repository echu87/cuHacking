from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup as bs
import requests
# Create your views here.
def homepage(request):
    context = { "video":findVideo()}
    return render(request,"projects/main.html",context)

def findVideo():
    mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}

    requests.get("https://www.youtube.com", headers = mozhdr)
   
    scrape_url="https://www.youtube.com"
    search_url="/results?search_query="
    search_hardcode = "cosine+law"

    sb_url = scrape_url + search_url + search_hardcode

    sb_get = requests.get(sb_url, headers = mozhdr)
    sb_get.content

    soupeddata = bs(sb_get.content, "html.parser")
    
    yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")

    for x in yt_links:
        yt_href = x.get("href")
        yt_title = x.get("title")
    
    link = scrape_url + yt_href
    title = yt_title
    
    return [link, title]




