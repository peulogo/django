from django.shortcuts import render

# Create your views here.

def main_view(request):
    return render(request, 'fourth_task/index.html')


def games_view(request):
    context = {
        'menu_items': [
            {'games': ["Atomic Heart", "Cyberpunk 2077"]}
        ]
    }

    return render(request, 'fourth_task/games.html', context)


def cart_view(request):
    return render(request, 'fourth_task/cart.html')
