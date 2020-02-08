from django.http import HttpResponse

def index1(request):
	return HttpResponse("<h1>HomePage</h1><br><a href = 'http://127.0.0.1:8000/room/'>CCD Room Allotment</a><br><a href = 'http://127.0.0.1:8000/about/'>About CCD</a>")