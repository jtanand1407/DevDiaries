from django.db import models

class Post(models.Model):
    id=models.AutoField(primary_key=True,unique=True, null=False)
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=250)
  
    def __str__(self):
        return self.title
