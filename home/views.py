from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncMonth
from apps.users.models import User
from apps.main.models import Laboratory, Computer, Projector, Security_camera, Air_Conditioner, Regulator_voltage, Monitor, Cpu, Ram, Disk, Processor, Recommendation, Task


# Create your views here.
def dashboard_stats_view(request):
    # Aquí puedes agregar la lógica para calcular las estadísticas de tus modelos.
    # Por ejemplo, puedes contar cuántos de cada objeto hay:
    lab_count = Laboratory.objects.count()
    computer_count = Computer.objects.count()
    projector_count = Projector.objects.count()
    # ...haz esto para cada modelo que necesites...

    # Si necesitas estadísticas mensuales como en el ejemplo, necesitarás un modelo con una fecha
    # para poder hacer un TruncMonth como se hizo con Order en tu ejemplo.
    # Vamos a asumir que tienes un modelo con una fecha y repetir el patrón:
    # items_by_month = (
    #     ModeloConFecha.objects.annotate(month=TruncMonth("fecha"))
    #     .values("month")
    #     .annotate(total=Count("id"))
    #     .order_by("month")
    # )
    # months = [item["month"].strftime("%b") for item in items_by_month]
    # totals = [item["total"] for item in items_by_month]

    # Aquí asumimos que tienes un contexto que incluye usuarios y tareas como en el ejemplo:
    users_count = User.objects.count()
    tasks_count = Task.objects.count()
     # Obtener el usuario actual, asumiendo que la solicitud está autenticada
    current_user = request.user

    # Contar las computadoras asignadas al usuario
    computers_assigned_count = Computer.objects.filter(responsible_user_id=current_user).count()

    # Contar las tareas asignadas al usuario
    tasks_assigned_count = Task.objects.filter(user_id=current_user).count()
    #contar las recomendaciones hechas por el usuario
    recommendations_count = Recommendation.objects.filter(user_id=current_user).count()
    # Construye el contexto con la información que hayas reunido:
    context = {
        "lab_count": lab_count,
        "computer_count": computer_count,
        "projector_count": projector_count,
        # ...continúa agregando el resto de las cuentas que calculaste...
        "users_count": users_count,
        "tasks_count": tasks_count,
        # "items_chart_data": {
        #     "months": months,
        #     "totals": totals,
        # },
        
        'computers_assigned_count': computers_assigned_count,
        'tasks_assigned_count': tasks_assigned_count,
        'recommendations_count': recommendations_count,
        
    }

    # No renderizamos la plantilla aquí, solo devolvemos el contexto
    return context
