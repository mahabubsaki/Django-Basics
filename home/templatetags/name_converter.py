from django import template
from  django.template.loader import get_template

register = template.Library()

def name_converter(value,arg):
    if arg == 'reverse':
        nameArr = value.split()
        nameArr.reverse()
        rev = ' '.join(nameArr)
        return rev
    
def demo():
    names = [{'name':'saki'},{'name':'mahabub'}]
    return {'names':names}


demo_template = get_template("custom/list.html")
register.filter('name_converter',name_converter)
register.inclusion_tag(demo_template)(demo)