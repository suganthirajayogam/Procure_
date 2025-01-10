from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from procure_app.models import Project
import json

@csrf_exempt
def webhook(request):
    try:
        data = json.loads(request.body)
        action = data.get("action")
        resource_id = data.get("resource_id")
        resource_name = data.get("resource_name")

        if action == "create":
            Project.objects.create(project_id=resource_id, name=resource_name)
        elif action == "update":
            project = Project.objects.get(project_id=resource_id)
            project.name = resource_name
            project.save()
        elif action == "delete":
            Project.objects.filter(project_id=resource_id).delete()

        return JsonResponse({"message": "Webhook processed successfully"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
