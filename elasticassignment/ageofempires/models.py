from django.db import models
from django.db.models.fields import IntegerField

class Civilization(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)
    army = models.TextField(blank=True)
    expansion = models.TextField(blank=True)
    unique_unit = models.TextField(blank=True)
    unique_tech = models.TextField(blank=True)
    team_bonus = models.TextField(blank=True)
    civilization_bonus = models.TextField(blank=True)
    def __str__(self):
        return '%s' % (self.name)

class Unit(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    expansion = models.TextField(blank=True)
    age = models.TextField(blank=True)
    created_in = models.TextField(blank=True)
    cost = models.TextField(blank=True)
    build_time = models.IntegerField(blank=True)
    reload_time = models.FloatField(blank=True)
    attack_delay = models.FloatField(blank=True)
    movement_rate = models.FloatField(blank=True)
    line_of_sight = models.IntegerField(blank=True)
    hit_points = models.IntegerField(blank=True)
    attack = models.IntegerField(blank=True)
    armor = models.TextField(blank=True)
    attack_bonus = models.TextField(blank=True)
    armor_bonus = models.TextField(blank=True)
    search_radius = models.IntegerField(blank=True)
    accuracy = models.TextField(blank=True)
    blast_radius = models.FloatField(blank=True)
    structure_range = models.TextField(blank=True)
    def __str__(self):
        return '%s' % (self.name)

class Structure(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)
    description= models.TextField(blank=True)
    expansion= models.TextField(blank=True)
    age= models.TextField(blank=True)
    cost= models.TextField(blank=True)
    build_time= models.IntegerField(blank=True)
    hit_points= models.IntegerField(blank=True)
    line_of_sight= models.IntegerField(blank=True)
    armor= models.TextField(blank=True)
    reload_time= models.FloatField(blank=True)
    attack= models.IntegerField(blank=True)
    special= models.TextField(blank=True)
    structure_range = models.TextField(blank=True)
    def __str__(self):
        return '%s' % (self.name)

class Technology(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)
    description= models.TextField(blank=True)
    expansion= models.TextField(blank=True)
    age= models.TextField(blank=True)
    develops_in = models.TextField(blank=True)
    cost= models.TextField(blank=True)
    build_time= models.IntegerField(blank=True)
    applies_to = models.TextField(blank=True)
    def __str__(self):
        return '%s' % (self.name)
