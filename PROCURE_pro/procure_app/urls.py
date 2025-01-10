from django.urls import path
from procure_app.views import import_projects, webhook

urlpatterns = [
    path("import-projects/<int:company_id>/", import_projects, name="import_projects"),
    path("webhook/", webhook, name="webhook"),
]
