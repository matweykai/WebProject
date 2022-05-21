from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Company(models.Model):
    """Represents company account in database"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_company_profile(sender, instance, created, **kwargs):
    """Controls post method for user registration"""
    if created:
        Company.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_company_profile(sender, instance, **kwargs):
    """Saving company profile instance"""
    instance.company.save()


class Discipline(models.Model):
    """Represents direction disciplines (subjects) in database"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Direction(models.Model):
    """Represents direction (education programs) in database"""
    name = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField(upload_to='direction_imgs/')
    disciplines = models.ManyToManyField(Discipline)

    def __str__(self):
        return self.name


class Vote(models.Model):
    """Represents company vote for the discipline in the database"""
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.company.user.username}->{self.discipline.name}({self.direction.name})'
