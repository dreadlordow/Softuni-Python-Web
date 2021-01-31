from django import template

register = template.Library()

@register.inclusion_tag('templates_advanced/tags/bootstrap_form.html')
def bootstrap_form(form, action, method):

    for (_,field) in form.fields.items():
        if 'class' in field.widget.attrs:
            field.widget.attrs['class'] += ' form-control'
        else:
            field.widget.attrs['class'] = 'form-control'

    return{
        'form': form,
        'action': action,
        'method': method,
    }