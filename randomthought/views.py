from django.shortcuts import render, redirect, get_object_or_404

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


def thought_list(request):

    sentences = Sentence.objects.all()

    return render(
        request,
        'randomthought/thought_list.html',
        context={
            'sentences': sentences
        }
    )


def thought_create_view(request):
    sentence = request.POST.get('sentence')

    if sentence:
        Sentence.objects.create(body=sentence)

        return redirect('randomthought:thought-list')

    return render(
        request,
        'randomthought/thought_form.html'
    )


def thought_update_view(request, pk):
    sentence = get_object_or_404(Sentence, pk=pk)

    modified_sentence = request.POST.get('sentence')
    if modified_sentence:
        sentence.body = modified_sentence
        sentence.save()

        return redirect('randomthought:thought-list')

    return render(
        request,
        'randomthought/thought_form.html',
        context={
            'sentence': sentence,
        }
    )


def thought_delete_view(request, pk):
    sentence = get_object_or_404(Sentence, pk=pk)

    if request.method == "POST":
        sentence.delete()
        return redirect('randomthought:thought-list')

    return render(
        request,
        'randomthought/thought_delete_confirm.html',
        context={
            'sentence': sentence,
        }
    )


def thought_detail_view(request, pk):
    sentence = get_object_or_404(Sentence, pk=pk)

    return render(
        request,
        'randomthought/thought_detail.html',
        context={
            'sentence': sentence,
        }
    )