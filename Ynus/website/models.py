from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    site_address = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username + f'({self.site_address})'


class Discipline(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Direction(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    img_path = models.TextField()

    def __str__(self):
        return self.name


class DisciplineVote(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.direction}-{self.discipline}'


class VoteCompany(models.Model):
    vote = models.ForeignKey(DisciplineVote, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.vote}-{self.company}'
