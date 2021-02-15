from django import forms
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Listing ,City ,ListingImage
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.forms import inlineformset_factory
class ListingImages(forms.ModelForm) :
    class Meta : 
        model =  ListingImage
        fields = ('image',"listing")
        exclude = ()
class CreateListing(forms.ModelForm) :
    description = forms.CharField(widget= SummernoteWidget())
    class  Meta:
        model = Listing 
        
        fields  = ("title","transaction_type","realestate_type",
                    "state","city","n_bedrooms","n_bathrooms","square_meter",
                    "description","garage","price","status","neiborhood",)
        
        widgets = {
            "realtor": forms.HiddenInput(),
            
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')
       
      
ImagesFormset = inlineformset_factory(Listing,ListingImage,form=ListingImages,fields=['image',"listing"] ,extra=1,can_delete=True)
class UpdateListing(forms.ModelForm) : 
    class Meta : 
        model = Listing 
        fields = "__all__"