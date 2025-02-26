

from django.urls import path

from expenses import views as vs


urlpatterns = [
    path('', vs.index, name='test_pay'),
    path('sources/', vs.Sources.as_view(), name='test_pay2'),
    path('transactions/', vs.Transactions.as_view(), name='test_pay3'),
    path('transfers/', vs.Transfers.as_view(), name='test_pay4'),

]



