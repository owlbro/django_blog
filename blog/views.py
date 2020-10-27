from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .schema import PostSchema






class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('title')
        schema = PostSchema(many = True)
        json_result = schema.dumps(posts)
        return Response({'posts': json_result})

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        schema = PostSchema()
        result = schema.dump(post)
        return Response({'post': result})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})