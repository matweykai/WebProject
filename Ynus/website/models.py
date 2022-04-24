from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    """Represents company account in database"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    site_address = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username + f'({self.site_address})'


class Discipline(models.Model):
    """Represents direction disciplines (subjects) in database"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Direction(models.Model):
    """Represents direction (education programs) in database"""
    name = models.CharField(max_length=50)
    description = models.TextField()
    img_path = models.TextField()
    disciplines = models.ManyToManyField(Discipline)

    def __str__(self):
        return self.name


class Vote(models.Model):
    """Represents company vote for the discipline in the database"""
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.company.site_address}->{self.discipline.name}({self.direction.name})'
