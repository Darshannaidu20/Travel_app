from rest_framework import serializers
from .models import Destination
from django.contrib.auth.models import User


class DestinationSerializer(serializers.ModelSerializer):

    """
    Serializer for the Destination model.

    Fields:
    - name: Name of the destination (CharField)
    - country: Country of the destination (CharField)
    - description: Description of the destination (TextField)
    - best_time_to_visit: Best time to visit the destination (CharField)
    - category: Category of the destination (CharField with choices)
    - image_url: URL of the destination image (URLField)
    - created_at: Date and time when the destination was created (DateTimeField)
    - updated_at: Date and time when the destination was last updated (DateTimeField)
    - creator: User who created the destination (ForeignKey to User model)
    """
    
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Destination
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer): 
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Destination.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'destinations')
