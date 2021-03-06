from django.conf.urls import url, include
from .views import (
    vessel_listview,
    berth_schedule,
    view_history,
    remove_arrival,
    remove_arrival_two,
    edit_arrival,
    vessel_timestamp,
    edit_arrival_done,
    vessel_info_details,
    remove_vessel,
    connot_remove_vessel,
    edit_vessel,
    edit_vessel_done,
    notification,
    notification_confirm,
    vessel_progress,
    vessel_no_progress

)

urlpatterns = [
    url('^$', vessel_listview, name="index"), 
    url('^vessel-details/$', vessel_info_details, name='vessel_info_details'),
    url('^vessel-timestamp/$', vessel_timestamp, name="vessel_timestamp"),
    url('^berth-schedule/$', berth_schedule, name="berthSchedule"),
    url('^history/$', view_history, name="viewHistory"),
    url('^remove_items_two/(?P<item_id>[0-9]+)/$', remove_arrival_two, name="remove_arrival_two"),
    url('^remove_items/(?P<item_id>[0-9]+)/$', remove_arrival, name="remove_arrival"),
    url('^remove-vessel/(?P<item_id>[0-9]+)/$', remove_vessel, name="remove_vessel"),
    url('^delete-warning/', connot_remove_vessel, name="connot_remove_vessel"),
    url('^edit_vessels/(?P<item_id>[0-9]+)/$', edit_arrival, name="edit_arrival"),
    url('^edit-vessel/(?P<item_id>[0-9]+)/$', edit_vessel, name = 'edit_vessel'),
    url('^edit_vessels/(?P<item_id>[0-9]+)/edit/$', edit_arrival_done, name="edit_arrival_done"),
    url('^edit-vessel/(?P<item_id>[0-9]+)/edit_vessel/$', edit_vessel_done, name="edit_vessel_done"),
    url('^notification/$', notification, name = 'notification'),
    url('^notification/(?P<item_id>[0-9]+)/$', notification_confirm, name="notification_confirm"),
    url('^vessel-progress/(?P<item_id>[0-9]+)/$', vessel_progress, name='vessel_progress'),
    url('^vessel-no-progress/$', vessel_no_progress, name='vessel_no_progress')
]
