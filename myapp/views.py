from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


PRODUCTS = {
    'dairy': {
        'category': 'Dairy products',
        'description': 'Fresh, wholesome dairy products for breakfast, baking and everyday meals.',
        'products': [
            {'name': 'Fresh milk', 'description': 'Creamy everyday milk from trusted producers.', 'price': 'From KES 450', 'icon': 'fas fa-glass-whiskey', 'image': 'images/milk.jpg'},
            {'name': 'Natural yoghurt', 'description': 'Smooth yoghurt with a clean, natural taste.', 'price': 'From KES 350', 'icon': 'fas fa-bowl-food', 'image': 'images/yoghurt.jpg'},
            {'name': 'Farm butter', 'description': 'Rich butter for cooking, baking and spreading.', 'price': 'From KES 500', 'icon': 'fas fa-cookie-bite', 'image': 'images/butter.jpg'},
            {'name': 'Farm cheese', 'description': 'Wholesome cheese for snacks, sandwiches and meals.', 'price': 'From KES 600', 'icon': 'fas fa-cheese', 'image': 'images/c h e e s e.jpg'},
            {'name': 'Fresh cream', 'description': 'Rich cream for desserts, sauces and baking.', 'price': 'From KES 500', 'icon': 'fas fa-glass-whiskey', 'image': 'images/heavycream.jpg'},
            {'name': 'Farm ghee', 'description': 'Traditional clarified butter for cooking and baking.', 'price': 'From KES 700', 'icon': 'fas fa-jar', 'image': 'images/ghee.jpg'},
        ],
    },
    'meat': {
        'category': 'Meat products',
        'description': 'Quality meat selected for freshness, flavour and value.',
        'products': [
            {'name': 'Fresh beef', 'description': 'Versatile cuts for family meals and special occasions.', 'price': 'From KES 1,000', 'icon': 'fas fa-drumstick-bite', 'image': 'images/beef.jpg'},
            {'name': 'Farm chicken', 'description': 'Tender chicken for quick and delicious recipes.', 'price': 'From KES 800', 'icon': 'fas fa-drumstick-bite', 'image': 'images/fullchick.jpg'},
            {'name': 'Chicken sale', 'description': ' Quality matured kienyeji chicken.', 'price': 'From KES 1,500', 'icon': 'fas fa-drumstick-bite', 'image': 'images/chickensale.jpg'},
            {'name': 'Duck meat selection', 'description': 'A flavourful choice for memorable meals.', 'price': 'From KES 1,200', 'icon': 'fas fa-drumstick-bite', 'image': 'images/duckmeat.jpg'},
        ],
    },
    'vegan': {
        'category': 'Vegan products',
        'description': 'Plant-based ingredients to make everyday meals nourishing and delicious.',
        'products': [
            {'name': 'Organic vegetables', 'description': 'Fresh seasonal vegetables for healthy meals.', 'price': 'From KES 600', 'icon': 'fas fa-leaf', 'image': 'images/vegetables.jpg'},
            {'name': 'Avocados', 'description': 'Creamy, nutritious avocados for salads and meals.', 'price': 'From KES 300', 'icon': 'fas fa-leaf', 'image': 'images/avocado.jpg'},
            {'name': 'Guavas', 'description': 'Sweet, fresh guavas packed with natural flavour.', 'price': 'From KES 250', 'icon': 'fas fa-apple-alt', 'image': 'images/guavas.jpg'},
            {'name': 'Oranges', 'description': 'Juicy oranges for a refreshing everyday snack.', 'price': 'From KES 300', 'icon': 'fas fa-apple-alt', 'image': 'images/oranges.jpg'},
            {'name': 'Pears', 'description': 'Fresh, crisp pears for a naturally sweet treat.', 'price': 'From KES 350', 'icon': 'fas fa-apple-alt', 'image': 'images/pears.jpg'},
            {'name': 'Lemons and limes', 'description': 'Bright citrus for cooking, drinks and dressings.', 'price': 'From KES 250', 'icon': 'fas fa-lemon', 'image': 'images/lemons$lime.jpg'},
            {'name': 'Fresh capsicum', 'description': 'Crisp, colourful capsicum for salads, cooking and meals.', 'price': 'From KES 500', 'icon': 'fas fa-shopping-basket', 'image': 'images/capsicum.jpg'},
        ],
    },
    'chicken-fish': {
        'category': 'Chicken, duck and fish',
        'description': 'Fresh poultry and fish for simple, satisfying meals.',
        'products': [
            {'name': 'Farm eggs', 'description': 'Fresh eggs from carefully raised hens.', 'price': 'From KES 350', 'icon': 'fas fa-egg', 'image': 'images/eggs.jpg'},
            {'name': 'Free-range chicken eggs', 'description': 'Wholesome eggs for breakfast, baking and cooking.', 'price': 'From KES 400', 'icon': 'fas fa-egg', 'image': 'images/chickeneggs.jpg'},
            {'name': 'Free-range duck eggs', 'description': 'Rich, nutritious eggs from free-range ducks.', 'price': 'From KES 450', 'icon': 'fas fa-egg', 'image': 'images/duckeggs.jpg'},
            {'name': 'Fresh chicken', 'description': 'Quality chicken for roasting, grilling or stews.', 'price': 'From KES 800', 'icon': 'fas fa-drumstick-bite', 'image': 'images/chicken.jpg'},
            {'name': 'Chicken variety pack', 'description': 'A convenient selection for family meals.', 'price': 'From KES 1,000', 'icon': 'fas fa-drumstick-bite', 'image': 'images/chickenvariety.jpg'},
            {'name': 'Duck selection', 'description': 'Pekin ducklings for sale.', 'price': 'From KES 1,000', 'icon': 'fas fa-feather', 'image': 'images/ducks.jpg'},
            {'name': 'Red snapper', 'description': 'Fresh fish selected for quality and taste.', 'price': 'From KES 1,100', 'icon': 'fas fa-fish', 'image': 'images/redsnapper.jpg'},
            {'name': 'Fresh tilapia', 'description': 'Delicate, fresh fish for simple family meals.', 'price': 'From KES 900', 'icon': 'fas fa-fish', 'image': 'images/tilapia.jpg'},
            {'name': 'Fresh juice', 'description': 'Refreshing juice made from ripe seasonal fruit.', 'price': 'From KES 450', 'icon': 'fas fa-glass-whiskey', 'image': 'images/freshjuice.jpg'},
        ],
    },
}


def category(request, category_name):
    category_data = PRODUCTS[category_name]
    return render(request, 'category.html', category_data)


def products(request):
    return render(request, 'category.html', {
        'category': 'Our products',
        'description': 'Explore fresh, organic and responsibly sourced products from Sisenye Organics.',
        'products': [product for data in PRODUCTS.values() for product in data['products']],
    })


def contact(request):
    return render(request, 'contact.html')
