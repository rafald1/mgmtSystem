from django import template

register = template.Library()


@register.filter(name="add_space")
def add_space(string, step=3):
    return " ".join(string[i:i + step] for i in range(0, len(string), step))
