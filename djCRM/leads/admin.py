from django.contrib import admin
from leads.models import User, Agent, Lead

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    model: User


class AgentAdmin(admin.ModelAdmin):
    model: Agent


class LeadAdmin(admin.ModelAdmin):
    model: Lead


admin.site.register(User, UserAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Lead, LeadAdmin)
