from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Books,Category
#rom .permissions import IAdminOrSeeOnly
from rest_framework import permissions
from .serializers import BooksSerializer,CategorySerializer, UserSerializer

# Create your views here.
class BooksViewSet(viewsets.ModelViewSet):
    queryset=Books.objects.all()
    serializer_class=BooksSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_permissions(self):
        if self.request.method in ["POST",'PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]
      
class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_permissions(self):
        if self.request.method in ["POST",'PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]
    
class UserViewset(viewsets.ModelViewSet):#new
    permission_classes=(permissions.IsAdminUser,)
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer