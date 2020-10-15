import os
import os

from django.utils import timezone
from datetime import timedelta
from blog.models import Post

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")

def auto_filling():
    for i in range(1,100):
        new = Post.objects.create(title = 'Заголовок № {}'.format(i), text = 'Текстовое поле № {}'.format(i), created_datetime__lte=timezone.now(), published_date__lte=timezone.now())
        return new

