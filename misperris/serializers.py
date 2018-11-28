from .models import Perro
from rest_framework import serializers

class perroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perro
        fields = '__all__'## esto es lo mismo que agregar una por una pero solo que las agregas toas mas rapido xddd tremendo atajo bueno saberlo
