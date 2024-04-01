from django.http import JsonResponse,HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import logindetails,fooddetails
from .serializer import dataserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

@api_view(['GET','POST'])
def getdetails(request):
	if request.method == 'GET':
		food_Details = fooddetails.objects.all()
		ser = dataserializer(food_Details,many=True)
		return JsonResponse({'dataobj':ser.data},safe=False)
	elif request.method == 'POST':
		ser = dataserializer(data = request.data)
		if ser.is_valid():
			ser.save()
			return Response(ser.data)
		else:
			return HttpResponse("Error while saving the data")


def login(request):
	if(request.POST.get('username')):
		uname = request.POST.get('username')
		pword = request.POST.get('password')
		list_of_emails = logindetails.objects.all().values_list('email', flat = True)
		if uname in list_of_emails:
			if pword == logindetails.objects.get(email = uname).password:
				return render(request,'index-3.html',{'msg': "Welcome"})
			else:
				return render(request,'page-login.html',{'error':"wrong password"})
		else:
			return render(request,'page-login.html',{'error':"User Not registered"})
	else:
		return render(request,'page-login.html')



def regsubmit(request):
    if request.method == 'POST':
        firstname = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        list_of_emails = logindetails.objects.all().values_list('email', flat=True)
        
        if email in list_of_emails:
            return render(request, 'page-login.html', {'error': 'Email already registered! Try Login'})
        else:
            logindetails.objects.create(user=firstname, password=password, email=email)
            return render(request, 'index-3.html', {'msg': 'Welcome ' + firstname})
    else:
        return render(request, 'signup.html')  # Render the signup page for GET requests

  

def logout(request):
	try:
		del request.session['username']
	except:
		pass
	return render(request,'login.html')

def recipe(request):
	list_of_recipes = fooddetails.objects.all().values()
	veg_recipes = fooddetails.objects.filter(Category='Veg_Recipe')
	return render(request, 'VegRecipes.html', {
				'name': fooddetails.objects.all().values()[0]['Recipe_Name'],
				'list_of': veg_recipes
				})

def recipe1(request):
	list_of_recipes = fooddetails.objects.all().values()
	chicken_recipes = fooddetails.objects.filter(Category='Chicken')
	return render(request, 'Chicken.html', {
				'name': fooddetails.objects.all().values()[0]['Recipe_Name'],
				'list_of': chicken_recipes
				})

def recipe2(request):
	list_of_recipes = fooddetails.objects.all().values()
	egg_recipes = fooddetails.objects.filter(Category='Egg')
	return render(request, 'Egg.html', {
				'name': fooddetails.objects.all().values()[0]['Recipe_Name'],
				'list_of': egg_recipes
				})

def recipe3(request):
	list_of_recipes = fooddetails.objects.all().values()
	egg_recipes = fooddetails.objects.filter(Category='Healthy_food')
	return render(request, 'Healthy.html', {
				'name': fooddetails.objects.all().values()[0]['Recipe_Name'],
				'list_of': egg_recipes
				})

def index(request):
	total = fooddetails.objects.all().count()
	return render(request, 'index-3.html',{"total_recipes" : fooddetails.objects.all().count()})




def recipe_detail(request, Recipe_Name):
    # Fetch details of a single recipe from your API using recipe_id
    response = requests.get(f'https://getdetails/{Recipe_Name}/')
    recipe = response.json()
    return render(request, 'recipe_detail.html', {'recipe': recipe})



def add_recipe(request):
    if request.method == 'POST':
        # Retrieve data from POST request
        name = request.POST.get('name')
        category = request.POST.get('category')
        time = request.POST.get('time')
        ingredients = request.POST.get('ing')
        process = request.POST.get('ins')
        img = request.POST.get('img')
        about_recipe = request.POST.get('about')
        origin = request.POST.get('origin')
        servings = request.POST.get('servings')
        author = request.POST.get('author')
        food = fooddetails(Recipe_Name=name,Ingredients=ingredients,author_Name=author,Cooking_process=process,about_recipe=about_recipe ,origin=origin,servings=servings,Cooking_time=time,Category=category,Recipe_image="static/recipe_img/"+img)
        food.save() 
        return render(request,'add-recipe.html')
    else:
        return render(request, 'add-recipe.html')

def fun(request,rname):
	name = fooddetails.objects.get(Recipe_Name=rname)
	cooking_time = name.Cooking_time
	ingredients = name.Ingredients
	cooking_process = name.Cooking_process
	origin = name.origin
	about_recipe = name.about_recipe
	servings = name.servings 
	author_Name = name.author_Name
	Recipe_image = name.Recipe_image
	category = name.Category
	return render(request, 'single_recipe.html',{'name':name,'time':cooking_time,'ing':ingredients,'process':cooking_process,
		'origin':origin,'about_recipe':about_recipe,'servings':servings,'author_Name':author_Name,'image':Recipe_image,'category':category})



def comment(request,rname):
    if request.method == 'POST':
        recipe = fooddetails.objects.get(Recipe_Name=rname)
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment_text = request.POST.get('comment')
        rating_value = int(request.POST.get('rating'))
        comment = Comment(recipe=recipe, name=name, email=email, comment=comment_text, rating=rating_value)
        comment.save()
        return render(request,'single_recipe.html')
 

def fun3(request,rname):
	name = Comment.objects.get(name=rname)
	email = name.email
	comment = name.comment
	rating = name.rating
	return render(request,'single_recipe.html',{'name':name,'email':email,'comment':comment,'rating':rating})

def recipe_detail(request, rname):
    recipe = get_object_or_404(fooddetails, Recipe_Name=rname)
    comments = recipe.comment_set.all()


'''def add_comment(request):
    recipe = get_object_or_404(fooddetails, Recipe_Name=recipe_name)

    if request.method == 'GET':
        comment_text = request.GET.get('text')
        created_at = request.GET.get('created_at')
        rating = request.GET.get('rate')
        user = request.user
        comment = Comment(
            recipe=recipe,
            author=name,
            email=email,
            text=comment_text,
            rating=rating
        )

        return redirect('single_recipe.html', recipe_name=recipe_name) '''

def add_comment(request,rname):
	recipe = get_object_or_404(fooddetails, pk=Recipe_Name)
	comments = Review.objects.filter(recipe=recipe)
	if request.method == 'POST':
		text = request.POST.get('text')
		rating = request.POST.get('rating')
		new_comment = Review.objects.create(user=request.user, recipe=recipe, text=text, rating=rating)
		new_comment.save()
	return render(request, 'single_recipe.html', {'recipe': recipe, 'comments': comments})



def recipe_detail(request, rname):
    recipe = get_object_or_404(fooddetails, Recipe_Name=rname)
    comments = Review.objects.filter(recipe=recipe)

    if request.method == "POST":
        text = request.POST.get('text')
        rating = request.POST.get('rating')
        user = request.user
        comment = Review.objects.create(user=user, recipe=recipe, text=text, rating=rating)
        comment.save()
    return render(request, 'comment.html', {'recipe': recipe, 'comments': comments})