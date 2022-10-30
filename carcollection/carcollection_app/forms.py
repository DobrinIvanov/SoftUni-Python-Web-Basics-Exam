from django import forms

from carcollection.carcollection_app.models import Profile, Car


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CreateCarForm(CarForm):
    pass


class EditCarForm(CarForm):
    pass


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hidden_fields()

    class Meta:
        model = Profile
        fields = "__all__"

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class DeleteCarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    class Meta:
        model = Car
        fields = "__all__"

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __disable_fields(self):
        for _, field in self.fields.items():
            field.disabled = True