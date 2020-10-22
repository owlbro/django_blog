#from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Post
from django.utils import timezone


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def dashboard(request):
    last_posts = Post.objects.filter(author_id = request.user).order_by('-published_date')[:5]
    return render(request, 'dashboard.html', {'last_posts' : last_posts})

"""def dashboard_edit(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save(commit=False)
            profile_form.save(commit=False)
            user.save()
            userprofile.save()
            return redirect('dashboard')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=userprofile)
    return render(request, 'dashboard_edit.html', {'user_form': user_form, 'profile_form': profile_form})"""