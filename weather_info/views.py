from weather_info.models import Summary
from weather_info.serializers import SummarySerializer
from rest_framework import viewsets
from rest_framework.response import Response


class SummaryViewSet(viewsets.ModelViewSet):
    """
    Summary Model Viewset to get filtered weather-data
    """
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer

    def create(self, request, *args, **kwargs):
        """Outputs filtered response based on order, region and parameter"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        filter_data = self.request.data

        if not filter_data:
            return Response("Please provide order, region and parameter to filter data")
        
        order = request.data.get('order')
        region = request.data.get('region')
        parameter = request.data.get('parameter')

        queryset = self.queryset.filter(order=order, region=region, parameter=parameter)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_allowed_methods(self):
        return ['POST']


