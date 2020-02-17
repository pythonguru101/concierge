from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, FormView, View
from django.urls import reverse
from django.shortcuts import get_list_or_404, redirect
from django.conf import settings

from .forms import ProfileEditForm
from .models import User


class GuestOnlyView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)

        return super().dispatch(request, *args, **kwargs)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profiles/profile.html'
    form_class = ProfileEditForm
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk', 0)
        try:
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            return None

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})


class SignUpView(GuestOnlyView, FormView):
    template_name = 'profiles/signup.html'
    form_class = ProfileEditForm
    context_object_name = 'profile'

    def form_valid(self, form):
        request = self.request
        form.save(commit=True)
        return redirect('/')
