from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["owner", "item_name", "category", "amount", "price", "description"]