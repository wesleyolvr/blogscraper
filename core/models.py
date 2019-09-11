from django.db import models

class News(models.Model):
   title_new = models.CharField(max_length=300, help_text='title of news')
   data_created= models.DateField(auto_now_add=True)

   verbose_name = 'New'
   verbose_name_plural = 'News'

   def __str__(self):
       return self.title_new
    
