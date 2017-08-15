# noinspection PyUnresolvedReferences
from django.conf.urls import url, include
# noinspection PyUnresolvedReferences,PyUnresolvedReferences
from django_pdfkit import PDFView
from .views import *


urlpatterns = [
    url(r'^home/$', dashboard, name='dashboard'),
    url(r'^home/$', dashboard_nav, name='dashboard-nav'),
    url(r'^report/view-1/(?P<project_id>[\-\w]+)/$', report_template_one, name='template_one'),
    url(r'^report/email/csv/(?P<project_id>[\-\w]+)/$', send_csv_attachment_email, name='email-csv'),
    url(r'^report/csv/(?P<project_id>[\-\w]+)/$', export_to_csv, name='csv'),
    url(r'^my-pdf/$', PDFView.as_view(template_name='report/my-pdf.html'), name='my-pdf'),
    url(r'^data/$', get_data_test),
    url(r'^chart/(?P<project_id>[\-\w]+)/$', demo_piechart),
]
