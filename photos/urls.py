from django.urls import path
from photos.views import home, album, about, type_albums

urlpatterns = [
    path('', home, name='home_page'),
    path('<int:t>', type_albums, name='type_albums'),
    path('album/<int:pk>', album, name='album'),
    path('about/', about, name='about'),
]
