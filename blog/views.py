from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views import generic  #General view  class based
from django.urls import reverse_lazy

from .forms import PostForm #create new form
from .models import Post
# functional view(def) ///  class_based view


#-------------------------------------------------------------------------------

# def blog_list(request):  #functional view
#     # posts_list = Post.objects.all()
#     posts_list=Post.objects.filter(status='pub').order_by('-datetime_modified')  #filter is **kwargs // queryset
#     return render(request, 'blog/posts_list.html',{'posts_list': posts_list})

class PostListView(generic.ListView):
    # model = Post  #its get all objects -> Post.objects.all()
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'
    def get_queryset(self): #if doesnt want all() we should use a function insted model // query zadan
        return Post.objects.filter(status='pub').order_by('-datetime_modified')

#-------------------------------------------------------------------------------

class PostDetailView(generic.DetailView):
    model = Post #outomatic check pk!!
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'   #if dont use this django send a context by model name: Post-> context:post


# def post_detail_view(request, pk):   #functional view
#     post = get_object_or_404(Post, pk=pk)   # try except in one line
#     # try:
#     #     post= Post.objects.get(pk=pk)
#     # except ObjectDoesNotExist:
#     #     post = None
#     #     print('excepted')
#     return render(request, 'blog/post_detail.html',{'post':post})


#-------------------------------------------------------------------------------

class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'
    #redirect -> call get_absolute_url and page that should reverse on that method



# def post_create_view(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save() # equal to :  Post.objects.create(title=post_title, text=post_text, author=user, status='pub')
#             return redirect('blog_list') # in redirect automaticly call reverse
#     else: # Get request
#         form = PostForm()
#     return render(request, 'blog/post_create.html', context={'form':form})

    # if request.method =='POST':  #ravesh ghadimi
    #     post_title = request.POST.get('title')  this code is not wrong but bad.
    #     post_text = request.POST.get('text')
    #     user=User.objects.all()[0]
    #     Post.objects.create(title=post_title, text=post_text, author=user, status='pub')
    # else:
    #     print('get request')
    # return render(request, 'blog/post_create.html')
#-------------------------------------------------------------------------------


class PostUpdateView(generic.UpdateView):
    model = Post  #we need pk -> must write model
    template_name = 'blog/post_create.html'
    form_class = PostForm
    context_object_name = 'post'


# def post_update_view(request,pk):
#     post = get_object_or_404(Post,pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():  #when Get request if dosent run
#         form.save()
#         return redirect('post_detail',pk)
#     return render(request, 'blog/post_create.html', context={'form':form})
#-------------------------------------------------------------------------------


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name ='blog/post_delete.html'
    success_url = reverse_lazy('blog_list')


# def post_delete_view(request,pk):
#     post = get_object_or_404(Post,pk=pk)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('blog_list')
#
#     return render(request, 'blog/post_delete.html',context={'post': post})







