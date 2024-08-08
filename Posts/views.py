from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Posts
from .forms import CreatePost

# Create your views here.
@login_required
def post(request):
    published_post = Posts.objects.all()
    return render(request, 'post.html', {'published_post': published_post})

@login_required
def post_details(request, slug):
    expand_post = Posts.objects.get(slug=slug)
    return render(request, 'details.html', {'expand_post': expand_post})

@login_required
def createPost(request):
    if request.method == 'POST':
        createpost = CreatePost(request.POST, request.FILES)
        if createpost.is_valid():
            #adding user that published the article
            instance = createpost.save(commit=False)
            instance.author = request.settings.AUTH_USER_MODEL
            instance.save()
            return redirect("post:posts")
    else:
        createpost = CreatePost()
    return render(request, 'creatpost.html', {'createpost': createpost})