from django import forms
from .models import Subscriber

from .utils import add_subscriber_to_sendpulse


class SubscriberForm(forms.ModelForm):
    """Форма создания подписчика"""

    class Meta:
        model = Subscriber
        exclude = ('sendpulse_status',)
        widgets = {
            "name": forms.TextInput(attrs={"id": "mailing__form-name", "placeholder": "имя", "class": "input"}),
            "phone": forms.TextInput(attrs={"id": "mailing__form-phone", "placeholder": "телефон", "class": "input"}),
            "email": forms.EmailInput(attrs={"id": "mailing__form-email", "placeholder": "email", "class": "input"}),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try: 
            match = Subscriber.objects.get(email=email)
        except Subscriber.DoesNotExist:
            return email
        raise forms.ValidationError('Вы уже подписаны на нашу рассылку!')
    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=True, *args, **kwargs)
        adition_result = add_subscriber_to_sendpulse(instance)
        if adition_result.get('result'):
            instance.sendpulse_status = True
            instance.save()
        return instance