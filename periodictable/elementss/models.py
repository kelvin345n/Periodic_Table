from django.db import models

# Create your models here.
class Element(models.Model):
    atomic_number = models.CharField(max_length=3)
    symbol = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    atomic_mass = models.CharField(max_length=20)
    hex_color = models.CharField(max_length=10)
    electron_config = models.CharField(max_length=200)
    electronegativity = models.CharField(max_length=20)
    atomic_radius = models.CharField(max_length=20)
    ionization_energy = models.CharField(max_length=20)
    electron_affinity = models.CharField(max_length=20)
    oxidation_states = models.CharField(max_length=200)
    standard_state = models.CharField(max_length=20)
    melting_point = models.CharField(max_length=20)
    boiling_point = models.CharField(max_length=20)
    density = models.CharField(max_length=20)
    group_block = models.CharField(max_length=20)
    year_discovered = models.CharField(max_length=20)

