from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count
        return context

    # 템플릿 모델명_list.html : post_list.html
    # index -> post_list 이름 바꾸기
    # 파라미터 모델명_list : post_list ('')있는거 'posts'
    
class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data() #위 함수와 super 매개변수의 차이
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count
        return context

def category_page(request, slug):
    if slug == 'no_category' :
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else :
        category = Category.objects.get(slug=slug) #왼쪽은 필드명, 오른쪽은 찾기 원하는 슬러그 값
        post_list = Post.objects.filter(category=category)
    return render(request, 'blog/post_list.html', {
        'category' : category, #템플릿 변수 : 함수 안에 category
        'post_list' : post_list, #Post.objects.filter(category=category), 포스트가 가진 : 슬러그를 통해 전달받은 함수 안 변수
        'categories' : Category.objects.all(),
        'no_category_post_count' : Post.objects.filter(category=None).count
    })


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