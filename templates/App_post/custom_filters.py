from django import template

register = template.Library()

@register.filter
def convert_value(value):
    if value == 1:
        return "Absent"
    elif value == 2:
        return "Present"
    return value
