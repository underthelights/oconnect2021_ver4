from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from newsapp.forms import NewsCreationForm
from newsapp.models import News


class NewsCreateView(CreateView):
    model = News
    form_class = NewsCreationForm # 만들기
    template_name = 'newsapp/create.html'

    def form_valid(self, form):
        temp_news = form.save(commit=False)
        temp_news.writer = self.request.user
        temp_news.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('newsapp:home') # 홈 연결 후 수정할 것


class NewsUpdateView(UpdateView):
    model = News
    context_object_name = 'target_news'
    form_class = NewsCreationForm
    template_name = 'newsapp/update.html'

    def get_success_url(self):
        return reverse('newsapp:home')


class NewsDeleteView(DeleteView):
    model = News
    context_object_name = 'target_news'
    success_url = reverse_lazy('newsapp:home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)