from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class BaseTimeModel(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    date_changed = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UserProfile(models.Model):
    is_credit_organization = models.BooleanField(
        verbose_name='Credit organization', default=False)
    is_partner = models.BooleanField(
        verbose_name='Partner', default=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile', null=True)

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'


class Offer(BaseTimeModel):
    CONSUMER_CREDIT = 0
    MORTGAGE = 1
    AUTO_CREDIT = 2

    CREDIT_TYPE = (
        (CONSUMER_CREDIT, 'consumer credit'),
        (MORTGAGE, 'mortgage'),
        (AUTO_CREDIT, 'auto credit'),
    )

    rotation_date_begin = models.DateTimeField()
    rotation_date_end = models.DateTimeField()
    offer_name = models.CharField(max_length=250)
    offer_type = models.PositiveSmallIntegerField(
        CREDIT_TYPE, default=CONSUMER_CREDIT)
    min_score = models.PositiveSmallIntegerField(default=0)
    max_score = models.PositiveSmallIntegerField(default=0)
    credit_organization = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Credit organization',
        limit_choices_to={'profile__is_credit_organization': True}, null=True)

    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'

    def get_offer_type(self):
        return Offer.CREDIT_TYPE[self.offer_type]

    def __str__(self):
        return '{} - {}'.format(self.offer_name, self.get_offer_type())


class ClientForm(BaseTimeModel):
    family_name = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    father_name = models.CharField(max_length=250)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=12)
    passport_number = models.CharField(max_length=10)
    score = models.PositiveSmallIntegerField(default=0)
    partner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Partner',
        limit_choices_to={'profile__is_partner': True}, null=True)

    class Meta:
        verbose_name = 'Client form'
        verbose_name_plural = 'Client forms'

    def get_fio(self):
        return '{} {} {}'.format(self.family_name, self.name, self.father_name)

    def __str__(self):
        return self.get_fio()


class CreditProposal(models.Model):
    NEW = 0
    SENT = 1
    RECEIVED = 2
    APPROVED = 3
    DECLINED = 4
    DONE = 5

    CREDIT_STATUS = (
        (NEW, 'new'),
        (SENT, 'sent'),
        (RECEIVED, 'received'),
        (APPROVED, 'approved'),
        (DECLINED, 'declined'),
        (DONE, 'done'),
    )

    date_created = models.DateTimeField(auto_now=True)
    date_sent = models.DateTimeField(auto_now=True)
    status = models.PositiveSmallIntegerField(
        CREDIT_STATUS, default=NEW)
    offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE, null=True, verbose_name='Offer')
    client_form = models.ForeignKey(
        ClientForm, on_delete=models.CASCADE, null=True, verbose_name='Client form')

    class Meta:
        verbose_name = 'Application for a credit organization'
        verbose_name_plural = 'Applications for a credit organizations'

    def get_status(self):
        return CreditProposal.CREDIT_STATUS[self.status]

    def __str__(self):
        return '{} {} {}'.format(self.client_form.get_fio(),
                                 self.offer.offer_name,
                                 self.get_status())


# API-token for a new user:
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        if not hasattr(instance, 'auth_token'):
            Token.objects.create(user=instance)
        if not hasattr(instance, 'profile'):
            UserProfile.objects.create(user=instance)
