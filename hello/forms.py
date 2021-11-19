from django import forms
from django.forms import fields
from hello.models import LogMessage


class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)  # trailing comma after message is required
