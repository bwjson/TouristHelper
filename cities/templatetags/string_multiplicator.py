from django import template

register = template.Library()

@register.filter
def multiply(str, times):
    return str * int(times)