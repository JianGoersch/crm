from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.edit import DeleteView
#essa classe irá exibir esse template consumindo desse model
from django.db.models import Q #q tem a função do "or" do select no banco de dados
class CustomerListView(ListView):
    template_name = "customer/customer_list.html"
    paginate_by = 2
    model = Customer

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            object_list = self.model.objects.filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name)
            )
        else:
            object_list = self.model.objects.all()
        return object_list


class CustomerCreateView(CreateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm


#validar o formulário
    def form_valid(self, form):
        return super().form_valid(form)

#pagina de retorno após preencher formulário
    def get_success_url(self):
        return reverse ("customer:customer_list")

class CustomerUpdateView(UpdateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("customer:customer_list")




class CustomerDeleteView(DeleteView):
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)

    def get_success_url(self):
        return reverse("customer:customer_list")