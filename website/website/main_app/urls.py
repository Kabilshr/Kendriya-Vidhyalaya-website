from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("Principal's_Message",views.principal_message,name="principal_message"),
    path("About_KV",views.about_kv,name="about_kv"),
    path("Contact_us",views.contact_us,name="contact_us"),
    path("Holidays",views.holidays,name="holidays"),
    path("TC_issued",views.tc_issued,name="tc_issued"),
    path("VMC_members",views.vmc_members,name="vmc_members"),
    path("Committees",views.committees,name="committees"),
    path("Notice",views.notice,name="notice"),
    path("News_and_Events",views.news_and_events,name="news_and_events"),
    path("Class_1",views.class_1,name="class_1"),
    path("Class_11",views.class_11,name="class_11"),
    path("Other_Class",views.other_class,name="other_class"),
    path("Alumni",views.alumni,name="alumni"),
    path("Achievements",views.achievements,name="achievement"),
    path("NewsLetter",views.newsletter,name="newsletter"),
    path("Members_List",views.members_list,name="members_list"),
    path("Vacancy",views.vacancy,name="vacancy"),
    path("Gallery",views.gallery,name="gallery"),
    path("Fee_Structure",views.fees,name='fees'),
    path("News_and_Events/<int:pk>",views.show_event,name='show_event'),
]