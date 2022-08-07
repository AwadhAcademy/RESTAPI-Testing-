from django.db import models

# Create your models here.
class collection(models.Model):
    id=models.IntegerField(primary_key=True)
    State=models.CharField(max_length=20)
    TotalSamples=models.IntegerField()
    Negative=models.IntegerField()
    Positive=models.IntegerField()

    def __str__(self):
        return self.State