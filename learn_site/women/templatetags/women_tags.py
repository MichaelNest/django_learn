from django import template
from women.models import Women, Category

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()

