from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
import face_recognition
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True, max_length=40000)
    route = ArrayField(models.CharField(max_length=120), null=True, blank=True)
    face_codes = ArrayField(
            models.FloatField(default=0, null=True, blank=True),
            size=128,
            null=True,
            blank=True,
    )


    def coding(self):
        return face_recognition.face_encodings(face_recognition.load_image_file(self.photo.path))[0].tolist()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print("created")
        UserProfile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#   instance.userprofile.save()