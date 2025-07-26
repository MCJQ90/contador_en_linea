from django import template

register = template.Library()

@register.simple_tag
def bootstrap_label(field):
    return field.label_tag(attrs={'class': 'form-label'})