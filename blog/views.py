from django.contrib.auth import authenticate,login
#from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from blog.forms import PostForm, LoginForm
from .models import Post

from tagging.models import Tag
from tagging.models import TaggedItem

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def tag_search(request,pk):
    queryset_list = TaggedItem.objects.get_by_model(Post,pk)
    all = Tag.objects.usage_for_model(Post,filters=dict(status='published'), counts=True)
    paginator = Paginator(queryset_list, 4)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    return render(request, 'blog/search_results.html', {'posts': queryset, 'query': pk,'all':all})

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            queryset_list = TaggedItem.objects.get_by_model(Post, q)
            all = Tag.objects.usage_for_model(Post,filters=dict(status='published'), counts=True)

            paginator = Paginator(queryset_list, 4)  # Show 25 contacts per page

            page = request.GET.get('page')
            try:
                queryset = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                queryset = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                queryset = paginator.page(paginator.num_pages)
            return render(request, 'blog/search_results.html', {'posts': queryset, 'query': q,'all':all})
    return render(request, 'blog/search_form.html', {'error': error})




"""def listing(request):
    contact_list = Contacts.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'contacts': contacts})
    """


def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now())
    #house_tag = Tag.objects.all()
    queryset_list = Post.published.all()
    all=Tag.objects.usage_for_model(Post,filters=dict(status='published'),counts=True)

    paginator = Paginator(queryset_list, 4)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)


    return render(request, 'blog/post_list.html', {'posts': queryset,'all':all,})




def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             #status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    #postprev=Post.objects.get(pk=post.pk-1)
    #postafter=Post.objects.get(pk=post.pk+1)
    tags=Tag.objects.get_for_object(post)
    all=Tag.objects.usage_for_model(Post,filters=dict(status='published'),counts=True)
    return render(request, 'blog/post_detail.html', {'post': post,'tags':tags,'all':all,})
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            #if(post.published_status):
                #post.publish()
            post.save()

            if request.user.is_superuser:
                queryset_list = Post.objects.all()
            else:
                queryset_list = Post.objects.filter(author__username=request.user.username)

            paginator = Paginator(queryset_list, 5)  # Show 25 contacts per page

            page = request.GET.get('page')
            try:
                queryset = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                queryset = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                queryset = paginator.page(paginator.num_pages)
            return render(request,'blog/dashboard.html',{'posts': queryset,})
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):

    if request.user.is_superuser:
        post = get_object_or_404(Post, pk=pk)

    else:
        query=Post.objects.filter(author=request.user)
        post = get_object_or_404(query, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #if (post.published_status):
                #post.publish()
            post.save()
            if request.user.is_superuser:
                queryset_list = Post.objects.all()
            else:
                queryset_list = Post.objects.filter(author__username=request.user.username)

            paginator = Paginator(queryset_list, 5)  # Show 25 contacts per page

            page = request.GET.get('page')
            try:
                queryset = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                queryset = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                queryset = paginator.page(paginator.num_pages)
            return render(request,'blog/dashboard.html',{'posts': queryset,})
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                    password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                        'successfully')
                else:
                    return HttpResponse('Disabled account')

            else:
                return HttpResponse('Invalid login')

    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})


@login_required
def dashboard(request):

    if request.user.is_superuser:
        queryset_list = Post.objects.all()
    else:
        queryset_list = Post.objects.filter(author__username=request.user.username)

    paginator = Paginator(queryset_list, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    return render(request,
    'blog/dashboard.html',
    {'posts': queryset,})