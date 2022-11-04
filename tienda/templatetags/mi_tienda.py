from django import template
register = template.Library()

@register.filter(name="en_pedido")
def en_pedido(producto, el_pedido):
    keys=el_pedido.keys()
    for id in keys:
        if int(id)==producto.id:
            return True
    return False
