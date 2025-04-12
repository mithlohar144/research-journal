from django.core.management.base import BaseCommand
from papers.models import ResearchPaper
from taggit.models import Tag

class Command(BaseCommand):
    help = 'Creates sample tags for the research papers'

    def handle(self, *args, **kwargs):
        # Common academic research tags
        tags = [
            'Machine Learning',
            'Artificial Intelligence',
            'Data Science',
            'Deep Learning',
            'Neural Networks',
            'Computer Vision',
            'Natural Language Processing',
            'Robotics',
            'Blockchain',
            'Cybersecurity',
            'Cloud Computing',
            'IoT',
            'Big Data',
            'Data Analytics',
            'Software Engineering',
            'Web Development',
            'Mobile Computing',
            'Network Security',
            'Database Systems',
            'Algorithms',
            'Quantum Computing',
            'Green Computing',
            'Human-Computer Interaction',
            'Information Systems',
            'Digital Transformation'
        ]

        # Create tags
        created_count = 0
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(name=tag_name.lower(), slug=tag_name.lower().replace(' ', '-'))
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Created tag: {tag_name}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} new tags'))
