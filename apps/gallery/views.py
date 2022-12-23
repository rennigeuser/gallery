from django.views.generic import ListView
from .models import Post



class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = 'gallery/main.jinja'


post_list_view = PostListView.as_view()