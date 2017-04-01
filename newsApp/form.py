from .models import Full_news
from django import forms
from main_app.models import News
class Full_newsForm(forms.ModelForm):
    class Meta:
        model = Full_news
        fields = ('__all__')

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('__all__')
