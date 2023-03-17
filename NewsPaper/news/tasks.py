from celery import shared_task

from NewsPaper import settings
from .models import Post, Category
from datetime import datetime, timedelta
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@shared_task
def my_week():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(date__gte=last_week)
    categories = set(posts.values_list('category__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'post_week.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Сататьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to= subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task()
def send_notifications(prewiew, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': prewiew,
            'Link': f'{settings.SITE_URL}/news/{pk}'
        }
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()