from django.shortcuts import render

from randomthought.models import Sentence


def thought(request):

    sentence = Sentence.objects.order_by('?').first()

    return render(
        request,
        'randomthought/todays_thought.html',
        context={
            'sentence':sentence
        }
    )

