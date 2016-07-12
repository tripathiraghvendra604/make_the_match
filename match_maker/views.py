from django.shortcuts import render, redirect
from .models import Question, Answer
from .forms import UserResponseForm
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    form = UserResponseForm(request.POST or None)
    if form.is_valid():
        print form.cleaned_data
    queryset = Question.objects.all().order_by('-timestamp')
    instance = queryset[0]
    question_id = form.cleaned_data.get('question_id')
    answer_id = form.cleaned_data.get('answer_id')
    question_instance = Question.objects.get(id=question_id)
    answer_instance = Answer.objects.get(id=answer_id)
    print instance
    context = {
        #'queryset': queryset,
        'form': form,
        'instance': instance,
    }
    return render(request, 'questions/home.html', context)


def single(request, id):
    form = UserResponseForm(request.POST or None)
    if form.is_valid():
        print form.cleaned_data
        question_id = form.cleaned_data.get('question_id')
        answer_id = form.cleaned_data.get('answer_id')
        question_instance = Question.objects.get(id=question_id)
        answer_instance = Answer.objects.get(id=answer_id)
        next_q = Question.objects.all().order_by('?').first()
        return redirect('question_single', id=next_q.id)
    queryset = Question.objects.all().order_by('-timestamp')
    instance = get_object_or_404(Question, id=id)

    context = {
        #'queryset': queryset,
        'form': form,
        'instance': instance,
    }
    return render(request, 'questions/home.html', context)