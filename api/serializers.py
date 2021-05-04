from rest_framework import serializers
from .models import Cadena


class CadenaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cadena
		fields ='__all__'