from django.template import Library
from django.template.defaulttags import firstof as _firstof

register = Library()

@register.tag
def firstof(*args, **kwargs):
    return _firstof(*args, **kwargs)