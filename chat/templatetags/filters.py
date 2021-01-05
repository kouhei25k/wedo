import ast
from django import template  # 追記 必須
register = template.Library()  # 追記 必須


@register.filter(name="literal_eval")
def literal_eval(value, key):
    converted = ast.literal_eval(value)
    return converted[key]
# message['content'] = ast.literal_eval(message['content'])
