from django.db import models

# Create your models here.
class Carusel(models.Model):

    head = models.CharField('Carusel head', max_length=50)
    text = models.TextField('Carusel text')
    img_bg = models.ImageField('Carusel img_bg', upload_to='carusel_img_bg')
    img = models.ImageField('Carusel img', upload_to='carusel_img_bg')

    def __str__(self):
        return self.head


class CategoryL0(models.Model):

    name = models.TextField('name')

    def __str__(self):
        return self.name

class CategoryL1(models.Model):

    category = models.ForeignKey(CategoryL0, on_delete=models.CASCADE, related_name='l0_l1')
    name = models.TextField('name')

    def __str__(self):
        return self.name
    

class Product(models.Model):

    availability_CHOICE = [
        ('In Stock', 'In Stock'),
        ('Not Available', 'Not Available')
    ]

    condition_CHOICE = [
        ('New', 'New'),
        ('Used', 'Used'),
    ]

    cotegory = models.ForeignKey(CategoryL1, on_delete=models.CASCADE, related_name='l1_prod')
    head = models.CharField('Product head', max_length=50)
    img = models.ImageField('Product image', upload_to='product')   
    price = models.PositiveBigIntegerField('Product price')
    availability = models.CharField('availability', choices=availability_CHOICE, max_length=30)
    condition = models.CharField('condition', choices=condition_CHOICE, max_length=30)

    def __ste__(self):
        return self.head


class Contact(models.Model):

    name = models.CharField('User name', max_length=30)
    email = models.EmailField('User email')
    subject = models.CharField('Subject', max_length=50)
    message = models.TextField('User message')

    def __ste__(self):
        return self.name