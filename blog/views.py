from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post
from .models import Category
from .forms import PostForm

# Create your views here.
def home(request):
	post = Post.objects.all()
	return render(request, 'blog/home.html', {})

def resume(request):
	return render(request, 'blog/resume.html', {})

def post_detail(request, category, pk=None):
	if pk == None:
		pk = Post.objects.all().filter(category = Category.objects.get(title = category))[0].pk
	posts = Post.objects.all().filter(category = Category.objects.get(title = category))
	post = get_object_or_404(posts, pk = pk)
	context = { 'post' : post,
				'posts' : posts,
				'category' : category}
	return render(request, 'blog/post_detail.html', context)

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk = post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {})

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
