from django.urls import path
from .views import BookListView,BookDetailView

urlpatterns=[

path('',BookListView.as_view()),
path('<uuid:pk>',BookDetailView.as_view(),name="BookDetails")

]