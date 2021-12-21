from django.shortcuts import render

def civilizations(request):
    return render(request, 'ageofempires/civilizations.html' )
