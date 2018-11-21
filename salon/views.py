# coding=utf-8
import json
from datetime import datetime
from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *
from dal_select2.views import Select2QuerySetView
from django.http import HttpResponse


class ContactAjaxFormView(generic.FormView):
    form_class = ContactModelForm
    template_name = 'ajax-form.html'

    def post(self, request, *args, **kwargs):
        contact = self.form_class(request.POST)
        if contact.is_valid():
            contact.save(commit=False)
            contact.created = datetime.now()
            contact.save()
            # contact.send_email()
            response_data = {"message": "Спасибо, что выбрали нас. Мы скоро с ваит свяжимся."}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        return self.form_invalid(contact)

    def form_invalid(self, form):
        errors = form.errors
        errors = json.dumps(errors)
        return HttpResponse(errors, content_type="application/json")


class SubCategorySelect2(Select2QuerySetView):
    model = SubCategory
    model_field_name = 'title'

    def get_queryset(self):
        qs = super(SubCategorySelect2, self).get_queryset()
        category = self.forwarded.get('category', None)
        if category:
            qs = qs.filter(category_id=category)
        return qs


class Home(generic.FormView):
    template_name = 'index.html'
    form_class = ContactModelForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['image_list'] = ImageCard.objects.all()
        context['instagram_links'] = InstagramLink.objects.all()
        context['categories'] = Category.objects.all().order_by("-id")
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
