from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Project, DeleteRequest
from telegram_bot.bot import bot

@receiver(post_save, sender=Project)
def project_created_signal(sender, instance, created, **kwargs):
    if created and hasattr(instance.author, "userprofile"):
        tg_id = instance.author.userprofile.telegram_id
        if tg_id:
            message = f"""
🎉 Новий проєкт створено!

📌 Назва: {instance.title}
📝 Опис: {instance.description[:100]}...
🔗 Посилання: {instance.link if instance.link else 'Не вказано'}
📅 Дата: {instance.created_at.strftime('%Y-%m-%d %H:%M')}

Використайте /projects щоб переглянути всі ваші проєкти.
            """
            bot.send_message(tg_id, message)

@receiver(post_save, sender=DeleteRequest)
def delete_request_signal(sender, instance, created, **kwargs):
    if created:
        # повідомлення адміністратору
        from django.contrib.auth.models import User
        admins = User.objects.filter(is_staff=True)
        for admin in admins:
            if hasattr(admin, "userprofile") and admin.userprofile.telegram_id:
                message = f"""
🗑️ Новий запит на видалення!

📌 Проєкт: {instance.project.title}
👤 Від: {instance.user.username}
📝 Причина: {instance.reason}
📅 Дата: {instance.created_at.strftime('%Y-%m-%d %H:%M')}

Використайте /requests щоб переглянути всі запити.
                """
                bot.send_message(admin.userprofile.telegram_id, message)
