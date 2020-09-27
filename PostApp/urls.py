from django.urls import path
from .views import HomeView, PostView, CreatePostView, UpdatePostView, DeletePostView, CatagoryView, CreateCatagory, \
    DeleteCatagory, UpdateCatagory, CatagoryDetail

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostView.as_view(), name="post"),
    path('create-post/', CreatePostView.as_view(), name="create-post"),
    path('update-post/<int:pk>', UpdatePostView.as_view(), name="update-post"),
    path('delete-post/<int:pk>', DeletePostView.as_view(), name="delete-post"),

    path('catagory/', CatagoryView.as_view(), name="catagory"),
    path('catagory-detail/<int:pk>', CatagoryDetail.as_view(), name="catagory-detail"),
    path('create-catagory/', CreateCatagory.as_view(), name="create-catagory"),
    path('delete-catagory/<int:pk>', DeleteCatagory.as_view(), name="delete-catagory"),
    path('update-catagory/<int:pk>', UpdateCatagory.as_view(), name="update-catagory"),
]
