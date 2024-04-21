from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length = 254, null=True)  # Allow null if needed
    Phone = PhoneNumberField()  # Better handling for phone numbers
    Message = models.CharField(max_length=1000)
    Date = models.DateField()

    def __str__(self):
        return self.Name
