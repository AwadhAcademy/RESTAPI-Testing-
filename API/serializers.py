from rest_framework import serializers
from data.models import collection

class collectionSerlializers(serializers.ModelSerializer):
    class Meta:
        model=collection
        fields='__all__'