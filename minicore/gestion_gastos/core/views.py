from django.shortcuts import render
from .models import Gasto
from django.db.models import Sum

def filtrar_gastos(request):
    gastos = None
    total = 0
    if request.method == 'POST':
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        gastos = Gasto.objects.filter(fecha__range=[fecha_inicio, fecha_fin])
        total = gastos.aggregate(Sum('monto'))['monto__sum'] or 0
    return render(request, 'core/filtrar_gastos.html', {'gastos': gastos, 'total': total})
