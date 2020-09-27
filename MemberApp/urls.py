from django.urls import path
from MemberApp.views import SiteLoginView, ProfileView, SiteLogoutView, SiteRegisterView, SitePasswordResetView, \
    SitePasswordResetDoneView, SitePasswordResetConfirmView, SitePasswordResetCompleteView, SitePasswordChangeView, \
    SitePasswordChangeDoneView

urlpatterns = [
    path('login/', SiteLoginView.as_view(), name="login"),
    path('register/', SiteRegisterView.as_view(), name="register"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('logout/', SiteLogoutView.as_view(), name="logout"),

    # forgot password
    path('password-reset/', SitePasswordResetView.as_view(), name="password-reset"),
    path('password-reset/done/', SitePasswordResetDoneView.as_view(), name="password-reset-done"),
    path('password-reset/confirm/<uidb64>/<token>/', SitePasswordResetConfirmView.as_view(),
         name="password-reset-confirm"),
    path('password-reset/complete/', SitePasswordResetCompleteView.as_view(), name="password-reset-complete"),

    #change password
    path('change-password/', SitePasswordChangeView.as_view(), name="change-password"),
    path('change-password-done/', SitePasswordChangeDoneView.as_view(), name="change-password-done"),
]
