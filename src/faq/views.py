from django.shortcuts import render
from .forms import QuestionModelForm
from .models import Question


def dashboard(request):
    return render(request, 'dashboard/home.html')


def forum(request):
    questions = Question.objects.all()
    if request.method == 'GET':
        question_form = QuestionModelForm()

    return render(request, 'dashboard/forum.html', {'questions': questions, 'question_form': question_form})
