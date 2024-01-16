from django.db import models
from django.urls import reverse

# Create your models here.




from django.db import models

# Create your models here.
class Creature(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100, default='default_value')
    family = models.CharField(max_length=100, default='default_value')
    diet = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    habitat = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='creatures/', null=True, blank=True)
    
    predators = models.CharField(max_length=100, default='default_value')
    prey = models.CharField(max_length=100, default='default_value')
    appearance = models.CharField(max_length=300, default='default_value')
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'creature_id': self.id})
