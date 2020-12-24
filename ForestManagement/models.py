from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
category_choice = (
		('Furniture', 'Furniture'),
		('IT Equipment', 'IT Equipment'),
		('Phone', 'Phone'),
	)
class Product(models.Model):
	category = models.CharField(max_length=50, blank=True, null=True)
	item_name = models.CharField(max_length=50, blank=True, null=True)
	quantity = models.IntegerField(default='0', blank=False, null=True)
	receive_quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_by = models.CharField(max_length=50, blank=True, null=True)
	issue_quantity = models.IntegerField(default='0', blank=True, null=True)
	issue_by = models.CharField(max_length=50, blank=True, null=True)
	issue_to = models.CharField(max_length=50, blank=True, null=True)
	phone_number = models.CharField(max_length=50, blank=True, null=True)
	created_by = models.CharField(max_length=50, blank=True, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	export_to_CSV = models.BooleanField(default=False)

	def __str__(self):
		return self.item_name

class Order(models.Model):
	item = models.ForeignKey(Product, on_delete = models.CASCADE)
	ordered_quantity = models.IntegerField(default=0, blank=False, null=True)
	ordered_date = models.DateTimeField(auto_now=True)
	delivery_date =  models.DateField()
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.item_name + " by " + str(self.user_name)