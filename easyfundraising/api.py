from .models import Item,User
from rest_framework import serializers,viewsets,routers
from django.db.models.query import QuerySet
from rest_framework.response import Response
from rest_framework import filters
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =User 
        fields = '__all__'
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Item
        
class UserViewset(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class= UserSerializer
    def retrieve(self,ruquest,*args,**kwargs):
        instance = self.get_object()
        serializers = UserSerializer(instance)
        return Response(serializers.data)
class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class=ItemSerializer
    
router = routers.DefaultRouter()
router.register(r'user', UserViewset)
router.register(r'ItemList',ItemViewset)