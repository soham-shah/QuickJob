from django.db import models

# Create your models here.
class Application(models.Model):
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    apply_date = models.DateTimeField('date published')
    application_type = models.CharField(max_length=200)
    job_location = models.CharField(max_length=200)
    resume_version = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    result= models.CharField(max_length=200)

    def __str__(self):
        return self.company_name + ": " + self.job_title