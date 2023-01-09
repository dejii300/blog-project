from django.shortcuts import render
from panda.models import Project

# Create your views here.
def project_index(request):
    panda = Project.objects.all()
    context = {
        'panda': panda
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'Project': project
    }    
    return render(request, 'project_detail.html', context)

