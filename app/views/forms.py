from django import forms
from captcha.fields import CaptchaField
from captcha.widgets import ReCaptchaV3
    
class MyForm(forms.Form):
    captcha = CaptchaField(widget=ReCaptchaV3)