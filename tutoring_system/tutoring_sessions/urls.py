from django.urls import path
from .views import CreateUserView, CreateSessionView, ListSessionsView, UserListSessionsView, BookSessionView, CustomAuthToken
# from .views import CustomUserPasswordListView
urlpatterns = [
    path('admin/create-user/', CreateUserView.as_view(), name='admin-create-user'),
    path('admin/create-session/', CreateSessionView.as_view(), name='admin-create-session'),
    path('admin/list-sessions/', ListSessionsView.as_view(), name='admin-list-sessions'),
    path('user-list-sessions/', UserListSessionsView.as_view(), name='user-list-sessions'),
    path('book-session/', BookSessionView.as_view(), name='book-session'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    # path('customusers/passwords/', CustomUserPasswordListView.as_view(), name='customuser-password-list'),
]
