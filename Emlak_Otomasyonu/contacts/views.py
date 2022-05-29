from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact (request):
    if request.method == "POST":
        listing_id = request.POST['list_id']
        listing = request.POST['listeleme']
        name = request.POST['Adı']
        email = request.POST['E-posta']
        phone = request.POST['telefone']
        message = request.POST['mesaj']
        user_id = request.POST['kullanıcı_id']
        realtor_email = request.POST['emlakçı_e-posta']


        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'Bu liste için zaten bir sorgu yaptınız')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

        contact.save()


        send_mail(
            'Mülk Listeleme Sorgulama',
            ' soruşturma açıldı ' + listing + '. Daha fazla bilgi için yönetici panelinde oturum açın.',
            'emlakçi@gmail.com',
            [realtor_email, ],
            fail_silently=False
        )

        messages.success(request, 'Talebiniz gönderildi, bir emlakçı yakında size geri dönecek.')
        return redirect('/listings/'+listing_id)