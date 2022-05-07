from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=75)
    picture = models.ImageField(upload_to='img',blank=True,null=True)

    class Meta:
        verbose_name_plural = 'pizzas'

    def __str__(self):
        return self.pizza_name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField()

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return self.topping_name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user_name = models.TextField()
    
    class Meta:
        verbose_name_plural =  'comments'

    def __str__(self):
        return self.comment_text + ' ' + self.date_added + ' ' + self.user_name