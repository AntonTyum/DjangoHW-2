from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def index(request):
    return HttpResponse("Добро пожаловать! Укажите рецепт, например, /omlet/")

def recipe_view(request, recipe_name):
    recipe = DATA.get(recipe_name)
    
    if not recipe:
        return HttpResponse("Рецепт не найден", status=404)

    servings = request.GET.get('servings', 1)
    
    try:
        servings = int(servings)
        if servings < 1:
            raise ValueError
    except ValueError:
        return HttpResponse("Параметр servings должен быть целым положительным числом.", status=400)

    recipe_servings = {ingredient: quantity * servings for ingredient, quantity in recipe.items()}

    context = {'recipe': recipe_servings}
    return render(request, 'calculator/index.html', context)
