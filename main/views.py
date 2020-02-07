from django.shortcuts import render,HttpResponse

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

import requests
import re



'''Image search'''

def get_url_images_in_text(html, protocol):
    urls = []
    all_urls = re.findall(r'((http\:|https\:)?\/\/[^"\' ]*?\.(png|jpg))', html, flags=re.IGNORECASE | re.MULTILINE | re.UNICODE)
    for url in all_urls:
        if not url[0].startswith("http"):
            urls.append(protocol + url[0])
        else:
            urls.append(url[0])
    return urls
def get_images_from_url(url):
    protocol = url.split('/')[0]
    resp = requests.get(url)
    return get_url_images_in_text(resp.text, protocol)



def generate_link(search_keyword):
    #https://news.google.com/rss/search?cf=all&hl=en-IN&q= 
    link_part_1 = 'https://news.google.com/news/feeds?cf=all&ned=in&hl=en&q='
    search_keyword = search_keyword.replace(" ","")
    link = link_part_1+search_keyword+'&output=rss'    
    return link

def generate_hindi_link(search_keyword):
    link_part_1 = 'https://news.google.com/news/feeds?cf=all&ned=in&hl=hi&q='
    search_keyword = search_keyword.replace(" ","")
    link = link_part_1+search_keyword+'&gl=IN&ceid=IN:hi'    
    return link
def get_news(url):
    '''news_link = "https://news.google.com/news/rss"'''
    
    page = urlopen(url)
    xml_page = page.read()
    page.close()

    soup_page = soup(xml_page, "xml")
    news_list = map(
        lambda item: {'title': item.title.text, 'date': item.pubDate.text,'links': item.link.text}
        ,soup_page.findAll("item"))    
    return news_list    

def index(request):
    if 'search_word' in request.POST:
        search_word = request.POST['search_word']
    else:
        search_word = 'world'    
    news = get_news(generate_link(search_word))
    return render(request,'index.html',{'news_list' : news,'keyword':search_word})

def hindi_news(request):
    if 'search_word' in request.POST:
        search_word = request.POST['search_word']
    else:
        search_word = 'world'    
    news = get_news(generate_hindi_link(search_word))
    return render(request,'hindi.html',{'news_list' : news,'keyword':search_word})