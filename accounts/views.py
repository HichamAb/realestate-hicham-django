from django.shortcuts import render,get_object_or_404
from django.views.generic import UpdateView,TemplateView,DetailView

from django.views import View
from .models import Profile,CustomUser
from .forms import CustomUserChangeForm,ProfileUpdate
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

class HomePageView(TemplateView) : 
    template_name = "accounts-temp/home.html"

class ProfileUpdateView(LoginRequiredMixin,View) : 
    template_name = "accounts-temp/profile-update.html"
    success_url = "profile"
   
    def get_object(self) : 
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(Profile,slug=slug)
        return obj 
    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get("slug")
        context = {}
        obj = self.get_object()
        context["object"] = obj
        user = get_object_or_404(CustomUser,profile__slug = slug)
        if user is not None :
            form_userinfo = CustomUserChangeForm(instance = user)
            form = ProfileUpdate(instance=obj)
            context["form"] = form
            context["form_userinfo"]= form_userinfo
        return render(request,self.template_name,context)
    
    def post(self, request, *args, **kwargs):
        slug = self.kwargs.get("slug")
        context = {}
        obj = self.get_object()
        context["object"] = obj
        user = get_object_or_404(CustomUser,profile__slug = slug)
        if user is not None :
            form_userinfo = CustomUserChangeForm(self.request.POST,instance = user)
            form = ProfileUpdate(self.request.POST,self.request.FILES,instance=obj)
            if form_userinfo.is_valid() and form.is_valid() : 
                form_userinfo.save()
                form.save()
            context["form"] = form
            context["form_userinfo"]= form_userinfo
        return render(request,self.template_name,context)    
    def get_redirect_url(self,*args, **kwargs) : 
        return obj.get_absolute_url()
    
class ProfileView(DetailView) : 
    model = Profile
    template_name = "accounts-temp/profile.html"

    def get_object(self) : 
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(Profile,slug=slug)
        return obj
    












