from django.db import models

# Create your models here.

#Gigs model
class gig(models.Model):
    name = models.CharField(max_length=100)
    rate = models.IntegerField()
    description = models.CharField(max_length=420)
    skill = models.CharField(max_length=120)
    location = models.CharField(max_length=30)
    date_posted = models.DateTimeField(auto_now_add=True)
    


#worker details
class employee(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_about = models.CharField(max_length=500)
    emp_photo = models.ImageField(upload_to="media/")
    emp_contact = models.CharField(max_length=35)
    emp_skills = models.CharField(max_length=420)
    emp_location = models.CharField(max_length=430)
    

##Employer details
class employer(models.Model):
    boss_name = models.CharField(max_length=70)
    boss_contact = models.CharField(max_length=70)
    boss_location = models.CharField(max_length=45)
    boss_about = models.CharField(max_length=420, null=True)
    
    
