import pytest
pytestmark = pytest.mark.django_db

class TestFoodModel:
    def test_str_return(self, food_factory): # from FoodFactory
        food = food_factory(name="test", price=2)
        print('food_str ',food.__str__())  # Debugging output
        assert food.__str__() == "test - 2"