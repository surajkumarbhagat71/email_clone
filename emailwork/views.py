from django.shortcuts import render,redirect
from django.views.generic import TemplateView ,View ,DetailView
from .models import *
from .forms import *
from django.db.models import Q

# Create your views here.

class Home(TemplateView):
    template_name = 'user/home.html'


class Signup(View):
    def get(self,request,*args,**kwargs):
        form = SignupForm()
        data = {"forms":form}
        return render(request,'user/signup.html',data)

    def post(self,request,*args,**kwargs):
        form = SignupForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')


class Login(View):
    def post(self,request,*args,**kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        cond = Q(email = username) & Q(password = password)

        check = User.objects.filter(cond).count()

        if (check == 1):
            request.session['login'] = username
            return redirect('inbox')
        else:
            return redirect('home')



class Inbox(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        email_to = User.objects.get(email = request.session['login']).user_id

        data = {"inbox":Massege.objects.filter(email_to = email_to)}

        return render(request,'user/inbox.html',data)



class Sent(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        email_by = User.objects.get(email = request.session['login']).user_id
        data = {"sentmsg":Massege.objects.filter(email_by = email_by)}

        return render(request,'user/sent.html',data)


class Masseges(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')
        return render(request,'user/compose.html')

    def post(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        email_by = User.objects.get(email = request.session['login']).user_id

        emails = request.POST.get('email_to')
        subject = request.POST.get('subject')
        file = request.POST.get('file')

        data = User.objects.filter(email=emails).count()

        if (data == 1):
            email_to = User.objects.get(email=emails).user_id

            msg = Massege()
            msg.email_to = User(email_to)
            msg.email_by = User(email_by)
            msg.subject = subject
            msg.file = file
            msg.save()
            return redirect('inbox')
        else:
            return redirect('massege')


class DetailsMsg(DetailView):
    model = Massege
    template_name = 'user/details.html'


class Logout(View):
    def get(self,request):
        if request.session.has_key('login'):
            del request.session['login']
        return render(request,'user/home.html')



