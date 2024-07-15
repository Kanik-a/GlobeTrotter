"""
Definition of urls for Skysearch.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from app.views import CheckoutView, callanalyticsView, MyBookingsView, hoteloptions, flightcall, flightdetails,flightfinal, booking_details,cancel_booking,cancel_flight_booking,hotel_options,hotel_options_sort


urlpatterns = [path('', views.home, name='home'),
    path('signup/',views.signup.as_view(), name='signup'),
    path('signin/',views.signin, name='signin'),
    path('mybookings/', views.MyBookingsView.as_view(), name='mybookings'),
    path('cancel/', views.MyBookingsView.as_view(), name='cancel'),
    path('hotel_options/', views.hoteloptions.as_view(), name='hotel_options'),
    path('room/', views.room, name='room'),
    path('roomselect/', views.roomselect, name='roomselect'),
    path("logout", views.logout_request, name= "logout"),
    path("roomconfirmed", views.roomconfirmed, name= "roomconfirmed"),
    path("roomselect", views.roomselect, name= "roomselect"),
    path("CheckoutView", views.CheckoutView.as_view(), name= "checkout"),
    path("final", views.final, name= "final"),
    path("analytics", views.analytics, name= "analytics"),
    path("callanalyticsView", views.callanalyticsView.as_view(), name= "callanalytics"),
    path("callmergesort", views.callmergesort.as_view(), name= "callmergesort"),
    path('flightcall', views.flightcall.as_view(), name='flightcall'),
    
    path('flightbookingdetails', views.flightbookingdetails.as_view(), name='flightbookingdetails'),
    path('flightcheckout', views.flightcheckout.as_view(), name='flightcheckout'),
    ]