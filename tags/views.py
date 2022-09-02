from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from tags.models import Tag
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class TagListView(ListView):
    model = Tag
    template_name = "tags/list.html"
    paginate_by = 2


class TagDetailView(DetailView):
    model = Tag
    template_name = "tags/detail.html"


class TagCreateView(CreateView):
    model = Tag
    template_name = "tags/new.html"
    fields = ["name"]
    success_url = reverse_lazy("tags_list")


class TagUpdateView(UpdateView):
    model = Tag
    template_name = "tags/edit.html"
    fields = ["name"]
    success_url = reverse_lazy("tags_list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tags/delete.html"
    success_url = reverse_lazy("tags_list")


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = "recipes/new.html"
    fields = ["name", "author", "description", "image"]
    success_url = reverse_lazy("recipes_list")
