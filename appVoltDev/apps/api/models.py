from typing import Iterable
from django.db import models


class Boss(models.Model):
    name = models.CharField(max_length=32)

    class Meta():
        verbose_name = "Mandante"
        verbose_name_plural = "Mandantes"

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Boss, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"


class Unit(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self) -> str:
        return f"{self.name}"
    

class Provider(models.Model):
    name = models.CharField(max_length=32)

    class Meta():
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Provider, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"


class Materials(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    description = models.CharField(max_length=512)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    class Meta():
        verbose_name = "Material"
        verbose_name_plural = "Materiales"

    def __str__(self) -> str:
        return f"{self.description}"
    

class Budget(models.Model):
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=64)
    total_budget = models.PositiveIntegerField(blank=True, null=True)
    file = models.FileField(upload_to='budgets/', blank=True, null=True)
    created = models.DateField(auto_created=True, auto_now_add=True)

    class Meta():
        verbose_name = "Presupuesto"
        verbose_name_plural = "Presupuestos"

    def save(self, *args, **kwargs):
        self.project_name = self.project_name.upper()
        super(Budget, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.project_name}"


class Items(models.Model):
    mount = models.PositiveIntegerField()
    item = models.ForeignKey(Materials, on_delete=models.CASCADE)
    total_item = models.PositiveIntegerField(null=True, blank=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='budget')

    class Meta():
        verbose_name = "Item"
        verbose_name_plural = "Items"
        unique_together= ['item', 'budget']

    def save(self, *args, **kwargs):
        self.total_item = self.mount * self.item.price
        super(Items, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.mount} - {self.item.description}"

    
