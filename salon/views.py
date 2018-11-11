from datetime import datetime
from django.shortcuts import render
from django.views.generic import FormView
from .calculate import calculate_delay
from .models import *
from .forms import *
from dal_select2.views import Select2QuerySetView


class SubCategorySelect2(Select2QuerySetView):
    model = SubCategory
    model_field_name = 'title'

    def get_queryset(self):
        qs = super(SubCategorySelect2, self).get_queryset()
        category = self.forwarded.get('category', None)
        if category:
            qs = qs.filter(category_id=category)
        return qs


class Home(FormView):
    template_name = 'index.html'
    form_class = ContactModelForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['image_list'] = ImageCard.objects.all()
        # context['price_set'] = calculate_delay()
        context['instagram_links'] = InstagramLink.objects.all()
        context['categories'] = Category.objects.all().order_by("-id")
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
