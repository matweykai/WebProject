from django import template
register = template.Library()


@register.filter
def divide(left_obj, right_obj):
    return int(left_obj / right_obj * 100)
