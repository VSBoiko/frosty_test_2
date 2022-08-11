from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from .models import Detail, Car, CarPrice


@receiver(m2m_changed, sender=Car.params.through)
def update_car_price_by_car(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        for car_price in CarPrice.objects.filter(car=instance.id):
            car_price.save()


@receiver(post_save, sender=Detail)
def update_car_price_by_detail(sender, instance, **kwargs):
    id_cars = [car.id for car in Car.objects.filter(params=instance.id)]
    for car_price in CarPrice.objects.filter(car__in=id_cars):
        car_price.save()
