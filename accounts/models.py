from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class PlayerData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    iap_cash = models.DecimalField(max_digits=20, decimal_places=2,null=True)
    renown = models.DecimalField(max_digits=20, decimal_places=2,null=True)
    plots = models.JSONField(null=True)
    barracks =  models.JSONField(null=True)
    current_hero = models.DecimalField(max_digits=4, decimal_places=0,null=True)
    area_unlock = models.DecimalField(max_digits=20, decimal_places=0,null=True)
    
    def initialize(self,*kwargs):
        self.iap_cash = 0
        self.renown = 0
        self.plots = {
            "0": 1,
            "1": 0,
            "2": 0,
            "3": 0,
            "4": -1,
            "5": -1,
            "6": -1,
            "7": -1
        }
        self.barracks = {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": -1,
            "6": -1,
            "7": -1,
            "8": -1,
            "9": -1,
            "10": -1,
            "11": -1,
            "12": -1,
            "13": -1,
            "14": -1,
            "15": -1,
            "16": -1,
            "17": -1,
            "18": -1,
            "19": -1,
            "20": -1,
            "21": -1,
            "22": -1,
            "23": -1,
            "24": -1,
            "25": -1,
            "26": -1,
            "27": -1,
            "28": -1,
            "29": -1,
            "30": -1,
            "31": -1,
            "32": -1,
            "33": -1,
            "34": -1,
            "35": -1,
            "16": -1,
            "37": -1,
            "38": -1,
            "39": -1,
            "40": -1,
            "41": -1,
            "42": -1,
            "43": -1,
            "44": -1,
            "45": -1,
            "46": -1,
            "47": -1,
            "48": -1,
            "49": -1
        }
        self.current_hero = 0
        self.area_unlock = 0
        return 1

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        PlayerData.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.playerdata.save() # Oh wow, it lowercases it automagically :O