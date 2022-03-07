from django.urls import path

from tags.views import show_tags

urlpatterns = [
    path("", show_tags, name="tags_list"),
]
