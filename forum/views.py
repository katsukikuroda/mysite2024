from django.shortcuts import get_object_or_404, render
from .models import Message, Topic

def index(request):
    TOPIC_LIST = Topic.objects.all()
    context = {
        "topics": TOPIC_LIST,
    }
    return render(request, "forum/index.html", context)

def forum(request, topic):
    topic_obj = get_object_or_404(Topic, name=topic)
    messages_obj = Message.objects.filter(topic=topic_obj).order_by('created_at')
    try:
        new_message = request.POST["send_message"]
        Message.objects.create(
            topic=topic_obj,
            content=new_message,
        )
    except:
        pass

    context = {
        "topic": topic_obj,
        "messages": messages_obj,
    }
    return render(request, "forum/forum.html", context)