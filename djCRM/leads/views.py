from django.shortcuts import render, redirect
from leads.models import Lead, Agent
from leads.forms import LeadForm, LeadModelForm

# Create your views here.


def lead_list(request):
    leads = Lead.objects.all()
    context = {"leads": leads}
    return render(request, "leads/home.html", context)


def lead_detail(request, id):
    leads = Lead.objects.filter(id=id).first()
    context = {"leads": leads}
    return render(request, "leads/lead_detail.html", context)


# def lead_create(request):
#     print(request.POST)
#     if request.method == "POST":
#         # print("Post request receiving")
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             first_name = form.cleaned_data["first_name"]
#             last_name = form.cleaned_data["last_name"]
#             age = form.cleaned_data["age"]
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name=first_name, last_name=last_name, age=age, agent=agent
#             )
#             # print("Lead has been created")
#             return redirect("/leads")
#     context = {"form": Lead()}
#     return render(request, "leads/create.html", context)


""" New Lead using LeadModelForm """


def lead_create(request):
    print(request.POST)
    if request.method == "POST":
        # print("Post request receiving")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            # first_name = form.cleaned_data["first_name"]
            # last_name = form.cleaned_data["last_name"]
            # age = form.cleaned_data["age"]
            # agent = form.cleaned_data["agent"]
            # Lead.objects.create(
            #     first_name=first_name, last_name=last_name, age=age, agent=agent
            # )
            # print("Lead has been created")
            return redirect("/leads")
    context = {"form": LeadModelForm()}
    return render(request, "leads/lead_create.html", context)


# UPDATE LEAD
def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect("/leads")
    context = {"lead": lead, "form": form}
    return render(request, "leads/lead_update.html", context)


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data["first_name"]
#             last_name = form.cleaned_data["last_name"]
#             age = form.cleaned_data["age"]
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect("/leads")
#     context = {"form": form, "lead": lead}
#     return render(request, "leads/lead_update.html", context)

# Lead Delete
def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    if lead:
        lead.delete()
        return redirect("/leads")
