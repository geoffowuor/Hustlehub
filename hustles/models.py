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
    
    def __str__(self):
        return self.name
    
    


#worker details
class employee(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_about = models.CharField(max_length=500)
    emp_photo = models.ImageField(upload_to="media/")
    emp_contact = models.CharField(max_length=35)
    emp_skills = models.CharField(max_length=420)
    emp_location = models.CharField(max_length=430)
    
    def __str__(self):
        return self.emp_name
    
    

##Employer details
class employer(models.Model):
    boss_name = models.CharField(max_length=70)
    boss_contact = models.CharField(max_length=70)
    boss_location = models.CharField(max_length=45)
    boss_about = models.CharField(max_length=420, null=True)
    
    def __str__(self):
        return self.boss_name
    
    
    
#gig applicaation
class application(models.Model):
    gig = models.ForeignKey(gig, on_delete=models.CASCADE)  # Related gig
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)  # Related employee
    cover_letter = models.TextField(max_length=1000, null=True, blank=True)  # Optional cover letter
    application_date = models.DateTimeField(auto_now_add=True)  # Date of application
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')],
        default='Pending'
    )  # Status of the application

    def __str__(self):
        return self.cover_letter
    
    
    
