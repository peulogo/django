from django.shortcuts import render

# Create your views here.

def main_view(request):
    return render(request, 'third_task/index.html')


def games_view(request):
    context = {
        'menu_items': [
            {'name': 'Atomic Heart', 'url': ''},
            {'name': 'Cyberpunk 2077', 'url': ''},
            {'name': 'PayDay 2', 'url': 'cart_view'},
        ]
    }

    return render(request, 'third_task/games.html', context)


def cart_view(request):
    return render(request, 'third_task/cart.html')
