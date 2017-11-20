from django.db import models
from datetime import datetime
from django.utils.encoding import python_2_unicode_compatible

class Toode(models.Model):
    nimetus = models.CharField(max_length=70)
    hind = models.FloatField(default=0)
    def __str__(self):
        return self.nimetus.capitalize()
    class Meta:
        verbose_name_plural = "Tooted"

class Tellimus(models.Model):
    toode = models.ForeignKey(Toode, on_delete=models.CASCADE)
    kuupaev = models.DateField("Tellimuse kuupäev")
    kogus = models.IntegerField(default=0)
    def __str__(self):
        if self.kogus > 1:
            tellimus_text = self.toode.nimetus.capitalize() + " - " + str(self.kogus) + " tükki - " + str(self.toode.hind*self.kogus) + " EUR"
        else:
            tellimus_text = self.toode.nimetus.capitalize() + " - " + str(self.kogus) + " tükk - " + str(self.toode.hind*self.kogus) + " EUR"
        return tellimus_text
    class Meta:
        verbose_name_plural = "Tellimused"
