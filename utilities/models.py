from django.db import models
from customauth.models import User


class Social(models.Model):
    PLATFORM_CHGOICES = [
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('github', 'Github')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(
        max_length=100, choices=PLATFORM_CHGOICES, null=True
    )
    url = models.URLField(max_length=100)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} {self.platform}"
