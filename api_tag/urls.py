"""api_tag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapi import views
from django.contrib.auth.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tag_home/', views.index, name='tag_home'),
    path('beanstalk_forum/', views.beanstalk_home, name='beanstalk_home'),

    path('beanstalk_policy/', views.beanstalk_policy, name='beanstalk_exe2'),

    # Downloads
    path('download_log/',views.download_log,name='download_log'),
    path('download_assetrr/', views.download_assetrr, name='download_assetrr'),


    path('beanstalk_amendment/', views.policy_endorsement, name='beanstalk_amendment'),
    path('beanstalk_transition/', views.policy_versioning, name='beanstalk_transition'),

    path('tag_user_login/',views.tag_user_login,name="tag_user_login"),
    path('tag_user_logout/',views.tag_user_logout,name="tag_user_logout"),
    path('tag_register/',views.tag_register,name="tag_register"),

    path('beanstalk_asset_home/',views.beanstalk_asset,name='beanstalk_asset_home'),
    path('asset_execution/', views.asset_execution, name='asset_execution'),

    path('load_check/',views.startp),

    # INSPECTOR
    path('inspector_tag/',views.inspector_tag,name='inspector_tag'),
    path('inspector_log/', views.download_trace, name='inspector_log'),

    # -------------------- TEST CHAMBER - PATH ------------------------
    path('test_chamber_home/', views.test_chamber, name="test_chamber_home"),
    path('test_suite_home/',views.test_suite_home,name='test_suite_home'),
    path('asset_end_to_end_home/',views.asset_end_to_end_home,name='asset_end_to_end_home'),

    # TEST SUITE FUNCTIONS:
    path('asset_homecontent_suite/',views.asset_homecon_suite,name='asset_homecontent_suite'),
    path('asset_end_to_end/', views.asset_end_to_end, name='asset_end_to_end'),
    path('asset_vehicle_suite/',views.asset_vehicle_suite,name='asset_vehicle_suite'),
    path('asset_allrisks_suite/', views.asset_allrisk_suite, name='asset_allrisk_suite'),
    path('asset_personal_liability/', views.asset_personal_liability_suite, name='asset_personal_liability'),

    path('test_report/', views.test_report, name='test_report'),

    path('test_load/',views.test_load,name='test_load')
]
