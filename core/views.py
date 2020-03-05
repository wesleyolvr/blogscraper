from django.shortcuts import render
from core.models import News
from django.http import HttpResponse
from django.views.generic import ListView
import sqlite3
   


class ListView(ListView):
    model = News
    template_name = 'news_list.html'
    ordering = ['-created']

    def get_queryset(self):
        save_news()
        query = self.request.GET.get('query')
        queryset = News.objects.all()
        if query:
            object_list = queryset.filter(title_new__icontains=query)
        else:
            return queryset
        return object_list

list_news = ListView.as_view()
    
def save_news():
    """
    saves mynews.db data captured by the crawler and creates the objects in the app core database, verifying the uniqueness of the objects.
    """
    try:
        objs= News.objects.all()
        objs_titles = [t.title_new for t in objs]
    except:
        objs_titles = News.objects.all()
    dados = list(set(db_select()))
    
    for d in dados:
        if objs_titles:
            if d[0] not in objs_titles:
                if d[1]:
                    new = News(title_new=d[0],pic=d[1])
                    new.save()
                else:
                    new = News(title_new=d[0])
                    new.save()
        else:
            if d[1]:
                new = News(title_new=d[0],pic=d[1])
                new.save()
            else:
                new = News(title_new=d[0])
                new.save()




def db_select():
    path = 'mynews.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    sql = """
    SELECT Title,Pic FROM news
    """
    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data