from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter
def lower(value):
    return value.lower()

@register.filter
def upper(value):
    return value.upper()

@register.filter
def parameter(value, arg):
    text = ''
    for i in range(arg):
        text += f"<p> {str(i)}){value} </p><br>"
    return text

@register.filter
@stringfilter
def text_duplicate(value):
    return (value + " ") * 2
