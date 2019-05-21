#Import libraries and packages for Flask and Pymongo
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
#Name of the database that the app connects with. 
app.config["MONGO_DBNAME"] = "recipe_app_test"
#Retrieve URI for database from enviroment variable.
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

'''
Used in Testing
@app.route('/')
def hello():
    return "Welcome to the cooking world of tomorrow..."
'''   
######## CRUD operations and templates for Recipes #############################    
#Route to the Index or Home page of the application.
@app.route('/')
@app.route('/get_categories/')
def get_categories():
    return render_template("categories.html", categories=mongo.db.categories.find())

#Route to display the recipes in a single category.    
@app.route('/display_category/<category_name>')
def display_category(category_name):
    #Retrieve recipes from the database that have the same category name as that selected by the user.
    category_recipes = mongo.db.recipes.find({"category": category_name})
    return render_template("displayCategory.html", category_name=category_name, category_recipes=category_recipes)
    #Passing the category name and recipes for rendering in the "displayCategory.html" file.

#Route to view a single recipe.    
@app.route('/display_recipe/<recipe_id>')
def display_recipe(recipe_id):
    recipes = mongo.db.recipes
    #Update/Increment the views field in the database record to show the number of times the recipe has been viewed.
    recipes.update({'_id': ObjectId(recipe_id)}, 
        { '$inc': { 'views': 1 } })
    #Retrieve the recipe with the same ID as the one selected by the user.
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("displayRecipe.html", the_recipe=the_recipe)

#This route provides the upvotes functionality to allow users to "Like" a recipe.    
@app.route('/like_recipe/<recipe_id>')
def like_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)}, 
        { '$inc': { 'upvotes': 1 } }) #Increment the upvotes field of the selected recipe.
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}) #Retrieve recipe after it has been updated.
    return render_template("displayRecipe.html", the_recipe=the_recipe) #Pass updated recipe for rendering.

#Route to allow user to create a new recipe.
@app.route('/create_recipe/')
def create_recipe():
    #Retrieving data from the database that will be used in the Create Recipe form.
    return render_template("createRecipe.html", categories=mongo.db.categories.find(), cuisines=mongo.db.cuisines.find(), allergens=mongo.db.allergens.find())

#Route to insert new recipe in the database once the submit button is selected.    
@app.route('/insert_recipe/', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    #Allergens taken in list type first as request.form.to_dict() was only retrieving first allergen selected.
    allergen_list = request.form.getlist('allergens')
    #Used in Testing -- print(allergen_list)
    recipe_dict = request.form.to_dict() #Read in data entered by the user on the form.
    #Convert data taken in from form to integer so that it can be incremented for views and upvotes.
    #Then place the converted type into the dictionary fields.
    recipe_dict['views'] = int( recipe_dict['views'])
    recipe_dict['upvotes'] = int( recipe_dict['upvotes'])
    separator = ', ' #Creating separator.
    allergen_list_to_string = separator.join(allergen_list) #Converting list of allergens to string so that  it can be stored efficiently in the database. 
    #Used in testing -- print(allergen_list_to_string)
    recipe_dict['allergens'] = allergen_list_to_string #Place created string into appropriate field in dictionary.
    #Used in testing -- print(recipe_dict['allergens'])
    recipes.insert_one(recipe_dict) #Insert new recipe into collection.
    return redirect(url_for('get_categories')) #Redirect to home page.
    
#Route to provide delete recipe functionality in the application.
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)}) #Remove recipe with provided ID from the collection.
    return redirect(url_for('get_categories'))

#Route to render edit recipe form in the application with recipe information pre-loaded.    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    #Retieve recipe to be edited using the provided ID.
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    allergen_list = the_recipe['allergens'].split(', ') #Split string field to create list.
    #Used in testing -- print(allergen_list)
    #Retrieve data required for edit form.
    all_categories=mongo.db.categories.find()
    all_cuisines=mongo.db.cuisines.find()
    all_allergens=mongo.db.allergens.find()
    return render_template("editRecipe.html", recipe=the_recipe, categories=all_categories, cuisines=all_cuisines, 
        allergens=all_allergens, recipe_allergen_list=allergen_list)

