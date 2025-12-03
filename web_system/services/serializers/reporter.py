from rest_framework import serializers

from relacionamentos.models import Reporter


class ReporterMinimalSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='services:reporter_list',
    #     lookup_field='pk',
    #     read_only=True,
    # )

    class Meta:
        model = Reporter
        fields = ['pk','name','cpf','email']

    def create(self, validated_data):
        return Reporter.objects.create(**validated_data)