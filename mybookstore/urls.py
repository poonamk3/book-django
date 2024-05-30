from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
]


1111111111111111111111111111111111111111111111