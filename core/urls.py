from django.contrib.auth import views as auth_views
from django.urls import include, path

from core.views import IndexView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', IndexView.as_view(), name='index'),
]


# auth_views é para fazer uso da propria view de Logout que a
# autenticação do Django proporciona para gente, sendo assim
# nao é necessário criar a nossa própria view de Logout