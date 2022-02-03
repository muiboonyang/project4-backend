from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class PersonalDetails(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, default=User, on_delete=models.CASCADE)
    phoneNumberRegex = RegexValidator(regex=r"[6,8,9]\d\d\d\d\d\d\d")
    contact = models.CharField(validators=[phoneNumberRegex], max_length=8, unique=False)
    date_of_birth = models.DateField()

    GENDER_CHOICE = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICE,
        default='M',
    )

    address_line = models.CharField(max_length=150)
    unit = models.CharField(max_length=10, default="")
    postal_code = models.CharField(max_length=10)

    emergency_contact = models.CharField(max_length=50)
    phoneNumberRegex = RegexValidator(regex=r"[6,8,9]\d\d\d\d\d\d\d")
    emergency_number = models.CharField(validators=[phoneNumberRegex], max_length=8, unique=False)

    def _str_(self):
        return self.user
