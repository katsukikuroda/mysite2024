from django.shortcuts import render

topic_list = ['HTML', 'CSS', 'JavaScript', 'Python', 'Java', 'C', 'PHP', 'R', 'Swift', 'Kotlin']

def index(request):
    context = {
        'topics': topic_list,
    }
    return render(request, 'forum/index.html', context)