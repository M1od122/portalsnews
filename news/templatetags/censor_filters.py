from django import template

register = template.Library()

@register.filter(name='censor')
def censor(text):
    # Список нежелательных слов
    bad_words = ['плохо', 'плохой', 'дурной']
    for word in bad_words:
        text = text.replace(word, '*' * len(word))
    return text