from django.db.models.signals import post_save, post_delete, pre_save 
from django.dispatch import receiver
from django.core.files.base import ContentFile
from .models import Items, Materials, Budget
import os

@receiver(post_delete, sender=Items)
@receiver(post_save, sender=Items)
def update_item_total(sender, instance, **kwargs):
    budget = instance.budget
    budget.total_budget = sum([i.total_item for i in budget.budget.all()])
    budget.save()
    

@receiver(post_save, sender=Budget)
def create_update_budget_file(sender, instance, created, **kwargs):
    # Verificar si el archivo ya existe en el campo `file`
    if instance.file:
        file_path = instance.file.path
        
    # Obtener el precio total, asignar 0 si es None
    total_budget = instance.total_budget if instance.total_budget is not None else 0
    
    # Crear contenido del archivo con el detalle del presupuesto y los items
    content = f"Proyecto: {instance.project_name}\n"
    content += f"Jefe: {instance.boss.name}\n"
    content += f"Total del presupuesto: ${total_budget:,.2f}\n\n"
    content += "Listado de Items:\n"
    
    for item in instance.budget.all():
        content += (
            f"{item.mount} {item.item.unit} - "
            f"{item.item.description} - "
            f"PROVEEDOR REF: {item.item.provider.name} - "
            f"PRECIO REF: ${item.item.price:,.2f}\n"
        )
    
    # Crear o actualizar el archivo
    if not instance.file or not os.path.exists(file_path):
        # Si no hay archivo, crearlo y asignarlo al campo `file`
        file_name = f"{instance.project_name.replace(' ', '_')}.txt"
        instance.file.save(file_name, ContentFile(content), save=True)
    else:
        # Si ya existe, actualizar el contenido del archivo
        with open(file_path, 'w') as f:
            f.write(content)


@receiver(post_delete, sender=Budget)
def delete_budget_file(sender, instance, **kwargs):
    if instance.file:
        file_path = instance.file.path
        os.remove(file_path)