from django.db.models import Sum
from django.shortcuts import render, redirect

from my_expenses.apps.expenses.forms import AddExpenseForm
from my_expenses.apps.expenses.models import Expense


def add_expense(request):
    form = AddExpenseForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'forms.html', context)


def expense_list(request):
    expenses = Expense.objects.all().order_by('-created')
    total = expenses.aggregate(Sum('amount'))['amount__sum']
    context = {
        'expenses': expenses,
        'total': total
    }
    return render(request, 'index.html', context)


def hello_world(request):
    # Give response
    return render(request, 'hello-world.html')
