from django.shortcuts import render, HttpResponse


# Create your views here.
def project(request):
    context={'project': 'active'}
    return render(request, 'project/project.html',context)

