from django.shortcuts import render
from .models import civilization, structure, technology, unit
from django.http.request import HttpRequest

def civilizations(request:HttpRequest):
    """
    Retrieves the civilization data and renders to template
    Gets the data from civilization model
    """
    civ_instance = civilization.Civilization()
    res = civ_instance.get_objects()
    civilization_list = res['hits']['hits']
    context = {'civilization_list' : civilization_list}
    return render(request, 'ageofempires/civilizations.html',context)

def units(request:HttpRequest):
    """
    Retrieves the civilization data and renders to template
    Gets the data from units model
    """
    unit_instance = unit.Unit()
    res = unit_instance.get_objects()   
    units_list = res['hits']['hits']
    context = {'units_list' : units_list}
    return render(request, 'ageofempires/units.html',context)

def structures(request:HttpRequest):
    """
    Retrieves the civilization data and renders to template
    Gets the data from structures model
    """
    struc_instance = structure.Structure()
    res = struc_instance.get_objects()
    structures_list = res['hits']['hits']
    context = {'structures_list' : structures_list}
    return render(request, 'ageofempires/structures.html',context)

def technologies(request:HttpRequest):
    """
    Retrieves the civilization data and renders to template
    Gets the data from technologies model
    """
    tech_instance = technology.Technology()
    res = tech_instance.get_objects()
    technologies_list = res['hits']['hits']
    context = {'technologies_list' : technologies_list}
    return render(request, 'ageofempires/technologies.html',context)
