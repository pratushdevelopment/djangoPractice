from django.shortcuts import render
from .forms import *
from .models import Recipe

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
            return render(request, 'receipe.html')
    else:
        form = RecipeForm()
    return render(request, 'receipe.html', {'form': form})


def recipe_list(request):
    recipe_list = Recipe.objects.all()
    return render(request, 'receipe.html', {'recipe_list': recipe_list})
