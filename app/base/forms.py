from django import forms


class MyProfileForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address = forms.CharField(
        label='Address',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'address-input',
            'autocomplete': 'off'
        })
    )
    age = forms.IntegerField(
        label='Age',
        min_value=17,
        max_value=100,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    number_of_adults = forms.IntegerField(
        label='Number of Adults',
        min_value=0,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    number_of_children = forms.IntegerField(
        label='Number of Children',
        min_value=0,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    is_student = forms.BooleanField(
        label='Is Student',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is-student'})
    )
    university_address = forms.CharField(
        label='University Address',
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'university-address-input',
            'autocomplete': 'off',
            'disabled': 'true'  
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        is_student = cleaned_data.get('is_student')
        university_address = cleaned_data.get('university_address')

        if is_student and not university_address:
            self.add_error('university_address', 'University address is required for students.')
        return cleaned_data