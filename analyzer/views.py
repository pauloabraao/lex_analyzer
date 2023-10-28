from django.shortcuts import render
from django.http import HttpResponse
from .analisador import process_input


def index(request):
    return render(request, 'index.html')


def resultado(request):
    return render(request, 'analisador_lexico/resultado.html')

# Create your views here.

def analisar(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file_content = request.FILES['file'].read().decode('utf-8')
            expression, tokens = process_input(file_content)
        else:
            manual_expression = request.POST['manual_expression']
            expression, tokens = process_input(manual_expression)

        return render(request, 'index.html', {'expression': expression, 'tokens': tokens})
    else:
        return HttpResponse("Método não permitido.")