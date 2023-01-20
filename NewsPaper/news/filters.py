from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter, ChoiceFilter
from .models import *
from django import forms
class PostFilter(FilterSet):
    search_title = CharFilter(
        field_name='title',
        label='Заголовок',
        lookup_expr='icontains',
    )

    search_author = ModelChoiceFilter(
        empty_label='Все авторы',
        field_name='author',
        label='Автор',
        queryset=Author.objects.all(),
    )


    post_date__gt = DateFilter(
        field_name='data',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата',
        lookup_expr='date__gte',
    )

