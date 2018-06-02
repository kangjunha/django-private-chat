from braces.views import LoginRequiredMixin
from django.views import generic
from django.contrib.auth import get_user_model
from django.shortcuts import render
import requests


class UserListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'custom_app/users.html'
    login_url = 'admin/'

def home(request):
    template = loader.get_template('django_private_chat/dialogs.html')
    number = 5;
    return HttpResponse(template.render(number,request))
