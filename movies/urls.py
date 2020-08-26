from django.urls import path
from . import view2
app_name="movies"

urlpatterns =[
    path('', view2.main, name="main"),
    path('moviePickUp/', view2.moviePickUp, name="pickup"),
    path('search/', view2.search, name="search"),
    path('<int:id>/', view2.detail, name="detail"),
    path('<int:id>/comment/create/',view2.commentCreate, name="commentCreate"),
    path('<int:id>/comments/<int:comment_id>/delete/', view2.commentDelete, name='commentDelete'),
    path('<int:id>/score/create/',view2.scoreCreate, name="scoreCreate"),
    path('person/', view2.person, name="person"),
]