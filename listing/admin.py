from django.db.models import Count
from django_summernote.admin import SummernoteModelAdmin


from django.contrib import admin
from .models import (
    State,
    City,
    TransactionType,
    RealestateType,
    Realtor,
    Listing,
    ListingImage,
)
class ListingImageAdmin(admin.StackedInline) : 
    model = ListingImage
class ListingModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')

    list_display = ("title","transaction_type","realestate_type","state","city","realtor","added_on")
    list_filter = ('transaction_type__name','realestate_type__name','state__name','city__name','realtor__user')
    search_fields = ('transaction_type__name','realestate_type__name','state__name','city__name','realtor__user')
    inlines =[ListingImageAdmin]
    filter_horizontal = ()


class CityModelAdmin(admin.ModelAdmin) : 
    list_display = ("name","state")
    ordering = ("state",)
    list_filter = ("state",)
    search_fields = ("name","state__name",)
class StateModelAdmin(admin.ModelAdmin) : 
    list_display = ("name","city_count")
    ordering  = ("pk",)

    def city_count(self,obj) :
        return obj.city_count
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(city_count=Count("city"))
        return queryset

@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Listing,ListingModelAdmin)

admin.site.register(State,StateModelAdmin)
admin.site.register(City,CityModelAdmin)
admin.site.register(TransactionType)
admin.site.register(RealestateType)
admin.site.register(Realtor)