from django import template

register = template.Library()


@register.filter(name="split")
def split(value):
    return value.split(",")
