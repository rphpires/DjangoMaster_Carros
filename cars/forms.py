from django import forms
from cars.models import Brand, Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    # def clean_value(self): ## a função inicia com 'clean_' pois é a forma que o Django identifique que é uma função de validação
    #     value = self.cleaned_data.get('value')
    #     if value < 20000:
    #         self.add_error("value", "Valor mínimo deve ser de 20 mil.")
    #     return value
    
    def clean_factory_year(self):
        year = self.cleaned_data.get('factory_year')
        if year < 1975:
            self.add_error("factory_year", "Não é possível cadastrar um veículo fabricado antes de 1975.")
        return year

class CarForm(forms.Form):
    ## Modo de declarar o Form de uma forma mais manual, utilizar o ModelForm é melhor.
    model = forms.CharField(max_length=200)    
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField(required=False)

    def save(self):
        car = Car(
            model = self.cleaned_data["model"],
            brand = self.cleaned_data["brand"],
            factory_year = self.cleaned_data["factory_year"],
            model_year = self.cleaned_data["model_year"],
            plate = self.cleaned_data["plate"],
            value = self.cleaned_data["value"],
            photo = self.cleaned_data["photo"]
        )
        car.save()
        return car


