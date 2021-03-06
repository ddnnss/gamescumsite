from django.db import models
from datetime import datetime

class News(models.Model):
    post_id = models.CharField(max_length=10,default=0)
    post_name = models.CharField(max_length=255,blank=False,null=False)
    post_url = models.CharField(max_length=255,blank=False,null=True,default=None)
    post_image = models.CharField(max_length=255, blank=False, null=True, default=None)
    post_local = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

