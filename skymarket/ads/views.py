
from rest_framework import pagination, viewsets, permissions
from rest_framework.decorators import action

from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer, AdDetailSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filterset_class = AdFilter

    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.usert).all()
        return Ad.objects.all()

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ["retrieve", "create", "me"]:
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AdDetailSerializer
        else:
            return AdSerializer

    @action(detail=False, methods=["get"])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ["retrieve", "create", "me"]:
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()
