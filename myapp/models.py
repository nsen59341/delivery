from django.db import models

# Create your models here.

class Food(models.Model):
    id = models.IntegerField(db_index=True,primary_key=True)
    name = models.CharField(max_length=54)
    type = models.CharField(max_length=54)
    price = models.FloatField()

    class Meta:
        ordering = ("type",)

    def __str__(self) -> str:
        self.price = round(self.price)
        return f"{self.name} - {self.price}"
