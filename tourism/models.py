from django.db import models

# Create your models here.
class alllist(models.Model):
	uname=models.CharField(max_length=300, blank=False)
	pimage=models.FileField(null=True , blank=True)
	placediscription=models.TextField()
	placeway=models.TextField()
	imagefigname=models.CharField(max_length=100)
	shortdiscription=models.CharField(max_length=100)
	
	def __str__(self):
		return self.uname
	class Meta:
		ordering = ['uname']
		
