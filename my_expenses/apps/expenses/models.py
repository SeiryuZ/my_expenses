from django.db import models


class Expense(models.Model):
    description = models.CharField(max_length=255)
    amount = models.IntegerField()

    TYPE = (
        (1, 'Food'),
        (2, 'Entertainment'),
        (3, 'Rent'),
        (4, 'Other'),
    )
    type = models.SmallIntegerField(choices=TYPE, default=4)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} on {self.created}"
