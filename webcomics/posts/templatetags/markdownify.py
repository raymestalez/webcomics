# markdownify
from django import template
import markdown
 
register = template.Library()
 
@register.filter
def markdownify(text):
    html = markdown.markdown(text)
    if html:
        return "<br/>"+html+"<br/>"
    else:
        return ""
