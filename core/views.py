from django.shortcuts import render

# Create your views here.

def index(request):
	mesage = "Página inicial do Sistema"
	return render(request, 'core/index.html', {'mesage': mesage})

