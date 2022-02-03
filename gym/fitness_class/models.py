from django.db import models


# Create your models here.

class FitnessClass(models.Model):
    id = models.AutoField(primary_key=True)
    CLASS_CHOICES = [
        ('DM', 'Dominate'),
        ('KO', 'Kore'),
        ('LO', 'Leanout'),
        ('MD', 'Meltdown'),
        ('RM', 'Remixed'),
    ]

    class_type = models.CharField(
        max_length=2,
        choices=CLASS_CHOICES,
        default='DM',
    )

    date_time = models.DateTimeField()

    INSTRUCTOR_CHOICE = [
        ('EM', 'Ernest'),
        ('ER', 'Eunice'),
        ('FG', 'Faith'),
        ('RK', 'Reagan'),
        ('SL', 'Samson'),
    ]

    instructor = models.CharField(
        max_length=2,
        choices=INSTRUCTOR_CHOICE,
        default='EM',
    )

    spot_one_booked = models.BooleanField(default=False)
    spot_two_booked = models.BooleanField(default=False)
    spot_three_booked = models.BooleanField(default=False)

    def _str_(self):
        return self.class_type
