from django.shortcuts import render, redirect
from ForestManagement.models import *
from ForestManagement.forms import ProductCreateForm, OrderCreateForm, SearchForm, ProductUpdateForm, OrderUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
	title = 'Forest Management System'
	context = {
	    "title": title,
	
	}
	return render(request, "home.html",context)

@login_required
def list_products(request):
	form = SearchForm(request.POST or None)
	title = 'Products'
	queryset = Product.objects.all()
	context = {
	    "title": title,
		"queryset":queryset,
		"okay":True,
		"form":form
	}
	if request.method == 'POST':
		if form.is_valid():
			cd = form.cleaned_data
			a= cd.get('name')
		if(a):
			queryset = Product.objects.filter(item_name__icontains=a) | Product.objects.filter(category__icontains=a)
		else:
			queryset = Product.objects.all()			
	context = {
	    "title": title,
		"queryset":queryset,
		"okay":True,
		"form":form
	}
	
	return render(request, "listitems.html",context)

@login_required
@csrf_exempt
def list_orders(request):
	form = SearchForm(request.POST or None)
	title = 'Orders'
	orders = Order.objects.all().order_by('delivery_date')
	# for i in orders:
	# 	print(i)
	context = {
	    "title": title,
		"orders":orders,
		"okay":False,
		"form":form
	}
	if request.method == "POST":
		order_id = request.POST.get('clear_order')
		x = Order.objects.get(pk=order_id)
		if x.item.quantity >= x.ordered_quantity:
			Product.objects.filter(pk=x.item.id).update(quantity=x.item.quantity-x.ordered_quantity)
			Order.objects.filter(pk=order_id).delete()
		else:
			messages.error(request, "Cannot clear the order as there is no sufficient quantity of "+ str(x.item))
	context = {
	    "title": title,
		"orders":orders,
		"okay":False,
		"form":form
	}
	return render(request, "list_orders.html",context)

@login_required
def add_products(request):
	form =ProductCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/list')
	context = {
		"form": form,
		"title": "Add Products",
	}
	return render(request, "add_items.html", context)
@login_required
def update_products(request, pk):
	queryset = Product.objects.get(id=pk)
	form = ProductUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = ProductUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/list')

	context = {
		'form':form
	}
	return render(request, 'add_items.html', context)

@login_required
def update_orders(request, pk):
	queryset = Order.objects.get(id=pk)
	form = OrderUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = ProductUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/list')

	context = {
		'form':form
	}
	return render(request, 'add_items.html', context)

@login_required
def delete_products(request, pk):
		queryset = Product.objects.get(id=pk)
		if request.method == 'POST':
			queryset.delete()
			return redirect('/list')
		return render(request, 'delete_products.html')

class OrderCreateView(LoginRequiredMixin, CreateView):
	model = Order
	template_name='add_items.html'
	fields = [ 'item', 'ordered_quantity', 'delivery_date']
	success_url='/'


	def form_valid(self, form):
		form.instance.user_name = self.request.user
		return super().form_valid(form)

class UserOrderListView(ListView):
    model = Order
    template_name = 'list_orders.html'
    context_object_name = 'orders'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Order.objects.filter(user_name=user).order_by('delivery_date')

