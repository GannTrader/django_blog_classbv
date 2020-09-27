# Create your views here.
# def home_site(request):
    # return HttpResponse("hello world")
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from PostApp.forms import PostCreateForm, EditCatagoryForm
from PostApp.models import Posts, Catagory


class HomeView(ListView):
    model = Posts
    template_name = "posts.html"
    context_object_name = "posts"


class PostView(DetailView):
    model = Posts
    template_name = "post.html"


class CreatePostView(CreateView):
    # model = Posts
    # fields = ['title', 'body']
    form_class = PostCreateForm
    template_name = "create-post.html"
    # success_url = reverse_lazy("home")


class UpdatePostView(UpdateView):
    model = Posts
    form_class = PostCreateForm
    template_name = "update-post.html"
    # fields = "__all__"


class DeletePostView(DeleteView):
    model = Posts
    template_name = "delete-post.html"
    success_url = reverse_lazy("home")


class CatagoryView(ListView):
    model = Catagory
    # model = Posts
    template_name = "view-catagories.html"

class CatagoryDetail(DetailView):
    model = Catagory
    template_name = "catagory.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Posts.objects.filter(catagory=self.kwargs['pk'])
        return context


class CreateCatagory(CreateView):
    # model = Catagory
    template_name = "create-catagory.html"
    # fields = "__all__"
    form_class = EditCatagoryForm

class DeleteCatagory(DeleteView):
    model = Catagory
    template_name = "delete-catagory.html"
    success_url = reverse_lazy("catagory")


class UpdateCatagory(UpdateView):
    model = Catagory
    form_class = EditCatagoryForm
    template_name = "update-catagory.html"