from rest_framework import serializers
from .models import *

class dataserializer(serializers.ModelSerializer):
	class Meta:
		model = fooddetails
		fields = "__all__"
