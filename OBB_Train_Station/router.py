from obb.views import PersonViewSet, PlatformViewSet, TrainStationViewSet, TrainSectionViewSet, TrainViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('people', PersonViewSet, base_name='People')
router.register('platform', PlatformViewSet, base_name='Platform')
router.register('train_station', TrainStationViewSet, base_name='Train Station')
router.register('train_section', TrainSectionViewSet, base_name='Train Section')
router.register('train', TrainViewSet, base_name='Train')
