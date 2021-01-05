from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Note
from .forms import ContactForm, NoteForm


# Create your views here.
def list_contacts(request):
    # use Django ORM to retrieve contacts from database
    contacts = Contact.objects.all()
    # user = request.user
    return render(request, "contacts/list_contacts.html",
                  {"contacts": contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = NoteForm()
    return render(request, "contacts/contact_detail.html", {"contact": contact, "form": form})

# Work in Progress
# we are going to change this so that the contact is detected automatically and the user doesn't have to choose
def add_note(request, pk):
    if request.method == 'POST':
        form = NoteForm(data=request.POST)
        contact = get_object_or_404(Contact, pk=pk)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.contact = contact
            new_note.save()
            return redirect(to='contact_detail', pk=pk)

def add_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/add_contact.html", {"form": form})


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


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect(to='list_contacts')

    return render(request, "contacts/delete_contact.html",
                  {"contact": contact})
