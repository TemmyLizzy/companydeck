from django.conf.urls import include, url

from company import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ResultsView, PageView
from .views import HomePageView, SearchResultsView



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sign_in/$', views.user_sign_in, name='sign_in'),
    url(r'^forget/$', views.forget, name='forget'),
    url(r'^employer/$', views.employer_page, name='employer_page'),
    url(r'^job/$', views.job_search, name='job_search'),
    url(r'^review/$', views.company_review, name='company_review'),
    url(r'^employ_form/$', views.employ_form, name='employ_form'),
    url(r'^employ_form2/$', views.employ_form2, name='employ_form2'),
    url(r'^employ_form3/$', views.employ_form3, name='employ_form3'),

    path('jobs/', ResultsView.as_view(), name='job_production'),
    path('jobs1/', PageView.as_view(), name='job1'),

    path('oauth/', include('social_django.urls', namespace='social')),

    path('company_search/', SearchResultsView.as_view(), name= 'search_production'),


    path('review1/', HomePageView.as_view(), name='review1'),

    path('login/', auth_views.LoginView.as_view(
        template_name = 'accounts/login.html'),
        name = 'login'), 




    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password/password_reset.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_sent.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_form.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_done.html"), name="password_reset_complete")

]