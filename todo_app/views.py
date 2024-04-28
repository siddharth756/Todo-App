from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo
from django.contrib.auth.models import User
from .forms import todoForm,signupForm,loginForm
from django.views.generic import View
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class todolistview(LoginRequiredMixin,ListView):
    model = Todo
    template_name = "home.html"
    context_object_name = "todo"

    def get_queryset(self):
        queryset = Todo.objects.all()
        return queryset.filter(user=self.request.user)
    

class tododetailview(LoginRequiredMixin,DetailView):
    model = Todo
    template_name = "detail.html"


class todocreateview(LoginRequiredMixin,CreateView):
    model = Todo
    form_class = todoForm
    template_name = "create.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class todoupdateview(LoginRequiredMixin,UpdateView):
    model = Todo
    form_class = todoForm
    template_name = "update.html"
    success_url = reverse_lazy("home")


class tododeleteview(LoginRequiredMixin,DeleteView):
    model = Todo
    template_name = "delete.html"
    success_url = reverse_lazy("home")

class signupview(CreateView):
    model = User
    form_class = signupForm
    template_name = "signup.html"
    success_url = reverse_lazy("login") 

class loginview(View):
    template_name = "login.html"
    form_class = loginForm

    def get(self, request):
        form = self.form_class()
        return render(request,self.template_name,context={'form': form })

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form })

def logoutview(request):
    logout(request)
    return redirect('login')