from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

User = settings.AUTH_USER_MODEL


# Create your models here.
class PersonalDetails(models.Model):

    user = models.ForeignKey(User, default=User, on_delete=models.CASCADE)
    phoneNumberRegex = RegexValidator(regex=r"[6,8,9]\d\d\d\d\d\d\d")
    contact = models.CharField(validators=[phoneNumberRegex], max_length=8, unique=False, default="")
    date_of_birth = models.DateField(default="")

    gender = models.CharField(max_length=10, default="")
    address_line = models.CharField(max_length=150, default="")
    unit = models.CharField(max_length=10, default="")
    postal_code = models.CharField(max_length=10, default="")


    def _str_(self):
        return self.user

#Signals

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    if created:
        PersonalDetails.objects.create(user=instance)
        print('Profile created!')

#post_save.connect(create_profile, sender=User)

# @receiver(post_save, sender=User)
# def update_profile(sender, instance, created, **kwargs):
#
#     if created == False:
#         instance.personaldetails.save()
#         print('Profile updated!')
#
# #post_save.connect(create_profile, sender=User)
