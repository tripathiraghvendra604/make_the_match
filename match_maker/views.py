from django.shortcuts import render
from .models import Question

# Create your views here.

def home(request):
    queryset = Question.objects.all().order_by('-timestamp')
    context = {
        'queryset': queryset,
    }
    return render(request, 'questions/home.html', context)