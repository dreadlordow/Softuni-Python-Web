from django import forms


class TodoForm(forms.Form):
    title = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    description = forms.CharField(

        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),

    )

    bot_catcher = forms.CharField(
        widget=forms.HiddenInput,
        required=False
    )

    def clean_bot_catcher(self):
        if len(self.cleaned_data['bot_catcher']):
            raise forms.ValidationError('This is a bot')
