from django import template

register = template.Library()


@register.filter('true_or_false')
def true_or_false(value):
    if value:
        return '<i class="fad fa-check-circle text-success"></i>'
    return '<i class="fad fa-times-circle text-danger"></i>'
