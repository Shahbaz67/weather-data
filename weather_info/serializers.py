import json
from weather_info.models import Summary, ORDER, REGION, PARAMETER
from rest_framework import serializers



class SummarySerializer(serializers.ModelSerializer):
    """
    Summary model serializer
    """
    order = serializers.ChoiceField(choices=[(choice, choice) for choice in ORDER], write_only=True)
    region = serializers.ChoiceField(choices=[(choice, choice) for choice in REGION], write_only=True)
    parameter = serializers.ChoiceField(choices=[(choice, choice) for choice in PARAMETER], write_only=True)

    class Meta:
        model = Summary
        fields = '__all__'
    
    def to_representation(self, instance):
        """Convert`JSON objects to dictionary before displaying"""
        res = super().to_representation(instance)
        if res.get('data'):
            res['data'] = [json.loads(data) for data in res['data']]
        return res