# First we need to register the TEMPLATE
from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This is a Doc String...
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

#register.filter('cut',cut)
