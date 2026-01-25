from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import NoteDetail, NoteListCreate

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('notes/', NoteListCreate.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetail.as_view(), name='note-detail')
]
