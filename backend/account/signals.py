from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
