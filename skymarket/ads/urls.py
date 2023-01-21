from django.conf.urls.static import static
from django.urls import include, path
from rest_framework_nested import routers

from ads.views import AdViewSet, CommentViewSet
from skymarket import settings

ad_router = routers.SimpleRouter()
comment_router = routers.SimpleRouter()
ad_router.register("api/ads", AdViewSet, basename="ads")
comment_router.register("comments", CommentViewSet, basename="ads")

urlpatterns = [
    path("", include(ad_router.urls)),
    path("api/ads/<int:ad_pk>/", include(comment_router.urls))
]

