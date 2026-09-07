import os
from dotenv import load_dotenv
from django.db.models.signals import pre_save
from django.dispatch import receiver
from gemini_api.client import get_course_ai_description
from courses.models import Course


load_dotenv()
api_key = os.getenv("API_KEY")

@receiver(pre_save, sender=Course)
def course_pre_save(sender, instance, **kwargs):
    if not instance.description:
        if len(api_key) > 0:
            ai_description = get_course_ai_description(instance.name)
            instance.description = ai_description