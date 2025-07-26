from django import template

register = template.Library()

@register.filter(name='add_attr')
def add_attr(field, attr):
    attrs = {}
    for atribute in attr.split(','):
        key, value = atribute.split(':')
        attrs[key] = value
    return field.as_widget(attrs=attrs)
