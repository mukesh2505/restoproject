from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, default=None)
    full_name = models.CharField(max_length=255, default=None)
    email = models.CharField(max_length=255, default=None)
    mobile = models.CharField(max_length=255, default=None)
    password = models.CharField(max_length=255, default=None)

    class Meta:
        managed = True
        db_table = 'users'


class Users2(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, default=None)
    full_name = models.CharField(max_length=255, default=None)
    email = models.CharField(max_length=255, default=None)
    mobile = models.CharField(max_length=255, default=None)
    password = models.CharField(max_length=255, default=None)

    class Meta:
        managed = True
        db_table = 'users2'


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default=None, null=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'category'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default=None, null=True)
    short_description = models.CharField(max_length=500, default=None, null=True)
    image = models.CharField(max_length=1000, default=None, null=True)
    price = models.IntegerField(null=True)
    description = models.TextField(default=None, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'product'


class OurTeam(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    designation = models.CharField(max_length=50, null=True, default=None)
    profile_pic = models.CharField(max_length=1000, null=True)
    facebook_url = models.CharField(max_length=1000, null=True)
    tweet_url = models.CharField(max_length=1000, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'our_team'


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=10, null=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.CharField(max_length=5, null=True)
    payment_status = models.CharField(max_length=2, null=True)
    transection = models.CharField(max_length=50, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'orders'
























