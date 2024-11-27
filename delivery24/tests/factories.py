import factory

from myapp.models import Food

class FoodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Food

    name = 'x'
    type = 'x'
    price = 1