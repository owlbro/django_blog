from django.utils import timezone
from datetime import timedelta
from blog.models import Post


def run():
    for i in range(1,100):
        new = Post.objects.create(title = 'Заголовок № {}'.format(i), text = 'Текстовое поле № {}'.format(i), created_datetime=timezone.now(), published_date=timezone.now(), author_id = 1)

