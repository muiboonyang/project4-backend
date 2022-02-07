from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.

class FitnessClass(models.Model):

    user = models.ForeignKey(User, default=User, on_delete=models.CASCADE)
    class_type = models.CharField(max_length=30, default="")
    class_instructor = models.CharField(max_length=30, default="")
    date = models.DateField(default="")
    time = models.TimeField(default="")
    spot = models.CharField(max_length=30, default="")
    name = models.CharField(max_length=20, default="")

    def _str_(self):
        return self.class_type


# Django Admin

  # CLASS_CHOICES = [
    #     ('DM', 'Dominate'),
    #     ('KO', 'Kore'),
    #     ('LO', 'Leanout'),
    #     ('MD', 'Meltdown'),
    #     ('RM', 'Remixed'),
    # ]
    #
    # class_type = models.CharField(
    #     max_length=2,
    #     choices=CLASS_CHOICES,
    #     default='DM',
    # )
    #
    # date_time = models.DateTimeField()
    #
    # INSTRUCTOR_CHOICE = [
    #     ('EM', 'Ernest'),
    #     ('ER', 'Eunice'),
    #     ('FG', 'Faith'),
    #     ('RK', 'Reagan'),
    #     ('SL', 'Samson'),
    # ]
    #
    # instructor = models.CharField(
    #     max_length=2,
    #     choices=INSTRUCTOR_CHOICE,
    #     default='EM',
    # )
    #
    # spot_one_booked = models.BooleanField(default=False)
    # spot_two_booked = models.BooleanField(default=False)
    # spot_three_booked = models.BooleanField(default=False)
    # spot_four_booked = models.BooleanField(default=False)
    # spot_five_booked = models.BooleanField(default=False)

    # def _str_(self):
    #     return self.class_type
