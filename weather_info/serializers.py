import json
from weather_info.models import Summary, ORDER, REGION, PARAMETER
from rest_framework import serializers


class SummarySerializer(serializers.ModelSerializer):
    """
    Summary model serializer
    """
    order = serializers.ChoiceField(choices=[(choice, choice) for choice in ORDER])
    region = serializers.ChoiceField(choices=[(choice, choice) for choice in REGION])
    parameter = serializers.ChoiceField(choices=[(choice, choice) for choice in PARAMETER])
    count = serializers.SerializerMethodField()

    class Meta:
        model = Summary
        fields = ['order', 'region', 'parameter', 'count', 'data']

    def to_representation(self, instance):
        """Convert JSON objects to dictionary before displaying"""
        res = super().to_representation(instance)
        data = res.pop('data')
        if data:
            res['data'] = [json.loads(item) for item in data]
        return res
    
    def get_count(self, instance):
        """Count of rows in summary table"""
        data = getattr(instance, 'data', None)
        if data:
            return len(data)
        return 0
    