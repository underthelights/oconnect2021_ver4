from django.urls import path

from django.views.generic import TemplateView

from newsapp.views import NewsCreateView, NewsDeleteView, NewsUpdateView

app_name = 'newsapp'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('news/create/', NewsCreateView.as_view(), name='create'),
    path('news/update/<int:pk>', NewsUpdateView.as_view(), name='update'),
    path('news/delete/<int:pk>', NewsDeleteView.as_view(), name='delete'),
]