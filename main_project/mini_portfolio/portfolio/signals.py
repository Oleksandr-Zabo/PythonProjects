from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Project, DeleteRequest
from telegram_bot.bot import bot

@receiver(post_save, sender=Project)
def project_created_signal(sender, instance, created, **kwargs):
    if created and hasattr(instance.author, "userprofile"):
        tg_id = instance.author.userprofile.telegram_id
        if tg_id:
            bot.send_message(tg_id, f"Ваш проєкт '{instance.title}' успішно створено!")

@receiver(post_save, sender=DeleteRequest)
def delete_request_signal(sender, instance, created, **kwargs):
    if created:
        # повідомлення адміністратору
        from django.contrib.auth.models import User
        admins = User.objects.filter(is_staff=True)
        for admin in admins:
            if hasattr(admin, "userprofile") and admin.userprofile.telegram_id:
                bot.send_message(admin.userprofile.telegram_id,
                                 f"Запит на видалення: {instance.project.title} від {instance.user.username}")
