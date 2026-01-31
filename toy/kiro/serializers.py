from rest_framework import serializers 
from .models import student, user

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['id','first_name','last_name','address','pincode','city','state','father_name','mother_name','phno','emailid','adhaar_no']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'name', 'email', 'age', 'phno', 'password']
        extra_kwargs = {'password': {'write_only': True}}      
        
