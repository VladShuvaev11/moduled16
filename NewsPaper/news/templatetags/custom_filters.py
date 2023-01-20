from django import template


register = template.Library()


UNWANTED_WORDS = ['редиска']


@register.filter(name='censor')
def censor(text):
    for word in UNWANTED_WORDS:
        if word in text:
            text = text.replace(word[1:len(word)], f'{len(word) * "*"}')
            return text
        else:
            return text