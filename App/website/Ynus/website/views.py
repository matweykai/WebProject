from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic
from .models import Direction
from .forms import CompanySignUpForm, CompanySignInForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView


def index(request):
    """Start page view"""
    return render(request, 'website/index.html')


def univ_info(request):
    """View for the page with university info"""
    return render(request, 'website/about_univ.html')


def project_info(request):
    """View for the page with project info"""
    return render(request, 'website/about_project.html')


def directions_view(request):
    """View for the page with all directions that university has"""
    grdnt_lst = list()  # stores colors of cells on the page
    directions = Direction.objects.all()

    grnts = ['purple_grad', 'green_grad', 'blue_grad']
    counter = 0

    for i in range(len(directions)):
        if i % len(grnts) == 0:
            counter += 1
        grdnt_lst.append(grnts[(i + counter) % 3])

    context = {'gradient_lst': grdnt_lst,
               'directions': directions}

    return render(request, 'website/directions.html', context=context)


class DirectionView(generic.DetailView):
    """View for the page with direction info"""
    model = Direction
    template_name = "website/direction_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            try:
                votes = self.request.user.company.vote_set.all()
                disciplines = [vote.discipline for vote in votes if vote.direction.name == self.get_object().name]
                context["votes"] = disciplines

            except User.company.RelatedObjectDoesNotExist:
                pass

        all_voted_companies = list()
        # Counting all votes in this direction
        print(self.get_object())
        print(self.get_object().vote_set.all())
        for vote in self.get_object().vote_set.all():
            all_voted_companies.append(vote.company.user.username)

        context['unique_votes_count'] = len(set(all_voted_companies))

        print(context['unique_votes_count'])

        return context


class SignUpView(generic.CreateView):
    """View for user registration"""
    form_class = CompanySignUpForm
    template_name = 'website/registration.html'
    success_url = reverse_lazy('main_page')


class SignInView(LoginView):
    """View for user authentification"""
    form_class = CompanySignInForm
    template_name = 'website/authorization.html'

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('main_page')


def logout_user(request):
    """View for user logging out"""
    logout(request)

    return redirect('main_page')
