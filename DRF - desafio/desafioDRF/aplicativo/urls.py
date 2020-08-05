from django.urls import path
from aplicativo import views 
from rest_framework.routers import DefaultRouter
from aplicativo.views import AfazeresViewSet

router = DefaultRouter()
router.register(r'afazeres', AfazeresViewSet)
urlpatterns = router.urls
