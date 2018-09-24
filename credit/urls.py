from django.conf.urls import url
from rest_framework.documentation import include_docs_urls

from . import views


urlpatterns = [
    url('^', include_docs_urls(title='Credit API')),

    # Common client forms:
    url(r'^api/client-forms/$', views.ClientFormList.as_view(),
        name='client-form-list'),
    url(r'^api/client-forms/(?P<pk>[0-9]+)/$', views.ClientFormDetail.as_view(),
        name='client-form-detail'),
    # Create client for partner:
    url(r'^api/client-forms-create/$', views.ClientFormCreate.as_view(),
        name='client-form-create'),
    # Update and delete client for superuser:
    url(r'^api/client-form-update-delete/(?P<pk>[0-9]+)/$', views.ClientFormUpdateDelete.as_view(),
        name='client-form-update-delete'),
    # Create proposal for partner:
    url(r'^api/credit-proposal-create/$', views.CreditProposalCreate.as_view(),
        name='credit-proposal-create'),
    # Credit proposals:
    url(r'^api/credit-proposals/$', views.CreditProposalList.as_view(),
        name='credit-proposals-list'),
    url(r'^api/credit-proposals/(?P<pk>[0-9]+)/$', views.CreditProposalDetail.as_view(),
        name='credit-proposals-detail'),
    # Credit proposal update and delete for superuser:
    url(r'^api/credit-proposal-update-delete/(?P<pk>[0-9]+)/$', views.CreditProposalUpdateDelete.as_view(),
        name='credit-proposal-update-delete'),
    # Credit proposal status update for credit organization:
    url(r'^api/credit-proposal-status-update/(?P<pk>[0-9]+)/$', views.CreditProposalStatusUpdate.as_view(),
        name='credit-proposal-status-update'),
    # Offers:
    url(r'^api/offers/$', views.OfferList.as_view(),
        name='offers-list'),
]
