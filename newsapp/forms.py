from django.forms import ModelForm

from newsapp.models import News


class NewsCreationForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'image', 'link']