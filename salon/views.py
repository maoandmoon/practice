from  datetime import datetime

from django.shortcuts import render, render_to_response
from django.utils import timezone
from django.views.generic import ListView, FormView
from .calculate import calculate_delay
from .models import *
from .forms import *


class Home(FormView):
    template_name = 'index.html'
    form_class = ContactModelForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['image_list'] = ImageCard.objects.all()
        context['price_set'] = calculate_delay()
        context['instagram_links'] = InstagramLink.objects.all()
        # context
        return context

    # TODO: AJAX
    def post(self, request, *args, **kwargs):
        contact = self.form_class(request.POST)
        if contact.is_valid():
            contact.save(commit=False)
            contact.created = datetime.now()
            contact.save()
            contact.send_email()
            return render(request, 'index.html')
        else:
            return self.form_invalid(contact)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
