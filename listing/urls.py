from django.urls import path 
from .views import (
    ListingListView,
    ListingCreateView,
    ListingUpdateView,
    ListingDetailView,
    ListingDeleteView,
    ListingsByCity,
    ListingsByState,
    load_cities
)
urlpatterns = [
    path('',ListingListView.as_view(),name = "all-listings"),
    path('listings/city=<str:city>/',ListingsByCity.as_view(),name = "listing-bycity"),
    path('listings/state=<str:state>/',ListingsByState.as_view(),name = "listing-bystate"),
    path('listing/create/',ListingCreateView.as_view(),name = "listing-create"),
    path('listing/<slug:slug>/',ListingDetailView.as_view(),name = "listing-detail"),
    path('listing/<slug:slug>/update/',ListingUpdateView.as_view(),name = "listing-update"),
    path('listing/<slug:slug>/delete/',ListingDeleteView.as_view(),name = "listing-delete"), 
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),  
]