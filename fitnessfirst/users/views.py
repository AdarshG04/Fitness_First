from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from users.forms import SignupForm, AccountAuthenticationForm
from users.models import User
from program.models import MembershipPlan
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
import stripe



def index(request):
    return render(request,"app/index.html")



def login_view(request):
    user = request.user
    if request.user.is_authenticated: 
        return redirect("index")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                messages.success(request, 'Logged in Sucessfully!!')
                return redirect("index")
            else:
                messages.error(request, 'Invalid email or password. Please try again.')


        else:
            messages.error(request, 'There was an error with your login details. Please correct the fields below.')

    else:
        form = AccountAuthenticationForm()

    return render(request, 'registration/login.html', {'login_form':form})



def logout_view(request):
    logout(request)
    messages.success(request, ' Logged out Sucessfully!')
    return redirect("index")



def signup_view(request):
    user = request.user

    if user.is_authenticated:
        return redirect('index')
    
    context = {}
    if request.POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            context['signup_form'] = form

    else:
        form = SignupForm()
    
    return render(request, 'registration/login.html', {'signup_form':form})



def password_reset_request(request):
    current_site = get_current_site(request)
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = 'Password Reset Requested'
                    email_template_name = 'password/password_reset_email.txt'
                    c = {
                        "email":user.email,
                        'domain':current_site,
                        'site_name': 'FitnessFirst',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    admin_email = settings.EMAIL_HOST_USER
                    try:
                        send_mail(subject, email, admin_email , [user.email], fail_silently=False)
                    except BadHeaderError:
                        messages.error(request, 'Something went wrong!!')

                    url = request.META.get('HTTP_REFERER')
                    messages.success(request,"We've emailed you instructions for setting your password, if an account exists with the email you entered. You should receive them shortly.If you don't receive an email, please make sure you've entered the address you registered with, and check your spam folder.")
                    return redirect (url)
            
            messages.error(request, 'Email is not registered!')
            return redirect('password_reset')

    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})





stripe.api_key=settings.STRIPE_SECRET_KEY
key1 = settings.STRIPE_PUBLISH_KEY

def process_payment(request):
    current_site = get_current_site(request)
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            amount = 200000
            
            
            stripe.PaymentIntent.create(
                amount=amount,
                currency="inr",
                payment_method_types=["card"],
            )

            email_subject = 'Order confirmed!'
            email_body = render_to_string('payment/confirm.txt', {
                'user': user,
                'domain': current_site,
                
            })

            admin_email = settings.EMAIL_HOST_USER
            try:
                send_mail(email_subject, email_body, admin_email , [user.email], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
            

    return render(request, 'payment/payment_status.html', {'user':user})
