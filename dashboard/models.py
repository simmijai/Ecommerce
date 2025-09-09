# from django.db import models
# from django.conf import settings

# class AdminLog(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     action = models.CharField(max_length=255)
#     extra = models.JSONField(null=True, blank=True)  # store metadata
#     created_at = models.DateTimeField(auto_now_add=True)
