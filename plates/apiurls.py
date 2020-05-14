from rest_framework import routers
from .api import PlateViewSet

router = routers.DefaultRouter()
router.register('plates', PlateViewSet, 'plates-api')

urlpatterns = router.urls