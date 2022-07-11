from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile
from django.conf import settings
import logging
from slugify import slugify
from django.contrib.auth import get_user_model

User1 = get_user_model()

User = settings.AUTH_USER_MODEL

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, *args, **kwargs):

    instance.profile.save()
    logger.info(f"{instance.username}'s profile has been created.")
