from django.urls import path
from .views import donation, donationlist, singledonation, newdonation, submitDonation
from .views import donation,projectslist,projectdetail,newproject,editproject,deleteproject

urlpatterns = [
    path('donation', donation, name="donation"),
    path('donationlist', donationlist, name="donationlist"),
    path('singledonation/<int:id>', singledonation, name="singledonation"),
    path('newdonation', newdonation, name="newdonation"),
    path('donate/<int:id>', submitDonation, name="submit_donation"),
    path('projectslist', projectslist, name="projectslist"),
    path('projectdetail/<int:id>', projectdetail, name="projectdetail"),
    path('newproject', newproject, name="newproject"),
    path('editproject/<int:id>', editproject, name="editproject"),
    path('deleteproject/<int:id>', deleteproject, name="deleteproject"),

]
