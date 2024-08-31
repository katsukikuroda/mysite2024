from django.shortcuts import render

def index(request):
    return render(request, 'polls/index.html', {
        'name': 'びえんじ',
        # 'money': f'{500 * 23}円',
        'money': str(500 * 23) + '円',
        })
