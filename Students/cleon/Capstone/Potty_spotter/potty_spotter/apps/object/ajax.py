import datetime
import itertools
from datetime import timedelta
from django.http import JsonResponse
from django.db.models import Count, Q, Sum
from django.db.models.functions import Coalesce
from django.db.utils import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy
from potty_spotter.apps.object import models as models_object


@login_required(login_url=reverse_lazy("auth_login"))
@require_http_methods(["POST"])
@permission_required("object.change_restroom")
def update_restroom_status(request):
    
    pk = int(request.POST.get("pk"))
    status = int(request.POST.get("status"))

    valid_statuses = [key for key, value in dict(
        models_object.Restroom.StatusChoices.choices).items()]
    if status not in valid_statuses:
        return JsonResponse(
            {"success": False, "status_message": "Invalid Status Input"}
        )

    if pk is not None:
        try:
            obj = models_object.Restroom.objects.get(pk=pk)
            obj.status = status
            obj.save()

            return JsonResponse(
                {
                    "success": True,
                    "status_message": "Status has been updated successfully.",
                }
            )
        except models_object.Restroom.DoesNotExist:
            return JsonResponse(
                {"success": False, "status_message": "Record doesn't exists"}
            )

    return JsonResponse({"success": False})
