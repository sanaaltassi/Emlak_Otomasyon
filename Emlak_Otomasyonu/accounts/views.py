from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


def register(request):
    if request.method == 'POST':

        first_name = request.POST['Adı']
        last_name = request.POST['Soyadı']
        username = request.POST['Kullanıcı Adı']
        email = request.POST['E-posta']
        password = request.POST['Parola']
        password2 = request.POST['Parola2']

        # Şifrelerin eşleşip eşleşmediğini kontrol etmek
        if password == password2:
           # Kullanıcı adını kontrol et
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Bu kullanıcı adı zaten kullanılıyor')
                return redirect('Kayıt ol')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'E-posta zaten var')
                    return redirect('Kayıt ol')
                else:
                    # Her şey geçti
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Kayıt olduktan sonra giriş yapın
                    user.save()
                    messages.success(request, 'Artık kayıt oldunuz ve Giriş Yapabilirsiniz')
                    return redirect('Giriş yapmak')
        else:
            messages.error(request, 'Parolalar uyuşmuyor')
            return redirect('Kayıt ol')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'İleti':
        username = request.POST['Kullanıcı adı']
        password = request.POST['Parola']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Giriş yaptınız')
            return redirect('kontrol Paneli')
        else:
            messages.error(request, 'Geçersiz kimlik bilgileri')
            return redirect('Giriş yap')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "İLETİ":
        auth.logout(request)
        messages.success(request, 'Şimdi Çıkış yaptın')
        return redirect('Giriş yap')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)
