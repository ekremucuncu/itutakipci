from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name='distribution'

urlpatterns=[
    path('',views.Index.as_view(),name='home'),
    path('hocalar/<slug:slug>/',views.LecturerDistribution.as_view(),name='lecturer_distribution'),
    path('dersler/<slug:slug>/',views.LectureDistribution.as_view(),name='lecture_distribution'),
]



urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
