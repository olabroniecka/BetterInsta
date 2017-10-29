from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.template.response import TemplateResponse
from django.views import View

from users.forms import UserLoginForm


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'users/login_form.html'

    def get(self, request):
        form = self.form_class()
        return TemplateResponse(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['login'],
                password=form.cleaned_data['password']
            )
            login(request, form.user)
            return redirect('/users/')
        else:
            return TemplateResponse(request, self.template_name, {'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/users/")


class MainView(View):
    def get(self, request):
        return TemplateResponse(request,
                                'users/main_view.html',
                                {}
                                )
