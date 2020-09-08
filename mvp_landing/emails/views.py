from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, Http404
# Create your views here.
from .models import EmailEntry
from .forms import EmailEntryForm, EmailEntryUpdateForm


# two types of view 1-function based view, 2.- class based ]
# @login_required
@staff_member_required(login_url='/login')
def email_entry_get_view(request, id=None, *args, **kwargs):
    # '''if not request.user.is_staff:
    # 	return render(request,'page_not_found.html')'''
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404
    # return HttpResponse(f"<h1> hello {obj.email} </h1>")
    return render(request, "get.html", {'object': obj, 'email': 'xyz@gmail.com'})


# def email_entry_list_view(request,*args,**kwargs):
# 	return

def email_entry_create_view(request, *args, **kwargs):
    context = {}
    if request.user.is_authenticated:
        context['some_cool_stuff'] = "whatever"
    print(request.user, request.user.is_authenticated)
    # if request.method == "POST":
    # 	print(dict(request.POST))
    # initialize the form
    form = EmailEntryForm(request.POST or None)
    context['form'] = form
    # validation for valid input
    if form.is_valid():
        '''
        obj = form.save(commit=False)# Model Instance
        obj.name= "shovan"
        obj.save()
        '''
        form.save()
        # reinitialize the form
        form = EmailEntryForm()
    return render(request, "form.html", context)


@staff_member_required(login_url='/login')
def email_entry_list_view(request, id=None, *args, **kwargs):
    qs = EmailEntry.objects.all()  # filter(email__icontains='abc')

    return render(request, "emails/list.html", {'object_list': qs})


@staff_member_required(login_url='/login')
def email_entry_update_view(request, id=None, *args, **kwargs):
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404
    form = EmailEntryUpdateForm(request.POST or None, instance=obj)
    if form.is_valid():
        updated_obj = form.save()
        return redirect(f"/email/{updated_obj.id}")
    return render(request, "emails/update.html", {'object': obj, "form": form})


@staff_member_required(login_url='/login')
def email_entry_destroy_view(request, id=None, *args, **kwargs):
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        # field_1 == 'delete me'
        obj.delete()  # it delete the items from the database
        return redirect("/")

    return render(request, "emails/destroy.html", {'object': obj})
