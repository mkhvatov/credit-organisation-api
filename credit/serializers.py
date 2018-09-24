from rest_framework import serializers

from .models import (
    Offer,
    ClientForm,
    CreditProposal,
)


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'date_created', 'date_changed', 'rotation_date_begin', 'rotation_date_end',
                  'offer_name', 'offer_type', 'min_score', 'max_score', 'credit_organization')


class ClientFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientForm
        fields = ('id', 'date_created', 'date_changed', 'family_name', 'name', 'father_name',
                  'birth_date', 'phone_number', 'passport_number', 'score')

    def create(self, validated_data):
        validated_data['partner'] = self.context['request'].user
        return super(ClientFormSerializer, self).create(validated_data)


class BaseCreditProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditProposal
        fields = ('id', 'date_created', 'date_sent', 'client_form', 'offer', 'status')


class StatusCreditProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditProposal
        fields = ('status',)


class PartnerCreditProposalSerializer(serializers.ModelSerializer):

    def validate(self, data):
        try:
            ClientForm.objects.get(pk=data['client_form'].pk,
                                   partner=self.context['request'].user)
        except ClientForm.DoesNotExist:
            raise serializers.ValidationError('Incorrect client form')

        return data

    class Meta:
        model = CreditProposal
        fields = ('client_form', 'offer')
