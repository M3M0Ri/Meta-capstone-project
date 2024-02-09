
from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'
        #return self.title
