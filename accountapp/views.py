from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accountapp.forms import AccountCreateForm


def show_main(request):
    return render(request, 'base.html')

class AccountCreateView(CreateView):
    model = User
    form_class = AccountCreateForm
    success_url = reverse_lazy('newsapp:home')
    template_name = 'accountapp/signup.html'
