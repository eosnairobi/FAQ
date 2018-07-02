from django.shortcuts import render


from .models import DappCategory, ToolCategory, Dapp, Tool


def dapps(request):
    dapps = Dapp.objects.all()
    categories = DappCategory.objects.all()
    return render(request, 'dashboard/dapps.html', {'dapps': dapps, 'categories': categories})


def tools(request):
    tools = Tool.objects.all()
    categories = ToolCategory.objects.all()
    return render(request, 'dashboard/tools.html', {'tools': tools, 'categories': categories})


def dapps_by_category(request):
    return render(request, 'dapp-category.html')
