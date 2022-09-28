from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BooksViewSet,CategoryViewSet, UserViewset

router=SimpleRouter()
router.register("users",UserViewset,basename="users")
router.register("books",BooksViewSet,basename="books")
router.register("categorys",CategoryViewSet,basename="category_list")
urlpatterns=router.urls
