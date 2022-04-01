from django.shortcuts import render


def todays_thought(request):

    return render(
        request,
        'randomthought/todays_thought.html'
    )