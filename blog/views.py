from django.shortcuts import render

# Create your views here.
def web_list(request):
    return render(request, 'blog/index.html')