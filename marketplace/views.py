from django.shortcuts import render


def home(request):
    return render(request, 'marketplace/home.html', {'message': 'Welcome to the Farming E-commerce Platform!'})


from django.shortcuts import render

def home(request):
    return render(request, 'marketplace/home.html')



