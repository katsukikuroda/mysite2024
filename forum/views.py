from django.shortcuts import render
from .models import Topic

def index(request):
    TOPIC_LIST = Topic.objects.all()
    context = {
        "topics": TOPIC_LIST,
    }
    return render(request, "forum/index.html", context)

def forum(request, topic):
    context = {
        "topic": topic,
    }
    return render(request, "forum/forum.html", context)