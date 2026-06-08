from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactSerializer

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

@api_view(['GET', 'POST'])
def api_contacts(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def api_contact_detail(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)