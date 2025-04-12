from django.db import migrations
from django.utils.text import slugify

def create_initial_categories(apps, schema_editor):
    Category = apps.get_model('categories', 'Category')
    categories = [
        {
            'name': 'Computer Science',
            'description': 'Research papers in computer science, including AI, algorithms, and software engineering.'
        },
        {
            'name': 'Physics',
            'description': 'Research papers in physics, including quantum mechanics, relativity, and particle physics.'
        },
        {
            'name': 'Mathematics',
            'description': 'Research papers in mathematics, including algebra, geometry, and number theory.'
        },
        {
            'name': 'Biology',
            'description': 'Research papers in biology, including genetics, ecology, and molecular biology.'
        },
        {
            'name': 'Chemistry',
            'description': 'Research papers in chemistry, including organic chemistry, inorganic chemistry, and biochemistry.'
        },
    ]
    
    for category_data in categories:
        Category.objects.create(
            name=category_data['name'],
            slug=slugify(category_data['name']),
            description=category_data['description']
        )

def remove_initial_categories(apps, schema_editor):
    Category = apps.get_model('categories', 'Category')
    Category.objects.filter(name__in=[
        'Computer Science',
        'Physics',
        'Mathematics',
        'Biology',
        'Chemistry',
    ]).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_categories, remove_initial_categories),
    ]
