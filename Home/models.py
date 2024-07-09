from django.db import models

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/',blank=True,null=True)
    role = models.CharField(max_length=100)
    about_me = models.TextField()
    degree = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    birthday = models.DateField()
    email = models.EmailField()
    freelance = models.BooleanField(default=False)
    cv = models.FileField(upload_to='cvs/')

    def __str__(self):
        return self.name

class EducationExperience(models.Model):
    school = models.CharField(max_length=255)
    board_university = models.CharField(max_length=255)
    year_of_study = models.CharField(max_length=9)

    def __str__(self):
        return self.school

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    start_year = models.DateField()
    end_year = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.project_name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    small_description = models.TextField()

    def __str__(self):
        return self.service_name

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return str(self.image)