#Route to provide edit recipe functionality in the application.    
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    #Retrieve recipe using passed recipe ID.
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    rec_views = the_recipe['views']
    rec_upvotes = the_recipe['upvotes']
    updated_allergen_list = request.form.getlist('allergens')
    separator = ', '
    updated_allergen_list_to_string = separator.join(updated_allergen_list)
    recipes.update({'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'category': request.form.get('category'),
        'cuisine': request.form.get('cuisine'),
        'allergens': updated_allergen_list_to_string, #Set allergens to created string.
        'ingredients': request.form.get('ingredients'),
        'instructions': request.form.get('instructions'),
        'prep': request.form.get('prep'),
        'cook': request.form.get('cook'),
        'author': request.form.get('author'),
        'views': rec_views, #Reset recipe views to same value prior to editing.
        'upvotes': rec_upvotes #Reset recipe upvotes to same value prior to editing.
    })
    return redirect(url_for('get_categories'))
    
######### Allergens ############################################################   
#Route to render allergens page.
@app.route('/manage_allergens/')
def manage_allergens():
    return render_template("allergens.html", allergens=mongo.db.allergens.find())

#Route to render edit allergens form.    
@app.route('/edit_allergen/<allergen_id>')
def edit_allergen(allergen_id):
    return render_template("editAllergen.html", the_allergen = mongo.db.allergens.find_one({"_id": ObjectId(allergen_id)}))

#Route to provide update/edit allergen functionality in the application.
@app.route('/update_allergen/<allergen_id>/', methods=['POST'])
def update_allergen(allergen_id):
    allergens = mongo.db.allergens
    #Update allergen record using data entered in the form.
    allergens.update({'_id': ObjectId(allergen_id)},
        {'allergen_name': request.form.get('allergen_name'),
        'allergen_description': request.form.get('allergen_description')})
    return redirect(url_for('manage_allergens'))

#Route to render create new allergen form.    
@app.route('/add_allergen/')
def add_allergen():
    return render_template("addAllergen.html")

#Route to insert new allergen in the database once the submit button is selected.    
@app.route('/insert_allergen/', methods=['POST'])
def insert_allergen():
    all_allergens = mongo.db.allergens
    #Insert new record in the database using data retrieved from the form.
    all_allergens.insert_one(request.form.to_dict())
    return redirect(url_for('manage_allergens'))

####### Manage Cuisines ########################################################
#Route to render cuisines page.
@app.route('/manage_cuisines/')
def manage_cuisines():
    return render_template("cuisines.html", cuisines=mongo.db.cuisines.find())

#Route to render edit cuisines form.     
@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    return render_template("editCuisine.html", the_cuisine = mongo.db.cuisines.find_one({"_id": ObjectId(cuisine_id)}))

#Route to provide update/edit allergen functionality in the application.   
@app.route('/update_cuisine/<cuisine_id>/', methods=['POST'])
def update_cuisine(cuisine_id):
    mongo.db.cuisines.update({'_id': ObjectId(cuisine_id)},
        {'cuisine_name': request.form.get('cuisine_name'),
        'cuisine_description': request.form.get('cuisine_description')})
    return redirect(url_for('manage_cuisines'))

#Route to render create new cuisine form.    
@app.route('/add_cuisine/')
def add_cuisine():
    return render_template("addCuisine.html")

#Route to insert new allergen in the database once the submit button is selected.    
@app.route('/insert_cuisine/', methods=['POST'])
def insert_cuisine():
    all_cuisines = mongo.db.cuisines
    all_cuisines.insert_one(request.form.to_dict())
    return redirect(url_for('manage_cuisines'))
    
####### Search Recipes #########################################################
#Route to render search recipes form/page.
@app.route('/search_recipes/')
def search_recipes():
    #Retrieve data required in the form.
    all_categories = mongo.db.categories.find()
    all_cuisines = mongo.db.cuisines.find()
    all_allergens = mongo.db.allergens.find()
    #Creating ingredients options list for all other recipes in the database.
    all_recipes = mongo.db.recipes.find()
    #print(all_recipes) -- used in testing.
    all_ingredients = [] #Empty list instantiated to record single instances of ingredients. 
    for recipe in all_recipes:
        recipe_ingredients = recipe['ingredients'].split(', ') #Split ingredients string in recipe into list.
        #Check to see if ingredient is not already in the all_ingredients list. If not, add ingredient to the list.
        for ingredient in recipe_ingredients:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    #print(all_ingredients) -- used in testing.
    return render_template("searchRecipes.html", categories=all_categories, cuisines=all_cuisines, 
            allergens=all_allergens, ingredients=all_ingredients)

