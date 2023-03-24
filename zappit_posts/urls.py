from rest_framework import routers
from .views import PostList

router =  routers.DefaultRouter()
router.register('api/posts', PostList, 'posts')

urlpatterns = router.urls