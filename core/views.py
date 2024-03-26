
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.views import View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import ( ImageUpload, TextUpload, Course, 
                     Technical, Fundamental, Risk, Analysis, Trick, Pschology, Pair
                     )

from .forms import (SignUpForm, LoginForm, ImageUploadForm, TextUploadForm, CourseForm, 
                    TechnicalForm, FundamentalForm, RiskForm, AnalysisForm, 
                    TrickForm, PschologyForm, PairForm)




#home page
class HomeView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


#page displaying live chart
class ChartView(View):
    template_name = 'chart.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class AboutView(View):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class TermsView(View):
    template_name = 'terms_condition.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
class ServicesView(View):
    template_name = 'services.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class PricingView(View):
    template_name = 'pricing.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)   
    
    
class LevarageView(View):
    template_name = 'levarage.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class NewsView(View):
    template_name = 'market_news.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ContactView(View):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)



class QuestionView(View):
    template_name = 'question.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)



class PolicyView(View):
    template_name = 'privacy.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)



class BankView(View):
    template_name = 'bank.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

        
#user registration view
class SignUpView(View):
    template_name = 'signup.html'
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. You are now registered.')
            return redirect('login')  # Success page
        else:
            messages.error(request, 'Error in registration. Please check the form.')
            return render(request, self.template_name, {'form': form})


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')  # the URL to redirect to after login

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'Login successful.')
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Invalid username or password.')
            return self.form_invalid(form)


class LogoutView(FormView):
    template_name = 'logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(self.request, 'You have been successfully logged out.')
        return redirect('login')  # Update with the URL you want to redirect to after logout


# uploading images 
@method_decorator(login_required, name='dispatch')
class ImageUploadCreateView(CreateView):
    model = ImageUpload
    form_class = ImageUploadForm
    template_name = 'image_upload_form.html'
    success_url = reverse_lazy('success')  # Redirect to a success page


#create a course
@method_decorator(login_required, name='dispatch')
class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_form.html'
    success_url = reverse_lazy('success')  # Redirect to a success page
 
#upload text
@method_decorator(login_required, name='dispatch')
class TextUploadCreateView(CreateView):
    model = TextUpload
    form_class = TextUploadForm
    template_name = 'text_upload_form.html'
    success_url = reverse_lazy('success')  # Redirect to a success page


#fundamental page & success page
class FundamentalView(View):
    template_name = 'fundamental.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


# create fundamental class
@method_decorator(login_required, name='dispatch')
class FundamentalCreateView(CreateView):
    model = Fundamental
    form_class = FundamentalForm
    template_name = 'fundamental_form.html'
    success_url = reverse_lazy('success')  # Redirect to a success page
    
     

#Pschology page & success page
class PschologyView(View):
    template_name = 'pschology.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


#  Pschology class
@method_decorator(login_required, name='dispatch')
class PschologyCreateView(CreateView):
    model = Pschology
    form_class = PschologyForm
    template_name = 'pschology_form.html'
    success_url = reverse_lazy('success')  # Redirect to a success page



#Pair page & success page
class PairView(View):
    template_name = 'pair.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


# Pair class
@method_decorator(login_required, name='dispatch')
class PairCreateView(CreateView):
    model = Pair
    form_class = PairForm
    template_name = 'pair_form.html'
    success_url = reverse_lazy('success')  # Redirect to a success page




#Technical page & success page
class TechnicalView(View):
    template_name = 'technical.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


#Technical class
@method_decorator(login_required, name='dispatch')
class TechnicalCreateView(CreateView):
    model = Technical
    form_class = TechnicalForm
    template_name = 'technical.html'
    success_url = reverse_lazy('technical')  # Redirect to a success page


#Risk page & success page
class RiskView(View):
    template_name = 'risk.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


# create Risk class
@method_decorator(login_required, name='dispatch')
class RiskCreateView(CreateView):
    model = Risk
    form_class = RiskForm
    template_name = 'risk_form.html'
    success_url = reverse_lazy('success')  # Redirect to a success page

 
#Trickpage & success page
class TrickView(View):
    template_name = 'trick.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


# create Trick class
@method_decorator(login_required, name='dispatch')
class TrickCreateView(CreateView):
    model = Trick
    form_class = TrickForm
    template_name = 'trick.html'
    success_url = reverse_lazy('success')  # Redirect to a success page


#Analysis & success page
class AnalysisView(View):
    template_name = 'analysis.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


# create Analysis class
@method_decorator(login_required, name='dispatch')
class AnalysisCreateView(CreateView):
    model = Analysis
    form_class = AnalysisForm
    template_name = 'analysis_form.html'
    success_url = reverse_lazy('success')  # Redirect to a success page
