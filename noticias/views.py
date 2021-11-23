from django.shortcuts import render
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='3e10e6f5c0d046a7aef93f1db3e778a9')

noticiasAPI = newsapi.get_everything(q='Climate Change',
                                    sort_by='relevancy',
                                    language='es')

def noticias(request):
    return render(request, "noticias.html", noticiasAPI)