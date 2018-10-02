#sites/urls.py

from django.urls import path
from sites import views

urlpatterns = [
    path('', views.home, name='sites-home'),

    path('AboutUs/', views.AboutPageView.as_view(), name='sites-about'),
    path('Contact/', views.ContactPageView.as_view(), name='sites-contact'),
    path('Consultants/', views.ConsultantsPageView.as_view(), name='sites-consultants'),
    path('Companies/', views.CompaniesPageView.as_view(), name='sites-companies'),
    path('Education/', views.EducationPageView.as_view(), name='sites-education'),
    path('Events/', views.EventsPageView.as_view(), name='sites-events'),
    path('Groups/', views.GroupsPageView.as_view(), name='sites-groups'),

]
