from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import View, CreateView,UpdateView,DeleteView,DetailView,ListView

from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import Listing,City,ListingImage,State
from .forms import CreateListing,UpdateListing ,ImagesFormset
from django.db import transaction



def load_cities(request) : 
    state = request.GET.get('state')
    cities = City.objects.filter(state=state).order_by('name')
    return render(request,"listing/city_dropdownlist_options.html",{'cities': cities})
class ListingListView(ListView):
    model           = Listing
    template_name   = "listing/all_listings.html"
    ordering        = "-added_on"
    paginate_by     = 10
    context_object_name = "listings"
    def get_context_data(self, **kwargs):
        context = super(ListingListView, self).get_context_data(**kwargs)
        context['states'] = State.objects.all()
        return context
class ListingsByCity(ListView) : 
    model           = Listing
    template_name   = "listing/listings_by_city.html"
    ordering        = "-added_on"
    paginate_by     = 10    
    context_object_name ="listings"
    def get_queryset(self):
        queryset = super(ListingsByCity, self).get_queryset()
        city        = self.kwargs.get("city")
        queryset = Listing.objects.filter(city__slug=city) # TODO
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(ListingsByCity, self).get_context_data(**kwargs)
        context['city'] = self.kwargs['city']
        context['states'] = State.objects.all()
        return context


class ListingsByState(ListView) : 
    model           = Listing
    template_name   = "listing/listings_by_state.html"
    ordering        = "-added_on"
    paginate_by     = 10    
    context_object_name ="listings"
    def get_queryset(self):
        queryset = super(ListingsByState, self).get_queryset()
        state        = self.kwargs.get("state")
        queryset = Listing.objects.filter(state__slug=state) # TODO
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(ListingsByState, self).get_context_data(**kwargs)
        context['state'] = self.kwargs['state']
        return context
    
    
class ListingCreateView(LoginRequiredMixin,View) : 
    template_name   = "listing/create_listing.html"
    
    def get(self,request,*args, **kwargs) : 
        context =  {}
        form = CreateListing()
        formset = ImagesFormset(instance=None)

        context["form"] = form 
        context["formset"] = formset
        return render(request,self.template_name,context)
    def post(self,request,*args, **kwargs) :
        context =  {}
        form = CreateListing(self.request.POST)
        formset = ImagesFormset(self.request.POST,self.request.FILES)
        if form.is_valid() :
            form.save(commit=False)
            form.instance.realtor = self.request.user.realtor
            self.object = form.save() 
        if formset.is_valid() :
            formset.instance = self.object
            formset.save()
            return HttpResponseRedirect(self.get_success_url())
        context["form"] = form 
        context["formset"] = formset
        
        return render(request,self.template_name,context)

    def get_success_url(self,**kwargs):
        return reverse_lazy('listing-detail', kwargs={'slug' : self.object.slug})
class ListingDetailView(DetailView) : 
    template_name   = "listing/listing.html"
    model           = Listing
    def get_object(self) :
        slug        = self.kwargs.get("slug")
        obj         = get_object_or_404(Listing,slug=slug)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        listing = self.get_object()
        context["listing"] = listing
        return context
    







class ListingUpdateView(View,LoginRequiredMixin) :
    template_name   = "listing/update_listing.html"
    
    def get_object(self) :
        slug        = self.kwargs.get("slug")
        obj         = get_object_or_404(Listing,slug=slug)
        return obj
    def get(self,request,*args, **kwargs) :
        context = {}
        obj = self.get_object()
        form    = CreateListing(instance=obj)
        formset = ImagesFormset(instance=obj)
        context["form"] = form 
        context["formset"] = formset
        context["object"] = obj 
        return render(request,self.template_name,context)
    def post(self,request,*args, **kwargs) : 
        context = {}
        obj = self.get_object()
        form    = CreateListing(self.request.POST,instance=obj)
        formset = ImagesFormset(self.request.POST,self.request.FILES,instance=obj)
        context["formset"] = formset
        context["form"] = form 
        context["object"] = obj 
        if form.is_valid() :
            form.save(commit=False)
            form.instance.realtor = self.request.user.realtor
            self.object = form.save()
        else : 
            print(form.errors)
        if formset.is_valid() : 
            
            formset.save()
            return HttpResponseRedirect(self.get_success_url())
        else : 
            print(formset.errors)
        return render(request,self.template_name,context)
    def get_success_url(self,**kwargs):
        return reverse_lazy('listing-detail', kwargs={'slug' : self.object.slug})

class ListingDeleteView(DeleteView,LoginRequiredMixin) : 
    success_url     = reverse_lazy("all-listings")
    template_name   = "listing/delete_listing.html"
    def get_object(self) :
        slug        = self.kwargs.get("slug")
        obj         = get_object_or_404(Listing,slug=slug)
        return obj


