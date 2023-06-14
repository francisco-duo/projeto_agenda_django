from contact.models import Contact
from django.http import Http404
from django.shortcuts import get_object_or_404, render


def index(request, ):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    return render(
        request,
        'contact/index.html',
        {
            'contacts': contacts
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
