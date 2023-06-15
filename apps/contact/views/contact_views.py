from contact.models import Contact
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render


def index(request, ):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'contact/index.html',
        {
            'page_obj': page_obj
        }
    )


def contact(request, contact_id):
    single_contacts = get_object_or_404(
        Contact.objects, pk=contact_id, show=True
        )

    return render(
        request,
        'contact/contact.html',
        {
            'contact': single_contacts
        }
    )


def search(request, ):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'contact/index.html',
        {
            'page_obj': page_obj
        }
    )
