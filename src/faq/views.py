from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import QuestionModelForm
from .models import Question, Category, Answer, Mention
from django.contrib.auth.models import User


def dashboard(request):
    return render(request, 'dashboard/home.html')


def forum(request):
    all_questions = Question.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(all_questions, 5)  # Show 5 contacts per page

    page = request.GET.get('page')
    questions = paginator.get_page(page)
    if request.method == 'GET':
        question_form = QuestionModelForm()

    return render(request, 'dashboard/forum.html', {'questions': questions,
                                                    'question_form': question_form, 'categories': categories})


def forum_list(request):
    all_questions = Question.objects.all()
    paginator = Paginator(all_questions, 5)  # Show 5 contacts per page

    page = request.GET.get('page')
    questions = paginator.get_page(page)
    if request.method == 'GET':
        question_form = QuestionModelForm()

    return render(request, 'dashboard/list_ajax.html', {'questions': questions, 'question_form': question_form})


def questions(request, id):
    category = Category.objects.get(id=id)
    print(category)
    qs = category.categories.all()
    return render(request, 'dashboard/questions_list.html', {'category': category, 'questions': qs})


def question(request, id):
    question = Question.objects.get(id=id)
    print(question)
    return render(request, 'dashboard/question_detail.html', {'question': question})


def answer(request, id):
    answer = Answer.objects.get(id=id)
    return render(request, 'dashboard/answer_detail.html')


def mentions(request, account):
    mentioned = User.objects.get(username=account)
    mentions = mentioned.mentioned.all()
    print(mentions)
    return render(request, 'dashboard/mentions.html', {'mentions': mentions})


def tools(request):
    return render(request, 'dashboard/tools.html')


def repos(request):
    return render(request, 'dashboard/github-repos.html')


def eos_911(request):
    return render(request, 'dashboard/911.html')
