from django.shortcuts import render, redirect
from .forms import TodoAppForm, UpdateForm
from .models import TodoApp
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
# Create your views here.


@csrf_exempt
def create(request):
    if request.method == 'POST':
        fm = TodoAppForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = TodoAppForm()
    else:
        fm = TodoAppForm()
    return render(request, 'todoapp/create.html', {'form': fm})


@csrf_exempt
def read(request):
    if request.method == 'GET':
        stu = TodoApp.objects.values()
        return JsonResponse(list(stu), safe=False)


@csrf_exempt
def update(request, id):
    fm = UpdateForm(request.POST)
    if request.method == 'POST':
        if fm.is_valid():
            name = fm.cleaned_data['name']
            text = fm.cleaned_data['text']
            reg = TodoApp(id=id, name=name, text=text)
            reg.save()
            return HttpResponse('Your Data Will Updated !!!...')
        else:
            return HttpResponse('Please Enter Valid Id')
    return render(request, 'todoapp/update.html', {'form': fm})
