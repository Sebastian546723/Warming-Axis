from django.shortcuts import render
from newsapi import NewsApiClient
from noticias import models as ModelObject
import time
import threading

newsapi = NewsApiClient(api_key='b585c643d93e40fd852c4cc7a8933a7e')#3e10e6f5c0d046a7aef93f1db3e778a9

"""def SearchLoop():
    def searchNews():
        newsLoaded = 0
        PageNews = 1
        while newsLoaded < 3:
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
        time.sleep(86400)

hilo = threading.Thread(target=SearchLoop)
hilo.start()"""

NewsList = {'articles':[]}
ForoId = {"ids": []}
#ModelObject.News.objects.all().order_by('-id')[:3]
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

print(ForoId)
def noticias(request):
    return render(request, "noticias.html", NewsList)

def foros(request):
    return render(request, "foros.html")