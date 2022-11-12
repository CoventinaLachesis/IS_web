from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token
from django.contrib.auth import get_user_model
from django.db.models import Q
User = get_user_model()

from IS import settings  # type: ignore

import os
from twilio.rest import Client


# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        phone=request.POST['phone']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist! Plase try some either")
            return redirect('home')
        if User.objects.filter(email=email):
            messages.error(request,"Email already exist! Plase try some either")
            return redirect('home')
        if User.objects.filter(phone_number=phone):
            messages.error(request,"Phone already exist! Plase try")
            return redirect('home')
        if len(username)>10:
            messages.error(request,"Username must be under 10 characters")
        if pass1!=pass2:
            messages.error(request,"Passwords didn't match")
        if not  username.isalnum():
            messages.error(request,"Username must be alphanumeric")
            return redirect('home')

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=username
        myuser.phone_number=phone
        myuser.is_active=False
        myuser.save()

      
        messages.success(request,"Your accout has been successfully created")
        #email
        subject="Welcom to XXX Resturant"
        message="Hello "+myuser.first_name+"!! You accout has been created \n Pleace confirm email to active"
        from_email = settings.EMAIL_HOST_USER
        to_list=[myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)

        #Email confirmation maill
        current_site=get_current_site(request)
        email_subject="Confirm your email "
        message2=render_to_string("email_Confirmation.html",{
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token':generate_token.make_token(myuser)
            })
        email=EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently=True
        email.send()
        


        return redirect('home')
    return render(request,"authentication/signup.html")


def signin(request):
    if request.method == 'POST':
        email_phone=request.POST['Email_or_phone']
        pass1=request.POST['pass1']
        try:
            user = User.objects.get(
                    Q(email=email_phone) | Q(phone_number=email_phone)
                )
            pwd_valid = user.check_password(pass1)
            if pwd_valid:            
                pass
            else:
                messages.error(request,"Bad Credentials")
                return redirect('home')
            
            if user is not None:    
                user=authenticate(username=user.username,password=pass1)
            
                login(request,user)
                fname=user.first_name
                return render(request,"authentication/index.html",{'fname':fname})
            else:
                
                return redirect('home')
        except:
            messages.error(request,"Bad Credentials")
            return redirect('home')
            
    return render(request,"authentication/index.html")


def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('home')


    
def activate(request,uidb64,token):
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        myuser=User.objects.get(pk=uid)
    except (TypeError, ValueError,OverflowError,User.DoesNotExist):
        myuser= None
    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active=True
        myuser.save()
        login(request,myuser)
        return redirect('home')
    else:
        return render(request,"activation_failed.html")

def forget(request):
    if request.method == "POST":
        #Email reset password maill
        if request.POST["email"] :
            email = request.POST["email"]
            myuser=User.objects.get(email=email)
            current_site=get_current_site(request)
            email_subject="Reset your account password "
            message2=render_to_string("email_setnewpassword.html",{
                'name': myuser.first_name,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
                'token':generate_token.make_token(myuser)
                })
            email=EmailMessage(
                email_subject,
                message2,
                settings.EMAIL_HOST_USER,
                [myuser.email],
            )
            email.fail_silently=True
            email.send()
        """
        elif request.POST["phone"] :
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            verify_sid = 'YOUR_VERIFY_SID'
            client = Client(account_sid, auth_token)

            verification = client.verify.services(
            'verifySid'
            ).verifications.create(to='+66952540422', channel='sms')

            print(verification.status)
            otp_code = input("Please enter the OTP:")

            verification_check = client.verify.services(
            'verifySid'
            ).verification_checks.create(to='+66952540422', code=otp_code)

            print(verification_check.status)
        """

        return redirect('home')
    return render(request,"authentication/forget.html")



def setnewpassword(request,uidb64,token):
    if request.method == 'POST':
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            myuser=User.objects.get(pk=uid)
        except (TypeError, ValueError,OverflowError,User.DoesNotExist):
            myuser= None
        if myuser is not None and generate_token.check_token(myuser,token):
            new_password=request.POST["password1"]
            confirm_password=request.POST["password2"]
            if(new_password==confirm_password):
                myuser.set_password(new_password)
                myuser.save()
                login(request,myuser)
                return redirect('home')
        else:
            return render(request,"authentication/setnewpassword.html")
    return render(request,"authentication/setnewpassword.html")

def pdpa(request):
    return render(request,"authentication/pdpa.html")



    