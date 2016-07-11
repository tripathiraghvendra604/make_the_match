from django.shortcuts import render
from .models import Question, Answer
from .forms import UserResponseForm

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