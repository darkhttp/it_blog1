from django.db import models

# Create your models here.



class Type_news(models.Model):
    type_news = models.CharField(verbose_name=u'Тип новости', max_length=64)
    def __str__(self):
        return self.type_news

class News(models.Model):
    name= models.CharField(verbose_name = "Заголовок", max_length = 128)
    desc = models.TextField(verbose_name = "Описание")
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    img = models.ImageField(upload_to='img', blank=True,null=True)
    type_news = models.ForeignKey(Type_news, verbose_name='Тип новости')
    def __str__(self):
        return self.name