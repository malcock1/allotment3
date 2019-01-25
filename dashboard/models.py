from django.db import models

class PermaculturePrinciple(models.Model):
	text = models.CharField(max_length=63)
