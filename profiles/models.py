from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=60, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    is_coach = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create/Update user profile
    """

    if created:
        UserProfile.objects.create(user=instance, email=User.email)
    # Existing users just save the profile
    instance.userprofile.save()


class Coach(models.Model):
    coach = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                              limit_choices_to={'is_coach': True})
    about_me = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Coaches"

    def __str__(self):
        return self.coach.full_name
