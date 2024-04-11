from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.models import User
from app import models

# Create your views here.

def main(request):
    return render(request, 'main.html')

def create(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            color_name = request.POST.get('name')
            new_color = models.Color.objects.create(color=color_name)
            palitra_id = request.POST.get('add')
            post = models.Palitra.objects.get(pk=palitra_id)
            post.colors.add(new_color)
            post.save()
        elif 'delete' in request.POST:
            palitra_id = request.POST.get('delete')
            post = models.Palitra.objects.get(pk=palitra_id)
            models.Color.objects.get(pk=request.POST.get('color')).delete()
        elif 'save' in request.POST:
            palitra_id = request.POST.get('save')
            post = models.Palitra.objects.get(pk=palitra_id)
            palitra_name = request.POST.get('palitra')
            post.name = palitra_name
            post.save()
            return redirect('main')
    else:
        post = models.Palitra.objects.create(user=request.user)
        post.colors.add(models.Color.objects.create())

    return render(request, 'create.html', context={'palitra': post.get_colors, 'id': post.pk})

def register(request):
    return HttpResponse("reg", content_type='text/plain')

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('main')
    
def logout_user(request):
    logout(request)
    return redirect('main')

def profile(request, user_id):
    get_user = get_object_or_404(User, id=user_id)
    return render(request, "profile.html", {"get_user": get_user})

class Palitras(ListView):
    model = models.Palitra
    template_name = "palitras.html"
    context_object_name = 'Palitras'

    def get_queryset(self):
        get_user = get_object_or_404(User, id=self.kwargs.get('user_id'))
        return models.Palitra.objects.filter(user=get_user)

class Users(ListView):
    model = User
    template_name = "users.html"
    context_object_name = 'users'