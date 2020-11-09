from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Habit(models.Model):
    verb = models.CharField(max_length=20)
    noun = models.CharField(max_length=20)
    noun_singular = models.CharField(max_length=20)
    number = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="habits", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.verb} {self.noun} {self.number}"


class Record(models.Model):
    number = models.FloatField()
    is_met = models.BooleanField(default=False)
    habit = models.ForeignKey(Habit, related_name="records", on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["habit", "date"], name="unique_record")
        ]

    def __str__(self):
        return f"{self.habit} {self.date}"
