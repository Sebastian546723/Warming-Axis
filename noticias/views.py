from django.shortcuts import render
from newsapi import NewsApiClient
from noticias import models as ModelObject
import schedule
import time
import threading

newsapi = NewsApiClient(api_key='3e10e6f5c0d046a7aef93f1db3e778a9')

NewsList = {'articles':[],
            'error': False}

def getIDs():
    NewsList["articles"] = []
    IDs= list(ModelObject.News.objects.values('id'))

    if NewsList["error"] == False and len(ModelObject.News.objects.values('id')) != 0:
        for i in range(1,4):
            getNews = ModelObject.News.objects.get(id = IDs[-i]['id'])

            NewsList['articles'].append(
                {
                "id": getNews.id,
                "title": getNews.Title, 
                "description": getNews.Description, 
                "urlToImage": getNews.ImgNews, 
                "url": getNews.URL, 
                "name": getNews.Source}
                )

def searchNews():
    NewsList["error"] = False
    keyWords = ["climate change", "global Warming", "climate crisis", "greenhouse effect", "fossil fuels", "renewable energy", "global temperature"]
    newsLoaded = 0
    PageNews = 0
    while newsLoaded < 3 and NewsList["error"] == False:
        if PageNews == len(keyWords):
            NewsList["error"] = True
        else:
            top_headlines = newsapi.get_everything(q=keyWords[PageNews],
                                    sort_by='relevancy',
                                    language='es')
        if top_headlines["status"] == "error":
            NewsList["error"] = True

        for a in top_headlines["articles"]:
            model = ModelObject.News.objects.filter(Title = a["title"])
            if len(model) == 0:
                if newsLoaded < 3:
                    ModelObject.News.objects.create(
                        Title = a["title"] or "",
                        Description = a["description"] or "",
                        ImgNews = a["urlToImage"] or "",
                        URL = a["url"] or "",
                        Source = a["source"]["name"] or ""
                    )
                    newsLoaded += 1
        PageNews +=1
    getIDs()

def SearchLoop():
    schedule.every().day.at("23:59").do(searchNews)
    #schedule.every(30).seconds.do(searchNews)

    while True:
        schedule.run_pending()
        time.sleep(1)

hilo = threading.Thread(target=SearchLoop)
hilo.start()

def noticias(request):
    if len(ModelObject.News.objects.values('id')) == 0:
        searchNews()
    if len(NewsList["articles"]) == 0:
        getIDs()

    return render(request, "noticias.html", NewsList)

def foros(request):
    if len(ModelObject.News.objects.values('id')) == 0:
        searchNews()
    if len(NewsList["articles"]) == 0:
        getIDs()
    return render(request, "foros.html", NewsList)
