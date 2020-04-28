from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from notice.models import Post



# Create your views here.


# ListView
class PostLV(ListView):
    model = Post  #테이블을 사용한다??
    template_name = 'post/post_all.html'
    context_object_name = 'posts'
    paginate_by = 5 # 페이지당 보여지는 개수


# DetailView
class PostDV(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
