from django.urls import path
from leads import views

app_name = "leads"

urlpatterns = [
    path("", views.lead_list, name="leads-list"),
    path("detail/<int:id>", views.lead_detail, name="leads-detail"),
    path("create/", views.lead_create, name="lead-create"),
    # path("update_lead/<int:id>", views.lead_update, name="lead-update"),
    path("detail/<int:pk>/update", views.lead_update, name="lead-update"),
    path("detail/<int:pk>/delete", views.lead_delete, name="lead-delete"),
]
