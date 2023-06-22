from django.db import models


class Categoriya(models.Model):
    name = models.CharField(max_length=150)
    img = models.ImageField(upload_to='product/')
    text = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()

    # mahs = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Product(models.Model):
    categoriya = models.ForeignKey(Categoriya, null=True, on_delete=models.RESTRICT)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="images/")
    price = models.IntegerField()
    text = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    text = models.TextField()
    buy_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
