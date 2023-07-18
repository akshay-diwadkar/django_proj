from django.shortcuts import render, redirect, get_object_or_404

#my code
from django.http import HttpResponse
from django.utils import timezone

from .models import Post

from .forms import PostForm

# Create your views here.
def home(request):
    data = Post.objects.all()
    context = {"my_data": data}
    return render(request, template_name="blog/home.html", context=context)

def contact(request):
    context = {"my_data": [1,2,3,4,5]}
    return render(request, template_name="blog/contacts.html", context=context)


def detail(request, id):
    data = Post.objects.get(id=id)
    context = {'my_data': data}
    return render(request, template_name="blog/detail.html", context=context)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detail',id=post.id)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'my_form': form})


def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detail',id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'my_form': form})


def post_delete(request, id):
    post = Post.objects.get(id=id)
    post_title = post.title
    post.delete()
    return render(request, 'blog/post_delete.html', {'post_title': post_title})