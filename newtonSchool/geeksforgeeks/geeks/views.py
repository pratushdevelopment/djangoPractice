from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import GeeksModel
from .forms import GeeksForm

def create_view(request):
    context = {}
    if request.method == 'POST':
        form = GeeksForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GeeksForm()
    context['form'] = form
    return render(request, 'create_view.html', context)

def list_view(request):
    context = {}
    geeks = GeeksModel.objects.all()
    context['dataset'] = geeks
    return render(request, 'list_view.html', context)

def detail_view(request, id):
    context = {}
    context["data"] = get_object_or_404(GeeksModel, id=id)
    return render(request, "detail_view.html", context)

def update_view(request, id):
    context = {}
    obj = get_object_or_404(GeeksModel, id=id)
    if request.method == 'POST':
        form = GeeksForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/geeks/list/")
    else:
        form = GeeksForm(instance=obj)
    context["form"] = form
    return render(request, "update_view.html", context)

def delete_view(request, id):
    context = {}
    obj = get_object_or_404(GeeksModel, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/geeks/list/")
    return render(request, "delete_view.html", context)