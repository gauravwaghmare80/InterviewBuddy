from django import template

register = template.Library()

@register.filter(name='percentage')
def percentage(value, total):
    try:
        return round((float(value) / float(total)) * 100, 2)
    except (ValueError, ZeroDivisionError):
        return 0
    
@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)