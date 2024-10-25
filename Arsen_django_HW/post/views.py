from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
from . forms import PostForm, CommentForm
from django.shortcuts import redirect
# Create your views here.


def http_response(request):
    return HttpResponse('Hello World from HttpResponse!')


def html_response(request):
    return render(request, 'index.html')


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    form = CommentForm()
    return render(request, 'posts/post_detail.html', {'post': post, 'form': form})


def post_create_view(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'posts/post_create.html', {'form': form})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            return render(request, 'posts/post_create.html', {'form': form})
        post = form.save()
        post.user = request.user
        post.save()
        return redirect('/posts/')


def comment_create_view(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if not form.is_valid():
            return render(request, 'posts/post_detail.html', {'form': form})
        comment = form.save(commit=False)
        comment.post_id = post_id
        comment.save()
        return redirect(f'/posts/{post_id}')