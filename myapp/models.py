from django.db import models
from django.contrib.auth.models import User

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


class Order(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Food)
    address = models.TextField(max_length=250, default='')
    is_placed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Order #{self.id}"