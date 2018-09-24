from django.shortcuts import redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (
    generics,
    filters
)

from .serializers import (
    BaseCreditProposalSerializer,
    ClientFormSerializer,
    PartnerCreditProposalSerializer,
    OfferSerializer,
    StatusCreditProposalSerializer,
)
from .models import (
    ClientForm,
    CreditProposal,
    Offer,
)
from . import permissions


# API for partners:
class ClientFormList(generics.ListAPIView):
    serializer_class = ClientFormSerializer
    permission_classes = (permissions.PartnerAndSuperUserPermisson,)

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'

    def get_queryset(self):
        user = self.request.user
        if user.profile.is_partner:
            return ClientForm.objects.filter(partner=user)
        if user.is_superuser:
            return ClientForm.objects.all()


class ClientFormDetail(generics.RetrieveAPIView):
    serializer_class = ClientFormSerializer
    permission_classes = (permissions.PartnerAndSuperUserPermisson,)

    def get_queryset(self):
        user = self.request.user
        if user.profile.is_partner:
            return ClientForm.objects.filter(partner=user)
        if user.is_superuser:
            return ClientForm.objects.all()


class ClientFormCreate(generics.CreateAPIView):
    serializer_class = ClientFormSerializer
    permission_classes = (permissions.PartnerPermisson,)


class ClientFormUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientFormSerializer
    permission_classes = (permissions.SuperUserPermisson,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return ClientForm.objects.all()


class CreditProposalCreate(generics.CreateAPIView):
    serializer_class = PartnerCreditProposalSerializer
    permission_classes = (permissions.PartnerPermisson,)


class OfferList(generics.ListAPIView):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
    permission_classes = (permissions.PartnerCreditOrganizationSuperUserPermisson,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'


# API for credit organizations:
class CreditProposalList(generics.ListAPIView):
    serializer_class = BaseCreditProposalSerializer
    permission_classes = (permissions.PartnerCreditOrganizationSuperUserPermisson,)

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'

    def get_queryset(self):
        user = self.request.user
        if user.profile.is_credit_organization:
            return CreditProposal.objects.filter(offer__credit_organization=user)
        if user.profile.is_partner:
            return CreditProposal.objects.filter(client_form__partner=user)
        if user.is_superuser:
            return CreditProposal.objects.all()


class CreditProposalDetail(generics.RetrieveAPIView):
    serializer_class = BaseCreditProposalSerializer
    permission_classes = (permissions.CreditOrganizationAndSuperUserPermisson,)

    def get_queryset(self):
        user = self.request.user
        if user.profile.is_credit_organization:
            return CreditProposal.objects.filter(offer__credit_organization=user)
        if user.is_superuser:
            return CreditProposal.objects.all()


class CreditProposalUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BaseCreditProposalSerializer
    permission_classes = (permissions.SuperUserPermisson,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return CreditProposal.objects.all()


class CreditProposalStatusUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = StatusCreditProposalSerializer
    permission_classes = (permissions.CreditOrganizationPermission,)

    def get_queryset(self):
        user = self.request.user
        if user.profile.is_credit_organization:
            return CreditProposal.objects.filter(offer__credit_organization=user)


def auth_redirect(request):
    if request.user and request.user.is_authenticated:
        return redirect('/docs/')
    else:
        return redirect('/admin/')
