from django.db import models

# Create your models here.
class PostIT(models.Model):
    tittel = models.CharField(max_length=20)
    innhold = models.TextField()
    status = models.CharField(max_length=10, default='ny')
    opprettet = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittel