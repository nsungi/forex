
from django.urls import path
from .views import (
                        HomeView, ChartView, AboutView, TermsView, ServicesView, PricingView, 
                        FundamentalView, SignUpView, LoginView, LogoutView, PschologyView,
                        AnalysisView, AnalysisCreateView,
                        RiskView, RiskCreateView, TrickView, TrickCreateView, 
                        FundamentalCreateView,PschologyCreateView, PairCreateView, ImageUploadCreateView,
                        TechnicalView, TechnicalCreateView, PairView,
                        LevarageView, NewsView, BankView,  PolicyView, QuestionView, ContactView,
                        )
                            

urlpatterns = [
   
    path('',  HomeView.as_view(), name='home'),
    path('about/',  AboutView.as_view(), name='about'),
    path('chart/',  ChartView.as_view(), name='chart'),
    path('terms/',  TermsView.as_view(), name='terms'),
    path('services/',  ServicesView.as_view(), name='services'),
    path('pricing/',  PricingView.as_view(), name='pricing'),
    path('levarage/',  LevarageView.as_view(), name='levarage'),
    path('news/',  NewsView.as_view(), name='market_news'),
    path('bank/',  BankView.as_view(), name='bank'),
    path('policy/',  PolicyView.as_view(), name='policy'),
    path('question/',  QuestionView.as_view(), name='question'),
    path('contact/',  ContactView.as_view(), name='contact'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
   
    
     # Paths for ImageUpload
    path('image_upload/create/', ImageUploadCreateView.as_view(), name='image_upload_create'),
    
    # Paths for Fundamental
    path('fundamental/',  FundamentalView.as_view(), name='fundamental'),
    path('fundamental/create/', FundamentalCreateView.as_view(), name='fundamental_create'),
    
    # Paths for Pschology
    path('pschology/',  PschologyView.as_view(), name='pschology'),
    path('pschology/create/', PschologyCreateView.as_view(), name='pschology_create'),
    
    # Paths for Pair
    path('pair/',  PairView.as_view(), name='pair'),
    path('pair/create/', PairCreateView.as_view(), name='pair_create'),
    
    
    
    # Paths for analysis
    path('analysis/',  AnalysisView.as_view(), name='analysis'),
    path('analysis/create/', AnalysisCreateView.as_view(), name='analysis_create'),
    
    
      # Paths for risk
    path('risk/',  RiskView.as_view(), name='risk'),  
    path('risk/create/', RiskCreateView.as_view(), name='risk_create'),
    
    
    # Paths for Trick and tips
    path('trick/',  TrickView.as_view(), name='trick'),  
    path('trick/create/', TrickCreateView.as_view(), name='trick_create'),
    
    
    # Paths for technical
    path('technical/',  TechnicalView.as_view(), name='technical'),  
    path('technical/create/', TechnicalCreateView.as_view(), name='technical_create'),
    
    
]