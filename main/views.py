from django.shortcuts import render,HttpResponse

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

from googletrans import Translator      #for translating keyword to english if input is given in other lang

def generate_link(search_keyword):
    #https://news.google.com/rss/search?cf=all&hl=en-IN&q= 
    try:
        link_part_1 = 'https://news.google.com/news/feeds?cf=all&ned=in&hl=en&q='
        search_keyword = search_keyword.replace("#","@")
        search_keyword = search_keyword.replace(" ","+")
        link = link_part_1+search_keyword+'&output=rss'
        return link    
    except:
        link = "https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en"
        return link

def generate_hindi_link(search_keyword):
    try:
        link_part_1 = 'https://news.google.com/news/feeds?cf=all&ned=in&hl=hi&q='
        search_keyword = search_keyword.replace("#","@")
        search_keyword = search_keyword.replace(" ","+")
        link = link_part_1+search_keyword+'&gl=IN&ceid=IN:hi'    
        return link
    except:
        link = "https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en"
        return link
def generate_marathi_link(search_keyword):
    try:
        link_part_1 = 'https://news.google.com/news/feeds?cf=all&ned=in&hl=mr&q='
        search_keyword = search_keyword.replace("#","@")
        search_keyword = search_keyword.replace(" ","+")
        link = link_part_1+search_keyword+'&gl=IN&ceid=IN:mr'    
        return link
    except:
        link = "https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en"
        return link
    #https://news.google.com/rss/search?cf=all&hl=mr&q=news&gl=IN&ceid=IN:mr

def get_news(url):
    '''news_link = "https://news.google.com/news/rss"'''
    
    page = urlopen(url)                         #open webpage
    xml_page = page.read()             
    page.close()

    soup_page = soup(xml_page, "xml")
    #extracting all data in map object
    news_list = map(
        lambda item: {'title': item.title.text, 'date': item.pubDate.text,'links': item.link.text}
        ,soup_page.findAll("item"))    
    return news_list    

def change_language(keyword):
    translator = Translator()       #translator object
    r_lang = translator.detect(keyword)             #detect the lkeyword language
    if r_lang.lang != 'en':             #if language is not english
        translated_sentence = translator.translate(keyword)   #translate keyword to english
        keyword = translated_sentence.text
    return keyword    

def index(request):
    if 'search_word' in request.GET:
        search_word = request.GET['search_word']
        #now translating if keyword is from different language
        search_word = change_language(search_word)
    else:
        search_word = 'world'    
    news = get_news(generate_link(search_word))
    return render(request,'index.html',{'news_list' : news,'keyword':search_word})

def hindi_news(request):
    if 'search_word' in request.GET:
        search_word = request.GET['search_word']
        #now translating if keyword is from different language
        search_word = change_language(search_word)        #replacing content of search word with translated word
    else:
        search_word = 'world'    
    news = get_news(generate_hindi_link(search_word))
    return render(request,'hindi.html',{'news_list' : news,'keyword':search_word})

def marathi_news(request):
    if 'search_word' in request.GET:
        search_word = request.GET['search_word']
        #now translating if keyword is from different language
        search_word = change_language(search_word)
    else:
        search_word = 'world'    #bt default, it shows worlds news
    news = get_news(generate_marathi_link(search_word))    #generating news from the above function
    return render(request,'marathi.html',{'news_list' : news,'keyword':search_word})
  