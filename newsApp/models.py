

from django.db import models
from main_app.models import News
class Full_news(models.Model):
    news= models.ForeignKey(News, verbose_name='новость')
    desc_all_1 = models.TextField(verbose_name = "Часть 1")
    img_1 = models.ImageField(upload_to='images/blog/%Y/%m/%d', blank=True)
    desc_all_2 = models.TextField(verbose_name="Часть 2",blank=True)
    img_2 = models.ImageField(upload_to='images/blog/%Y/%m/%d', blank=True)
    desc_all_3 = models.TextField(verbose_name="Часть 3", blank=True)
    img_3 = models.ImageField(upload_to='images/blog/%Y/%m/%d', blank=True)
    desc_all_4 = models.TextField(verbose_name="Часть 4", blank=True)
    img_4 = models.ImageField(upload_to='images/blog/%Y/%m/%d', blank=True)
    desc_all_5 = models.TextField(verbose_name="Часть 5", blank=True)
    def __str__(self):
        return "Новость"
