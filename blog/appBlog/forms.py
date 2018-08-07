from django import forms
 
class UserComments(forms.Form):
    name = forms.CharField(label="Имя", min_length=3, max_length=10)
    text = forms.TextField(label="Комментарий", min_length=1, max_length=150)

class UserMessage(forms.Form):
    name = forms.CharField(label="Имя", min_length=3, max_length=20)
    text = forms.TextArea(label="Сообщение", min_length=10, max_length=350)