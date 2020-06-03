from django.db import models

# Create your models here.
class postjobs(models.Model):
    Job_title = models.CharField(max_length = 100)
    slug = models.SlugField()
    Job_Description = models.TextField()
    Experience = models.CharField(max_length = 100)
    Location = models.CharField(max_length = 100)
    Salary = models.CharField(max_length = 100)

    def __str__(self):
        return self.Job_title

    def snippet(self):
        return self.Job_Description[0:50]
