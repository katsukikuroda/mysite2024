from django.shortcuts import render

def index(request):
    return render(request, 'polls/index.html', {
        'name': 'びえんじ',
        'money': 500 * 23,
    }
)

favorite_list = ['アイスクリーム', 'ソフトクリーム', 'シュークリーム']

def test(request):
    context = {
        'name': 'びえんじ',
        'age': 17,
        'favorite': favorite_list,
    }
    return render(request, 'polls/test.html', context)



