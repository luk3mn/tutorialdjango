from django.views.generic import DetailView, ListView
# DetailView -> Mostra somente um
# ListView -> Lista vários posts
from .models import Post

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post