from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306152443',
        'name': 'Utandra Nur Ahmad Jais',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)