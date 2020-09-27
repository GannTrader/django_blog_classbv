from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, PasswordChangeForm, \
    PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, CreateView


class EditLoginView(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Username or Email...'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'class': 'form-control', 'placeholder': 'Password...'}),
    )


class SiteLoginView(LoginView):
    form_class = EditLoginView
    template_name = "registration/login.html"


class SiteLogoutView(LogoutView):
    template_name = "registration/logout.html"


class ProfileView(TemplateView):
    template_name = "profile.html"


class EditRegisterView(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

        widgets = {
            "username": forms.TextInput(attrs=({
                'class': 'form-control',
                'placeholder': 'Username...'
            })),
            "email": forms.TextInput(attrs=({
                'class': 'form-control',
                'placeholder': 'Email...'
            })),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password...'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password...'})


class SiteRegisterView(CreateView):
    form_class = EditRegisterView
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


# Xử lý trường hợp quên mật khẩu
class EditPasswordResetView(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email...'})

class SitePasswordResetView(PasswordResetView):
    form_class = EditPasswordResetView
    template_name = "passwordReset/password-reset.html"
    email_template_name = "passwordReset/email-body.html"
    success_url = reverse_lazy('password-reset-done')


class SitePasswordResetDoneView(PasswordResetDoneView):
    template_name = "passwordReset/password-reset-done.html"


class SitePasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "passwordReset/password-reset-confirm.html"
    success_url = reverse_lazy('password-reset-complete')


class SitePasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "passwordReset/password-reset-complete.html"


# Xử lý trường hợp đổi mật khẩu
class EditPasswordChangeView(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Old password...'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New password...'})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirm new password...'})


class SitePasswordChangeView(PasswordChangeView):
    form_class = EditPasswordChangeView
    template_name = "passwordReset/password-change.html"
    success_url = reverse_lazy("change-password-done")


class SitePasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "passwordReset/password-change-done.html"
