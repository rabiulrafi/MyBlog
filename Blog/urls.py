from django.urls import path
from .views import HomeView,DetailsView,CreateEntryView
urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('detail/<int:pk>', DetailsView.as_view(), name='detail'),
    path('create-entry/', CreateEntryView.as_view(success_url="/"), name='create-entry'),

]
