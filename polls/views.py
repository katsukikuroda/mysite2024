from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'polls/index.html', {
        'name': 'びえんじ',
        'money': 500 * 23,
    }
)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)




favorite_list = ['アイスクリーム', 'ソフトクリーム', 'シュークリーム']

def test(request):
    context = {
        'name': 'びえんじ',
        'age': 17,
        'favorite': favorite_list,
    }
    return render(request, 'polls/test.html', context)



