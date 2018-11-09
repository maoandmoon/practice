from django import forms
from salon.models import Contact
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

    # def __init__(self, *args, **kwargs):
    #     super(ContactModelForm, self).__init__(*args, **kwargs)
    #     from crispy_forms.helper import FormHelper
    #     self.helper = FormHelper()
    #     self.helper.form_class = 'border border-light p-5 z-depth-1-half'
    #     self.helper.form_method = 'post'
    #     from django.urls import reverse
    #     self.helper.form_action = reverse('contacts')
    #     self.helper.help_text_inline = True
    #     self.helper.html5_required = True
    #     self.helper.label_class = 'col-md-2 control-label'
    #     self.helper.field_class = 'col-md-10'
    #     from crispy_forms.layout import Submit
    #     self.helper.add_input(Submit('send_button', u'Отправить'))