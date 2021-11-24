from django.shortcuts import render
from newsapi import NewsApiClient
from noticias import models as ModelObject
import time
import threading

newsapi = NewsApiClient(api_key='3e10e6f5c0d046a7aef93f1db3e778a9')

def SearchLoop():
    def searchNews():
        newsLoaded = 0
        while newsLoaded < 3:
            PageNews = 1
            top_headlines = newsapi.get_everything(q='Cambio climatico',
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

    while True:
        searchNews()
        time.sleep(5)

hilo = threading.Thread(target=SearchLoop)
hilo.start()

def noticias(request):
    return render(request, "noticias.html")