
from django.urls import path
from .views import (
                        HomeView, ChartView, AboutView, TermsView, ServicesView, PricingView, 
                        FundamentalView, SignUpView, LoginView, LogoutView, PschologyView, FundamentalUpdateView,
                        AnalysisView, AnalysisCreateView, AnalysisUpdateView, AnalysisDeleteView,
                        RiskView, RiskCreateView, RiskUpdateView, RiskDeleteView, TrickView, TrickCreateView, 
                        FundamentalCreateView,PschologyCreateView, PairCreateView, ImageUploadCreateView,
                        TrickUpdateView, TrickDeleteView, TechnicalView, TechnicalCreateView, TechnicalUpdateView, 
                        TechnicalDeleteView,  ImageUploadUpdateView, ImageUploadDeleteView,  PairDeleteView,
                        FundamentalDeleteView, PschologyUpdateView, PschologyDeleteView, PairUpdateView, PairView,
                        LevarageView, NewsView, BankView, PolicyView, QuestionView, ContactView,
                        NotificationView, SendNotificationView, MessageView,SendMessageView)
                            

urlpatterns = [
   
    path('',  HomeView.as_view(), name='index'),
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
    
    path('notifications/', NotificationView.as_view(), name='notification_list'),
    path('notify/', SendNotificationView.as_view(), name='notify'),
    path('send-message/<int:recipient_id>/', SendMessageView.as_view(), name='send_message'),
    path('messages/', MessageView.as_view(), name='message_list'),
    
  
    
    
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
   
    
    
     # Paths for ImageUpload
    path('image_upload/create/', ImageUploadCreateView.as_view(), name='image_upload_create'),
    path('image_upload/<int:pk>/update/', ImageUploadUpdateView.as_view(), name='image_upload_update'),
    path('image_upload/<int:pk>/delete/', ImageUploadDeleteView.as_view(), name='image_upload_delete'),

    # Paths for Fundamental
    path('fundamental/',  FundamentalView.as_view(), name='fundamental'),
    path('fundamental/create/', FundamentalCreateView.as_view(), name='fundamental_create'),
    path('fundamental/<int:pk>/update/', FundamentalUpdateView.as_view(), name='fundamental_update'),
    path('fundamental/<int:pk>/delete/', FundamentalDeleteView.as_view(), name='fundamental_delete'),

    # Paths for Pschology
    path('pschology/',  PschologyView.as_view(), name='pschology'),
    path('pschology/create/', PschologyCreateView.as_view(), name='pschology_create'),
    path('pschology/<int:pk>/update/', PschologyUpdateView.as_view(), name='pschology_update'),
    path('pschology/<int:pk>/delete/', PschologyDeleteView.as_view(), name='pschology_delete'),

    # Paths for Pair
    path('pair/',  PairView.as_view(), name='pair'),
    path('pair/create/', PairCreateView.as_view(), name='pair_create'),
    path('pair/<int:pk>/update/', PairUpdateView.as_view(), name='pair_update'),
    path('pair/<int:pk>/delete/', PairDeleteView.as_view(), name='pair_delete'),
    
    
    
    
    # Paths for analysis
    path('analysis/',  AnalysisView.as_view(), name='analysis'),
    path('analysis/create/', AnalysisCreateView.as_view(), name='analysis_create'),
    path('analysis/<int:pk>/update/', AnalysisUpdateView.as_view(), name='analysis_update'),
    path('analysis/<int:pk>/delete/', AnalysisDeleteView.as_view(), name='analysis_delete'),
    
    
      # Paths for risk
    path('risk/',  RiskView.as_view(), name='risk'),  
    path('risk/create/', RiskCreateView.as_view(), name='risk_create'),
    path('risk/<int:pk>/update/', RiskUpdateView.as_view(), name='risk_update'),
    path('risk/<int:pk>/delete/', RiskDeleteView.as_view(), name='risk_delete'),
    
    
    # Paths for Trick and tips
    path('trick/',  TrickView.as_view(), name='trick'),  
    path('trick/create/', TrickCreateView.as_view(), name='trick_create'),
    path('trick/<int:pk>/update/', TrickUpdateView.as_view(), name='trick_update'),
    path('trick/<int:pk>/delete/', TrickDeleteView.as_view(), name='trick_delete'),
    
    
    # Paths for technical
    path('technical/',  TechnicalView.as_view(), name='technical'),  
    path('technical/create/', TechnicalCreateView.as_view(), name='technical_create'),
    path('technical/<int:pk>/update/', TechnicalUpdateView.as_view(), name='technical_update'),
    path('technical/<int:pk>/delete/', TechnicalDeleteView.as_view(), name='technical_delete'),
    
    
]