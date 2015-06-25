from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    full_name=models.CharField(blank=True, null=True,max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.email
