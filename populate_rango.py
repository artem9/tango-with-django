import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page


def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/",
         "views": 52},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/",
         "views": 112},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/",
         "views": 37}
    ]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views": 161},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/",
         "views": 96},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/",
         "views": 173}
    ]

    pascal_pages = [
        {"title": "Pascal - programming language",
         "url": "http://progopedia.ru/language/pascal/",
         "views": 16},
        {"title": "Source codes Programming Pascal",
         "url": "http://www.pascal.helpov.net/",
         "views": 41},
        {"title": "Online guide to language Pascal",
         "url": "http://pascal.org.ua/",
         "views": 19}
    ]

    perl_pages = [
        {"title": "Track updates to Perl modules",
         "url": "www.perlmodules.net",
         "views": 13},
        {"title": "The Perl Programming Language",
         "url": "https://www.perl.org/",
         "views": 27},
        {"title": "A short excursion into Perl programming",
         "url": "https://www.opennet.ru/docs/RUS/perl_help/",
         "views": 32}
    ]

    php_pages = [
        {"title": "What is PHP?",
         "url": "http://php.net/manual/ru/intro-whatis.php",
         "views": 54},
        {"title": "All about PHP, MySQL and more!",
         "url": "http://www.php.su/",
         "views": 76},
        {"title": "PHP - Interesting publications",
         "url": "https://habrahabr.ru/hub/php/",
         "views": 115}
    ]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/",
         "views": 41},
        {"title": "Flask",
         "url": "http://flask.pocoo.org",
         "views": 69}
    ]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "Other Frameworks": {"pages": other_pages,  "views": 32, "likes": 16},
            "Pascal": {"pages": pascal_pages, "views": 39, "likes": 8},
            "Perl": {"pages": perl_pages, "views": 67, "likes": 17},
            "PHP": {"pages": php_pages, "views": 178, "likes": 98},
            "Prolog": {"pages": [], "views": 32, "likes": 16},
            "Programming": {"pages": [], "views": 32, "likes": 16},
            }

    # If you want to add more catergories or pages,
    # add them to the dictionaries above.
    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.

    def add_page(category, title, url, views=0):
        page = Page.objects.get_or_create(category=category, title=title)[0]
        page.url = url
        page.views = views
        page.save()
        return page

    def add_cat(name, views=0, likes=0):
        category = Category.objects.get_or_create(name=name)[0]
        category.views = views
        category.likes = likes
        category.save()
        return category

    for cat, cat_data in cats.iteritems():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- %s - %s" % (str(c), str(p)))

# Start execution here!
if __name__ == '__main__':
    print ("Starting Rango population script...")
    populate()
