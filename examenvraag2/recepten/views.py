from django.shortcuts import render
from .models import Recept

def list_all_recepten(request):
    recepten = Recept.objects.all()
    context = {'recepten': recepten}
    return render(request, 'recepten/index.html', context)

def search(request):
    if request.method == 'POST':
        recept_name = request.POST.get('name').title() # Capitalize name
        try:
            recept = Recept.objects.get(name=recept_name)
            context = {'recepten': recepten}
            return render(request, 'recepten/index.html', context)
        except:
            return render(request, 'recepten/index.html', None)
    else:
        return render(request, 'recepten/search.html', None)

def add(request):
    if request.method == 'POST':
        recept_name = request.POST.get('name').title() # Capitalize name
        try:
            a = Recept(name=recept_name)
            a.save()
            for r in recepten:
                r = Recept(recept_name=recept, recept_id=a.id)
                q.save()
            return render(request, 'recepten/ok.html', None)
        except:
            return render(request, 'recepten/index.html', None)
    else:
        return render(request, 'recepten/add.html', None)
