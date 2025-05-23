from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.node_mgmt.filters.collector import CollectorFilter
from apps.node_mgmt.models.sidecar import Collector
from apps.node_mgmt.serializers.collector import CollectorSerializer
from django.core.cache import cache


class CollectorViewSet(ModelViewSet):
    queryset = Collector.objects.all()
    serializer_class = CollectorSerializer
    filterset_class = CollectorFilter

    @swagger_auto_schema(
        operation_summary="获取采集器列表",
        tags=['Collector']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="创建采集器",
        tags=['Collector']
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # 清除cache中的etag
        cache.delete("collectors_etag")

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @swagger_auto_schema(
        operation_summary="更新采集器",
        tags=['Collector']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="collector_del",
        operation_summary="删除采集器",
        tags=['Collector']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="获取采集器详情",
        tags=['Collector']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
