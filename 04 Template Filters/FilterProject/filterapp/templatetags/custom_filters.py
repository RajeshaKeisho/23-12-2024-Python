from django import template
import math

register = template.Library()

@register.filter
def add_hello(value):
    return f"Hello {value}"

@register.filter
def square(value):
    return value ** 2

@register.filter
def reverse_string(value):
    return value[::-1]

@register.filter
def absolute(value):
    return abs(value)

@register.filter
def factorial(value):
    return math.factorial(value)

@register.filter
def even_or_odd(value):
    if value % 2 == 0:
        return "Even"
    else:
        return "Odd"
