# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸 (Blueking) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from apps.gsekit.configfile import mock_data
from apps.gsekit.process.serializers.process import ProcessFilterBaseSerializer


class LatestConfigInstanceRequestSerializer(serializers.Serializer):
    config_template_id = serializers.IntegerField(help_text=_("配置模板ID"))
    bk_process_id = serializers.IntegerField(help_text=_("进程实例ID"))
    inst_id = serializers.IntegerField(help_text=_("InstID"), required=False)

    class Meta:
        swagger_schema_fields = {"example": mock_data.LATEST_CONFIG_INSTANCE_REQUEST_BODY}


class LatestConfigInstanceResponseSerializer(serializers.Serializer):
    class Meta:
        swagger_schema_fields = {"example": mock_data.LATEST_CONFIG_INSTANCE_RESPONSE}


class ListConfigInstancesRequestSerializer(ProcessFilterBaseSerializer):
    bk_cloud_ids = serializers.ListField(help_text=_("云区域ID列表"), required=False)
    process_status = serializers.IntegerField(help_text=_("进程状态"), required=False)
    is_auto = serializers.BooleanField(help_text=_("托管状态"), required=False)
    config_template_id = serializers.IntegerField(help_text=_("配置模板ID"), required=False)
    config_version_ids = serializers.ListField(help_text=_("配置模板版本ID列表"), required=False)
    filter_released = serializers.BooleanField(help_text=_("是否过滤出已下发的版本"), required=False)

    class Meta:
        swagger_schema_fields = {"example": mock_data.LIST_CONFIG_INSTANCES_REQUEST_BODY}


class ListConfigInstancesResponseSerializer(serializers.Serializer):
    class Meta:
        swagger_schema_fields = {"example": mock_data.LIST_CONFIG_INSTANCES_RESPONSE_BODY}


class RetrieveConfigInstancResponseSerializer(serializers.Serializer):
    class Meta:
        swagger_schema_fields = {"example": mock_data.RETRIEVE_CONFIG_INSTANCE_RESPONSE_BODY}


class TopoInstSerializer(serializers.Serializer):
    node_id = serializers.CharField(help_text=_("节点ID"))
    node_type = serializers.CharField(help_text=_("节点类型"))


class GetConfigInstanceByAppTopoRequestSerializer(serializers.Serializer):
    sha256 = serializers.CharField(help_text=_("当前文件配置sha256"))
    topo_list = serializers.ListField(help_text=_("过滤拓扑节点列表"), child=TopoInstSerializer())

    class Meta:
        swagger_schema_fields = {
            "example": {
                "sha256": "current sha256",
                "filter_topo_list": [
                    {"node_id": "cmdb", "node_type": "application"},
                    {"node_id": "execute-service", "node_type": "service"},
                    {"node_id": "execute-service-2", "node_type": "service_inst"},
                ],
            }
        }


class GetConfigInstanceByAppTopoResponseSerializer(serializers.Serializer):
    config = serializers.CharField(help_text=_("配置内容"))
    sha256 = serializers.CharField(help_text=_("配置文件sha256"))
    has_change = serializers.BooleanField(help_text=_("是否有变更"))

    class Meta:
        swagger_schema_fields = {
            "example": {"has_change": True, "sha256": "new config sha256", "config": "config content"}
        }


class CreateConfigInstanceRequestSerializer(serializers.Serializer):
    content = serializers.CharField(help_text=_("配置内容"))
    sha256 = serializers.CharField(help_text=_("配置文件sha256"))

    class Meta:
        swagger_schema_fields = {"content": "config content", "sha256": "sha256"}


class CreateConfigInstanceResponseSerializer(serializers.Serializer):
    config_instance_id = serializers.IntegerField(help_text=_("配置实例ID"))

    class Meta:
        swagger_schema_fields = {"config_instance_id": 1}


class BindConfigInstanceToAppTopoRequestSerializer(serializers.Serializer):
    config_instance_id = serializers.IntegerField(help_text=_("配置实例ID"))
    topo_list = serializers.ListField(help_text=_("过滤拓扑节点列表"), child=TopoInstSerializer())

    class Meta:
        swagger_schema_fields = {
            "example": {
                "config_instance_id": 1,
                "topo_list": [
                    {"node_id": "biz_2", "node_type": "business"},
                    {"node_id": "cmdb", "node_type": "application"},
                    {"node_id": "execute-service", "node_type": "service"},
                    {"node_id": "execute-service-2", "node_type": "service_inst"},
                ],
            }
        }


class BindConfigInstanceToAppTopoResponseSerializer(serializers.Serializer):
    class Meta:
        swagger_schema_fields = {}
