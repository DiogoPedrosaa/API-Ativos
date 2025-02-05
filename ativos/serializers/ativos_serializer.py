from rest_framework import serializers
from ..models import Fabricante, Tag, Ativo, Setor

class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = ['id', 'nome'] 
        
class FabricanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricante
        fields = ['id', 'nome'] 

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag']  

class AtivoSerializer(serializers.ModelSerializer):
    modelo = FabricanteSerializer(read_only=True)
    tag = TagSerializer(read_only=True)
    setor = SetorSerializer(read_only=True)  
    modelo_id = serializers.PrimaryKeyRelatedField(source='modelo', queryset=Fabricante.objects.all(), write_only=True)
    tag_id = serializers.PrimaryKeyRelatedField(source='tag', queryset=Tag.objects.all(), write_only=True)
    setor_id = serializers.PrimaryKeyRelatedField(source='setor', queryset=Setor.objects.all(), write_only=True)
    class Meta:
        model = Ativo
        fields = '__all__'


