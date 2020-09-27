from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PostApp.urls')),
    path('member/', include('MemberApp.urls')),
]
