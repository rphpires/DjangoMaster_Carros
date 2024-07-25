from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from cars.models import Car, CarInventory

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = 'Sem descrição.'

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, created, **kwargs):
    # print('Car Created') if created else print('Car Updated')
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print('### POST-DELETE ###')
    car_inventory_update()

def car_inventory_update():
    count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']

    CarInventory.objects.create(cars_count=count, cars_value=cars_value)