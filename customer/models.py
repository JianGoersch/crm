from django.db import models
from django.urls import reverse
# Create your models here.
#classe customer(cliente) que vai virar tabela no banco da dedos

class Customer(models.Model): #sempre models.Model
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField()
    area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=9)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    created_datre = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

#essa função serve para que sempre quando eu chamar um objeto da classe customer ele vai retornar o que estiver dentro da função
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#funções para pegar dados completos para exibir na table
    def get_full_phone_number(self):
        return f"({self.area_code}) {self.phone_number}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_city(self):
        return f"{self.city} - {self.state}"

    def get_absolute_url(self):
        return reverse ("customer:customer_update", kwargs={"id":self.id})

    def get_delete_url(self):
        return reverse("customer:customer_delete", kwargs={"id":self.id})

#class Meta serve para fixa o nome da tabela no banco (se não fizer ele cria nome do app_nome da tabela
    class Meta:
        db_table = "customer"



