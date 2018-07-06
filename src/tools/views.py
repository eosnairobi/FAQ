from django.shortcuts import render
from .forms import SuggestionForm

from .models import DappCategory, ToolCategory, Dapp, Tool


def dapps(request):
    dapps = Dapp.objects.all()
    categories = DappCategory.objects.all()
    return render(request, 'dashboard/dapps.html', {'dapps': dapps, 'categories': categories})


def tools(request):
    tools = Tool.objects.all()
    categories = ToolCategory.objects.all()
    if request.method == 'POST':
        form = SuggestionForm(request.POST or None, files=request.FILES)
        if form.is_valid():
            form.save()
            print('Saved')
        else:
            print(form.errors)
    
    elif request.method =='GET':
        form = SuggestionForm()
    return render(request, 'dashboard/tools.html', {'tools': tools, 'categories': categories, 'form':form})


def dapps_by_category(request):
    return render(request, 'dapp-category.html')

