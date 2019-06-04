from django.shortcuts import render

def home(request):
	info = {"name": request.GET['name']}
	return render(request, 'templates.html', info)