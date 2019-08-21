# RECIPE APPLICATION

This three tier web application was developed as part completion of the 
Code Institute Full Stack Web Developer course. It is the milestone project for the 
Data Centric Development stream. The application follows the project brief and is developed using 
HTML, CSS, Materialize CSS library, jQuery, Javascript, Python and a MongoDB Database.

## UX
1. The application has attempted to meet all of the requirements laid out in the 
assignment outline and design brief except one. The developer did not include a login 
feature for the user as this was described as an optional feature in the
project outline. This was due to time contraints on the student's part and felt it was more 
appropriate to focus on the required elements.


## GitHub & Heroku Repository
* GitHub reposity for the project is located [here](https://github.com/KikiDow/Data-Centric-Project)


## Features
* The application contains a **Navigation (Nav) Bar** which contains all the buttons required to
navigate the application. The Nav Bar contains five different buttons that allow the
user to access all elements/features of the application. The Nav Bar is also mobile responsive utilising 
the "Materialize CSS"  navbar component/class resulting in the navbar being condensed when viewed on 
mobile. 
* The application contains a **Drill Down/Hot Key** buttons on the Home page. These allow the user 
to access more quickly the type of recipe they are looking for and is requirement of the project brief.
The user can then select to view a recipe from the list presented which again is a requirement of the 
project outline.
* The application contains a **View Recipe**  page. This page allows the user to view all the information
relating to a single recipe. 
* The application contains a feature to **Update a Recipe** which allows the user to update any recipe 
in the database. Once the user elects to edit a recipe, all required data relating to that recipe is 
retrieved and presented in the edit recipe form to the user. The user can then make their desired changes 
and submit to update the document in the database.
* The application contains a feature to **Delete a Recipe** which allows the user to update any recipe 
in the database.
* The application contains an **Upvotes**  feature. This allows users to "Like" recipes.
* The application contains a **Views**  feature. The feature records the number of times a recipe has been 
viewed by different users.
* The application contains a **Create Recipe**  page. This allows the user to enter a recipe of their 
own so that it can be viewed by other users. The Create Recipe page contains a form that is implemented 
using the "Materialize CSS" form component/class, requesting the required data to create a new document 
in the MongoDB database.
* The application contains a **Search** feature. This will allow the user to search the entire database 
by selecting various fields/options to find a recipe(s) that matches their request.
* The application contains both a **Manage Allergens** and **Manage Cuisines** page. These pages are 
built using the same basic structure and are designed to allow the user to view, update and create 
records in the database relating to the allergens and cuisines information.
* The application also contains a **Pagination** feature when presenting results from the recipe
searching features.

## Tecnologies Used
- HTML
- CSS
- jQuery
- Javascript
- Python3
- MongoDB
- Materialize CSS library.

## Files Included
- README.md
- Procfile
- requirements.txt
- style.css
- Breakfast.jpg
- Create Recipe.jpg
- Desserts.jpg
- FruitAndVeg.jpg
- healthy-dish.jpg
- Lunch.jpg
- Mains.jpg
- Starters.jpg
- recipe-app-test.py
- addAllergen.html
- addCuisine.html
- allergens.html
- base.html
- categories.html
- createRecipe.html
- cuisines.html
- displayCategory.html
- displayRecipe.html
- editRecipe.html
- searchRecipes.html
- searchResults.html

## Testing
* A form of White Box testing was conducted by the developer using potential use 
cases or user stories to ensure that each link in the application followed the intended path. 
This was also done for each feature outlined in the Features section to ensure they 
were working as intended.
* A form of Black Box testing was done by asking both a friend and the student's 
mentor on the course to use the application without instruction. Their feedback was 
then used to make improvements.
* Fundamental testing was used to ensure that the stack of technologies was working together 
successfully. (e.g.) Retrieving one field from a document in the database, manipulating it with 
Python, passing it through the Flask framework and presenting it to the user.
* Component testing was used for each block of code developed to serve a particular function. 
(e.g.) In lines 191-194 of the "recipe-app-test.py" file, the code block is attempting to filter
result by category, placing only recipes with the same category as those selected by the user
in the list of results. This was tested with using none, single and multiple categories selected, 
to ensure it was producing the correct result. Similar testing was used on all code blocks developed/used.
* Combination testing was used to ensure that code blocks were working in conjunction to produce the 
intended and expected results.

## Deployment
* The application is deployed using Heroku [here](https://data-centric-project-kd.herokuapp.com/)

## Credits

### Content
* All textual content was taken directly from the following sources. This content was chosen to
provide a professional look and feel to the application. **IMPORTANT NOTE:** Please note that any 
information relating to dietary requirements and food allergens is intended for illustrative purposes 
only.
* Information relating to allergens was taken directly from
[here](https://www.healthline.com/nutrition/common-food-allergies#section3)

* Information relating to cuisines was taken directly from the following resources;
- Italian - [here](https://en.wikipedia.org/wiki/Italian_cuisine)
- French - [here](https://en.wikipedia.org/wiki/French_cuisine)
- Irish - [here](https://en.wikipedia.org/wiki/Irish_cuisine)

* The recipes used in the project were taken directly from the following links;
- Smoked salmon on horseradish potato farls - [here](http://allrecipes.co.uk/recipe/4029/smoked-salmon-on-horseradish-potato-farls.aspx)
- Salmon mousse choux pastries - [here](http://allrecipes.co.uk/recipe/26109/salmon-mousse-choux-pastries.aspx)
- Mushroom risotto - [here](http://allrecipes.co.uk/recipe/6422/mushroom-risotto.aspx)
- Boeuf bourguignon with shallots - [here](http://allrecipes.co.uk/recipe/15808/boeuf-bourguignon-with-shallots.aspx)
- Baked gnocchi with bolognese ragu - [here](http://allrecipes.co.uk/recipe/37695/baked-gnocchi-with-bolognese-ragu.aspx)
- Irish stew - [here](http://allrecipes.co.uk/recipe/2958/irish-stew.aspx)
- Christine's quiche Lorraine - [here](http://allrecipes.co.uk/recipe/15998/christine-s-quiche-lorraine.aspx)
- Italian ciabatta sandwich - [here](http://allrecipes.co.uk/recipe/29087/italian-ciabatta-sandwich.aspx)
- Irish soda bread - [here](http://allrecipes.co.uk/recipe/2794/irish-soda-bread.aspx)
- Creme Brulee - [here](http://allrecipes.co.uk/recipe/4716/creme-brulee.aspx)
- Limoncello Cake - [here](http://allrecipes.co.uk/recipe/9719/limoncello-cake.aspx)
- Irish cream sponge cake - [here](http://allrecipes.co.uk/recipe/20014/irish-cream-sponge-cake.aspx)
- Eggs Benedict - [here](http://allrecipes.co.uk/recipe/31267/eggs-benedict.aspx)
- Irish fry up - [here](http://allrecipes.co.uk/recipe/4646/irish-fry-up.aspx)
- French toast - [here](http://allrecipes.co.uk/recipe/25572/french-toast.aspx)

### Media
* The file "healthy-dish.jpg" used as the background image was retrieved from
[here](https://www.bbc.com/news/uk-northern-ireland-46616637)
* The file "Breakfast.jpg" was retrieved from
[here](https://www.shutterstock.com/it/image-photo/continental-breakfast-fresh-croissants-orange-juice-1062875051?src=hIhJYlcIrByRiAIGj_DXQw-1-71)
* The file "Create Recipe.jpg" was retrieved from 
[here](https://www.shutterstock.com/ja/image-photo/cooking-ingredients-dark-background-space-text-637340239?src=ul_NtqaTbsS-8VyKULQb2Q-1-17)
* The file "Desserts.jpg" was retrieved from
[here](https://www.shutterstock.com/ja/image-photo/piece-chocolate-cake-mint-on-table-347770127?src=PBI_P1QK5TgwgYMsS_vA8A-1-46)
* The file "Lunch.jpg" was retrieved from
[here](https://www.shutterstock.com/image-photo/woman-eating-healthy-lunch-on-dark-1105520444?src=AEw4sliqYraOF2bMp6qfEQ-1-63)
* The file "Mains.jpg" was retrieved from
[here](https://www.shutterstock.com/image-photo/roast-chicken-potatoes-brussels-sprouts-carrots-1174376536?src=gs5RSWH6gV01qxqqaZYRGQ-1-3)
* The file "Starters.jpg" was retrieved from
[here](https://www.shutterstock.com/image-photo/dainty-morsels-white-asparagus-on-rocket-397406353)

### Acknowledgements
#### References
* The code in this project was heavily influenced by the sample mini project in the Code Institute Data Centric Module located
[here]()

#### Bibliography
* Pymongo - [here](https://api.mongodb.com/python/current/)
* Python - [here](https://www.w3schools.com/python/)
* Flask - [here](https://www.tutorialspoint.com/flask)
* MongoDB - [here](http://api.mongodb.com/python/current/tutorial.html)