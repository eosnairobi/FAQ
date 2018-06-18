from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import QuestionModelForm
from .models import Question


def dashboard(request):
    return render(request, 'dashboard/home.html')


def forum(request):
    all_questions = Question.objects.all()
    paginator = Paginator(all_questions, 5)  # Show 5 contacts per page

    page = request.GET.get('page')
    questions = paginator.get_page(page)
    if request.method == 'GET':
        question_form = QuestionModelForm()

    return render(request, 'dashboard/forum.html', {'questions': questions, 'question_form': question_form})
