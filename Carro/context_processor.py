def importe_total_carro(request):
    total=0.0
    if request.user.is_authenticated:
        if "carro" in request.session.keys():
                for key, value in request.session['carro'].items():
                        total=total+(float(value['price']) * value ['quantity'])
    return {'importe_total_carro': total}