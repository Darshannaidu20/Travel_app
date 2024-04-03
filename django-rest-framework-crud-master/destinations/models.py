from django.db import models

class Destination(models.Model):

    """
    Model to represent a travel destination.

    Attributes:
    - name (CharField): Name of the destination.
    - country (CharField): Country of the destination.
    - description (TextField): Description of the destination.
    - best_time_to_visit (CharField): Best time to visit the destination.
    - category (CharField): Category of the destination.
    - image_url (URLField): URL of the destination image.
    - created_at (DateTimeField): Date and time when the destination was created.
    - updated_at (DateTimeField): Date and time when the destination was last updated.
    - creator (ForeignKey to User): User who created the destination.
    """
    
    CATEGORY_CHOICES = [
        ('Beach', 'Beach'),
        ('Mountain', 'Mountain'),
        ('City', 'City'),
        ('Historical', 'Historical'),
    ]

    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    best_time_to_visit = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User', related_name='destinations', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


