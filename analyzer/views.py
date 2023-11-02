from django.shortcuts import render
from django.http import HttpResponse
from .analisador import process_input


def index(request):
    return render(request, 'index.html')


def result(request):
    try:
        if request.method == 'POST':
            if 'file' in request.FILES:
                file_content = request.FILES['file'].read().decode('utf-8')
                expression, tokens = process_input(file_content)
            else:
                manual_expression = request.POST['manual_expression']
                expression, tokens = process_input(manual_expression)

            return render(request, 'index.html', {'expression': expression, 'tokens': tokens})
    except ValueError as error:
        print("An exception occurred:", str(error))
        return render(request, 'index.html', {'error_message': str(error)})
    else:
        return HttpResponse("Método não permitido.")
