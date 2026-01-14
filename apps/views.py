from django.shortcuts import render



def home(request):
    return render(request, 'home.html')

def badiiy_kitoblar(request):
    return render(request, 'badiiy_kitoblar.html')

def tarixiy_kitoblar(request):
    return render(request, 'tarixiy_kitoblar.html')

def fantastik_kitoblar(request):
    return render(request, 'fantastik_kitoblar.html')

def ensiklopediyalar(request):
    return render(request, 'ensikloediyalar.html')

def badiiy_kitoblar_haqida(request):
    return render(request, 'badiiy_kitoblar_haqida.html')

def tarixiy_kitoblar_haqida(request):
    return render(request, 'tarixiy_kitoblar_haqida.html')

def fantastik_kitoblar_haqida(request):
    return render(request, 'fantastik_kitoblar_haqida.html')

def ensiklopediyalar_haqida(request):
    return render(request, 'ensiklopediyalar_haqida.html')