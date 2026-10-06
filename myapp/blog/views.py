from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Post,Contact,AboutUs
from .forms import ContactForm
# Create your views here.
# posts =[
        # {'id':1, 'title':'first post','content':'this is the first post content'},
        # {'id':2, 'title':'second post','content':'this is the second post content'},
        # {'id':3, 'title':'third post','content':'this is the third post content'},
        # {'id':4, 'title':'fourth post','content':'this is the fourth post content'},
        # {'id':5, 'title':'fifth post','content':'this is the fifth post content'},
# ]
def index(request):
    # return HttpResponse("hello world")
    blog_title ='latest blog'
    posts = Post.objects.all()
    return render(request,'blog/index.html',{'blog_title':blog_title,'posts':posts})


def detail(request,post_id):
    # return HttpResponse(f"your viewing post detail page and post id is {post_id}")
    # post =next((item for item in posts if item ['id']==int(post_id)),None)
    try:
        post=Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return HttpResponse("post no found")
    return render(request,'blog/detail.html',{'post':post})

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url)"))

def new_url_views(request):
    return HttpResponse("this is the new url")


def contact(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST)
        if form.is_valid():
            # Manually save to DB
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            success_message = 'Your message has been saved in the database!'
            return render(request, 'blog/contact.html', {
                'form': ContactForm(),  # reset form
                'success_message': success_message
            })
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})

def about (request):
    about_content = AboutUs.objects.first()
    if about_content is None or not about_content.content:
        about_content = "Default content goes here." 
    else:
        about_content = about_content.content 
    return render(request,'blog/about.html',{'about_content':about_content})