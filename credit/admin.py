from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.models import Token
from rangefilter.filter import (
    DateRangeFilter,
    DateTimeRangeFilter,
)

from .models import (
    UserProfile,
    CreditProposal,
    Offer,
    ClientForm,
)


@admin.register(CreditProposal)
class CreditProposalAdmin(admin.ModelAdmin):

    def statuses(self, instance):
        return CreditProposal.CREDIT_STATUS[instance.status][1]

    list_display = ['date_created', 'date_sent', 'statuses', 'offer', 'client_form']
    search_fields = ['offer', 'client_form']
    list_filter = (
        ('date_created', DateRangeFilter),
        ('date_sent', DateRangeFilter),
    )


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):

    def offer_types(self, instance):
        return Offer.CREDIT_TYPE[instance.offer_type][1]

    list_display = ['date_created', 'date_changed', 'rotation_date_begin', 'rotation_date_end',
                    'offer_name', 'offer_types', 'min_score', 'max_score', 'credit_organization']
    search_fields = ['credit_organization', 'offer_name']
    list_filter = (
        ('date_created', DateRangeFilter),
        ('date_changed', DateRangeFilter)
    )


@admin.register(ClientForm)
class ClientFormAdmin(admin.ModelAdmin):
    list_display = ['date_created', 'date_changed', 'family_name', 'name',
                    'father_name', 'birth_date', 'partner', 'phone_number',
                    'passport_number', 'score']
    search_fields = ['partner', 'family_name']
    list_filter = (
        ('date_created', DateRangeFilter),
        ('date_changed', DateRangeFilter),
    )


class InlineUserProfile(admin.StackedInline):
    model = UserProfile


class InlineToken(admin.StackedInline):
    model = Token


class UserProfileAdmin(UserAdmin):

    def api_token(self, user):
        return Token.objects.get(user=user)

    def partner(self, user):
        return bool(UserProfile.objects.get(user=user).is_partner)

    def credit_organization(self, user):
        return bool(UserProfile.objects.get(user=user).is_credit_organization)

    def get_list_display(self, request):
        list_display = list(
            super(UserProfileAdmin, self).get_list_display(request)
        )
        list_display.insert(1, 'api_token')
        list_display.insert(2, 'credit_organization')
        list_display.insert(3, 'partner')
        return list_display

    inlines = [InlineUserProfile, InlineToken]


admin.site.unregister(User)
admin.site.unregister(Token)
admin.site.register(User, UserProfileAdmin)
