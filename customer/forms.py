from django import forms
import re

from .models import Customer


# classe para criar campo de dada no form de inserção
class DateInput(forms.DateInput):
    input_type = "date"


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Nome",
        error_messages={"max_length": "Nome não pode conter mais de 30 caracteres"}
    )
    last_name = forms.CharField(
        label="Sobrenome",
        error_messages={"max_length": "Sobrenome não pode conter mais de 30 caracteres"}
    )
    email = forms.EmailField(label="Email")
    birth_date = forms.CharField(label="Data de nascimento", widget=DateInput())
    area_code = forms.RegexField(  # regex serve para criar máscaras para os campos
      label="DDD",
      regex=r"^\d{2}$", #r para iniciar o regex, ^\inicio de significa numeros entre [0-9] {2} numero de digitos $fim do regex
      error_messages={"invalid": "Número de DDD inválido!"}
    )
    phone_number = forms.RegexField(
        label="Telefone",
        regex=r"^\+?1?[0-9]{9,15}$",#outra forma de fazer +?1? recebe 1 string caracteres entre 0 e 9 valor total entre 9 e 15 caracteres
        error_messages = {"invalid": "Número de telefone inválido!"}
    )
    country = forms.CharField(label="País")
    state = forms.CharField(label="State")
    city = forms.CharField(label="Cidade")

    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "area_code",
            "phone_number",
            "country",
            "state",
            "city"
        )
