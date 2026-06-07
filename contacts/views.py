from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    
    contacts = Contact.objects.all()
    context = {
        'title': 'Contact Book',
        'contacts': contacts,
        'form': form,
    }
    return render(request, 'contacts/home.html', context)

def delete_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    return redirect('home')

# def update_contact(request, pk):
#     contact = Contact.objectsbject.get(pk=pk)
#     if request.method == 'POST':
#         form = ContactForm(request.POST, instance=Contact)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = ContactForm(instance=Contact)
#     return render (request, 'contacts/update.html',{'form':form, 'contact':Contact})  

def update_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/update.html', {'form': form, 'contact': contact})
