from django.db import models

# Create your models here.
class user(models.Model):
    titles=models.CharField(max_length=100)
    imagess=models.ImageField(upload_to='images/')
    upload_to=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
