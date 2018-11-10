from dal import autocomplete
from django import forms
from salon.models import Contact, PriceItem
from django.core.mail import send_mail
from django.conf import settings


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'message']
        exclude = ('created',)

    def send_email(self):
        concat_subject = 'Новый контакт: {0} {1}'.format(self.cleaned_data["name"], self.cleaned_data["phone"])
        send_mail(subject=concat_subject,
                  message=self.cleaned_data["message"],
                  from_email=settings.DEFAULT_FROM_EMAIL,
                  recipient_list=settings.PRACTICE_ADMINS)


class PriceItemForm(forms.ModelForm):
    def clean_subcategory(self):
        category = self.cleaned_data.get('category', None)
        subcategory = self.cleaned_data.get('subcategory', None)
        if subcategory and category and subcategory.category != category:
            raise forms.ValidationError('Wrong subcategory for category  ')
        return subcategory

    class Meta:
        model = PriceItem
        fields = ('title', 'price', 'category', 'subcategory', 'description')
        widgets = {'subcategory': autocomplete.ModelSelect2(url='subcategory_autocomplete', forward=('category',))}
