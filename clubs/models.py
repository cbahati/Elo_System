from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Club(models.Model):
    club_name = models.CharField( max_length = 100)
    player_name = models.CharField( max_length = 100)
    rank_score = models.FloatField(default = 1000.0)
    wins = models.IntegerField(default = 0)
    loss = models.IntegerField(default = 0)
    draws = models.IntegerField(default = 0)
    rank = models.IntegerField()
    last_rank = models.IntegerField()
    rank_difference = models.CharField(max_length = 20, default = "-")
    goal_for =  models.IntegerField(default = 0)
    goal_against = models.IntegerField( default = 0)
    goal_difference = models.IntegerField( default = 0)
    club_image = models.ImageField(upload_to=get_image_path, default = 'Elo_System/static/static_dirs/img/club_banners/deault.jpg',  blank=True, null=True)                                                          
  

   
    def __unicode__(self):
        return self.club_name
        
        
    class Meta:
        ordering = ['-rank_score']
    
