from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [

    {
        'author': 'geof.hoffman',
        'title' : 'post1',
        'content': 'FirstPostContent',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jessica.Hoffman',
        'title' : 'post2',
        'content': 'SecondPostContent',
        'date_posted': 'August 28, 2018'
    },


]

def home(request):
    return render(request, 'rsvp/home.html')

def about(request):
    return HttpResponse('<h1> About Home</h1>',{'title':'About'})

def guestbook(request):
    context = {
        'posts': posts
    }
    return render(request, 'rsvp/guestbook.html', context)
    
def events(request):
    return render(request, 'rsvp/events.html')