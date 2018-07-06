from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import QuestionModelForm
from .models import Question, Category, Answer, Mention
from tools.models import Tool, ToolCategory
from django.contrib.auth.models import User


def dashboard(request):
    categories = ToolCategory.objects.all().order_by('name')
    tools = Tool.objects.all()
    categories = ToolCategory.objects.all()
    return render(request, 'dashboard/home.html', {'categories':categories})


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


def repos(request):
    tools = Tool.objects.all()
    categories = ToolCategory.objects.all()
    return render(request, 'dashboard/github-repos.html',{'categories': categories})


def eos_911(request):
    tools = Tool.objects.all()
    categories = ToolCategory.objects.all()
    return render(request, 'dashboard/911.html',{'categories': categories})


def news(request):
    tools = Tool.objects.all()
    categories = ToolCategory.objects.all()
    return render(request, 'dashboard/news.html',{'categories': categories})


def youtube(request):
    tools = Tool.objects.all()
    categories = ToolCategory.objects.all()
    return render(request, 'dashboard/youtube.html', {'categories': categories})


def testnets(request):
    tools = Tool.objects.all()
    categories = ToolCategory.objects.all()
    return render(request, 'dashboard/testnets.html', {'categories': categories})


def steem(request):
    tools = Tool.objects.all()
    categories = ToolCategory.objects.all()
    return render(request, 'dashboard/steem.html', {'categories': categories})


def twitter(request):
    tools = Tool.objects.all()
    categories = ToolCategory.objects.all()
    return render(request, 'dashboard/twitter.html', {'categories': categories})
