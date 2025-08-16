from django.db import models

class Category(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    COLOR_CHOICES = (
        ('R', 'Red'),
        ('A', 'Apricot'),
        ('B', 'Black'),
        ('S','Silver'),
        ('T', 'Tan')
    )
    BREED_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    color = models.CharField(max_length=1, choices=COLOR_CHOICES)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    breed = models.CharField(max_length=1, choices=BREED_CHOICES)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class Pets(models.Model):
    GENE_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENE_CHOICES)
    age = models.IntegerField()
    image = models.ImageField(upload_to='pets/')
    price = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class Product(models.Model):
    TYPE_CHOICES = (
        ('DF', 'Dog food'),
        ('CF', 'Cat food'),
        ('T', 'Toy'),
        ('C', 'Costume')
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    size = models.IntegerField(null=True, blank=True)
    price = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

class Seller(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sellers/')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class PetKnowledge(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pet-knowledge/')
    text = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

class ProductDetail(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product-detail/')
    sku = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    vaccinated = models.CharField(max_length=3)
    dewormed = models.CharField(max_length=3)
    cert = models.CharField(max_length=100)
    microchip = models.CharField(max_length=3)
    location = models.CharField(max_length=100)
    pub_date = models.DateField()
    additional_info = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class Costumer(models.Model):
    image = models.ImageField(upload_to='costumer/')

