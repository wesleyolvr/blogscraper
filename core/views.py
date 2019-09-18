from django.shortcuts import render
from core.models import News
from django.http import HttpResponse
from django.views.generic import ListView
import sqlite3
   

def home(request):
    return HttpResponse("Hello!")


class ListView(ListView):
    model = News
    template_name = 'core/news_list.html'
    ordering = ['-created']

    def get_queryset(self):
        query = self.request.GET.get('query')
        queryset = News.objects.all()
        if query:
            object_list = queryset.filter(title_new__icontains=query)
        else:
            return queryset
        return object_list

    
def save_news(request):
    try:
        objs_titles = [t.title_new for t in News.objects.all()]
    except:
        objs_titles = News.objects.all()
    dados = db_select()
    for d in dados:
        if objs_titles:
            if d[0] not in objs_titles:
                new = News(title_new=d[0])
                new.save()
        else:
            new = News(title_new=d[0])
            new.save()
    return HttpResponse("dados salvos no banco")



def db_select():
    path = 'mynews.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    sql = """
    SELECT Title FROM news
    """
    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data