from django import forms
from my_expenses.apps.expenses.models import Expense


class AddExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        exclude = ('created',)
