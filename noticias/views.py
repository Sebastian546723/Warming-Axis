from django.shortcuts import render
from newsapi import NewsApiClient
from noticias import models as ModelObject
import schedule
import time
import threading

newsapi = NewsApiClient(api_key='3e10e6f5c0d046a7aef93f1db3e778a9')

NewsList = {'articles':[]}
ForoId = {"ids": []}

def getIDs():
        ForoId["ids"] = []
        IDs= list(ModelObject.News.objects.values('id'))

        for i in range(1,4):
            getNews = ModelObject.News.objects.get(id = IDs[-i]['id'])

            ForoId["ids"].append(IDs[-i]['id'])
            NewsList['articles'].append(
                {"title": getNews.Title, 
                "description": getNews.Description, 
                "urlToImage": getNews.ImgNews, 
                "url": getNews.URL, 
                "name": getNews.Source}
                )

def searchNews():
        NewsList["articles"] = []
        newsLoaded = 0
        PageNews = 1
        while newsLoaded < 3:
            top_headlines = newsapi.get_everything(q='Climate Change',
                                    sort_by='relevancy',
                                    language='es')
            for a in top_headlines["articles"]:
                model = ModelObject.News.objects.filter(Title = a["title"])
                if len(model) == 0:
                    if newsLoaded < 3:
                        ModelObject.News.objects.create(
                            Title = a["title"],
                            Description = a["description"],
                            ImgNews = a["urlToImage"],
                            URL = a["url"],
                            Source = a["source"]["name"]
                        )
                        newsLoaded += 1
            
            PageNews +=1

if len(ModelObject.News.objects.values('id')) == 0:
    searchNews()

getIDs()

def SearchLoop():
    
    schedule.every().day.at("23:55").do(searchNews)
    schedule.every().day.at("23:59").do(getIDs)

    while True:
        schedule.run_pending()
        time.sleep(1)

hilo = threading.Thread(target=SearchLoop)
hilo.start()

def noticias(request):
    return render(request, "noticias.html", NewsList)

def foros(request):
    return render(request, "foros.html", ForoId)