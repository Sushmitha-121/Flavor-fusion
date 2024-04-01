from django.db import models

# Create your models here.

class logindetails(models.Model):
	user = models.CharField(max_length = 15)
	password = models.CharField(max_length = 10)
	email = models.CharField(max_length = 30,primary_key = True)
	
class fooddetails(models.Model):
	verbose_name_plural = "Food Details"
	Recipe_Name = models.CharField(max_length = 100)
	Ingredients = models.TextField()
	Cooking_process = models.TextField()
	about_recipe = models.TextField()
	origin = models.TextField()
	servings = models.IntegerField()
	Cooking_time = models.CharField(max_length = 100)
	author_Name = models.CharField(max_length = 100)
	class category_choice(models.TextChoices):
		Healthy_food = "Healthy_food"
		Chicken = "Chicken"
		Egg = "Egg"
		Veg_Recipe = "Veg_Recipe"

	Category = models.CharField(max_length = 50,choices = category_choice.choices,default = category_choice.Healthy_food)
	Recipe_image = models.ImageField(upload_to = 'static/recipe_img') 

	def __str__(self):
		return self.Recipe_Name
		

class Review(models.Model):
	user = models.ForeignKey(logindetails, on_delete=models.CASCADE)
	recipe = models.ForeignKey(fooddetails, on_delete=models.CASCADE)
	text = models.TextField(max_length=250)
	rating = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)


class Ratings(models.Model):
    comment = models.ForeignKey(Review, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)


