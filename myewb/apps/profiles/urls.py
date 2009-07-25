"""myEWB profile URLs

This file is part of myEWB
Copyright 2009 Engineers Without Borders (Canada) Organisation and/or volunteer contributors

Created on: 2009-06-30
Last modified: 2009-07-21
@author: Joshua Gorner
"""
from django.conf.urls.defaults import *

urlpatterns = patterns('profiles.views',
    url(r'^$', 'profiles', name='profiles_index'),    
    url(r'^$', 'profiles', name='profile_list'),    
    url(r'^(?P<username>[\w\._-]+)/$', 'profile', name='profile_detail'),

    url(r'^(?P<username>[\w\._-]+)/student/(?P<student_record_id>\d+)/$', 'student_record_detail', name='profile_student_record'),
    url(r'^(?P<username>[\w\._-]+)/student/(?P<student_record_id>\d+)/$', 'student_record_detail', name='student_record_detail'),
    url(r'^(?P<username>[\w\._-]+)/student/(?P<student_record_id>\d+)/delete/$', 'delete_student_record', name='delete_student_record'),
    url(r'^(?P<username>[\w\._-]+)/student/$', 'student_records_index', name='student_records_index'),
    url(r'^(?P<username>[\w\._-]+)/student/new/$', 'new_student_record', name='new_student_record'),
    url(r'^(?P<username>[\w\._-]+)/student/(?P<student_record_id>\d+)/edit/$', 'edit_student_record', name='edit_student_record'),

    url(r'^(?P<username>[\w\._-]+)/work/(?P<work_record_id>\d+)/$', 'work_record_detail', name='profile_work_record'),
    url(r'^(?P<username>[\w\._-]+)/work/(?P<work_record_id>\d+)/$', 'work_record_detail', name='work_record_detail'),
    url(r'^(?P<username>[\w\._-]+)/work/(?P<work_record_id>\d+)/delete/$', 'delete_work_record', name='delete_work_record'),
    url(r'^(?P<username>[\w\._-]+)/work/$', 'work_records_index', name='work_records_index'),
    url(r'^(?P<username>[\w\._-]+)/work/new/$', 'new_work_record', name='new_work_record'),
    url(r'^(?P<username>[\w\._-]+)/work/(?P<work_record_id>\d+)/edit/$', 'edit_work_record', name='edit_work_record'),
    
    url(r'^(?P<username>[\w\._-]+)/search/$', 'search_profile', name='profile_search'),
)

urlpatterns = urlpatterns + patterns('misc.views',
    url(r'^username_autocomplete/$', 'username_autocomplete_friends', name='profile_username_autocomplete'),
)