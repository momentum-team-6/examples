from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Note
from .forms import ContactForm, NoteForm


@login_required
def list_contacts(request):
    # use Django ORM to retrieve contacts from database for the logged in user
    contacts = Contact.objects.filter(user=request.user)
    # user = request.user
    return render(request, "contacts/list_contacts.html",
                  {"contacts": contacts})

@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if contact.user == request.user:
        form = NoteForm()
        return render(request, "contacts/contact_detail.html", {"contact": contact, "form": form})
    else:
        return render(request, "contacts/permission_denied.html")

@login_required
def add_note(request, pk):
    if request.method == 'POST':
        form = NoteForm(data=request.POST)
        contact = get_object_or_404(Contact, pk=pk)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.contact = contact
            new_note.save()
            return redirect(to='contact_detail', pk=pk)

@login_required
def add_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/add_contact.html", {"form": form})

@login_required
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'GET':
        form = ContactForm(instance=contact)
    else:
        form = ContactForm(data=request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/edit_contact.html", {
        "form": form,
        "contact": contact
    })

@login_required
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect(to='list_contacts')

    return render(request, "contacts/delete_contact.html",
                  {"contact": contact})

def make_family(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if not contact.is_family:
        contact.is_family = True
        contact.save()
    else:
        contact.is_family = False
        contact.save()

    return redirect(to='list_contacts')
