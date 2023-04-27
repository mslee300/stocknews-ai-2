from django import forms
from stocknewsai.models import Email


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email  # 사용할 모델
        fields = ['email']  # EmailForm에서 사용할 Email 모델의 속성