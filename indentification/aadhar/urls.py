from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterAPI.as_view(), name = 'register'),
    path('login', views.LoginAPI.as_view(), name = 'login'),
    path('profile/', views.Profile.as_view(), name = 'profile'),
    path('', views.AadharAPI.as_view(), name = 'aadhar'),
    path('address/',views.AddressListCreateAPI.as_view(), name = 'address-list-create'),
    path('address/id/<str:pk>/',views.AddressRetrieveUpdateDestroy.as_view(), name = 'address-retrive-update-delete'),
    path('qualification/',views.QualificationListCreateAPI.as_view(), name = 'qualification-list-create'),
    path('qualification/id/<str:pk>/',views.QualificationRetrieveUpdateDestroy.as_view(), name = 'qualification-retrive-update-delete'),
    path('bank/',views.BankListCreateAPI.as_view(), name = 'bank-list-create'),
    path('bank/id/<str:pk>/',views.BankRetrieveUpdateDestroy.as_view(), name = 'bank-retrive-update-delete'),
    path('experience/',views.ExperienceListCreateAPI.as_view(), name = 'experience-list-create'),
    path('experience/id/<str:pk>/',views.ExperienceRetrieveUpdateDestroy.as_view(), name = 'experience-retrive-update-delete'),
    path('personal/',views.PersonalDetailsListCreateAPI.as_view(), name = 'personal-list-create'),
    path('personal/id/<str:pk>/',views.PersonalDetailsRetrieveUpdateDestroy.as_view(), name = 'personal-retrive-update-delete'),
]