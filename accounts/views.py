#from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Post
from django.utils import timezone
from .forms import UserForm, ProfileForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def dashboard(request):
    last_posts = Post.objects.filter(author_id = request.user).order_by('-published_date')[:5]
    return render(request, 'dashboard.html', {'last_posts' : last_posts})

#@login_required
#@transaction.atomic
def dashboard_edit(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #messages.success(request, _('Ваш профиль был успешно обновлен!'))
            return redirect('dashboard')
        #else:
            #messages.error(request, _('Пожалуйста, исправьте ошибки.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'dashboard_edit.html', {'user_form': user_form, 'profile_form': profile_form})