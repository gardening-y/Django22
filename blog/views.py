from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # 템플릿 모델명_list.html : post_list.html
    # index -> post_list 이름 바꾸기
    # 파라미터 모델명_list : post_list ('')있는거 'posts'
    
class PostDetail(DetailView):
    model = Post
    # 템플릿 모델명_detail.html : post_detail.html
    # blog/single_post_page -> post_detail 이름 바꾸기
    # 파라미터 모델명 : post

# def index(request):
#     posts1 = Post.objects.all().order_by('-pk')
#     return render(request, 'blog/index.html', {'posts': posts1})
#
# def single_post_page(request, pk):
#     post2 = Post.objects.get(pk=pk)
#     return render(request, 'blog/single_post_page.html', {'post': post2})