#Route to provide search functionality in the application.            
@app.route('/search_results/', methods=['POST'])
def search_results():
    #Collect User's input from form.
    category_list = request.form.getlist('category')
    cuisine_list = request.form.getlist('cuisine')
    #Used in testing -- print(cuisine_list)
    allergen_list = request.form.getlist('allergens')
    ingredient_list = request.form.getlist('ingredients')
    all_recipes = mongo.db.recipes.find() #Retrieve all recipes from the database.
    # Used in testing -- print(type(all_recipes) is list)
    recipe_search_results = [] #Empty list instantiated to store recipes that meet search criteria.
    
    if len(category_list) > 0: #Check that user has selected category(ies). If not, move on to next block of code.
        for recipe in all_recipes:
            if recipe['category'] in category_list:
                recipe_search_results.append(recipe) #If a recipe is from the same category as those selected, add it to the results list.
     
    if len(cuisine_list) > 0: #Check that user has selected cuisine(s). If not, move on to next block of code.
        if len(recipe_search_results) == 0: #Check to see if any recipes have been added to the search results list. If not, all recipes must be searched.
            for recipe in all_recipes:
                if recipe['cuisine'] in cuisine_list:
                    recipe_search_results.append(recipe) #If a recipe is from the same category as those selected, add it to the results list.
        elif len(recipe_search_results) > 0:
            #print(len(recipe_search_results))
            for recipe in recipe_search_results:
                if recipe['cuisine'] not in cuisine_list:
                    recipe_search_results.remove(recipe) #Loop through recipes placed in the results list so far, if they do not contain the selected cuisine, remove from the results list.
                    
    if len(allergen_list) > 0:  #Check that user has selected allergen(s). If not, move on to next block of code.
        if len(recipe_search_results) == 0:  #Check to see if any recipes have been added to the search results list. If not, all recipes must be searched.
            for recipe in all_recipes:
                recipe_allergens = recipe['allergens'].split(', ') #Split string to create iterable list.
                allergen_control = 0 #Instantiate control accumulator, used to ensure a recipe does not contain any allergen selected before adding to results list.  
                for a in recipe_allergens:
                    if a in allergen_list:
                        allergen_control += 1
                if allergen_control == 0: #If control accumulator has not been incremented, append recipe to results list.
                    recipe_search_results.append(recipe)
        else:
            for recipe in recipe_search_results: #Results list already contains recipe so only need to loop through these here.
                recipe_allergens = recipe['allergens'].split(', ')
                for a in recipe_allergens:
                    if a in allergen_list:
                        recipe_search_results.remove(recipe) #If recipe contains slected allergen, remove recipe from results list.
                        
    if len(ingredient_list) > 0: #Check that user has selected ingredient(s). If not, move on to next block of code.
        if len(recipe_search_results) == 0:  #Check to see if any recipes have been added to the search results list. If not, all recipes must be searched.
            for recipe in all_recipes:
                recipe_ingredients = recipe['ingredients'].split(', ') #Split string to create iterable list.
                number_of_ingredients = len(ingredient_list) #Initialise control accumulator to the number of ingredients selected by user.
                ingredient_control = 0 #Instantiate control accumulator
                for i in recipe_ingredients:
                    if i in ingredient_list:
                        ingredient_control += 1
                if ingredient_control == number_of_ingredients:
                    recipe_search_results.append(recipe) #Recipe only added to results list if it contains all the ingreditns selected.
        else:
            for recipe in recipe_search_results: #Results list already contains recipes so only need to loop through these here. 
                recipe_ingredients = recipe['ingredients'].split(', ')
                number_of_ingredients = len(ingredient_list)
                ingredient_control = 0
                for i in recipe_ingredients:
                    if i in ingredient_list:
                        ingredient_control += 1
                if ingredient_control != number_of_ingredients:
                    recipe_search_results.remove(recipe) #Remove recipe from current results list if it does not contain all ingredients selected.
                    
                        
    number_of_results = len(recipe_search_results) #Used to control the content in "displayResults.html"
    return render_template("searchResults.html", search_results=recipe_search_results, no_of_results=number_of_results)
                
            
###### Run __main__ function ###################################################
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)