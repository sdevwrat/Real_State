from django.shortcuts import redirect, render
from django.urls.conf import path
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=request.user.id)
            if has_contacted:
                messages.error(request,'You have already made Inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)

        contact.save()

        """send_mail(
            'property listing inquiry',
            'there has been an inquiry for ' + listing + '.Sign into admin panel for more info',
            'drivemovies.32@gmail.com',
            [realtor_email],
            fail_silently=False
        )"""

        messages.success(request,'Your request has been submitted')
    return redirect('/listings/'+listing_id)