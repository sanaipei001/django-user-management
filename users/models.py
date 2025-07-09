from django.db import models
from django.contrib.auth.models import User
import uuid

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    verification_token = models.CharField(max_length=50, blank=True)
    is_verified = models.BooleanField(default=False)

    def generate_verification_token(self):
        self.verification_token = uuid.uuid4().hex[:50]
        self.save()
        return self.verification_token
