from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=255)
    street_number = models.CharField(max_length=50)
    city_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.street} {self.street_number}, {self.city}"
class AppUser(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    customer_id = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    birthday = models.DateField()
    last_updated = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CustomerRelationship(models.Model):
    points = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)
    appuser = models.ForeignKey(
        AppUser,
        related_name="customerrelationships",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.appuser} {self.points} pts"

class OptimizedAddress(models.Model):
    street = models.CharField(max_length=255)
    street_number = models.CharField(max_length=50)
    city_code = models.CharField(max_length=20, db_index=True)
    city = models.CharField(max_length=100, db_index=True)
    country = models.CharField(max_length=100, db_index=True)

    def __str__(self) -> str:
        return f"{self.street} {self.street_number}, {self.city}"


class OptimizedAppUser(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )

    first_name = models.CharField(max_length=255, db_index=True)
    last_name = models.CharField(max_length=255, db_index=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, db_index=True)
    customer_id = models.CharField(max_length=100, unique=True, db_index=True)
    phone_number = models.CharField(max_length=20, db_index=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    birthday = models.DateField(db_index=True)
    last_updated = models.DateTimeField(auto_now=True, db_index=True)
    address = models.ForeignKey(
        OptimizedAddress,
        related_name="users",
        on_delete=models.CASCADE,
        db_index=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['id']


class OptimizedCustomerRelationship(models.Model):
    points = models.IntegerField(db_index=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    last_activity = models.DateTimeField(auto_now=True, db_index=True)
    appuser = models.ForeignKey(
        OptimizedAppUser,
        related_name="customerrelationships",
        on_delete=models.CASCADE,
        db_index=True
    )

    def __str__(self):
        return f"{self.appuser} {self.points} pts"
