from django import template
register = template.Library()


@register.filter
def divide(left_num: int, right_num: int):
    """Divides the left number on the right number. If the right number is 0, then 0 returned"""
    return int(left_num / right_num * 100) if right_num != 0 else 0
