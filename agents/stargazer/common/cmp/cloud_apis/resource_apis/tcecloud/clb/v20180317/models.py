# -*- coding: utf8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from common.cmp.cloud_apis.resource_apis.tcecloud.common.abstract_model import AbstractModel


class AddCustomizedConfigRequest(AbstractModel):
    """AddCustomizedConfig请求参数结构体"""

    def __init__(self):
        """
        :param ConfigName: 配置名字
        :type ConfigName: str
        :param ConfigType: 配置类型
        :type ConfigType: str
        :param ConfigContent: 配置内容
        :type ConfigContent: str
        """
        self.ConfigName = None
        self.ConfigType = None
        self.ConfigContent = None

    def _deserialize(self, params):
        self.ConfigName = params.get("ConfigName")
        self.ConfigType = params.get("ConfigType")
        self.ConfigContent = params.get("ConfigContent")


class AddCustomizedConfigResponse(AbstractModel):
    """AddCustomizedConfig返回参数结构体"""

    def __init__(self):
        """
        :param ConfigId: 配置ID
        :type ConfigId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ConfigId = None
        self.RequestId = None

    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.RequestId = params.get("RequestId")


class AssociateCustomizedConfigRequest(AbstractModel):
    """AssociateCustomizedConfig请求参数结构体"""

    def __init__(self):
        """
        :param UconfigId: 配置ID
        :type UconfigId: str
        :param BindList: 关联的server或location
        :type BindList: list of BindItem
        """
        self.UconfigId = None
        self.BindList = None

    def _deserialize(self, params):
        self.UconfigId = params.get("UconfigId")
        if params.get("BindList") is not None:
            self.BindList = []
            for item in params.get("BindList"):
                obj = BindItem()
                obj._deserialize(item)
                self.BindList.append(obj)


class AssociateCustomizedConfigResponse(AbstractModel):
    """AssociateCustomizedConfig返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateTargetGroupsRequest(AbstractModel):
    """AssociateTargetGroups请求参数结构体"""

    def __init__(self):
        """
        :param Associations: 绑定的关系数组
        :type Associations: list of TargetGroupAssociation
        """
        self.Associations = None

    def _deserialize(self, params):
        if params.get("Associations") is not None:
            self.Associations = []
            for item in params.get("Associations"):
                obj = TargetGroupAssociation()
                obj._deserialize(item)
                self.Associations.append(obj)


class AssociateTargetGroupsResponse(AbstractModel):
    """AssociateTargetGroups返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociationItem(AbstractModel):
    """目标组关联到的规则"""

    def __init__(self):
        """
                :param LoadBalancerId: 关联到的负载均衡ID
                :type LoadBalancerId: str
                :param ListenerId: 关联到的监听器ID
                :type ListenerId: str
                :param LocationId: 关联到的转发规则ID
        注意：此字段可能返回 null，表示取不到有效值。
                :type LocationId: str
                :param Protocol: 关联到的监听器协议类型，如HTTP,TCP,
                :type Protocol: str
                :param Port: 关联到的监听器端口
                :type Port: int
                :param Domain: 关联到的转发规则域名
        注意：此字段可能返回 null，表示取不到有效值。
                :type Domain: str
                :param Url: 关联到的转发规则URL
        注意：此字段可能返回 null，表示取不到有效值。
                :type Url: str
                :param LoadBalancerName: 负载均衡名称
                :type LoadBalancerName: str
                :param ListenerName: 监听器名称
                :type ListenerName: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationId = None
        self.Protocol = None
        self.Port = None
        self.Domain = None
        self.Url = None
        self.LoadBalancerName = None
        self.ListenerName = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationId = params.get("LocationId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.ListenerName = params.get("ListenerName")


class AutoRewriteRequest(AbstractModel):
    """AutoRewrite请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID
        :type LoadBalancerId: str
        :param ListenerId: HTTPS:443监听器的ID
        :type ListenerId: str
        :param Domains: HTTPS:443监听器下需要重定向的域名
        :type Domains: list of str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domains = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domains = params.get("Domains")


class AutoRewriteResponse(AbstractModel):
    """AutoRewrite返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Backend(AbstractModel):
    """监听器绑定的后端服务的详细信息"""

    def __init__(self):
        """
                :param Type: 后端服务的类型，可取：CVM、ENI（即将支持）
                :type Type: str
                :param InstanceId: 后端服务的唯一 ID，如 ins-abcd1234
                :type InstanceId: str
                :param Port: 后端服务的监听端口
                :type Port: int
                :param Weight: 后端服务的转发权重，取值范围：[0, 100]，默认为 10。
                :type Weight: int
                :param PublicIpAddresses: 后端服务的外网 IP
        注意：此字段可能返回 null，表示取不到有效值。
                :type PublicIpAddresses: list of str
                :param PrivateIpAddresses: 后端服务的内网 IP
        注意：此字段可能返回 null，表示取不到有效值。
                :type PrivateIpAddresses: list of str
                :param InstanceName: 后端服务的实例名称
        注意：此字段可能返回 null，表示取不到有效值。
                :type InstanceName: str
                :param RegisteredTime: 后端服务被绑定的时间
        注意：此字段可能返回 null，表示取不到有效值。
                :type RegisteredTime: str
                :param EniId: 弹性网卡唯一ID，如 eni-1234abcd
        注意：此字段可能返回 null，表示取不到有效值。
                :type EniId: str
        """
        self.Type = None
        self.InstanceId = None
        self.Port = None
        self.Weight = None
        self.PublicIpAddresses = None
        self.PrivateIpAddresses = None
        self.InstanceName = None
        self.RegisteredTime = None
        self.EniId = None

    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.InstanceName = params.get("InstanceName")
        self.RegisteredTime = params.get("RegisteredTime")
        self.EniId = params.get("EniId")


class BasicTargetGroupInfo(AbstractModel):
    """监听器或者转发规则绑定的目标组基本信息"""

    def __init__(self):
        """
        :param TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param TargetGroupName: 目标组名称
        :type TargetGroupName: str
        """
        self.TargetGroupId = None
        self.TargetGroupName = None

    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.TargetGroupName = params.get("TargetGroupName")


class BatchDeregisterTargetsRequest(AbstractModel):
    """BatchDeregisterTargets请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡ID
        :type LoadBalancerId: str
        :param Targets: 解绑目标
        :type Targets: list of BatchTarget
        """
        self.LoadBalancerId = None
        self.Targets = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self.Targets.append(obj)


class BatchDeregisterTargetsResponse(AbstractModel):
    """BatchDeregisterTargets返回参数结构体"""

    def __init__(self):
        """
        :param FailListenerIdSet: 解绑失败的监听器ID
        :type FailListenerIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FailListenerIdSet = None
        self.RequestId = None

    def _deserialize(self, params):
        self.FailListenerIdSet = params.get("FailListenerIdSet")
        self.RequestId = params.get("RequestId")


class BatchModifyTargetWeightRequest(AbstractModel):
    """BatchModifyTargetWeight请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ModifyList: 要批量修改权重的列表
        :type ModifyList: list of RsWeightRule
        """
        self.LoadBalancerId = None
        self.ModifyList = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ModifyList") is not None:
            self.ModifyList = []
            for item in params.get("ModifyList"):
                obj = RsWeightRule()
                obj._deserialize(item)
                self.ModifyList.append(obj)


class BatchModifyTargetWeightResponse(AbstractModel):
    """BatchModifyTargetWeight返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BatchRegisterTargetsRequest(AbstractModel):
    """BatchRegisterTargets请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡ID
        :type LoadBalancerId: str
        :param Targets: 绑定目标
        :type Targets: list of BatchTarget
        """
        self.LoadBalancerId = None
        self.Targets = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self.Targets.append(obj)


class BatchRegisterTargetsResponse(AbstractModel):
    """BatchRegisterTargets返回参数结构体"""

    def __init__(self):
        """
        :param FailListenerIdSet: 绑定失败的监听器ID，如为空表示全部绑定成功。
        :type FailListenerIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FailListenerIdSet = None
        self.RequestId = None

    def _deserialize(self, params):
        self.FailListenerIdSet = params.get("FailListenerIdSet")
        self.RequestId = params.get("RequestId")


class BatchTarget(AbstractModel):
    """批量绑定类型"""

    def __init__(self):
        """
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param Port: 绑定端口
        :type Port: int
        :param InstanceId: 子机ID
        :type InstanceId: str
        :param EniIp: 弹性网卡ip
        :type EniIp: str
        :param Weight: 子机权重，范围[0, 100]。绑定时如果不存在，则默认为10。
        :type Weight: int
        :param LocationId: 七层规则ID
        :type LocationId: str
        """
        self.ListenerId = None
        self.Port = None
        self.InstanceId = None
        self.EniIp = None
        self.Weight = None
        self.LocationId = None

    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        self.EniIp = params.get("EniIp")
        self.Weight = params.get("Weight")
        self.LocationId = params.get("LocationId")


class BindConfigItem(AbstractModel):
    """配置绑定关系，含配置ID。"""

    def __init__(self):
        """
                :param UconfigId: 配置ID
                :type UconfigId: str
                :param LoadBalancerId: 配置绑定的CLB ID
                :type LoadBalancerId: str
                :param ListenerId: 配置绑定的监听器ID
                :type ListenerId: str
                :param Domain: 配置绑定的域名
                :type Domain: str
                :param LocationId: 配置绑定的规则
        注意：此字段可能返回 null，表示取不到有效值。
                :type LocationId: str
        """
        self.UconfigId = None
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domain = None
        self.LocationId = None

    def _deserialize(self, params):
        self.UconfigId = params.get("UconfigId")
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.LocationId = params.get("LocationId")


class BindDetailItem(AbstractModel):
    """绑定关系，包含监听器名字、协议、url、vport。"""

    def __init__(self):
        """
                :param LoadBalancerId: 配置绑定的CLB ID
                :type LoadBalancerId: str
                :param ListenerId: 配置绑定的监听器ID
        注意：此字段可能返回 null，表示取不到有效值。
                :type ListenerId: str
                :param Domain: 配置绑定的域名
        注意：此字段可能返回 null，表示取不到有效值。
                :type Domain: str
                :param LocationId: 配置绑定的规则
        注意：此字段可能返回 null，表示取不到有效值。
                :type LocationId: str
                :param ListenerName: 监听器名字
        注意：此字段可能返回 null，表示取不到有效值。
                :type ListenerName: str
                :param Protocol: 监听器协议
        注意：此字段可能返回 null，表示取不到有效值。
                :type Protocol: str
                :param Vport: 监听器端口
        注意：此字段可能返回 null，表示取不到有效值。
                :type Vport: int
                :param Url: location的url
        注意：此字段可能返回 null，表示取不到有效值。
                :type Url: str
                :param UconfigId: 配置ID
        注意：此字段可能返回 null，表示取不到有效值。
                :type UconfigId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domain = None
        self.LocationId = None
        self.ListenerName = None
        self.Protocol = None
        self.Vport = None
        self.Url = None
        self.UconfigId = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.LocationId = params.get("LocationId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.Vport = params.get("Vport")
        self.Url = params.get("Url")
        self.UconfigId = params.get("UconfigId")


class BindItem(AbstractModel):
    """配置绑定关系"""

    def __init__(self):
        """
                :param LoadBalancerId: 配置绑定的CLB ID
                :type LoadBalancerId: str
                :param ListenerId: 配置绑定的监听器ID
        注意：此字段可能返回 null，表示取不到有效值。
                :type ListenerId: str
                :param Domain: 配置绑定的域名
        注意：此字段可能返回 null，表示取不到有效值。
                :type Domain: str
                :param LocationId: 配置绑定的规则
        注意：此字段可能返回 null，表示取不到有效值。
                :type LocationId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domain = None
        self.LocationId = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.LocationId = params.get("LocationId")


class BlockedIP(AbstractModel):
    """加入了12306黑名单的IP"""

    def __init__(self):
        """
        :param IP: 黑名单IP
        :type IP: str
        :param CreateTime: 加入黑名单的时间
        :type CreateTime: str
        :param ExpireTime: 过期时间
        :type ExpireTime: str
        """
        self.IP = None
        self.CreateTime = None
        self.ExpireTime = None

    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")


class CertIdRelatedWithLoadBalancers(AbstractModel):
    """证书ID，以及与该证书ID关联的负载均衡实例列表"""

    def __init__(self):
        """
                :param CertId: 证书ID
                :type CertId: str
                :param LoadBalancers: 与证书关联的负载均衡实例列表
        注意：此字段可能返回 null，表示取不到有效值。
                :type LoadBalancers: list of LoadBalancer
        """
        self.CertId = None
        self.LoadBalancers = None

    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        if params.get("LoadBalancers") is not None:
            self.LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self.LoadBalancers.append(obj)


class CertificateInput(AbstractModel):
    """证书信息"""

    def __init__(self):
        """
        :param SSLMode: 认证类型，UNIDIRECTIONAL：单向认证，MUTUAL：双向认证
        :type SSLMode: str
        :param CertId: 服务端证书的 ID，如果不填写此项则必须上传证书，包括 CertContent，CertKey，CertName。
        :type CertId: str
        :param CertCaId: 客户端证书的 ID，当监听器采用双向认证，即 SSLMode=MUTUAL 时，如果不填写此项则必须上传客户端证书，包括 CertCaContent，CertCaName。
        :type CertCaId: str
        :param CertName: 上传服务端证书的名称，如果没有 CertId，则此项必传。
        :type CertName: str
        :param CertKey: 上传服务端证书的 key，如果没有 CertId，则此项必传。
        :type CertKey: str
        :param CertContent: 上传服务端证书的内容，如果没有 CertId，则此项必传。
        :type CertContent: str
        :param CertCaName: 上传客户端 CA 证书的名称，如果 SSLMode=mutual，如果没有 CertCaId，则此项必传。
        :type CertCaName: str
        :param CertCaContent: 上传客户端证书的内容，如果 SSLMode=mutual，如果没有 CertCaId，则此项必传。
        :type CertCaContent: str
        """
        self.SSLMode = None
        self.CertId = None
        self.CertCaId = None
        self.CertName = None
        self.CertKey = None
        self.CertContent = None
        self.CertCaName = None
        self.CertCaContent = None

    def _deserialize(self, params):
        self.SSLMode = params.get("SSLMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        self.CertName = params.get("CertName")
        self.CertKey = params.get("CertKey")
        self.CertContent = params.get("CertContent")
        self.CertCaName = params.get("CertCaName")
        self.CertCaContent = params.get("CertCaContent")


class CertificateOutput(AbstractModel):
    """证书相关信息"""

    def __init__(self):
        """
                :param SSLMode: 认证类型，UNIDIRECTIONAL：单向认证，MUTUAL：双向认证
                :type SSLMode: str
                :param CertId: 服务端证书的 ID。
                :type CertId: str
                :param CertCaId: 客户端证书的 ID。
        注意：此字段可能返回 null，表示取不到有效值。
                :type CertCaId: str
        """
        self.SSLMode = None
        self.CertId = None
        self.CertCaId = None

    def _deserialize(self, params):
        self.SSLMode = params.get("SSLMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")


class ClassicalHealth(AbstractModel):
    """传统型负载均衡后端服务的健康状态"""

    def __init__(self):
        """
        :param IP: 后端服务的内网 IP
        :type IP: str
        :param Port: 后端服务的端口
        :type Port: int
        :param ListenerPort: 负载均衡的监听端口
        :type ListenerPort: int
        :param Protocol: 转发协议
        :type Protocol: str
        :param HealthStatus: 健康检查结果，1 表示健康，0 表示不健康
        :type HealthStatus: int
        """
        self.IP = None
        self.Port = None
        self.ListenerPort = None
        self.Protocol = None
        self.HealthStatus = None

    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Port = params.get("Port")
        self.ListenerPort = params.get("ListenerPort")
        self.Protocol = params.get("Protocol")
        self.HealthStatus = params.get("HealthStatus")


class ClassicalListener(AbstractModel):
    """传统型负载均衡监听器信息"""

    def __init__(self):
        """
        :param ListenerId: 负载均衡监听器ID
        :type ListenerId: str
        :param ListenerPort: 负载均衡监听器端口
        :type ListenerPort: int
        :param InstancePort: 监听器后端转发端口
        :type InstancePort: int
        :param ListenerName: 监听器名称
        :type ListenerName: str
        :param Protocol: 监听器协议类型
        :type Protocol: str
        :param SessionExpire: 会话保持时间
        :type SessionExpire: int
        :param HealthSwitch: 是否开启了健康检查：1（开启）、0（关闭）
        :type HealthSwitch: int
        :param TimeOut: 响应超时时间
        :type TimeOut: int
        :param IntervalTime: 检查间隔
        :type IntervalTime: int
        :param HealthNum: 健康阈值
        :type HealthNum: int
        :param UnhealthNum: 不健康阈值
        :type UnhealthNum: int
        :param HttpHash: 传统型公网负载均衡的 HTTP、HTTPS 监听器的请求均衡方法。wrr 表示按权重轮询，ip_hash 表示根据访问的源 IP 进行一致性哈希方式来分发
        :type HttpHash: str
        :param HttpCode: 传统型公网负载均衡的 HTTP、HTTPS 监听器的健康检查返回码。具体可参考创建监听器中对该字段的解释
        :type HttpCode: int
        :param HttpCheckPath: 传统型公网负载均衡的 HTTP、HTTPS 监听器的健康检查路径
        :type HttpCheckPath: str
        :param SSLMode: 传统型公网负载均衡的 HTTPS 监听器的认证方式
        :type SSLMode: str
        :param CertId: 传统型公网负载均衡的 HTTPS 监听器的服务端证书 ID
        :type CertId: str
        :param CertCaId: 传统型公网负载均衡的 HTTPS 监听器的客户端证书 ID
        :type CertCaId: str
        :param Status: 监听器的状态，0 表示创建中，1 表示运行中
        :type Status: int
        """
        self.ListenerId = None
        self.ListenerPort = None
        self.InstancePort = None
        self.ListenerName = None
        self.Protocol = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.HttpHash = None
        self.HttpCode = None
        self.HttpCheckPath = None
        self.SSLMode = None
        self.CertId = None
        self.CertCaId = None
        self.Status = None

    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerPort = params.get("ListenerPort")
        self.InstancePort = params.get("InstancePort")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.HttpHash = params.get("HttpHash")
        self.HttpCode = params.get("HttpCode")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.SSLMode = params.get("SSLMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        self.Status = params.get("Status")


class ClassicalLoadBalancerInfo(AbstractModel):
    """负载均衡信息"""

    def __init__(self):
        """
                :param InstanceId: 后端实例ID
                :type InstanceId: str
                :param LoadBalancerIds: 负载均衡实例ID列表
        注意：此字段可能返回 null，表示取不到有效值。
                :type LoadBalancerIds: list of str
        """
        self.InstanceId = None
        self.LoadBalancerIds = None

    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LoadBalancerIds = params.get("LoadBalancerIds")


class ClassicalTarget(AbstractModel):
    """传统型负载均衡的后端服务相关信息"""

    def __init__(self):
        """
                :param Type: 后端服务的类型，可取值：CVM、ENI（即将支持）
                :type Type: str
                :param InstanceId: 后端服务的唯一 ID，可通过 DescribeInstances 接口返回字段中的 unInstanceId 字段获取
                :type InstanceId: str
                :param Weight: 后端服务的转发权重，取值范围：[0, 100]，默认为 10。
                :type Weight: int
                :param PublicIpAddresses: 后端服务的外网 IP
        注意：此字段可能返回 null，表示取不到有效值。
                :type PublicIpAddresses: list of str
                :param PrivateIpAddresses: 后端服务的内网 IP
        注意：此字段可能返回 null，表示取不到有效值。
                :type PrivateIpAddresses: list of str
                :param InstanceName: 后端服务的实例名称
        注意：此字段可能返回 null，表示取不到有效值。
                :type InstanceName: str
                :param RunFlag: 后端服务的状态
        1：故障，2：运行中，3：创建中，4：已关机，5：已退还，6：退还中， 7：重启中，8：开机中，9：关机中，10：密码重置中，11：格式化中，12：镜像制作中，13：带宽设置中，14：重装系统中，19：升级中，21：热迁移中
        注意：此字段可能返回 null，表示取不到有效值。
                :type RunFlag: int
        """
        self.Type = None
        self.InstanceId = None
        self.Weight = None
        self.PublicIpAddresses = None
        self.PrivateIpAddresses = None
        self.InstanceName = None
        self.RunFlag = None

    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.InstanceName = params.get("InstanceName")
        self.RunFlag = params.get("RunFlag")


class ClassicalTargetInfo(AbstractModel):
    """传统型负载均衡的后端信息"""

    def __init__(self):
        """
        :param InstanceId: 后端实例ID
        :type InstanceId: str
        :param Weight: 权重，取值范围 [0, 100]
        :type Weight: int
        """
        self.InstanceId = None
        self.Weight = None

    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")


class Cluster(AbstractModel):
    """集群的详细信息，如集群ID，名称，类型，可用区，标签等"""

    def __init__(self):
        """
                :param ClusterId: 集群唯一ID
                :type ClusterId: str
                :param ClusterName: 集群名称
                :type ClusterName: str
                :param ClusterType: 集群类型，如TGW，STGW，VPCGW
                :type ClusterType: str
                :param ClusterTag: 集群标签，只有STGW集群有标签
        注意：此字段可能返回 null，表示取不到有效值。
                :type ClusterTag: str
                :param Zone: 集群所在可用区，如ap-guangzhou-1
                :type Zone: str
                :param Network: 集群网络类型，如Public，Private
                :type Network: str
                :param MaxConn: 最大连接数
        注意：此字段可能返回 null，表示取不到有效值。
                :type MaxConn: int
                :param MaxInFlow: 最大入带宽
        注意：此字段可能返回 null，表示取不到有效值。
                :type MaxInFlow: int
                :param MaxInPkg: 最大入包量
        注意：此字段可能返回 null，表示取不到有效值。
                :type MaxInPkg: int
                :param MaxOutFlow: 最大出带宽
        注意：此字段可能返回 null，表示取不到有效值。
                :type MaxOutFlow: int
                :param MaxOutPkg: 最大出包量
        注意：此字段可能返回 null，表示取不到有效值。
                :type MaxOutPkg: int
                :param MaxNewConn: 最大新建连接数
        注意：此字段可能返回 null，表示取不到有效值。
                :type MaxNewConn: int
                :param HTTPMaxNewConn: http最大新建连接数
        注意：此字段可能返回 null，表示取不到有效值。
                :type HTTPMaxNewConn: int
                :param HTTPSMaxNewConn: https最大新建连接数
        注意：此字段可能返回 null，表示取不到有效值。
                :type HTTPSMaxNewConn: int
                :param HTTPQps: http QPS
        注意：此字段可能返回 null，表示取不到有效值。
                :type HTTPQps: int
                :param HTTPSQps: https QPS
        注意：此字段可能返回 null，表示取不到有效值。
                :type HTTPSQps: int
                :param ResourceCount: 集群内资源总数目
                :type ResourceCount: int
                :param IdleResourceCount: 集群内空闲资源数目
        注意：此字段可能返回 null，表示取不到有效值。
                :type IdleResourceCount: int
                :param LoadBalanceDirectorCount: 集群内转发机的数目
        注意：此字段可能返回 null，表示取不到有效值。
                :type LoadBalanceDirectorCount: int
                :param Isp: 集群的Isp属性，如："BGP","CMCC","CUCC","CTCC","INTERNAL"。
        注意：此字段可能返回 null，表示取不到有效值。
                :type Isp: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.ClusterType = None
        self.ClusterTag = None
        self.Zone = None
        self.Network = None
        self.MaxConn = None
        self.MaxInFlow = None
        self.MaxInPkg = None
        self.MaxOutFlow = None
        self.MaxOutPkg = None
        self.MaxNewConn = None
        self.HTTPMaxNewConn = None
        self.HTTPSMaxNewConn = None
        self.HTTPQps = None
        self.HTTPSQps = None
        self.ResourceCount = None
        self.IdleResourceCount = None
        self.LoadBalanceDirectorCount = None
        self.Isp = None

    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterType = params.get("ClusterType")
        self.ClusterTag = params.get("ClusterTag")
        self.Zone = params.get("Zone")
        self.Network = params.get("Network")
        self.MaxConn = params.get("MaxConn")
        self.MaxInFlow = params.get("MaxInFlow")
        self.MaxInPkg = params.get("MaxInPkg")
        self.MaxOutFlow = params.get("MaxOutFlow")
        self.MaxOutPkg = params.get("MaxOutPkg")
        self.MaxNewConn = params.get("MaxNewConn")
        self.HTTPMaxNewConn = params.get("HTTPMaxNewConn")
        self.HTTPSMaxNewConn = params.get("HTTPSMaxNewConn")
        self.HTTPQps = params.get("HTTPQps")
        self.HTTPSQps = params.get("HTTPSQps")
        self.ResourceCount = params.get("ResourceCount")
        self.IdleResourceCount = params.get("IdleResourceCount")
        self.LoadBalanceDirectorCount = params.get("LoadBalanceDirectorCount")
        self.Isp = params.get("Isp")


class ClusterItem(AbstractModel):
    """独占集群信息"""

    def __init__(self):
        """
                :param ClusterId: 集群唯一ID
                :type ClusterId: str
                :param ClusterName: 集群名称
        注意：此字段可能返回 null，表示取不到有效值。
                :type ClusterName: str
                :param Zone: 集群所在可用区，如ap-guangzhou-1
        注意：此字段可能返回 null，表示取不到有效值。
                :type Zone: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Zone = None

    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Zone = params.get("Zone")


class ClusterResource(AbstractModel):
    """集群内资源类型"""

    def __init__(self):
        """
                :param ClusterId: 集群唯一ID，如tgw-12345678。
                :type ClusterId: str
                :param Vip: ip地址。
                :type Vip: str
                :param LoadBalancerId: 负载均衡唯一ID，如lb-12345678。
        注意：此字段可能返回 null，表示取不到有效值。
                :type LoadBalancerId: str
                :param Idle: 资源是否闲置。
        注意：此字段可能返回 null，表示取不到有效值。
                :type Idle: str
                :param ClusterName: 集群名称。
                :type ClusterName: str
        """
        self.ClusterId = None
        self.Vip = None
        self.LoadBalancerId = None
        self.Idle = None
        self.ClusterName = None

    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Vip = params.get("Vip")
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Idle = params.get("Idle")
        self.ClusterName = params.get("ClusterName")


class ConfigListItem(AbstractModel):
    """配置内容"""

    def __init__(self):
        """
                :param UconfigId: 配置ID
                :type UconfigId: str
                :param ConfigType: 配置类型
                :type ConfigType: str
                :param ConfigName: 配置名字
        注意：此字段可能返回 null，表示取不到有效值。
                :type ConfigName: str
                :param ConfigContent: 配置内容
                :type ConfigContent: str
                :param CreateTimestamp: 增加配置时间
                :type CreateTimestamp: str
                :param UpdateTimestamp: 修改配置时间
                :type UpdateTimestamp: str
        """
        self.UconfigId = None
        self.ConfigType = None
        self.ConfigName = None
        self.ConfigContent = None
        self.CreateTimestamp = None
        self.UpdateTimestamp = None

    def _deserialize(self, params):
        self.UconfigId = params.get("UconfigId")
        self.ConfigType = params.get("ConfigType")
        self.ConfigName = params.get("ConfigName")
        self.ConfigContent = params.get("ConfigContent")
        self.CreateTimestamp = params.get("CreateTimestamp")
        self.UpdateTimestamp = params.get("UpdateTimestamp")


class CreateListenerRequest(AbstractModel):
    """CreateListener请求参数结构体"""

    def __init__(self):
        """
                :param LoadBalancerId: 负载均衡实例 ID
                :type LoadBalancerId: str
                :param Ports: 要将监听器创建到哪些端口，每个端口对应一个新的监听器
                :type Ports: list of int
                :param Protocol: 监听器协议： TCP | UDP | HTTP | HTTPS | TCP_SSL（TCP_SSL 正在内测中，如需使用请通过工单申请）
                :type Protocol: str
                :param ListenerNames: 要创建的监听器名称列表，名称与Ports数组按序一一对应，如不需立即命名，则无需提供此参数
                :type ListenerNames: list of str
                :param HealthCheck: 健康检查相关参数，此参数仅适用于TCP/UDP/TCP_SSL监听器
                :type HealthCheck: :class:`tcecloud.clb.v20180317.models.HealthCheck`
                :param Certificate: 证书相关信息，此参数仅适用于TCP_SSL监听器和未开启SNI特性的HTTPS监听器。
                :type Certificate: :class:`tcecloud.clb.v20180317.models.CertificateInput`
                :param SessionExpireTime: 会话保持时间，单位：秒。可选值：30~3600，默认 0，表示不开启。此参数仅适用于TCP/UDP监听器。
                :type SessionExpireTime: int
                :param Scheduler: 监听器转发的方式。可选值：WRR、LEAST_CONN
        分别表示按权重轮询、最小连接数， 默认为 WRR。此参数仅适用于TCP/UDP/TCP_SSL监听器。
                :type Scheduler: str
                :param SniSwitch: 是否开启SNI特性，此参数仅适用于HTTPS监听器。
                :type SniSwitch: int
                :param TargetType: 后端目标类型，NODE表示绑定普通节点，TARGETGROUP表示绑定目标组。
                :type TargetType: str
        """
        self.LoadBalancerId = None
        self.Ports = None
        self.Protocol = None
        self.ListenerNames = None
        self.HealthCheck = None
        self.Certificate = None
        self.SessionExpireTime = None
        self.Scheduler = None
        self.SniSwitch = None
        self.TargetType = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Ports = params.get("Ports")
        self.Protocol = params.get("Protocol")
        self.ListenerNames = params.get("ListenerNames")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.SessionExpireTime = params.get("SessionExpireTime")
        self.Scheduler = params.get("Scheduler")
        self.SniSwitch = params.get("SniSwitch")
        self.TargetType = params.get("TargetType")


class CreateListenerResponse(AbstractModel):
    """CreateListener返回参数结构体"""

    def __init__(self):
        """
        :param ListenerIds: 创建的监听器的唯一标识数组
        :type ListenerIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ListenerIds = None
        self.RequestId = None

    def _deserialize(self, params):
        self.ListenerIds = params.get("ListenerIds")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancerRequest(AbstractModel):
    """CreateLoadBalancer请求参数结构体"""

    def __init__(self):
        """
                :param LoadBalancerType: 负载均衡实例的网络类型：
        OPEN：公网属性， INTERNAL：内网属性。
                :type LoadBalancerType: str
                :param Forward: 负载均衡实例的类型。1：通用的负载均衡实例，目前只支持传入1
                :type Forward: int
                :param LoadBalancerName: 负载均衡实例的名称，只在创建一个实例的时候才会生效。规则：1-50 个英文、汉字、数字、连接线“-”或下划线“_”。
        注意：如果名称与系统中已有负载均衡实例的名称相同，则系统将会自动生成此次创建的负载均衡实例的名称。
                :type LoadBalancerName: str
                :param VpcId: 负载均衡后端目标设备所属的网络 ID，如vpc-12345678，可以通过 DescribeVpcEx 接口获取。 不传此参数则默认为基础网络（"0"）。
                :type VpcId: str
                :param SubnetId: 在私有网络内购买内网负载均衡实例的情况下，必须指定子网 ID，内网负载均衡实例的 VIP 将从这个子网中产生。
                :type SubnetId: str
                :param ProjectId: 负载均衡实例所属的项目 ID，可以通过 DescribeProject 接口获取。不传此参数则视为默认项目。
                :type ProjectId: int
                :param AddressIPVersion: 仅适用于公网负载均衡。IP版本，可取值：IPV4、IPV6、IPv6FullChain，默认值 IPV4。
                :type AddressIPVersion: str
                :param Number: 创建负载均衡的个数，默认值 1。
                :type Number: int
                :param MasterZoneId: 仅适用于公网负载均衡。设置跨可用区容灾时的主可用区ID，例如 100001 或 ap-guangzhou-1
        注：主可用区是需要承载流量的可用区，备可用区默认不承载流量，主可用区不可用时才使用备可用区，平台将为您自动选择最佳备可用区。可通过 DescribeMasterZones 接口查询一个地域的主可用区的列表。
                :type MasterZoneId: str
                :param ZoneId: 仅适用于公网负载均衡。可用区ID，指定可用区以创建负载均衡实例。如：ap-guangzhou-1
                :type ZoneId: str
                :param AnycastZone: 仅适用于公网负载均衡。Anycast的发布域，可取 ZONE_A 或 ZONE_B。仅带宽非上移用户支持此参数。（已下线）
                :type AnycastZone: str
                :param InternetAccessible: 仅适用于公网负载均衡。负载均衡的网络计费模式。
                :type InternetAccessible: :class:`tcecloud.clb.v20180317.models.InternetAccessible`
                :param VipIsp: 仅适用于公网负载均衡。CMCC | CTCC | CUCC，分别对应 移动 | 电信 | 联通，如果不指定本参数，
                则默认使用BGP。可通过 DescribeSingleIsp 接口查询一个地域所支持的Isp。
                如果指定运营商，则网络计费式只能使用按带宽包计费(BANDWIDTH_PACKAGE)。
                :type VipIsp: str
                :param Tags: 购买负载均衡同时，给负载均衡打上标签
                :type Tags: list of TagInfo
                :param ZhiTong: 是否支持直通（仅供自研用户使用）
                :type ZhiTong: bool
                :param Vip: 指定Vip申请负载均衡，必须同时指定 TgwGroupName 参数
                :type Vip: str
                :param TgwGroupName: Tgw独占集群的名称
                :type TgwGroupName: str
                :param IsDDos: 是否可绑定高防包
                :type IsDDos: bool
                :param BandwidthPackageId: 带宽包ID，网络计费方式选择带宽包时必须指定带宽包ID
                :type BandwidthPackageId: str
                :param ExclusiveCluster: 独占集群信息
                :type ExclusiveCluster: :class:`tcecloud.clb.v20180317.models.ExclusiveCluster`
        """
        self.LoadBalancerType = None
        self.Forward = None
        self.LoadBalancerName = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.AddressIPVersion = None
        self.Number = None
        self.MasterZoneId = None
        self.ZoneId = None
        self.AnycastZone = None
        self.InternetAccessible = None
        self.VipIsp = None
        self.Tags = None
        self.ZhiTong = None
        self.Vip = None
        self.TgwGroupName = None
        self.IsDDos = None
        self.BandwidthPackageId = None
        self.ExclusiveCluster = None

    def _deserialize(self, params):
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Forward = params.get("Forward")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.AddressIPVersion = params.get("AddressIPVersion")
        self.Number = params.get("Number")
        self.MasterZoneId = params.get("MasterZoneId")
        self.ZoneId = params.get("ZoneId")
        self.AnycastZone = params.get("AnycastZone")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.VipIsp = params.get("VipIsp")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.ZhiTong = params.get("ZhiTong")
        self.Vip = params.get("Vip")
        self.TgwGroupName = params.get("TgwGroupName")
        self.IsDDos = params.get("IsDDos")
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        if params.get("ExclusiveCluster") is not None:
            self.ExclusiveCluster = ExclusiveCluster()
            self.ExclusiveCluster._deserialize(params.get("ExclusiveCluster"))


class CreateLoadBalancerResponse(AbstractModel):
    """CreateLoadBalancer返回参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerIds: 由负载均衡实例唯一 ID 组成的数组。
        :type LoadBalancerIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancerIds = None
        self.RequestId = None

    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancerSnatIpsRequest(AbstractModel):
    """CreateLoadBalancerSnatIps请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡唯一性Id，如lb-12345678
        :type LoadBalancerId: str
        :param SnatIps: 添加SnatIp信息，可指定Ip申请，或者指定子网自动申请
        :type SnatIps: list of SnatIp
        """
        self.LoadBalancerId = None
        self.SnatIps = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("SnatIps") is not None:
            self.SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self.SnatIps.append(obj)


class CreateLoadBalancerSnatIpsResponse(AbstractModel):
    """CreateLoadBalancerSnatIps返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 监听器 ID
        :type ListenerId: str
        :param Rules: 新建转发规则的信息
        :type Rules: list of RuleInput
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Rules = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInput()
                obj._deserialize(item)
                self.Rules.append(obj)


class CreateRuleResponse(AbstractModel):
    """CreateRule返回参数结构体"""

    def __init__(self):
        """
        :param LocationIds: 创建的转发规则的唯一标识数组
        :type LocationIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LocationIds = None
        self.RequestId = None

    def _deserialize(self, params):
        self.LocationIds = params.get("LocationIds")
        self.RequestId = params.get("RequestId")


class CreateTargetGroupRequest(AbstractModel):
    """CreateTargetGroup请求参数结构体"""

    def __init__(self):
        """
        :param TargetGroupName: 目标组名称，限定50个字符
        :type TargetGroupName: str
        :param VpcId: 目标组的vpcid属性，不填则使用默认vpc
        :type VpcId: str
        :param Port: 目标组的默认端口， 后续添加服务器时可使用该默认端口
        :type Port: int
        :param TargetGroupInstances: 目标组绑定的后端服务器
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupName = None
        self.VpcId = None
        self.Port = None
        self.TargetGroupInstances = None

    def _deserialize(self, params):
        self.TargetGroupName = params.get("TargetGroupName")
        self.VpcId = params.get("VpcId")
        self.Port = params.get("Port")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)


class CreateTargetGroupResponse(AbstractModel):
    """CreateTargetGroup返回参数结构体"""

    def __init__(self):
        """
        :param TargetGroupId: 创建目标组后生成的id
        :type TargetGroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TargetGroupId = None
        self.RequestId = None

    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.RequestId = params.get("RequestId")


class DeleteCustomizedConfigRequest(AbstractModel):
    """DeleteCustomizedConfig请求参数结构体"""

    def __init__(self):
        """
        :param UconfigIdList: 删除的配置ID列表
        :type UconfigIdList: list of str
        """
        self.UconfigIdList = None

    def _deserialize(self, params):
        self.UconfigIdList = params.get("UconfigIdList")


class DeleteCustomizedConfigResponse(AbstractModel):
    """DeleteCustomizedConfig返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteListenerRequest(AbstractModel):
    """DeleteListener请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 要删除的监听器 ID
        :type ListenerId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")


class DeleteListenerResponse(AbstractModel):
    """DeleteListener返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancerListenersRequest(AbstractModel):
    """DeleteLoadBalancerListeners请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerIds: 指定删除的监听器ID数组，若不填则删除负载均衡的所有监听器
        :type ListenerIds: list of str
        """
        self.LoadBalancerId = None
        self.ListenerIds = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")


class DeleteLoadBalancerListenersResponse(AbstractModel):
    """DeleteLoadBalancerListeners返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancerRequest(AbstractModel):
    """DeleteLoadBalancer请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerIds: 要删除的负载均衡实例 ID数组，数组大小最大支持20
        :type LoadBalancerIds: list of str
        """
        self.LoadBalancerIds = None

    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")


class DeleteLoadBalancerResponse(AbstractModel):
    """DeleteLoadBalancer返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancerSnatIpsRequest(AbstractModel):
    """DeleteLoadBalancerSnatIps请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡唯一Id，如lb-12345678
        :type LoadBalancerId: str
        :param Ips: 删除SnatIp地址数组
        :type Ips: list of str
        """
        self.LoadBalancerId = None
        self.Ips = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Ips = params.get("Ips")


class DeleteLoadBalancerSnatIpsResponse(AbstractModel):
    """DeleteLoadBalancerSnatIps返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRewriteRequest(AbstractModel):
    """DeleteRewrite请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID
        :type LoadBalancerId: str
        :param SourceListenerId: 源监听器ID
        :type SourceListenerId: str
        :param TargetListenerId: 目标监听器ID
        :type TargetListenerId: str
        :param RewriteInfos: 转发规则之间的重定向关系
        :type RewriteInfos: list of RewriteLocationMap
        """
        self.LoadBalancerId = None
        self.SourceListenerId = None
        self.TargetListenerId = None
        self.RewriteInfos = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SourceListenerId = params.get("SourceListenerId")
        self.TargetListenerId = params.get("TargetListenerId")
        if params.get("RewriteInfos") is not None:
            self.RewriteInfos = []
            for item in params.get("RewriteInfos"):
                obj = RewriteLocationMap()
                obj._deserialize(item)
                self.RewriteInfos.append(obj)


class DeleteRewriteResponse(AbstractModel):
    """DeleteRewrite返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param LocationIds: 要删除的转发规则的ID组成的数组
        :type LocationIds: list of str
        :param Domain: 要删除的转发规则的域名，已提供LocationIds参数时本参数不生效
        :type Domain: str
        :param Url: 要删除的转发规则的转发路径，已提供LocationIds参数时本参数不生效
        :type Url: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationIds = None
        self.Domain = None
        self.Url = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationIds = params.get("LocationIds")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")


class DeleteRuleResponse(AbstractModel):
    """DeleteRule返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTargetGroupsRequest(AbstractModel):
    """DeleteTargetGroups请求参数结构体"""

    def __init__(self):
        """
        :param TargetGroupIds: 目标组的ID数组
        :type TargetGroupIds: list of str
        """
        self.TargetGroupIds = None

    def _deserialize(self, params):
        self.TargetGroupIds = params.get("TargetGroupIds")


class DeleteTargetGroupsResponse(AbstractModel):
    """DeleteTargetGroups返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeregisterTargetGroupInstancesRequest(AbstractModel):
    """DeregisterTargetGroupInstances请求参数结构体"""

    def __init__(self):
        """
        :param TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param TargetGroupInstances: 待解绑的服务器信息
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupId = None
        self.TargetGroupInstances = None

    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)


class DeregisterTargetGroupInstancesResponse(AbstractModel):
    """DeregisterTargetGroupInstances返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeregisterTargetsFromClassicalLBRequest(AbstractModel):
    """DeregisterTargetsFromClassicalLB请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param InstanceIds: 后端服务的实例ID列表
        :type InstanceIds: list of str
        """
        self.LoadBalancerId = None
        self.InstanceIds = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.InstanceIds = params.get("InstanceIds")


class DeregisterTargetsFromClassicalLBResponse(AbstractModel):
    """DeregisterTargetsFromClassicalLB返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeregisterTargetsRequest(AbstractModel):
    """DeregisterTargets请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID，格式如 lb-12345678
        :type LoadBalancerId: str
        :param ListenerId: 监听器 ID，格式如 lbl-12345678
        :type ListenerId: str
        :param Targets: 要解绑的后端服务列表，数组长度最大支持20
        :type Targets: list of Target
        :param LocationId: 转发规则的ID，格式如 loc-12345678，当从七层转发规则解绑机器时，必须提供此参数或Domain+Url两者之一
        :type LocationId: str
        :param Domain: 目标规则的域名，提供LocationId参数时本参数不生效
        :type Domain: str
        :param Url: 目标规则的URL，提供LocationId参数时本参数不生效
        :type Url: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Targets = None
        self.LocationId = None
        self.Domain = None
        self.Url = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")


class DeregisterTargetsResponse(AbstractModel):
    """DeregisterTargets返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBlockIPListRequest(AbstractModel):
    """DescribeBlockIPList请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID。
        :type LoadBalancerId: str
        :param Offset: 数据偏移量，默认为 0。
        :type Offset: int
        :param Limit: 返回IP的最大个数，默认为 100000。
        :type Limit: int
        """
        self.LoadBalancerId = None
        self.Offset = None
        self.Limit = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeBlockIPListResponse(AbstractModel):
    """DescribeBlockIPList返回参数结构体"""

    def __init__(self):
        """
        :param BlockedIPCount: 返回的IP的数量
        :type BlockedIPCount: int
        :param ClientIPField: 获取用户真实IP的字段
        :type ClientIPField: str
        :param BlockedIPList: 加入了12360黑名单的IP列表
        :type BlockedIPList: list of BlockedIP
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BlockedIPCount = None
        self.ClientIPField = None
        self.BlockedIPList = None
        self.RequestId = None

    def _deserialize(self, params):
        self.BlockedIPCount = params.get("BlockedIPCount")
        self.ClientIPField = params.get("ClientIPField")
        if params.get("BlockedIPList") is not None:
            self.BlockedIPList = []
            for item in params.get("BlockedIPList"):
                obj = BlockedIP()
                obj._deserialize(item)
                self.BlockedIPList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBlockIPTaskRequest(AbstractModel):
    """DescribeBlockIPTask请求参数结构体"""

    def __init__(self):
        """
        :param TaskId: ModifyBlockIPList 接口返回的异步任务的ID。
        :type TaskId: str
        """
        self.TaskId = None

    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeBlockIPTaskResponse(AbstractModel):
    """DescribeBlockIPTask返回参数结构体"""

    def __init__(self):
        """
        :param Status: 1 running，2 fail，6 succ
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None

    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeClassicalLBByInstanceIdRequest(AbstractModel):
    """DescribeClassicalLBByInstanceId请求参数结构体"""

    def __init__(self):
        """
        :param InstanceIds: 后端实例ID列表
        :type InstanceIds: list of str
        """
        self.InstanceIds = None

    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class DescribeClassicalLBByInstanceIdResponse(AbstractModel):
    """DescribeClassicalLBByInstanceId返回参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerInfoList: 负载均衡相关信息列表
        :type LoadBalancerInfoList: list of ClassicalLoadBalancerInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancerInfoList = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("LoadBalancerInfoList") is not None:
            self.LoadBalancerInfoList = []
            for item in params.get("LoadBalancerInfoList"):
                obj = ClassicalLoadBalancerInfo()
                obj._deserialize(item)
                self.LoadBalancerInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClassicalLBHealthStatusRequest(AbstractModel):
    """DescribeClassicalLBHealthStatus请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器ID
        :type ListenerId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")


class DescribeClassicalLBHealthStatusResponse(AbstractModel):
    """DescribeClassicalLBHealthStatus返回参数结构体"""

    def __init__(self):
        """
        :param HealthList: 后端健康状态列表
        :type HealthList: list of ClassicalHealth
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HealthList = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("HealthList") is not None:
            self.HealthList = []
            for item in params.get("HealthList"):
                obj = ClassicalHealth()
                obj._deserialize(item)
                self.HealthList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClassicalLBListenersRequest(AbstractModel):
    """DescribeClassicalLBListeners请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerIds: 负载均衡监听器ID列表
        :type ListenerIds: list of str
        :param Protocol: 负载均衡监听的协议, 'TCP', 'UDP', 'HTTP', 'HTTPS'
        :type Protocol: str
        :param ListenerPort: 负载均衡监听端口， 范围[1-65535]
        :type ListenerPort: int
        :param Status: 监听器的状态，0 表示创建中，1 表示运行中
        :type Status: int
        """
        self.LoadBalancerId = None
        self.ListenerIds = None
        self.Protocol = None
        self.ListenerPort = None
        self.Status = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        self.Protocol = params.get("Protocol")
        self.ListenerPort = params.get("ListenerPort")
        self.Status = params.get("Status")


class DescribeClassicalLBListenersResponse(AbstractModel):
    """DescribeClassicalLBListeners返回参数结构体"""

    def __init__(self):
        """
        :param Listeners: 监听器列表
        :type Listeners: list of ClassicalListener
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Listeners = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ClassicalListener()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClassicalLBTargetsRequest(AbstractModel):
    """DescribeClassicalLBTargets请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        """
        self.LoadBalancerId = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")


class DescribeClassicalLBTargetsResponse(AbstractModel):
    """DescribeClassicalLBTargets返回参数结构体"""

    def __init__(self):
        """
        :param Targets: 后端服务列表
        :type Targets: list of ClassicalTarget
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Targets = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = ClassicalTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterResourcesRequest(AbstractModel):
    """DescribeClusterResources请求参数结构体"""

    def __init__(self):
        """
                :param Limit: 返回集群中资源列表数目，默认20，最大值100
                :type Limit: int
                :param Offset: 返回集群中资源列表起始偏移量，默认0
                :type Offset: int
                :param Filters: 查询集群中资源列表条件，详细的过滤条件如下：
        <li> cluster-id - String - 是否必填：否 - （过滤条件）按照 集群 的唯一ID过滤，如 ："tgw-12345678","stgw-12345678","vpcgw-12345678"。</li>
        <li> vip - String - 是否必填：否 - （过滤条件）按照vip过滤。</li>
        <li> loadblancer-id - String - 是否必填：否 - （过滤条件）按照负载均衡唯一ID过滤。</li>
        <li> idle - String 是否必填：否 - （过滤条件）按照是否闲置过滤，如"True","False"。</li>
                :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None

    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeClusterResourcesResponse(AbstractModel):
    """DescribeClusterResources返回参数结构体"""

    def __init__(self):
        """
        :param ClusterResourceSet: 集群中资源列表
        :type ClusterResourceSet: list of ClusterResource
        :param TotalCount: 集群中资源总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterResourceSet = None
        self.TotalCount = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("ClusterResourceSet") is not None:
            self.ClusterResourceSet = []
            for item in params.get("ClusterResourceSet"):
                obj = ClusterResource()
                obj._deserialize(item)
                self.ClusterResourceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCustomizedConfigAssociateListRequest(AbstractModel):
    """DescribeCustomizedConfigAssociateList请求参数结构体"""

    def __init__(self):
        """
        :param UconfigId: 配置ID
        :type UconfigId: str
        :param Offset: 拉取绑定关系列表开始位置，默认值 0
        :type Offset: int
        :param Limit: 拉取绑定关系列表数目，默认值 20
        :type Limit: int
        :param Domain: 搜索域名
        :type Domain: str
        :param UconfigIds: CLB维度的配置ID列表，不支持根据 Domain 过滤
        :type UconfigIds: list of str
        """
        self.UconfigId = None
        self.Offset = None
        self.Limit = None
        self.Domain = None
        self.UconfigIds = None

    def _deserialize(self, params):
        self.UconfigId = params.get("UconfigId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Domain = params.get("Domain")
        self.UconfigIds = params.get("UconfigIds")


class DescribeCustomizedConfigAssociateListResponse(AbstractModel):
    """DescribeCustomizedConfigAssociateList返回参数结构体"""

    def __init__(self):
        """
        :param BindList: 绑定关系列表
        :type BindList: list of BindDetailItem
        :param TotalCount: 绑定关系总数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BindList = None
        self.TotalCount = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("BindList") is not None:
            self.BindList = []
            for item in params.get("BindList"):
                obj = BindDetailItem()
                obj._deserialize(item)
                self.BindList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCustomizedConfigContentRequest(AbstractModel):
    """DescribeCustomizedConfigContent请求参数结构体"""

    def __init__(self):
        """
        :param UconfigIdList: 拉取的配置id列表
        :type UconfigIdList: list of str
        """
        self.UconfigIdList = None

    def _deserialize(self, params):
        self.UconfigIdList = params.get("UconfigIdList")


class DescribeCustomizedConfigContentResponse(AbstractModel):
    """DescribeCustomizedConfigContent返回参数结构体"""

    def __init__(self):
        """
        :param ConfigList: 配置列表
        :type ConfigList: list of ConfigListItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ConfigList = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("ConfigList") is not None:
            self.ConfigList = []
            for item in params.get("ConfigList"):
                obj = ConfigListItem()
                obj._deserialize(item)
                self.ConfigList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCustomizedConfigLBAssociateListRequest(AbstractModel):
    """DescribeCustomizedConfigLBAssociateList请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerIds: CLB ID列表
        :type LoadBalancerIds: list of str
        :param ConfigType: 配置类型
        :type ConfigType: str
        """
        self.LoadBalancerIds = None
        self.ConfigType = None

    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.ConfigType = params.get("ConfigType")


class DescribeCustomizedConfigLBAssociateListResponse(AbstractModel):
    """DescribeCustomizedConfigLBAssociateList返回参数结构体"""

    def __init__(self):
        """
        :param BindList: 绑定列表
        :type BindList: list of BindConfigItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BindList = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("BindList") is not None:
            self.BindList = []
            for item in params.get("BindList"):
                obj = BindConfigItem()
                obj._deserialize(item)
                self.BindList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCustomizedConfigListRequest(AbstractModel):
    """DescribeCustomizedConfigList请求参数结构体"""

    def __init__(self):
        """
        :param ConfigType: 配置类型:CLB 负载均衡维度。 SERVER 域名维度。 LOCATION 规则维度。
        :type ConfigType: str
        :param Offset: 拉取页偏移，默认值0
        :type Offset: int
        :param Limit: 拉取数目，默认值20
        :type Limit: int
        :param ConfigName: 拉取指定配置名字，模糊匹配。
        :type ConfigName: str
        :param UconfigIds: 配置ID
        :type UconfigIds: list of str
        """
        self.ConfigType = None
        self.Offset = None
        self.Limit = None
        self.ConfigName = None
        self.UconfigIds = None

    def _deserialize(self, params):
        self.ConfigType = params.get("ConfigType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ConfigName = params.get("ConfigName")
        self.UconfigIds = params.get("UconfigIds")


class DescribeCustomizedConfigListResponse(AbstractModel):
    """DescribeCustomizedConfigList返回参数结构体"""

    def __init__(self):
        """
        :param ConfigList: 配置列表
        :type ConfigList: list of ConfigListItem
        :param TotalCount: 配置数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ConfigList = None
        self.TotalCount = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("ConfigList") is not None:
            self.ConfigList = []
            for item in params.get("ConfigList"):
                obj = ConfigListItem()
                obj._deserialize(item)
                self.ConfigList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeExclusiveClustersRequest(AbstractModel):
    """DescribeExclusiveClusters请求参数结构体"""

    def __init__(self):
        """
                :param Limit: 返回集群列表数目，默认20，最大值100
                :type Limit: int
                :param Offset: 返回集群列表起始偏移量，默认0
                :type Offset: int
                :param Filters: 查询集群列表条件，详细的过滤条件如下：
        <li> cluster-type - String - 是否必填：否 - （过滤条件）按照 集群 的类型过滤，包括"TGW","STGW","VPCGW"。</li>
        <li> cluster-id - String - 是否必填：否 - （过滤条件）按照 集群 的唯一ID过滤，如 ："tgw-12345678","stgw-12345678","vpcgw-12345678"。</li>
        <li> cluster-name - String - 是否必填：否 - （过滤条件）按照 集群 的名称过滤。</li>
        <li> cluster-tag - String - 是否必填：否 - （过滤条件）按照 集群 的标签过滤。（只有STGW集群有集群标签） </li>
        <li> vip - String - 是否必填：否 - （过滤条件）按照 集群 内的vip过滤。</li>
        <li> loadblancer-id - String - 是否必填：否 - （过滤条件）按照 集群 内的负载均衡唯一ID过滤。</li>
        <li> network - String - 是否必填：否 - （过滤条件）按照 集群 的网络类型过滤，如："Public","Private"。</li>
        <li> zone - String - 是否必填：否 - （过滤条件）按照 集群 所在可用区过滤，如："ap-guangzhou-1"（广州一区）。</li>
                :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None

    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeExclusiveClustersResponse(AbstractModel):
    """DescribeExclusiveClusters返回参数结构体"""

    def __init__(self):
        """
        :param ClusterSet: 集群列表
        :type ClusterSet: list of Cluster
        :param TotalCount: 集群总数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterSet = None
        self.TotalCount = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("ClusterSet") is not None:
            self.ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = Cluster()
                obj._deserialize(item)
                self.ClusterSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeLBActionLimitRequest(AbstractModel):
    """DescribeLBActionLimit请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerIds: 负载均衡唯一ID列表
        :type LoadBalancerIds: list of str
        :param ActionType: 负载均衡相关操作，当前仅支持"ModifyLBNetwork"
        :type ActionType: str
        """
        self.LoadBalancerIds = None
        self.ActionType = None

    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.ActionType = params.get("ActionType")


class DescribeLBActionLimitResponse(AbstractModel):
    """DescribeLBActionLimit返回参数结构体"""

    def __init__(self):
        """
        :param QuotaSet: 负载均衡的操作配额详细信息
        :type QuotaSet: list of Quota
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QuotaSet = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("QuotaSet") is not None:
            self.QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = Quota()
                obj._deserialize(item)
                self.QuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLBListenersRequest(AbstractModel):
    """DescribeLBListeners请求参数结构体"""

    def __init__(self):
        """
        :param Backends: 需要查询的内网ip列表
        :type Backends: list of LbRsItem
        """
        self.Backends = None

    def _deserialize(self, params):
        if params.get("Backends") is not None:
            self.Backends = []
            for item in params.get("Backends"):
                obj = LbRsItem()
                obj._deserialize(item)
                self.Backends.append(obj)


class DescribeLBListenersResponse(AbstractModel):
    """DescribeLBListeners返回参数结构体"""

    def __init__(self):
        """
        :param LoadBalancers: 绑定的后端规则
        :type LoadBalancers: list of LBItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancers = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("LoadBalancers") is not None:
            self.LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LBItem()
                obj._deserialize(item)
                self.LoadBalancers.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListenersRequest(AbstractModel):
    """DescribeListeners请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerIds: 要查询的负载均衡监听器 ID数组
        :type ListenerIds: list of str
        :param Protocol: 要查询的监听器协议类型，取值 TCP | UDP | HTTP | HTTPS | TCP_SSL
        :type Protocol: str
        :param Port: 要查询的监听器的端口
        :type Port: int
        :param Filters: 过滤条件，与ListenerIds互斥，如果ListenerIds参数存在，则本参数不起作用
        :type Filters: list of Filter
        :param Limit: 显示的条数限制，不传则获取所有
        :type Limit: int
        :param Offset: 显示的偏移起始量
        :type Offset: int
        :param OrderBy: 排序参数，支持CreateTime字段
        :type OrderBy: str
        :param OrderType: 取值 DESC | ASC
        :type OrderType: str
        """
        self.LoadBalancerId = None
        self.ListenerIds = None
        self.Protocol = None
        self.Port = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderType = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")


class DescribeListenersResponse(AbstractModel):
    """DescribeListeners返回参数结构体"""

    def __init__(self):
        """
        :param Listeners: 监听器列表
        :type Listeners: list of Listener
        :param TotalCount: 总的监听器个数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Listeners = None
        self.TotalCount = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = Listener()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancerCountRequest(AbstractModel):
    """DescribeLoadBalancerCount请求参数结构体"""


class DescribeLoadBalancerCountResponse(AbstractModel):
    """DescribeLoadBalancerCount返回参数结构体"""

    def __init__(self):
        """
        :param TotalCount: 一个账户在一个地域的负载均衡实例总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RequestId = None

    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancerListByCertIdRequest(AbstractModel):
    """DescribeLoadBalancerListByCertId请求参数结构体"""

    def __init__(self):
        """
        :param CertIds: 服务端证书的ID，或客户端证书的ID
        :type CertIds: list of str
        """
        self.CertIds = None

    def _deserialize(self, params):
        self.CertIds = params.get("CertIds")


class DescribeLoadBalancerListByCertIdResponse(AbstractModel):
    """DescribeLoadBalancerListByCertId返回参数结构体"""

    def __init__(self):
        """
        :param CertSet: 证书ID，以及与该证书ID关联的负载均衡实例列表
        :type CertSet: list of CertIdRelatedWithLoadBalancers
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertSet = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("CertSet") is not None:
            self.CertSet = []
            for item in params.get("CertSet"):
                obj = CertIdRelatedWithLoadBalancers()
                obj._deserialize(item)
                self.CertSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancersFeatureRequest(AbstractModel):
    """DescribeLoadBalancersFeature请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerIds: 负载均衡ID列表
        :type LoadBalancerIds: list of str
        :param Features: 功能列表
        :type Features: list of str
        """
        self.LoadBalancerIds = None
        self.Features = None

    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.Features = params.get("Features")


class DescribeLoadBalancersFeatureResponse(AbstractModel):
    """DescribeLoadBalancersFeature返回参数结构体"""

    def __init__(self):
        """
        :param Cos: 支持cos日志的负载均衡ID
        :type Cos: list of str
        :param NotSupportNewHealth: 不支持新健康探测的负载均衡ID
        :type NotSupportNewHealth: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Cos = None
        self.NotSupportNewHealth = None
        self.RequestId = None

    def _deserialize(self, params):
        self.Cos = params.get("Cos")
        self.NotSupportNewHealth = params.get("NotSupportNewHealth")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancersForVpcRequest(AbstractModel):
    """DescribeLoadBalancersForVpc请求参数结构体"""

    def __init__(self):
        """
                :param LoadBalancerType: 负载均衡实例的网络类型：
        OPEN：公网属性， INTERNAL：内网属性。
                :type LoadBalancerType: str
                :param VpcId: 负载均衡实例所属私有网络唯一ID，如 vpc-bhqkbhdx。兼容整型的VpcId。
                :type VpcId: list of str
                :param SubnetId: 负载均衡实例所属子网唯一ID，暂时只支持整型SubnetId。
        后续会兼容字符串的子网ID（subnet-1122ccbb）。
                :type SubnetId: list of str
                :param Offset: 数据偏移量，默认为 0。
                :type Offset: int
                :param Limit: 返回负载均衡实例的数量，默认为20。
                :type Limit: int
        """
        self.LoadBalancerType = None
        self.VpcId = None
        self.SubnetId = None
        self.Offset = None
        self.Limit = None

    def _deserialize(self, params):
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeLoadBalancersForVpcResponse(AbstractModel):
    """DescribeLoadBalancersForVpc返回参数结构体"""

    def __init__(self):
        """
        :param TotalCount: 满足过滤条件的负载均衡实例总数。此数值与入参中的Limit无关。
        :type TotalCount: int
        :param LoadBalancerSet: 返回的负载均衡实例数组。
        :type LoadBalancerSet: list of LoadBalancer
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.LoadBalancerSet = None
        self.RequestId = None

    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LoadBalancerSet") is not None:
            self.LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self.LoadBalancerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancersRequest(AbstractModel):
    """DescribeLoadBalancers请求参数结构体"""

    def __init__(self):
        """
                :param LoadBalancerIds: 负载均衡实例 ID。
                :type LoadBalancerIds: list of str
                :param LoadBalancerType: 负载均衡实例的网络类型：
        OPEN：公网属性， INTERNAL：内网属性。
                :type LoadBalancerType: str
                :param Forward: 负载均衡实例的类型。1：通用的负载均衡实例，0：传统型负载均衡实例。如果不传此参数，则查询所有类型的负载均衡实例。
                :type Forward: int
                :param LoadBalancerName: 负载均衡实例的名称。
                :type LoadBalancerName: str
                :param Domain: Tce为负载均衡实例分配的域名，本参数仅对传统型公网负载均衡才有意义。
                :type Domain: str
                :param LoadBalancerVips: 负载均衡实例的 VIP 地址，支持多个。
                :type LoadBalancerVips: list of str
                :param BackendPublicIps: 负载均衡绑定的后端服务的外网 IP。
                :type BackendPublicIps: list of str
                :param BackendPrivateIps: 负载均衡绑定的后端服务的内网 IP。
                :type BackendPrivateIps: list of str
                :param Offset: 数据偏移量，默认为 0。
                :type Offset: int
                :param Limit: 返回负载均衡实例的数量，默认为20，最大值为100。
                :type Limit: int
                :param OrderBy: 排序参数，支持以下字段：LoadBalancerName，CreateTime，Domain，LoadBalancerType。
                :type OrderBy: str
                :param OrderType: 1：倒序，0：顺序，默认按照创建时间倒序。
                :type OrderType: int
                :param SearchKey: 搜索字段，模糊匹配名称、域名、VIP。
                :type SearchKey: str
                :param ProjectId: 负载均衡实例所属的项目 ID，可以通过 DescribeProject 接口获取。
                :type ProjectId: int
                :param WithRs: 负载均衡是否绑定后端服务，0：没有绑定后端服务，1：绑定后端服务，-1：查询全部。
                :type WithRs: int
                :param VpcId: 负载均衡实例所属私有网络唯一ID，如 vpc-bhqkbhdx，
        基础网络可传入'0'。
                :type VpcId: str
                :param SecurityGroup: 安全组ID，如 sg-m1cc9123
                :type SecurityGroup: str
                :param MasterZone: 主可用区ID，如 ："100001" （对应的是广州一区）
                :type MasterZone: str
                :param Filters: 每次请求的`Filters`的上限为10，
                `Filter.Values`的上限为100。详细的过滤条件如下：
        <li> internet-charge-type - String - 是否必填：否 - （过滤条件）按照 CLB 的网络计费模式过滤，
        包括"BANDWIDTH_PREPAID","TRAFFIC_POSTPAID_BY_HOUR","BANDWIDTH_POSTPAID_BY_HOUR","BANDWIDTH_PACKAGE"。</li>
        <li> master-zone-id - String - 是否必填：否 -
        （过滤条件）按照 CLB 的主可用区ID过滤，如 ："100001" （对应的是广州一区）。</li>
        <li> tag-key - String - 是否必填：否 - （过滤条件）按照 CLB 标签的键过滤。</li>
                :type Filters: list of Filter
        """
        self.LoadBalancerIds = None
        self.LoadBalancerType = None
        self.Forward = None
        self.LoadBalancerName = None
        self.Domain = None
        self.LoadBalancerVips = None
        self.BackendPublicIps = None
        self.BackendPrivateIps = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.OrderType = None
        self.SearchKey = None
        self.ProjectId = None
        self.WithRs = None
        self.VpcId = None
        self.SecurityGroup = None
        self.MasterZone = None
        self.Filters = None

    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Forward = params.get("Forward")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.Domain = params.get("Domain")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.BackendPublicIps = params.get("BackendPublicIps")
        self.BackendPrivateIps = params.get("BackendPrivateIps")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.SearchKey = params.get("SearchKey")
        self.ProjectId = params.get("ProjectId")
        self.WithRs = params.get("WithRs")
        self.VpcId = params.get("VpcId")
        self.SecurityGroup = params.get("SecurityGroup")
        self.MasterZone = params.get("MasterZone")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeLoadBalancersResponse(AbstractModel):
    """DescribeLoadBalancers返回参数结构体"""

    def __init__(self):
        """
        :param TotalCount: 满足过滤条件的负载均衡实例总数。此数值与入参中的Limit无关。
        :type TotalCount: int
        :param LoadBalancerSet: 返回的负载均衡实例数组。
        :type LoadBalancerSet: list of LoadBalancer
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.LoadBalancerSet = None
        self.RequestId = None

    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LoadBalancerSet") is not None:
            self.LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self.LoadBalancerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMasterZonesRequest(AbstractModel):
    """DescribeMasterZones请求参数结构体"""

    def __init__(self):
        """
        :param Groups: 园区标识字符串
        :type Groups: list of str
        """
        self.Groups = None

    def _deserialize(self, params):
        self.Groups = params.get("Groups")


class DescribeMasterZonesResponse(AbstractModel):
    """DescribeMasterZones返回参数结构体"""

    def __init__(self):
        """
        :param MasterZoneSet: 可用区信息
        :type MasterZoneSet: list of MasterZoneInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MasterZoneSet = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("MasterZoneSet") is not None:
            self.MasterZoneSet = []
            for item in params.get("MasterZoneSet"):
                obj = MasterZoneInfo()
                obj._deserialize(item)
                self.MasterZoneSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeQuotaRequest(AbstractModel):
    """DescribeQuota请求参数结构体"""


class DescribeQuotaResponse(AbstractModel):
    """DescribeQuota返回参数结构体"""

    def __init__(self):
        """
        :param QuotaSet: 配额列表
        :type QuotaSet: list of Quota
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QuotaSet = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("QuotaSet") is not None:
            self.QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = Quota()
                obj._deserialize(item)
                self.QuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRewriteRequest(AbstractModel):
    """DescribeRewrite请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID
        :type LoadBalancerId: str
        :param SourceListenerIds: 负载均衡监听器ID数组
        :type SourceListenerIds: list of str
        :param SourceLocationIds: 负载均衡转发规则的ID数组
        :type SourceLocationIds: list of str
        """
        self.LoadBalancerId = None
        self.SourceListenerIds = None
        self.SourceLocationIds = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SourceListenerIds = params.get("SourceListenerIds")
        self.SourceLocationIds = params.get("SourceLocationIds")


class DescribeRewriteResponse(AbstractModel):
    """DescribeRewrite返回参数结构体"""

    def __init__(self):
        """
        :param RewriteSet: 重定向转发规则构成的数组，若无重定向规则，则返回空数组
        :type RewriteSet: list of RuleOutput
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RewriteSet = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("RewriteSet") is not None:
            self.RewriteSet = []
            for item in params.get("RewriteSet"):
                obj = RuleOutput()
                obj._deserialize(item)
                self.RewriteSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSetByVipRequest(AbstractModel):
    """DescribeSetByVip请求参数结构体"""

    def __init__(self):
        """
        :param Type: 查询四层或七层  只能为L4 或者 L7
        :type Type: str
        :param VipList: ip和端口号信息
        :type VipList: list of VipAndVport
        """
        self.Type = None
        self.VipList = None

    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("VipList") is not None:
            self.VipList = []
            for item in params.get("VipList"):
                obj = VipAndVport()
                obj._deserialize(item)
                self.VipList.append(obj)


class DescribeSetByVipResponse(AbstractModel):
    """DescribeSetByVip返回参数结构体"""

    def __init__(self):
        """
        :param SetInfo: 集群信息
        :type SetInfo: list of SetNameVIP
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SetInfo = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("SetInfo") is not None:
            self.SetInfo = []
            for item in params.get("SetInfo"):
                obj = SetNameVIP()
                obj._deserialize(item)
                self.SetInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSetCapacityRequest(AbstractModel):
    """DescribeSetCapacity请求参数结构体"""

    def __init__(self):
        """
        :param Type: 查询四层或七层  只能为L4 或者 L7
        :type Type: str
        :param SetName: 独占集群名字
        :type SetName: list of str
        """
        self.Type = None
        self.SetName = None

    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.SetName = params.get("SetName")


class DescribeSetCapacityResponse(AbstractModel):
    """DescribeSetCapacity返回参数结构体"""

    def __init__(self):
        """
        :param SetCapacity: 集群信息
        :type SetCapacity: list of OneCapacity
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SetCapacity = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("SetCapacity") is not None:
            self.SetCapacity = []
            for item in params.get("SetCapacity"):
                obj = OneCapacity()
                obj._deserialize(item)
                self.SetCapacity.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSetInnerNameRequest(AbstractModel):
    """DescribeSetInnerName请求参数结构体"""

    def __init__(self):
        """
        :param Type: 集群类型。四层："L4"，七层：“L7”
        :type Type: str
        :param SetNames: 集群名字
        :type SetNames: list of str
        :param ClusterIds: 集群ID
        :type ClusterIds: list of str
        """
        self.Type = None
        self.SetNames = None
        self.ClusterIds = None

    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.SetNames = params.get("SetNames")
        self.ClusterIds = params.get("ClusterIds")


class DescribeSetInnerNameResponse(AbstractModel):
    """DescribeSetInnerName返回参数结构体"""

    def __init__(self):
        """
        :param SetInnerNames: 集群实际名字
        :type SetInnerNames: list of SetNameItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SetInnerNames = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("SetInnerNames") is not None:
            self.SetInnerNames = []
            for item in params.get("SetInnerNames"):
                obj = SetNameItem()
                obj._deserialize(item)
                self.SetInnerNames.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSetVipRequest(AbstractModel):
    """DescribeSetVip请求参数结构体"""

    def __init__(self):
        """
        :param Type: 查询四层独占集群还是七层，只能为L4或者L7
        :type Type: str
        :param SetName: 集群名字数组
        :type SetName: list of str
        """
        self.Type = None
        self.SetName = None

    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.SetName = params.get("SetName")


class DescribeSetVipResponse(AbstractModel):
    """DescribeSetVip返回参数结构体"""

    def __init__(self):
        """
        :param SetVip: 返回独占集群Vip的使用信息
        :type SetVip: list of SetVip
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SetVip = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("SetVip") is not None:
            self.SetVip = []
            for item in params.get("SetVip"):
                obj = SetVip()
                obj._deserialize(item)
                self.SetVip.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSetsRequest(AbstractModel):
    """DescribeSets请求参数结构体"""

    def __init__(self):
        """
        :param Offset: 数据偏移量，默认为 0。
        :type Offset: int
        :param Limit: 集群数目，默认20。
        :type Limit: int
        :param SetId: 集群Id
        :type SetId: int
        :param SetName: 集群名
        :type SetName: str
        :param SetTag: 7层标签名
        :type SetTag: str
        :param Vip: vip地址
        :type Vip: str
        :param Type: 集群搜索类型
        :type Type: str
        :param ClusterId: 集群Id
        :type ClusterId: str
        """
        self.Offset = None
        self.Limit = None
        self.SetId = None
        self.SetName = None
        self.SetTag = None
        self.Vip = None
        self.Type = None
        self.ClusterId = None

    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SetId = params.get("SetId")
        self.SetName = params.get("SetName")
        self.SetTag = params.get("SetTag")
        self.Vip = params.get("Vip")
        self.Type = params.get("Type")
        self.ClusterId = params.get("ClusterId")


class DescribeSetsResponse(AbstractModel):
    """DescribeSets返回参数结构体"""

    def __init__(self):
        """
        :param SetInfo: 集群信息
        :type SetInfo: list of SetItem
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SetInfo = None
        self.TotalCount = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("SetInfo") is not None:
            self.SetInfo = []
            for item in params.get("SetInfo"):
                obj = SetItem()
                obj._deserialize(item)
                self.SetInfo.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSingleIspRequest(AbstractModel):
    """DescribeSingleIsp请求参数结构体"""


class DescribeSingleIspResponse(AbstractModel):
    """DescribeSingleIsp返回参数结构体"""

    def __init__(self):
        """
        :param IspSet: CMCC：移动、CTCC：电信、CUCC：联通
        :type IspSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IspSet = None
        self.RequestId = None

    def _deserialize(self, params):
        self.IspSet = params.get("IspSet")
        self.RequestId = params.get("RequestId")


class DescribeTargetCountForLoadBalancersRequest(AbstractModel):
    """DescribeTargetCountForLoadBalancers请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerIds: 负载均衡ID
        :type LoadBalancerIds: list of str
        """
        self.LoadBalancerIds = None

    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")


class DescribeTargetCountForLoadBalancersResponse(AbstractModel):
    """DescribeTargetCountForLoadBalancers返回参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerSet: 查询负载均衡实例，及其绑定的后端服务总数
        :type LoadBalancerSet: list of TargetCountForLoadBalancer
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancerSet = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("LoadBalancerSet") is not None:
            self.LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = TargetCountForLoadBalancer()
                obj._deserialize(item)
                self.LoadBalancerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTargetGroupInstancesRequest(AbstractModel):
    """DescribeTargetGroupInstances请求参数结构体"""

    def __init__(self):
        """
        :param Filters: 过滤条件，当前仅支持TargetGroupId，BindIP，InstanceId过滤
        :type Filters: list of Filter
        :param Limit: 显示数量限制，默认20
        :type Limit: int
        :param Offset: 显示的偏移量，默认为0
        :type Offset: int
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None

    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeTargetGroupInstancesResponse(AbstractModel):
    """DescribeTargetGroupInstances返回参数结构体"""

    def __init__(self):
        """
        :param TotalCount: 本次查询的结果数量
        :type TotalCount: int
        :param TargetGroupInstanceSet: 绑定的服务器信息
        :type TargetGroupInstanceSet: list of TargetGroupBackend
        :param RealCount: 实际统计数量，不受Limit，Offset，CAM的影响
        :type RealCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TargetGroupInstanceSet = None
        self.RealCount = None
        self.RequestId = None

    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TargetGroupInstanceSet") is not None:
            self.TargetGroupInstanceSet = []
            for item in params.get("TargetGroupInstanceSet"):
                obj = TargetGroupBackend()
                obj._deserialize(item)
                self.TargetGroupInstanceSet.append(obj)
        self.RealCount = params.get("RealCount")
        self.RequestId = params.get("RequestId")


class DescribeTargetGroupListRequest(AbstractModel):
    """DescribeTargetGroupList请求参数结构体"""

    def __init__(self):
        """
        :param TargetGroupIds: 目标组ID数组
        :type TargetGroupIds: list of str
        :param Filters: 过滤条件数组，支持TargetGroupVpcId和TargetGroupName。与TargetGroupIds互斥，优先使用目标组ID，
        :type Filters: list of Filter
        :param Offset: 显示的偏移起始量
        :type Offset: int
        :param Limit: 显示条数限制，默认为20
        :type Limit: int
        """
        self.TargetGroupIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None

    def _deserialize(self, params):
        self.TargetGroupIds = params.get("TargetGroupIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTargetGroupListResponse(AbstractModel):
    """DescribeTargetGroupList返回参数结构体"""

    def __init__(self):
        """
        :param TotalCount: 显示的结果数量
        :type TotalCount: int
        :param TargetGroupSet: 显示的目标组信息集合
        :type TargetGroupSet: list of TargetGroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TargetGroupSet = None
        self.RequestId = None

    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TargetGroupSet") is not None:
            self.TargetGroupSet = []
            for item in params.get("TargetGroupSet"):
                obj = TargetGroupInfo()
                obj._deserialize(item)
                self.TargetGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTargetGroupsRequest(AbstractModel):
    """DescribeTargetGroups请求参数结构体"""

    def __init__(self):
        """
        :param TargetGroupIds: 目标组ID，与Filters互斥
        :type TargetGroupIds: list of str
        :param Limit: 显示条数限制，默认为20
        :type Limit: int
        :param Offset: 显示的偏移起始量
        :type Offset: int
        :param Filters: 过滤条件数组，与TargetGroupIds互斥，支持TargetGroupVpcId和TargetGroupName
        :type Filters: list of Filter
        """
        self.TargetGroupIds = None
        self.Limit = None
        self.Offset = None
        self.Filters = None

    def _deserialize(self, params):
        self.TargetGroupIds = params.get("TargetGroupIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeTargetGroupsResponse(AbstractModel):
    """DescribeTargetGroups返回参数结构体"""

    def __init__(self):
        """
        :param TotalCount: 显示的结果数量
        :type TotalCount: int
        :param TargetGroupSet: 显示的目标组信息集合
        :type TargetGroupSet: list of TargetGroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TargetGroupSet = None
        self.RequestId = None

    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TargetGroupSet") is not None:
            self.TargetGroupSet = []
            for item in params.get("TargetGroupSet"):
                obj = TargetGroupInfo()
                obj._deserialize(item)
                self.TargetGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTargetHealthRequest(AbstractModel):
    """DescribeTargetHealth请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerIds: 要查询的负载均衡实例 ID列表
        :type LoadBalancerIds: list of str
        """
        self.LoadBalancerIds = None

    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")


class DescribeTargetHealthResponse(AbstractModel):
    """DescribeTargetHealth返回参数结构体"""

    def __init__(self):
        """
        :param LoadBalancers: 负载均衡实例列表
        :type LoadBalancers: list of LoadBalancerHealth
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancers = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("LoadBalancers") is not None:
            self.LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancerHealth()
                obj._deserialize(item)
                self.LoadBalancers.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTargetsRequest(AbstractModel):
    """DescribeTargets请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerIds: 监听器 ID列表
        :type ListenerIds: list of str
        :param Protocol: 监听器协议类型
        :type Protocol: str
        :param Port: 监听器端口
        :type Port: int
        """
        self.LoadBalancerId = None
        self.ListenerIds = None
        self.Protocol = None
        self.Port = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")


class DescribeTargetsResponse(AbstractModel):
    """DescribeTargets返回参数结构体"""

    def __init__(self):
        """
        :param Listeners: 监听器后端绑定的机器信息
        :type Listeners: list of ListenerBackend
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Listeners = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerBackend()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体"""

    def __init__(self):
        """
        :param TaskId: 请求ID，即接口返回的 RequestId 参数
        :type TaskId: str
        :param DealName: 订单id
        :type DealName: str
        """
        self.TaskId = None
        self.DealName = None

    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.DealName = params.get("DealName")


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回参数结构体"""

    def __init__(self):
        """
        :param Status: 任务的当前状态。 0：成功，1：失败，2：进行中。
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None

    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DisassociateCustomizedConfigRequest(AbstractModel):
    """DisassociateCustomizedConfig请求参数结构体"""

    def __init__(self):
        """
        :param UconfigId: 配置ID
        :type UconfigId: str
        :param BindList: 解绑的列表
        :type BindList: list of BindItem
        """
        self.UconfigId = None
        self.BindList = None

    def _deserialize(self, params):
        self.UconfigId = params.get("UconfigId")
        if params.get("BindList") is not None:
            self.BindList = []
            for item in params.get("BindList"):
                obj = BindItem()
                obj._deserialize(item)
                self.BindList.append(obj)


class DisassociateCustomizedConfigResponse(AbstractModel):
    """DisassociateCustomizedConfig返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateTargetGroupsRequest(AbstractModel):
    """DisassociateTargetGroups请求参数结构体"""

    def __init__(self):
        """
        :param Associations: 待解绑的规则关系数组
        :type Associations: list of TargetGroupAssociation
        """
        self.Associations = None

    def _deserialize(self, params):
        if params.get("Associations") is not None:
            self.Associations = []
            for item in params.get("Associations"):
                obj = TargetGroupAssociation()
                obj._deserialize(item)
                self.Associations.append(obj)


class DisassociateTargetGroupsResponse(AbstractModel):
    """DisassociateTargetGroups返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ExclusiveCluster(AbstractModel):
    """独占集群"""

    def __init__(self):
        """
                :param L4Clusters: 4层独占集群列表
        注意：此字段可能返回 null，表示取不到有效值。
                :type L4Clusters: list of ClusterItem
                :param L7Clusters: 7层独占集群列表
        注意：此字段可能返回 null，表示取不到有效值。
                :type L7Clusters: list of ClusterItem
                :param ClassicalCluster: vpcgw集群
        注意：此字段可能返回 null，表示取不到有效值。
                :type ClassicalCluster: :class:`tcecloud.clb.v20180317.models.ClusterItem`
        """
        self.L4Clusters = None
        self.L7Clusters = None
        self.ClassicalCluster = None

    def _deserialize(self, params):
        if params.get("L4Clusters") is not None:
            self.L4Clusters = []
            for item in params.get("L4Clusters"):
                obj = ClusterItem()
                obj._deserialize(item)
                self.L4Clusters.append(obj)
        if params.get("L7Clusters") is not None:
            self.L7Clusters = []
            for item in params.get("L7Clusters"):
                obj = ClusterItem()
                obj._deserialize(item)
                self.L7Clusters.append(obj)
        if params.get("ClassicalCluster") is not None:
            self.ClassicalCluster = ClusterItem()
            self.ClassicalCluster._deserialize(params.get("ClassicalCluster"))


class ExtraInfo(AbstractModel):
    """暂做保留，一般用户无需关注。"""

    def __init__(self):
        """
                :param ZhiTong: 是否开通VIP直通
        注意：此字段可能返回 null，表示取不到有效值。
                :type ZhiTong: bool
                :param TgwGroupName: TgwGroup名称
        注意：此字段可能返回 null，表示取不到有效值。
                :type TgwGroupName: str
        """
        self.ZhiTong = None
        self.TgwGroupName = None

    def _deserialize(self, params):
        self.ZhiTong = params.get("ZhiTong")
        self.TgwGroupName = params.get("TgwGroupName")


class Filter(AbstractModel):
    """过滤器条件"""

    def __init__(self):
        """
        :param Name: 过滤器的名称
        :type Name: str
        :param Values: 过滤器的值数组
        :type Values: list of str
        """
        self.Name = None
        self.Values = None

    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class HealthCheck(AbstractModel):
    """健康检查信息。
    注意，自定义探测相关参数 目前只有少量区域灰度支持。

    """

    def __init__(self):
        """
                :param HealthSwitch: 是否开启健康检查：1（开启）、0（关闭）。
                :type HealthSwitch: int
                :param TimeOut: 健康检查的响应超时时间（仅适用于四层监听器），可选值：2~60，默认值：2，单位：秒。响应超时时间要小于检查间隔时间。
        注意：此字段可能返回 null，表示取不到有效值。
                :type TimeOut: int
                :param IntervalTime: 健康检查探测间隔时间，默认值：5，可选值：5~300，单位：秒。
        注意：此字段可能返回 null，表示取不到有效值。
                :type IntervalTime: int
                :param HealthNum: 健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2~10，单位：次。
        注意：此字段可能返回 null，表示取不到有效值。
                :type HealthNum: int
                :param UnHealthNum: 不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发异常，可选值：2~10，单位：次。
        注意：此字段可能返回 null，表示取不到有效值。
                :type UnHealthNum: int
                :param HttpCode: 健康检查状态码（仅适用于HTTP/HTTPS转发规则、TCP监听器的HTTP健康检查方式）。
                可选值：1~31，默认 31。
        1 表示探测后返回值 1xx 代表健康，2 表示返回 2xx 代表健康，4 表示返回 3xx 代表健康，
        8 表示返回 4xx 代表健康，16 表示返回 5xx 代表健康。若希望多种返回码都可代表健康，则将相应的值相加。
        注意：TCP监听器的HTTP健康检查方式，只支持指定一种健康检查状态码。
        注意：此字段可能返回 null，表示取不到有效值。
                :type HttpCode: int
                :param HttpCheckPath: 健康检查路径（仅适用于HTTP/HTTPS转发规则、TCP监听器的HTTP健康检查方式）。
        注意：此字段可能返回 null，表示取不到有效值。
                :type HttpCheckPath: str
                :param HttpCheckDomain: 健康检查域名（仅适用于HTTP/HTTPS转发规则、TCP监听器的HTTP健康检查方式）。
        注意：此字段可能返回 null，表示取不到有效值。
                :type HttpCheckDomain: str
                :param HttpCheckMethod: 健康检查方法（仅适用于HTTP/HTTPS转发规则、TCP监听器的HTTP健康检查方式），
                默认值：HEAD，可选值HEAD或GET。
        注意：此字段可能返回 null，表示取不到有效值。
                :type HttpCheckMethod: str
                :param CheckPort: 自定义探测相关参数。健康检查端口，默认为后端服务的端口，
                除非您希望指定特定端口，否则建议留空。（仅适用于TCP/UDP监听器）。
        注意：此字段可能返回 null，表示取不到有效值。
                :type CheckPort: int
                :param ContextType: 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，
                代表健康检查的输入格式，可取值：HEX或TEXT；取值为HEX时，
                SendContext和RecvContext的字符只能在0123456789ABCDEF中选取且长度必须是偶数位。（仅适用于TCP/UDP监听器）
        注意：此字段可能返回 null，表示取不到有效值。
                :type ContextType: str
                :param SendContext: 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，
                代表健康检查发送的请求内容，只允许ASCII可见字符，最大长度限制500。（仅适用于TCP/UDP监听器）。
        注意：此字段可能返回 null，表示取不到有效值。
                :type SendContext: str
                :param RecvContext: 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，
                代表健康检查返回的结果，只允许ASCII可见字符，最大长度限制500。（仅适用于TCP/UDP监听器）。
        注意：此字段可能返回 null，表示取不到有效值。
                :type RecvContext: str
                :param CheckType: 自定义探测相关参数。健康检查使用的协议：TCP | HTTP | CUSTOM
                （仅适用于TCP/UDP监听器，其中UDP监听器只支持CUSTOM；如果使用自定义健康检查功能，则必传）。
        注意：此字段可能返回 null，表示取不到有效值。
                :type CheckType: str
                :param HttpVersion: 自定义探测相关参数。健康检查协议CheckType的值取HTTP时，必传此字段，
                代表后端服务的HTTP版本：HTTP/1.0、HTTP/1.1；（仅适用于TCP监听器）
        注意：此字段可能返回 null，表示取不到有效值。
                :type HttpVersion: str
        """
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnHealthNum = None
        self.HttpCode = None
        self.HttpCheckPath = None
        self.HttpCheckDomain = None
        self.HttpCheckMethod = None
        self.CheckPort = None
        self.ContextType = None
        self.SendContext = None
        self.RecvContext = None
        self.CheckType = None
        self.HttpVersion = None

    def _deserialize(self, params):
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnHealthNum = params.get("UnHealthNum")
        self.HttpCode = params.get("HttpCode")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.HttpCheckDomain = params.get("HttpCheckDomain")
        self.HttpCheckMethod = params.get("HttpCheckMethod")
        self.CheckPort = params.get("CheckPort")
        self.ContextType = params.get("ContextType")
        self.SendContext = params.get("SendContext")
        self.RecvContext = params.get("RecvContext")
        self.CheckType = params.get("CheckType")
        self.HttpVersion = params.get("HttpVersion")


class InquiryPriceCreateLoadBalancerRequest(AbstractModel):
    """InquiryPriceCreateLoadBalancer请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerType: 询价的负载均衡类型，OPEN为公网类型，INTERNAL为内网类型
        :type LoadBalancerType: str
        :param LoadBalancerChargeType: 询价的收费类型，POSTPAID为按量计费，"PREPAID"为预付费包年包月
        :type LoadBalancerChargeType: str
        :param LoadBalancerChargePrepaid: 询价的收费周期
        :type LoadBalancerChargePrepaid: :class:`tcecloud.clb.v20180317.models.LBChargePrepaid`
        :param InternetAccessible: 询价的网络计费方式
        :type InternetAccessible: :class:`tcecloud.clb.v20180317.models.InternetAccessible`
        :param GoodsNum: 询价的负载均衡实例个数，默认为1
        :type GoodsNum: int
        """
        self.LoadBalancerType = None
        self.LoadBalancerChargeType = None
        self.LoadBalancerChargePrepaid = None
        self.InternetAccessible = None
        self.GoodsNum = None

    def _deserialize(self, params):
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.LoadBalancerChargeType = params.get("LoadBalancerChargeType")
        if params.get("LoadBalancerChargePrepaid") is not None:
            self.LoadBalancerChargePrepaid = LBChargePrepaid()
            self.LoadBalancerChargePrepaid._deserialize(params.get("LoadBalancerChargePrepaid"))
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.GoodsNum = params.get("GoodsNum")


class InquiryPriceCreateLoadBalancerResponse(AbstractModel):
    """InquiryPriceCreateLoadBalancer返回参数结构体"""

    def __init__(self):
        """
        :param Price: 该参数表示对应的价格。
        :type Price: :class:`tcecloud.clb.v20180317.models.Price`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceModifyLoadBalancerRequest(AbstractModel):
    """InquiryPriceModifyLoadBalancer请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡ID
        :type LoadBalancerId: str
        :param InternetAccessible: 修改后的网络带宽信息
        :type InternetAccessible: :class:`tcecloud.clb.v20180317.models.InternetAccessible`
        """
        self.LoadBalancerId = None
        self.InternetAccessible = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))


class InquiryPriceModifyLoadBalancerResponse(AbstractModel):
    """InquiryPriceModifyLoadBalancer返回参数结构体"""

    def __init__(self):
        """
        :param Price: 描述价格信息
        :type Price: :class:`tcecloud.clb.v20180317.models.Price`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceRefundLoadBalancerRequest(AbstractModel):
    """InquiryPriceRefundLoadBalancer请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡ID
        :type LoadBalancerId: str
        """
        self.LoadBalancerId = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")


class InquiryPriceRefundLoadBalancerResponse(AbstractModel):
    """InquiryPriceRefundLoadBalancer返回参数结构体"""

    def __init__(self):
        """
        :param Price: 该参数表示对应的价格。
        :type Price: :class:`tcecloud.clb.v20180317.models.Price`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceRenewLoadBalancerRequest(AbstractModel):
    """InquiryPriceRenewLoadBalancer请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡ID
        :type LoadBalancerId: str
        :param LoadBalancerChargePrepaid: 续费周期
        :type LoadBalancerChargePrepaid: :class:`tcecloud.clb.v20180317.models.LBChargePrepaid`
        """
        self.LoadBalancerId = None
        self.LoadBalancerChargePrepaid = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("LoadBalancerChargePrepaid") is not None:
            self.LoadBalancerChargePrepaid = LBChargePrepaid()
            self.LoadBalancerChargePrepaid._deserialize(params.get("LoadBalancerChargePrepaid"))


class InquiryPriceRenewLoadBalancerResponse(AbstractModel):
    """InquiryPriceRenewLoadBalancer返回参数结构体"""

    def __init__(self):
        """
        :param Price: 表示续费价格
        :type Price: :class:`tcecloud.clb.v20180317.models.Price`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InternetAccessible(AbstractModel):
    """网络计费模式，最大出带宽"""

    def __init__(self):
        """
                :param InternetChargeType: TRAFFIC_POSTPAID_BY_HOUR 按流量按小时后计费 ; BANDWIDTH_POSTPAID_BY_HOUR 按带宽按小时后计费;
        BANDWIDTH_PACKAGE 按带宽包计费（当前，只有指定运营商时才支持此种计费模式）
        注意：此字段可能返回 null，表示取不到有效值。
                :type InternetChargeType: str
                :param InternetMaxBandwidthOut: 最大出带宽，单位Mbps，范围支持0到2048，仅对公网属性的LB生效，默认值 10
        注意：此字段可能返回 null，表示取不到有效值。
                :type InternetMaxBandwidthOut: int
                :param BandwidthpkgSubType: 带宽包的类型，如SINGLEISP
        注意：此字段可能返回 null，表示取不到有效值。
                :type BandwidthpkgSubType: str
        """
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.BandwidthpkgSubType = None

    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.BandwidthpkgSubType = params.get("BandwidthpkgSubType")


class ItemPrice(AbstractModel):
    """描述了单项的价格信息"""

    def __init__(self):
        """
                :param UnitPrice: 后付费单价，单位：元。
        注意：此字段可能返回 null，表示取不到有效值。
                :type UnitPrice: float
                :param ChargeUnit: 后续计价单元，可取值范围：
        HOUR：表示计价单元是按每小时来计算。当前涉及该计价单元的场景有：实例按小时后付费（POSTPAID_BY_HOUR）、带宽按小时后付费（BANDWIDTH_POSTPAID_BY_HOUR）；
        GB：表示计价单元是按每GB来计算。当前涉及该计价单元的场景有：流量按小时后付费（TRAFFIC_POSTPAID_BY_HOUR）。
        注意：此字段可能返回 null，表示取不到有效值。
                :type ChargeUnit: str
                :param OriginalPrice: 预支费用的原价，单位：元。
        注意：此字段可能返回 null，表示取不到有效值。
                :type OriginalPrice: float
                :param DiscountPrice: 预支费用的折扣价，单位：元。
        注意：此字段可能返回 null，表示取不到有效值。
                :type DiscountPrice: float
                :param UnitPriceDiscount: 后付费的折扣单价，单位:元
        注意：此字段可能返回 null，表示取不到有效值。
                :type UnitPriceDiscount: float
        """
        self.UnitPrice = None
        self.ChargeUnit = None
        self.OriginalPrice = None
        self.DiscountPrice = None
        self.UnitPriceDiscount = None

    def _deserialize(self, params):
        self.UnitPrice = params.get("UnitPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        self.UnitPriceDiscount = params.get("UnitPriceDiscount")


class LBChargePrepaid(AbstractModel):
    """lb实例包年包月相关配置属性"""

    def __init__(self):
        """
                :param RenewFlag: 续费类型：AUTO_RENEW 自动续费，  MANUAL_RENEW 手动续费
        注意：此字段可能返回 null，表示取不到有效值。
                :type RenewFlag: str
                :param Period: 购买时长，单位：月
        注意：此字段可能返回 null，表示取不到有效值。
                :type Period: int
        """
        self.RenewFlag = None
        self.Period = None

    def _deserialize(self, params):
        self.RenewFlag = params.get("RenewFlag")
        self.Period = params.get("Period")


class LBItem(AbstractModel):
    """反查Lb绑定关系。"""

    def __init__(self):
        """
        :param LoadBalancerId: lb的字符串id
        :type LoadBalancerId: str
        :param Vip: lb的vip
        :type Vip: str
        :param Listeners: 监听器规则
        :type Listeners: list of ListenerItem
        :param Region: LB所在地域
        :type Region: str
        """
        self.LoadBalancerId = None
        self.Vip = None
        self.Listeners = None
        self.Region = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Vip = params.get("Vip")
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerItem()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.Region = params.get("Region")


class LbRsItem(AbstractModel):
    """查询类型"""

    def __init__(self):
        """
        :param VpcId: vpc的字符串id，只支持字符串id。
        :type VpcId: str
        :param PrivateIp: 需要查询后端的内网ip，可以是cvm和弹性网卡。
        :type PrivateIp: str
        """
        self.VpcId = None
        self.PrivateIp = None

    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.PrivateIp = params.get("PrivateIp")


class LbRsTargets(AbstractModel):
    """反查结果数据类型。"""

    def __init__(self):
        """
                :param Type: 内网ip类型。“cvm”或“eni”
                :type Type: str
                :param PrivateIp: 后端实例的内网ip。
                :type PrivateIp: str
                :param Port: 绑定后端实例的端口。
                :type Port: int
                :param VpcId: rs的vpcId
        注意：此字段可能返回 null，表示取不到有效值。
                :type VpcId: int
                :param Weight: rs的权重
        注意：此字段可能返回 null，表示取不到有效值。
                :type Weight: int
        """
        self.Type = None
        self.PrivateIp = None
        self.Port = None
        self.VpcId = None
        self.Weight = None

    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PrivateIp = params.get("PrivateIp")
        self.Port = params.get("Port")
        self.VpcId = params.get("VpcId")
        self.Weight = params.get("Weight")


class Listener(AbstractModel):
    """监听器的信息"""

    def __init__(self):
        """
                :param ListenerId: 负载均衡监听器 ID
                :type ListenerId: str
                :param Protocol: 监听器协议
                :type Protocol: str
                :param Port: 监听器端口
                :type Port: int
                :param Certificate: 监听器绑定的证书信息
        注意：此字段可能返回 null，表示取不到有效值。
                :type Certificate: :class:`tcecloud.clb.v20180317.models.CertificateOutput`
                :param HealthCheck: 监听器的健康检查信息
        注意：此字段可能返回 null，表示取不到有效值。
                :type HealthCheck: :class:`tcecloud.clb.v20180317.models.HealthCheck`
                :param Scheduler: 请求的调度方式
        注意：此字段可能返回 null，表示取不到有效值。
                :type Scheduler: str
                :param SessionExpireTime: 会话保持时间
        注意：此字段可能返回 null，表示取不到有效值。
                :type SessionExpireTime: int
                :param SniSwitch: 是否开启SNI特性（本参数仅对于HTTPS监听器有意义）
        注意：此字段可能返回 null，表示取不到有效值。
                :type SniSwitch: int
                :param Rules: 监听器下的全部转发规则（本参数仅对于HTTP/HTTPS监听器有意义）
        注意：此字段可能返回 null，表示取不到有效值。
                :type Rules: list of RuleOutput
                :param ListenerName: 监听器的名称
        注意：此字段可能返回 null，表示取不到有效值。
                :type ListenerName: str
                :param CreateTime: 监听器的创建时间。
        注意：此字段可能返回 null，表示取不到有效值。
                :type CreateTime: str
                :param EndPort: 端口段结束端口
        注意：此字段可能返回 null，表示取不到有效值。
                :type EndPort: int
                :param TargetType: 后端服务器类型
        注意：此字段可能返回 null，表示取不到有效值。
                :type TargetType: str
                :param TargetGroup: 绑定的目标组基本信息；当监听器绑定目标组时，会返回该字段
        注意：此字段可能返回 null，表示取不到有效值。
                :type TargetGroup: :class:`tcecloud.clb.v20180317.models.BasicTargetGroupInfo`
        """
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.Certificate = None
        self.HealthCheck = None
        self.Scheduler = None
        self.SessionExpireTime = None
        self.SniSwitch = None
        self.Rules = None
        self.ListenerName = None
        self.CreateTime = None
        self.EndPort = None
        self.TargetType = None
        self.TargetGroup = None

    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Certificate") is not None:
            self.Certificate = CertificateOutput()
            self.Certificate._deserialize(params.get("Certificate"))
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        self.Scheduler = params.get("Scheduler")
        self.SessionExpireTime = params.get("SessionExpireTime")
        self.SniSwitch = params.get("SniSwitch")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleOutput()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.ListenerName = params.get("ListenerName")
        self.CreateTime = params.get("CreateTime")
        self.EndPort = params.get("EndPort")
        self.TargetType = params.get("TargetType")
        if params.get("TargetGroup") is not None:
            self.TargetGroup = BasicTargetGroupInfo()
            self.TargetGroup._deserialize(params.get("TargetGroup"))


class ListenerBackend(AbstractModel):
    """监听器上绑定的后端服务的信息"""

    def __init__(self):
        """
                :param ListenerId: 监听器 ID
                :type ListenerId: str
                :param Protocol: 监听器的协议
                :type Protocol: str
                :param Port: 监听器的端口
                :type Port: int
                :param Rules: 监听器下的规则信息（仅适用于HTTP/HTTPS监听器）
        注意：此字段可能返回 null，表示取不到有效值。
                :type Rules: list of RuleTargets
                :param Targets: 监听器上绑定的后端服务列表（仅适用于TCP/UDP/TCP_SSL监听器）
        注意：此字段可能返回 null，表示取不到有效值。
                :type Targets: list of Backend
                :param EndPort: 若支持端口段，则为端口段结束端口；若不支持端口段，则为0
        注意：此字段可能返回 null，表示取不到有效值。
                :type EndPort: int
        """
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.Rules = None
        self.Targets = None
        self.EndPort = None

    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleTargets()
                obj._deserialize(item)
                self.Rules.append(obj)
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Backend()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.EndPort = params.get("EndPort")


class ListenerHealth(AbstractModel):
    """监听器的健康检查信息"""

    def __init__(self):
        """
                :param ListenerId: 监听器ID
                :type ListenerId: str
                :param ListenerName: 监听器名称
        注意：此字段可能返回 null，表示取不到有效值。
                :type ListenerName: str
                :param Protocol: 监听器的协议
                :type Protocol: str
                :param Port: 监听器的端口
                :type Port: int
                :param Rules: 监听器的转发规则列表
        注意：此字段可能返回 null，表示取不到有效值。
                :type Rules: list of RuleHealth
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.Port = None
        self.Rules = None

    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleHealth()
                obj._deserialize(item)
                self.Rules.append(obj)


class ListenerItem(AbstractModel):
    """反查监听器类型"""

    def __init__(self):
        """
                :param ListenerId: 监听器ID
                :type ListenerId: str
                :param Protocol: 监听器协议
                :type Protocol: str
                :param Port: 监听器端口
                :type Port: int
                :param Rules: 绑定规则
        注意：此字段可能返回 null，表示取不到有效值。
                :type Rules: list of RulesItems
                :param Targets: 四层绑定对象
        注意：此字段可能返回 null，表示取不到有效值。
                :type Targets: list of LbRsTargets
                :param EndPort: 端口段监听器的结束端口
        注意：此字段可能返回 null，表示取不到有效值。
                :type EndPort: int
        """
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.Rules = None
        self.Targets = None
        self.EndPort = None

    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RulesItems()
                obj._deserialize(item)
                self.Rules.append(obj)
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = LbRsTargets()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.EndPort = params.get("EndPort")


class LoadBalancer(AbstractModel):
    """负载均衡实例的信息"""

    def __init__(self):
        """
                :param LoadBalancerId: 负载均衡实例 ID。
                :type LoadBalancerId: str
                :param LoadBalancerName: 负载均衡实例的名称。
                :type LoadBalancerName: str
                :param LoadBalancerType: 负载均衡实例的网络类型：
        OPEN：公网属性， INTERNAL：内网属性。
                :type LoadBalancerType: str
                :param Forward: 负载均衡类型标识，1：负载均衡，0：传统型负载均衡。
                :type Forward: int
                :param Domain: 负载均衡实例的域名，仅公网传统型负载均衡实例才提供该字段
        注意：此字段可能返回 null，表示取不到有效值。
                :type Domain: str
                :param LoadBalancerVips: 负载均衡实例的 VIP 列表。
        注意：此字段可能返回 null，表示取不到有效值。
                :type LoadBalancerVips: list of str
                :param Status: 负载均衡实例的状态，包括
        0：创建中，1：正常运行。
        注意：此字段可能返回 null，表示取不到有效值。
                :type Status: int
                :param CreateTime: 负载均衡实例的创建时间。
        注意：此字段可能返回 null，表示取不到有效值。
                :type CreateTime: str
                :param StatusTime: 负载均衡实例的上次状态转换时间。
        注意：此字段可能返回 null，表示取不到有效值。
                :type StatusTime: str
                :param ProjectId: 负载均衡实例所属的项目 ID， 0 表示默认项目。
                :type ProjectId: int
                :param VpcId: 私有网络的 ID
        注意：此字段可能返回 null，表示取不到有效值。
                :type VpcId: str
                :param OpenBgp: 高防 LB 的标识，1：高防负载均衡 0：非高防负载均衡。
        注意：此字段可能返回 null，表示取不到有效值。
                :type OpenBgp: int
                :param Snat: 在 2016 年 12 月份之前的传统型内网负载均衡都是开启了 snat 的。
        注意：此字段可能返回 null，表示取不到有效值。
                :type Snat: bool
                :param Isolation: 0：表示未被隔离，1：表示被隔离。
        注意：此字段可能返回 null，表示取不到有效值。
                :type Isolation: int
                :param Log: 用户开启日志的信息，日志只有公网属性创建了 HTTP 、HTTPS 监听器的负载均衡才会有日志。
        注意：此字段可能返回 null，表示取不到有效值。
                :type Log: str
                :param SubnetId: 负载均衡实例所在的子网（仅对内网VPC型LB有意义）
        注意：此字段可能返回 null，表示取不到有效值。
                :type SubnetId: str
                :param Tags: 负载均衡实例的标签信息
        注意：此字段可能返回 null，表示取不到有效值。
                :type Tags: list of TagInfo
                :param SecureGroups: 负载均衡实例的安全组
        注意：此字段可能返回 null，表示取不到有效值。
                :type SecureGroups: list of str
                :param TargetRegionInfo: 负载均衡实例绑定的后端设备的基本信息
        注意：此字段可能返回 null，表示取不到有效值。
                :type TargetRegionInfo: :class:`tcecloud.clb.v20180317.models.TargetRegionInfo`
                :param AnycastZone: anycast负载均衡的发布域，对于非anycast的负载均衡，此字段返回为空字符串
        注意：此字段可能返回 null，表示取不到有效值。
                :type AnycastZone: str
                :param AddressIPVersion: IP版本，ipv4 | ipv6
        注意：此字段可能返回 null，表示取不到有效值。
                :type AddressIPVersion: str
                :param NumericalVpcId: 数值形式的私有网络 ID
        注意：此字段可能返回 null，表示取不到有效值。
                :type NumericalVpcId: int
                :param VipIsp: 负载均衡IP地址所属的ISP
        注意：此字段可能返回 null，表示取不到有效值。
                :type VipIsp: str
                :param MasterZone: 主可用区
        注意：此字段可能返回 null，表示取不到有效值。
                :type MasterZone: :class:`tcecloud.clb.v20180317.models.ZoneInfo`
                :param BackupZoneSet: 备可用区
        注意：此字段可能返回 null，表示取不到有效值。
                :type BackupZoneSet: list of ZoneInfo
                :param IsolatedTime: 负载均衡实例被隔离的时间
        注意：此字段可能返回 null，表示取不到有效值。
                :type IsolatedTime: str
                :param ExpireTime: 负载均衡实例的过期时间，仅对预付费负载均衡生效
        注意：此字段可能返回 null，表示取不到有效值。
                :type ExpireTime: str
                :param ChargeType: 负载均衡实例的计费类型
        注意：此字段可能返回 null，表示取不到有效值。
                :type ChargeType: str
                :param NetworkAttributes: 负载均衡实例的网络属性
        注意：此字段可能返回 null，表示取不到有效值。
                :type NetworkAttributes: :class:`tcecloud.clb.v20180317.models.InternetAccessible`
                :param PrepaidAttributes: 负载均衡实例的预付费相关属性
        注意：此字段可能返回 null，表示取不到有效值。
                :type PrepaidAttributes: :class:`tcecloud.clb.v20180317.models.LBChargePrepaid`
                :param LogSetId: 负载均衡日志服务(CLS)的日志集ID
        注意：此字段可能返回 null，表示取不到有效值。
                :type LogSetId: str
                :param LogTopicId: 负载均衡日志服务(CLS)的日志主题ID
        注意：此字段可能返回 null，表示取不到有效值。
                :type LogTopicId: str
                :param AddressIPv6: 负载均衡实例的IPv6地址
        注意：此字段可能返回 null，表示取不到有效值。
                :type AddressIPv6: str
                :param ExtraInfo: 暂做保留，一般用户无需关注。
        注意：此字段可能返回 null，表示取不到有效值。
                :type ExtraInfo: :class:`tcecloud.clb.v20180317.models.ExtraInfo`
                :param IsDDos: 是否可绑定高防包
        注意：此字段可能返回 null，表示取不到有效值。
                :type IsDDos: bool
                :param ConfigId: 负载均衡维度的个性化配置ID
        注意：此字段可能返回 null，表示取不到有效值。
                :type ConfigId: str
                :param LoadBalancerPassToTarget: 后端服务是否放通来自LB的流量
        注意：此字段可能返回 null，表示取不到有效值。
                :type LoadBalancerPassToTarget: bool
                :param ExclusiveCluster: 内网独占集群
        注意：此字段可能返回 null，表示取不到有效值。
                :type ExclusiveCluster: :class:`tcecloud.clb.v20180317.models.ExclusiveCluster`
                :param IPv6Mode: IP地址版本为ipv6时此字段有意义， IPv6Nat64 | IPv6FullChain
        注意：此字段可能返回 null，表示取不到有效值。
                :type IPv6Mode: str
                :param SnatPro: 是否开启SnatPro
        注意：此字段可能返回 null，表示取不到有效值。
                :type SnatPro: bool
                :param SnatIps: 开启SnatPro负载均衡后，SnatIp列表
        注意：此字段可能返回 null，表示取不到有效值。
                :type SnatIps: list of SnatIp
                :param SlaType: 性能保障规格
        注意：此字段可能返回 null，表示取不到有效值。
                :type SlaType: str
                :param IsBlock: vip是否被封堵
        注意：此字段可能返回 null，表示取不到有效值。
                :type IsBlock: bool
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.LoadBalancerType = None
        self.Forward = None
        self.Domain = None
        self.LoadBalancerVips = None
        self.Status = None
        self.CreateTime = None
        self.StatusTime = None
        self.ProjectId = None
        self.VpcId = None
        self.OpenBgp = None
        self.Snat = None
        self.Isolation = None
        self.Log = None
        self.SubnetId = None
        self.Tags = None
        self.SecureGroups = None
        self.TargetRegionInfo = None
        self.AnycastZone = None
        self.AddressIPVersion = None
        self.NumericalVpcId = None
        self.VipIsp = None
        self.MasterZone = None
        self.BackupZoneSet = None
        self.IsolatedTime = None
        self.ExpireTime = None
        self.ChargeType = None
        self.NetworkAttributes = None
        self.PrepaidAttributes = None
        self.LogSetId = None
        self.LogTopicId = None
        self.AddressIPv6 = None
        self.ExtraInfo = None
        self.IsDDos = None
        self.ConfigId = None
        self.LoadBalancerPassToTarget = None
        self.ExclusiveCluster = None
        self.IPv6Mode = None
        self.SnatPro = None
        self.SnatIps = None
        self.SlaType = None
        self.IsBlock = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Forward = params.get("Forward")
        self.Domain = params.get("Domain")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.StatusTime = params.get("StatusTime")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.OpenBgp = params.get("OpenBgp")
        self.Snat = params.get("Snat")
        self.Isolation = params.get("Isolation")
        self.Log = params.get("Log")
        self.SubnetId = params.get("SubnetId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.SecureGroups = params.get("SecureGroups")
        if params.get("TargetRegionInfo") is not None:
            self.TargetRegionInfo = TargetRegionInfo()
            self.TargetRegionInfo._deserialize(params.get("TargetRegionInfo"))
        self.AnycastZone = params.get("AnycastZone")
        self.AddressIPVersion = params.get("AddressIPVersion")
        self.NumericalVpcId = params.get("NumericalVpcId")
        self.VipIsp = params.get("VipIsp")
        if params.get("MasterZone") is not None:
            self.MasterZone = ZoneInfo()
            self.MasterZone._deserialize(params.get("MasterZone"))
        if params.get("BackupZoneSet") is not None:
            self.BackupZoneSet = []
            for item in params.get("BackupZoneSet"):
                if item:
                    obj = ZoneInfo()
                    obj._deserialize(item)
                    self.BackupZoneSet.append(obj)
        self.IsolatedTime = params.get("IsolatedTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ChargeType = params.get("ChargeType")
        if params.get("NetworkAttributes") is not None:
            self.NetworkAttributes = InternetAccessible()
            self.NetworkAttributes._deserialize(params.get("NetworkAttributes"))
        if params.get("PrepaidAttributes") is not None:
            self.PrepaidAttributes = LBChargePrepaid()
            self.PrepaidAttributes._deserialize(params.get("PrepaidAttributes"))
        self.LogSetId = params.get("LogSetId")
        self.LogTopicId = params.get("LogTopicId")
        self.AddressIPv6 = params.get("AddressIPv6")
        if params.get("ExtraInfo") is not None:
            self.ExtraInfo = ExtraInfo()
            self.ExtraInfo._deserialize(params.get("ExtraInfo"))
        self.IsDDos = params.get("IsDDos")
        self.ConfigId = params.get("ConfigId")
        self.LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        if params.get("ExclusiveCluster") is not None:
            self.ExclusiveCluster = ExclusiveCluster()
            self.ExclusiveCluster._deserialize(params.get("ExclusiveCluster"))
        self.IPv6Mode = params.get("IPv6Mode")
        self.SnatPro = params.get("SnatPro")
        if params.get("SnatIps") is not None:
            self.SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self.SnatIps.append(obj)
        self.SlaType = params.get("SlaType")
        self.IsBlock = params.get("IsBlock")


class LoadBalancerHealth(AbstractModel):
    """负载均衡实例的健康检查状态"""

    def __init__(self):
        """
                :param LoadBalancerId: 负载均衡实例ID
                :type LoadBalancerId: str
                :param LoadBalancerName: 负载均衡实例名称
        注意：此字段可能返回 null，表示取不到有效值。
                :type LoadBalancerName: str
                :param Listeners: 监听器列表
        注意：此字段可能返回 null，表示取不到有效值。
                :type Listeners: list of ListenerHealth
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.Listeners = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerHealth()
                obj._deserialize(item)
                self.Listeners.append(obj)


class LoadBalancerIdPair(AbstractModel):
    """关联操作的两个负载均衡类型"""

    def __init__(self):
        """
        :param SrcId: 源负载均衡ID
        :type SrcId: str
        :param DstId: 目的负载均衡ID
        :type DstId: str
        """
        self.SrcId = None
        self.DstId = None

    def _deserialize(self, params):
        self.SrcId = params.get("SrcId")
        self.DstId = params.get("DstId")


class ManualRewriteRequest(AbstractModel):
    """ManualRewrite请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID
        :type LoadBalancerId: str
        :param SourceListenerId: 源监听器ID
        :type SourceListenerId: str
        :param TargetListenerId: 目标监听器ID
        :type TargetListenerId: str
        :param RewriteInfos: 转发规则之间的重定向关系
        :type RewriteInfos: list of RewriteLocationMap
        """
        self.LoadBalancerId = None
        self.SourceListenerId = None
        self.TargetListenerId = None
        self.RewriteInfos = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SourceListenerId = params.get("SourceListenerId")
        self.TargetListenerId = params.get("TargetListenerId")
        if params.get("RewriteInfos") is not None:
            self.RewriteInfos = []
            for item in params.get("RewriteInfos"):
                obj = RewriteLocationMap()
                obj._deserialize(item)
                self.RewriteInfos.append(obj)


class ManualRewriteResponse(AbstractModel):
    """ManualRewrite返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MasterZoneInfo(AbstractModel):
    """主可用区相关信息"""

    def __init__(self):
        """
                :param ZoneId: 可用区数值形式的唯一ID，如：100001
        注意：此字段可能返回 null，表示取不到有效值。
                :type ZoneId: int
                :param Zone: 可用区字符串形式的唯一ID，如：ap-guangzhou-1
        注意：此字段可能返回 null，表示取不到有效值。
                :type Zone: str
                :param ZoneName: 可用区名称，如：广州一区
        注意：此字段可能返回 null，表示取不到有效值。
                :type ZoneName: str
                :param BackupZoneSet: 备可用区列表
        注意：此字段可能返回 null，表示取不到有效值。
                :type BackupZoneSet: list of ZoneInfo
        """
        self.ZoneId = None
        self.Zone = None
        self.ZoneName = None
        self.BackupZoneSet = None

    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        if params.get("BackupZoneSet") is not None:
            self.BackupZoneSet = []
            for item in params.get("BackupZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.BackupZoneSet.append(obj)


class MigrateAppIdVIPRequest(AbstractModel):
    """MigrateAppIdVIP请求参数结构体"""

    def __init__(self):
        """
        :param SrcAppId: 源开发商AppId
        :type SrcAppId: int
        :param LoadBalancerIdPairs: 操作的一对负载均衡ID
        :type LoadBalancerIdPairs: list of LoadBalancerIdPair
        """
        self.SrcAppId = None
        self.LoadBalancerIdPairs = None

    def _deserialize(self, params):
        self.SrcAppId = params.get("SrcAppId")
        if params.get("LoadBalancerIdPairs") is not None:
            self.LoadBalancerIdPairs = []
            for item in params.get("LoadBalancerIdPairs"):
                obj = LoadBalancerIdPair()
                obj._deserialize(item)
                self.LoadBalancerIdPairs.append(obj)


class MigrateAppIdVIPResponse(AbstractModel):
    """MigrateAppIdVIP返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBlockIPListRequest(AbstractModel):
    """ModifyBlockIPList请求参数结构体"""

    def __init__(self):
        """
                :param LoadBalancerIds: 负载均衡实例ID
                :type LoadBalancerIds: list of str
                :param Type: 操作类型，可取：
        <li> add_customized_field（首次设置header，开启黑名单功能）</li>
        <li> set_customized_field（修改header）</li>
        <li> del_customized_field（删除header）</li>
        <li> add_blocked（添加黑名单）</li>
        <li> del_blocked（删除黑名单）</li>
        <li> flush_blocked（清空黑名单）</li>
                :type Type: str
                :param ClientIPField: 客户端真实IP存放的header字段名
                :type ClientIPField: str
                :param BlockIPList: 封禁IP列表，单次操作数组最大长度支持200000
                :type BlockIPList: list of str
                :param ExpireTime: 过期时间，单位秒，默认值3600
                :type ExpireTime: int
                :param AddStrategy: 添加IP的策略，可取：fifo（如果黑名单容量已满，新加入黑名单的IP采用先进先出策略）
                :type AddStrategy: str
        """
        self.LoadBalancerIds = None
        self.Type = None
        self.ClientIPField = None
        self.BlockIPList = None
        self.ExpireTime = None
        self.AddStrategy = None

    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.Type = params.get("Type")
        self.ClientIPField = params.get("ClientIPField")
        self.BlockIPList = params.get("BlockIPList")
        self.ExpireTime = params.get("ExpireTime")
        self.AddStrategy = params.get("AddStrategy")


class ModifyBlockIPListResponse(AbstractModel):
    """ModifyBlockIPList返回参数结构体"""

    def __init__(self):
        """
        :param JodId: 异步任务的ID
        :type JodId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JodId = None
        self.RequestId = None

    def _deserialize(self, params):
        self.JodId = params.get("JodId")
        self.RequestId = params.get("RequestId")


class ModifyCustomizedConfigRequest(AbstractModel):
    """ModifyCustomizedConfig请求参数结构体"""

    def __init__(self):
        """
        :param ConfigName: 配置名字
        :type ConfigName: str
        :param UconfigId: 配置ID
        :type UconfigId: str
        :param ConfigContent: 配置内容
        :type ConfigContent: str
        """
        self.ConfigName = None
        self.UconfigId = None
        self.ConfigContent = None

    def _deserialize(self, params):
        self.ConfigName = params.get("ConfigName")
        self.UconfigId = params.get("UconfigId")
        self.ConfigContent = params.get("ConfigContent")


class ModifyCustomizedConfigResponse(AbstractModel):
    """ModifyCustomizedConfig返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDnatRequest(AbstractModel):
    """ModifyDnat请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: clb的字符串id
        :type LoadBalancerId: str
        :param Switch: 开关参数。1 开启直通，0 关闭直通。
        :type Switch: int
        """
        self.LoadBalancerId = None
        self.Switch = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Switch = params.get("Switch")


class ModifyDnatResponse(AbstractModel):
    """ModifyDnat返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDomainAttributesRequest(AbstractModel):
    """ModifyDomainAttributes请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param Domain: 域名（必须是已经创建的转发规则下的域名）
        :type Domain: str
        :param NewDomain: 要修改的新域名
        :type NewDomain: str
        :param Certificate: 域名相关的证书信息，注意，仅对启用SNI的监听器适用。
        :type Certificate: :class:`tcecloud.clb.v20180317.models.CertificateInput`
        :param Http2: 是否开启Http2，注意，只有HTTPS域名才能开启Http2。
        :type Http2: bool
        :param DefaultServer: 是否设为默认域名，注意，一个监听器下只能设置一个默认域名。
        :type DefaultServer: bool
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domain = None
        self.NewDomain = None
        self.Certificate = None
        self.Http2 = None
        self.DefaultServer = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.NewDomain = params.get("NewDomain")
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.Http2 = params.get("Http2")
        self.DefaultServer = params.get("DefaultServer")


class ModifyDomainAttributesResponse(AbstractModel):
    """ModifyDomainAttributes返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDomainRequest(AbstractModel):
    """ModifyDomain请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param Domain: 监听器下的某个旧域名。
        :type Domain: str
        :param NewDomain: 新域名，	长度限制为：1-120。有三种使用格式：
        非正则表达式格式，通配符格式，正则表达式格式。非正则表达式格式只能使用字母、数字、‘-’、‘.’。
        通配符格式的使用 ‘*’ 只能在开头或者结尾。正则表达式以'~'开头。
        :type NewDomain: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domain = None
        self.NewDomain = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.NewDomain = params.get("NewDomain")


class ModifyDomainResponse(AbstractModel):
    """ModifyDomain返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyListenerRequest(AbstractModel):
    """ModifyListener请求参数结构体"""

    def __init__(self):
        """
                :param LoadBalancerId: 负载均衡实例 ID
                :type LoadBalancerId: str
                :param ListenerId: 负载均衡监听器 ID
                :type ListenerId: str
                :param ListenerName: 新的监听器名称
                :type ListenerName: str
                :param SessionExpireTime: 会话保持时间，单位：秒。可选值：30~3600，默认 0，表示不开启。此参数仅适用于TCP/UDP监听器。
                :type SessionExpireTime: int
                :param HealthCheck: 健康检查相关参数，此参数仅适用于TCP/UDP/TCP_SSL监听器
                :type HealthCheck: :class:`tcecloud.clb.v20180317.models.HealthCheck`
                :param Certificate: 证书相关信息，此参数仅适用于HTTPS/TCP_SSL监听器
                :type Certificate: :class:`tcecloud.clb.v20180317.models.CertificateInput`
                :param Scheduler: 监听器转发的方式。可选值：WRR、LEAST_CONN
        分别表示按权重轮询、最小连接数， 默认为 WRR。
                :type Scheduler: str
                :param SniSwitch: 是否开启SNI特性，此参数仅适用于HTTPS监听器。注意：未开启SNI的监听器可以开启SNI；已开启SNI的监听器不能关闭SNI
                :type SniSwitch: int
                :param TargetType: 后端目标类型，NODE表示绑定普通节点，TARGETGROUP表示绑定目标组
                :type TargetType: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.ListenerName = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Certificate = None
        self.Scheduler = None
        self.SniSwitch = None
        self.TargetType = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.Scheduler = params.get("Scheduler")
        self.SniSwitch = params.get("SniSwitch")
        self.TargetType = params.get("TargetType")


class ModifyListenerResponse(AbstractModel):
    """ModifyListener返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancerAttributesRequest(AbstractModel):
    """ModifyLoadBalancerAttributes请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡的唯一ID
        :type LoadBalancerId: str
        :param LoadBalancerName: 负载均衡实例名称
        :type LoadBalancerName: str
        :param TargetRegionInfo: 负载均衡绑定的后端服务的地域信息
        :type TargetRegionInfo: :class:`tcecloud.clb.v20180317.models.TargetRegionInfo`
        :param InternetChargeInfo: 网络计费相关参数
        :type InternetChargeInfo: :class:`tcecloud.clb.v20180317.models.InternetAccessible`
        :param LoadBalancerPassToTarget: Target是否放通来自CLB的流量。开启放通（true）：只验证CLB上的安全组；不开启放通（false）：需同时验证CLB和后端实例上的安全组。
        :type LoadBalancerPassToTarget: bool
        :param ChargeType: 负载均衡实例的计费类型，后付费：POSTPAID_BY_HOUR，预付费：PREPAID。
        :type ChargeType: str
        :param SwitchFlag: 不同计费模式之间的切换：0表示不切换，1表示预付费和后付费切换，2表示后付费之间切换。默认值：0
        :type SwitchFlag: int
        :param PrepaidInfo: 负载均衡实例的预付费相关属性
        :type PrepaidInfo: :class:`tcecloud.clb.v20180317.models.LBChargePrepaid`
        :param ExclusiveCluster: 7层集群列表
        :type ExclusiveCluster: :class:`tcecloud.clb.v20180317.models.ExclusiveCluster`
        :param SnatPro: 是否开启SnatPro
        :type SnatPro: bool
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.TargetRegionInfo = None
        self.InternetChargeInfo = None
        self.LoadBalancerPassToTarget = None
        self.ChargeType = None
        self.SwitchFlag = None
        self.PrepaidInfo = None
        self.ExclusiveCluster = None
        self.SnatPro = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("TargetRegionInfo") is not None:
            self.TargetRegionInfo = TargetRegionInfo()
            self.TargetRegionInfo._deserialize(params.get("TargetRegionInfo"))
        if params.get("InternetChargeInfo") is not None:
            self.InternetChargeInfo = InternetAccessible()
            self.InternetChargeInfo._deserialize(params.get("InternetChargeInfo"))
        self.LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        self.ChargeType = params.get("ChargeType")
        self.SwitchFlag = params.get("SwitchFlag")
        if params.get("PrepaidInfo") is not None:
            self.PrepaidInfo = LBChargePrepaid()
            self.PrepaidInfo._deserialize(params.get("PrepaidInfo"))
        if params.get("ExclusiveCluster") is not None:
            self.ExclusiveCluster = ExclusiveCluster()
            self.ExclusiveCluster._deserialize(params.get("ExclusiveCluster"))
        self.SnatPro = params.get("SnatPro")


class ModifyLoadBalancerAttributesResponse(AbstractModel):
    """ModifyLoadBalancerAttributes返回参数结构体"""

    def __init__(self):
        """
        :param DealName: 切换负载均衡计费方式时，可用此参数查询切换任务是否成功。
        :type DealName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None

    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancersProjectRequest(AbstractModel):
    """ModifyLoadBalancersProject请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerIds: 一个或多个待操作的负载均衡实例ID。
        :type LoadBalancerIds: list of str
        :param ProjectId: 项目ID。
        :type ProjectId: int
        """
        self.LoadBalancerIds = None
        self.ProjectId = None

    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.ProjectId = params.get("ProjectId")


class ModifyLoadBalancersProjectResponse(AbstractModel):
    """ModifyLoadBalancersProject返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule请求参数结构体"""

    def __init__(self):
        """
                :param LoadBalancerId: 负载均衡实例 ID
                :type LoadBalancerId: str
                :param ListenerId: 负载均衡监听器 ID
                :type ListenerId: str
                :param LocationId: 要修改的转发规则的 ID。
                :type LocationId: str
                :param Url: 转发规则的新的转发路径，如不需修改Url，则不需提供此参数
                :type Url: str
                :param HealthCheck: 健康检查信息
                :type HealthCheck: :class:`tcecloud.clb.v20180317.models.HealthCheck`
                :param Scheduler: 规则的请求转发方式，可选值：WRR、LEAST_CONN、IP_HASH
        分别表示按权重轮询、最小连接数、按IP哈希， 默认为 WRR。
                :type Scheduler: str
                :param SessionExpireTime: 会话保持时间
                :type SessionExpireTime: int
                :param ForwardType: 负载均衡实例与后端服务之间的转发协议，默认HTTP，可取值：HTTP、HTTPS
                :type ForwardType: str
                :param TargetType: 后端目标类型，NODE表示绑定普通节点，TARGETGROUP表示绑定目标组
                :type TargetType: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationId = None
        self.Url = None
        self.HealthCheck = None
        self.Scheduler = None
        self.SessionExpireTime = None
        self.ForwardType = None
        self.TargetType = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationId = params.get("LocationId")
        self.Url = params.get("Url")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        self.Scheduler = params.get("Scheduler")
        self.SessionExpireTime = params.get("SessionExpireTime")
        self.ForwardType = params.get("ForwardType")
        self.TargetType = params.get("TargetType")


class ModifyRuleResponse(AbstractModel):
    """ModifyRule返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetGroupAttributeRequest(AbstractModel):
    """ModifyTargetGroupAttribute请求参数结构体"""

    def __init__(self):
        """
        :param TargetGroupId: 目标组的ID
        :type TargetGroupId: str
        :param TargetGroupName: 目标组的新名称
        :type TargetGroupName: str
        :param Port: 目标组的新默认端口
        :type Port: int
        """
        self.TargetGroupId = None
        self.TargetGroupName = None
        self.Port = None

    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.TargetGroupName = params.get("TargetGroupName")
        self.Port = params.get("Port")


class ModifyTargetGroupAttributeResponse(AbstractModel):
    """ModifyTargetGroupAttribute返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetGroupInstancesPortRequest(AbstractModel):
    """ModifyTargetGroupInstancesPort请求参数结构体"""

    def __init__(self):
        """
        :param TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param TargetGroupInstances: 待修改端口的服务器数组
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupId = None
        self.TargetGroupInstances = None

    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)


class ModifyTargetGroupInstancesPortResponse(AbstractModel):
    """ModifyTargetGroupInstancesPort返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetGroupInstancesWeightRequest(AbstractModel):
    """ModifyTargetGroupInstancesWeight请求参数结构体"""

    def __init__(self):
        """
        :param TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param TargetGroupInstances: 待修改权重的服务器数组
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupId = None
        self.TargetGroupInstances = None

    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)


class ModifyTargetGroupInstancesWeightResponse(AbstractModel):
    """ModifyTargetGroupInstancesWeight返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetPortRequest(AbstractModel):
    """ModifyTargetPort请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param Targets: 要修改端口的后端服务列表
        :type Targets: list of Target
        :param NewPort: 后端服务绑定到监听器或转发规则的新端口
        :type NewPort: int
        :param LocationId: 转发规则的ID，当后端服务绑定到七层转发规则时，必须提供此参数或Domain+Url两者之一
        :type LocationId: str
        :param Domain: 目标规则的域名，提供LocationId参数时本参数不生效
        :type Domain: str
        :param Url: 目标规则的URL，提供LocationId参数时本参数不生效
        :type Url: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Targets = None
        self.NewPort = None
        self.LocationId = None
        self.Domain = None
        self.Url = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.NewPort = params.get("NewPort")
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")


class ModifyTargetPortResponse(AbstractModel):
    """ModifyTargetPort返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetWeightRequest(AbstractModel):
    """ModifyTargetWeight请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param LocationId: 转发规则的ID，当绑定机器到七层转发规则时，必须提供此参数或Domain+Url两者之一
        :type LocationId: str
        :param Domain: 目标规则的域名，提供LocationId参数时本参数不生效
        :type Domain: str
        :param Url: 目标规则的URL，提供LocationId参数时本参数不生效
        :type Url: str
        :param Targets: 要修改权重的后端服务列表
        :type Targets: list of Target
        :param Weight: 后端服务新的转发权重，取值范围：0~100，默认值10。如果设置了 Targets.Weight 参数，则此参数不生效。
        :type Weight: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Targets = None
        self.Weight = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.Weight = params.get("Weight")


class ModifyTargetWeightResponse(AbstractModel):
    """ModifyTargetWeight返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OneCapacity(AbstractModel):
    """返回独占集群容量信息"""

    def __init__(self):
        """
                :param SetName: 集群名字
                :type SetName: str
                :param MaxConn: 最大连接数
        注意：此字段可能返回 null，表示取不到有效值。
                :type MaxConn: int
                :param MaxQps: 最大Qps
        注意：此字段可能返回 null，表示取不到有效值。
                :type MaxQps: int
                :param MaxInPkg: 最大入包量，单位pps
        注意：此字段可能返回 null，表示取不到有效值。
                :type MaxInPkg: int
                :param MaxOutPkg: 最大出包量，单位pps
        注意：此字段可能返回 null，表示取不到有效值。
                :type MaxOutPkg: int
                :param MaxInFlow: 最大入带宽 ，单位Mbps
        注意：此字段可能返回 null，表示取不到有效值。
                :type MaxInFlow: int
                :param MaxOutFlow: 最大出带宽 ，单位Mbps
        注意：此字段可能返回 null，表示取不到有效值。
                :type MaxOutFlow: int
                :param MaxNewConn: 最大新建连接速率，单位：cps
        注意：此字段可能返回 null，表示取不到有效值。
                :type MaxNewConn: int
                :param HttpMaxNewConn: 最大新建连接速率，单位：cps
        注意：此字段可能返回 null，表示取不到有效值。
                :type HttpMaxNewConn: int
                :param HttpsMaxNewConn: 最大新建连接速率，单位：cps
        注意：此字段可能返回 null，表示取不到有效值。
                :type HttpsMaxNewConn: int
                :param HttpsQps: 最大新建连接速率，单位：cps
        注意：此字段可能返回 null，表示取不到有效值。
                :type HttpsQps: int
        """
        self.SetName = None
        self.MaxConn = None
        self.MaxQps = None
        self.MaxInPkg = None
        self.MaxOutPkg = None
        self.MaxInFlow = None
        self.MaxOutFlow = None
        self.MaxNewConn = None
        self.HttpMaxNewConn = None
        self.HttpsMaxNewConn = None
        self.HttpsQps = None

    def _deserialize(self, params):
        self.SetName = params.get("SetName")
        self.MaxConn = params.get("MaxConn")
        self.MaxQps = params.get("MaxQps")
        self.MaxInPkg = params.get("MaxInPkg")
        self.MaxOutPkg = params.get("MaxOutPkg")
        self.MaxInFlow = params.get("MaxInFlow")
        self.MaxOutFlow = params.get("MaxOutFlow")
        self.MaxNewConn = params.get("MaxNewConn")
        self.HttpMaxNewConn = params.get("HttpMaxNewConn")
        self.HttpsMaxNewConn = params.get("HttpsMaxNewConn")
        self.HttpsQps = params.get("HttpsQps")


class Price(AbstractModel):
    """表示负载均衡的价格"""

    def __init__(self):
        """
                :param InstancePrice: 描述了实例价格。
        注意：此字段可能返回 null，表示取不到有效值。
                :type InstancePrice: :class:`tcecloud.clb.v20180317.models.ItemPrice`
                :param BandwidthPrice: 描述了网络价格。
        注意：此字段可能返回 null，表示取不到有效值。
                :type BandwidthPrice: :class:`tcecloud.clb.v20180317.models.ItemPrice`
        """
        self.InstancePrice = None
        self.BandwidthPrice = None

    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self.InstancePrice = ItemPrice()
            self.InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("BandwidthPrice") is not None:
            self.BandwidthPrice = ItemPrice()
            self.BandwidthPrice._deserialize(params.get("BandwidthPrice"))


class QueryBlockIPTaskRequest(AbstractModel):
    """QueryBlockIPTask请求参数结构体"""

    def __init__(self):
        """
        :param TaskId: 异步任务的ID
        :type TaskId: str
        """
        self.TaskId = None

    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class QueryBlockIPTaskResponse(AbstractModel):
    """QueryBlockIPTask返回参数结构体"""

    def __init__(self):
        """
        :param Status: 1 running，2 fail，6 succ
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None

    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class QuerySetByVipRequest(AbstractModel):
    """QuerySetByVip请求参数结构体"""

    def __init__(self):
        """
        :param Type: 查询四层或七层  只能为L4 或者 L7
        :type Type: str
        :param VipList: ip和端口号信息
        :type VipList: list of VipAndVport
        """
        self.Type = None
        self.VipList = None

    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("VipList") is not None:
            self.VipList = []
            for item in params.get("VipList"):
                obj = VipAndVport()
                obj._deserialize(item)
                self.VipList.append(obj)


class QuerySetByVipResponse(AbstractModel):
    """QuerySetByVip返回参数结构体"""

    def __init__(self):
        """
        :param SetInfo: 集群信息
        :type SetInfo: list of SetNameVIP
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SetInfo = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("SetInfo") is not None:
            self.SetInfo = []
            for item in params.get("SetInfo"):
                obj = SetNameVIP()
                obj._deserialize(item)
                self.SetInfo.append(obj)
        self.RequestId = params.get("RequestId")


class QuerySetCapacityRequest(AbstractModel):
    """QuerySetCapacity请求参数结构体"""

    def __init__(self):
        """
        :param Type: 查询四层或七层  只能为L4 或者 L7
        :type Type: str
        :param SetName: 独占集群名字
        :type SetName: list of str
        """
        self.Type = None
        self.SetName = None

    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.SetName = params.get("SetName")


class QuerySetCapacityResponse(AbstractModel):
    """QuerySetCapacity返回参数结构体"""

    def __init__(self):
        """
        :param SetCapacity: 集群信息
        :type SetCapacity: list of OneCapacity
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SetCapacity = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("SetCapacity") is not None:
            self.SetCapacity = []
            for item in params.get("SetCapacity"):
                obj = OneCapacity()
                obj._deserialize(item)
                self.SetCapacity.append(obj)
        self.RequestId = params.get("RequestId")


class QuerySetVipRequest(AbstractModel):
    """QuerySetVip请求参数结构体"""

    def __init__(self):
        """
        :param Type: 查询四层独占集群还是七层，只能为L4或者L7
        :type Type: str
        :param SetName: 集群名字数组
        :type SetName: list of str
        """
        self.Type = None
        self.SetName = None

    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.SetName = params.get("SetName")


class QuerySetVipResponse(AbstractModel):
    """QuerySetVip返回参数结构体"""

    def __init__(self):
        """
        :param SetVip: 返回独占集群Vip的使用信息
        :type SetVip: list of SetVip
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SetVip = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("SetVip") is not None:
            self.SetVip = []
            for item in params.get("SetVip"):
                obj = SetVip()
                obj._deserialize(item)
                self.SetVip.append(obj)
        self.RequestId = params.get("RequestId")


class Quota(AbstractModel):
    """描述配额信息"""

    def __init__(self):
        """
                :param QuotaId: 配额名称
                :type QuotaId: str
                :param QuotaCurrent: 使用数量
        注意：此字段可能返回 null，表示取不到有效值。
                :type QuotaCurrent: int
                :param QuotaLimit: 配额数量
                :type QuotaLimit: int
        """
        self.QuotaId = None
        self.QuotaCurrent = None
        self.QuotaLimit = None

    def _deserialize(self, params):
        self.QuotaId = params.get("QuotaId")
        self.QuotaCurrent = params.get("QuotaCurrent")
        self.QuotaLimit = params.get("QuotaLimit")


class RegisterTargetGroupInstancesRequest(AbstractModel):
    """RegisterTargetGroupInstances请求参数结构体"""

    def __init__(self):
        """
        :param TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param TargetGroupInstances: 服务器实例数组
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupId = None
        self.TargetGroupInstances = None

    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)


class RegisterTargetGroupInstancesResponse(AbstractModel):
    """RegisterTargetGroupInstances返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegisterTargetsRequest(AbstractModel):
    """RegisterTargets请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param Targets: 待绑定的后端服务列表，数组长度最大支持20
        :type Targets: list of Target
        :param LocationId: 转发规则的ID，当绑定后端服务到七层转发规则时，必须提供此参数或Domain+Url两者之一
        :type LocationId: str
        :param Domain: 目标转发规则的域名，提供LocationId参数时本参数不生效
        :type Domain: str
        :param Url: 目标转发规则的URL，提供LocationId参数时本参数不生效
        :type Url: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Targets = None
        self.LocationId = None
        self.Domain = None
        self.Url = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")


class RegisterTargetsResponse(AbstractModel):
    """RegisterTargets返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegisterTargetsWithClassicalLBRequest(AbstractModel):
    """RegisterTargetsWithClassicalLB请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param Targets: 后端服务信息
        :type Targets: list of ClassicalTargetInfo
        """
        self.LoadBalancerId = None
        self.Targets = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = ClassicalTargetInfo()
                obj._deserialize(item)
                self.Targets.append(obj)


class RegisterTargetsWithClassicalLBResponse(AbstractModel):
    """RegisterTargetsWithClassicalLB返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceCertForLoadBalancersRequest(AbstractModel):
    """ReplaceCertForLoadBalancers请求参数结构体"""

    def __init__(self):
        """
        :param OldCertificateId: 需要被替换的证书的ID，可以是服务端证书或客户端证书
        :type OldCertificateId: str
        :param Certificate: 新证书的内容等相关信息
        :type Certificate: :class:`tcecloud.clb.v20180317.models.CertificateInput`
        """
        self.OldCertificateId = None
        self.Certificate = None

    def _deserialize(self, params):
        self.OldCertificateId = params.get("OldCertificateId")
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))


class ReplaceCertForLoadBalancersResponse(AbstractModel):
    """ReplaceCertForLoadBalancers返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RewriteLocationMap(AbstractModel):
    """转发规则之间的重定向关系"""

    def __init__(self):
        """
        :param SourceLocationId: 源转发规则ID
        :type SourceLocationId: str
        :param TargetLocationId: 重定向至的目标转发规则ID
        :type TargetLocationId: str
        """
        self.SourceLocationId = None
        self.TargetLocationId = None

    def _deserialize(self, params):
        self.SourceLocationId = params.get("SourceLocationId")
        self.TargetLocationId = params.get("TargetLocationId")


class RewriteTarget(AbstractModel):
    """重定向目标的信息"""

    def __init__(self):
        """
                :param TargetListenerId: 重定向目标的监听器ID
        注意：此字段可能返回 null，表示无重定向。
        注意：此字段可能返回 null，表示取不到有效值。
                :type TargetListenerId: str
                :param TargetLocationId: 重定向目标的转发规则ID
        注意：此字段可能返回 null，表示无重定向。
        注意：此字段可能返回 null，表示取不到有效值。
                :type TargetLocationId: str
        """
        self.TargetListenerId = None
        self.TargetLocationId = None

    def _deserialize(self, params):
        self.TargetListenerId = params.get("TargetListenerId")
        self.TargetLocationId = params.get("TargetLocationId")


class RsWeightRule(AbstractModel):
    """修改节点权重的数据类型"""

    def __init__(self):
        """
        :param ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param Targets: 要修改权重的后端机器列表
        :type Targets: list of Target
        :param LocationId: 转发规则的ID，七层规则时需要此参数，4层规则不需要
        :type LocationId: str
        :param Domain: 目标规则的域名，提供LocationId参数时本参数不生效
        :type Domain: str
        :param Url: 目标规则的URL，提供LocationId参数时本参数不生效
        :type Url: str
        :param Weight: 后端服务新的转发权重，取值范围：0~100。
        :type Weight: int
        """
        self.ListenerId = None
        self.Targets = None
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Weight = None

    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.Weight = params.get("Weight")


class RuleHealth(AbstractModel):
    """一条转发规则的健康检查状态"""

    def __init__(self):
        """
                :param LocationId: 转发规则ID
                :type LocationId: str
                :param Domain: 转发规则的域名
        注意：此字段可能返回 null，表示取不到有效值。
                :type Domain: str
                :param Url: 转发规则的Url
        注意：此字段可能返回 null，表示取不到有效值。
                :type Url: str
                :param Targets: 本规则上绑定的后端的健康检查状态
        注意：此字段可能返回 null，表示取不到有效值。
                :type Targets: list of TargetHealth
        """
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Targets = None

    def _deserialize(self, params):
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = TargetHealth()
                obj._deserialize(item)
                self.Targets.append(obj)


class RuleInput(AbstractModel):
    """HTTP/HTTPS转发规则（输入）"""

    def __init__(self):
        """
                :param Domain: 转发规则的域名。长度限制为：1~80。
                :type Domain: str
                :param Url: 转发规则的路径。长度限制为：1~200。
                :type Url: str
                :param SessionExpireTime: 会话保持时间。设置为0表示关闭会话保持，开启会话保持可取值30~3600，单位：秒。
                :type SessionExpireTime: int
                :param HealthCheck: 健康检查信息
                :type HealthCheck: :class:`tcecloud.clb.v20180317.models.HealthCheck`
                :param Certificate: 证书信息
                :type Certificate: :class:`tcecloud.clb.v20180317.models.CertificateInput`
                :param Scheduler: 规则的请求转发方式，可选值：WRR、LEAST_CONN、IP_HASH
        分别表示按权重轮询、最小连接数、按IP哈希， 默认为 WRR。
                :type Scheduler: str
                :param ForwardType: 负载均衡与后端服务之间的转发协议，目前支持 HTTP/HTTPS/TRPC
                :type ForwardType: str
                :param DefaultServer: 是否将该域名设为默认域名，注意，一个监听器下只能设置一个默认域名。
                :type DefaultServer: bool
                :param Http2: 是否开启Http2，注意，只有HTTPS域名才能开启Http2。
                :type Http2: bool
                :param TargetType: 后端目标类型，NODE表示绑定普通节点，TARGETGROUP表示绑定目标组
                :type TargetType: str
                :param TrpcCallee: TRPC被调服务器路由，ForwardType为TRPC时必填
                :type TrpcCallee: str
                :param TrpcFunc: TRPC调用服务接口，ForwardType为TRPC时必填
                :type TrpcFunc: str
        """
        self.Domain = None
        self.Url = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Certificate = None
        self.Scheduler = None
        self.ForwardType = None
        self.DefaultServer = None
        self.Http2 = None
        self.TargetType = None
        self.TrpcCallee = None
        self.TrpcFunc = None

    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.Scheduler = params.get("Scheduler")
        self.ForwardType = params.get("ForwardType")
        self.DefaultServer = params.get("DefaultServer")
        self.Http2 = params.get("Http2")
        self.TargetType = params.get("TargetType")
        self.TrpcCallee = params.get("TrpcCallee")
        self.TrpcFunc = params.get("TrpcFunc")


class RuleOutput(AbstractModel):
    """HTTP/HTTPS监听器的转发规则（输出）"""

    def __init__(self):
        """
                :param LocationId: 转发规则的 ID
                :type LocationId: str
                :param Domain: 转发规则的域名。
        注意：此字段可能返回 null，表示取不到有效值。
                :type Domain: str
                :param Url: 转发规则的路径。
        注意：此字段可能返回 null，表示取不到有效值。
                :type Url: str
                :param SessionExpireTime: 会话保持时间
                :type SessionExpireTime: int
                :param HealthCheck: 健康检查信息
        注意：此字段可能返回 null，表示取不到有效值。
                :type HealthCheck: :class:`tcecloud.clb.v20180317.models.HealthCheck`
                :param Certificate: 证书信息
        注意：此字段可能返回 null，表示取不到有效值。
                :type Certificate: :class:`tcecloud.clb.v20180317.models.CertificateOutput`
                :param Scheduler: 规则的请求转发方式
                :type Scheduler: str
                :param ListenerId: 转发规则所属的监听器 ID
                :type ListenerId: str
                :param RewriteTarget: 转发规则的重定向目标信息
        注意：此字段可能返回 null，表示取不到有效值。
                :type RewriteTarget: :class:`tcecloud.clb.v20180317.models.RewriteTarget`
                :param HttpGzip: 是否开启gzip
                :type HttpGzip: bool
                :param BeAutoCreated: 转发规则是否为自动创建
                :type BeAutoCreated: bool
                :param DefaultServer: 是否作为默认域名
                :type DefaultServer: bool
                :param Http2: 是否开启Http2
                :type Http2: bool
                :param ForwardType: 负载均衡与后端服务之间的转发协议
                :type ForwardType: str
                :param CreateTime: 转发规则的创建时间
                :type CreateTime: str
                :param TargetType: 后端服务器类型
                :type TargetType: str
                :param TargetGroup: 绑定的目标组基本信息；当规则绑定目标组时，会返回该字段
        注意：此字段可能返回 null，表示取不到有效值。
                :type TargetGroup: :class:`tcecloud.clb.v20180317.models.BasicTargetGroupInfo`
                :param WafDomainId: WAF实例ID
        注意：此字段可能返回 null，表示取不到有效值。
                :type WafDomainId: str
                :param TrpcCallee: TRPC被调服务器路由，ForwardType为TRPC时有效
        注意：此字段可能返回 null，表示取不到有效值。
                :type TrpcCallee: str
                :param TrpcFunc: TRPC调用服务接口，ForwardType为TRPC时有效
        注意：此字段可能返回 null，表示取不到有效值。
                :type TrpcFunc: str
        """
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Certificate = None
        self.Scheduler = None
        self.ListenerId = None
        self.RewriteTarget = None
        self.HttpGzip = None
        self.BeAutoCreated = None
        self.DefaultServer = None
        self.Http2 = None
        self.ForwardType = None
        self.CreateTime = None
        self.TargetType = None
        self.TargetGroup = None
        self.WafDomainId = None
        self.TrpcCallee = None
        self.TrpcFunc = None

    def _deserialize(self, params):
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self.Certificate = CertificateOutput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.Scheduler = params.get("Scheduler")
        self.ListenerId = params.get("ListenerId")
        if params.get("RewriteTarget") is not None:
            self.RewriteTarget = RewriteTarget()
            self.RewriteTarget._deserialize(params.get("RewriteTarget"))
        self.HttpGzip = params.get("HttpGzip")
        self.BeAutoCreated = params.get("BeAutoCreated")
        self.DefaultServer = params.get("DefaultServer")
        self.Http2 = params.get("Http2")
        self.ForwardType = params.get("ForwardType")
        self.CreateTime = params.get("CreateTime")
        self.TargetType = params.get("TargetType")
        if params.get("TargetGroup") is not None:
            self.TargetGroup = BasicTargetGroupInfo()
            self.TargetGroup._deserialize(params.get("TargetGroup"))
        self.WafDomainId = params.get("WafDomainId")
        self.TrpcCallee = params.get("TrpcCallee")
        self.TrpcFunc = params.get("TrpcFunc")


class RuleTargets(AbstractModel):
    """HTTP/HTTPS监听器下的转发规则绑定的后端服务信息"""

    def __init__(self):
        """
                :param LocationId: 转发规则的 ID
                :type LocationId: str
                :param Domain: 转发规则的域名
                :type Domain: str
                :param Url: 转发规则的路径。
                :type Url: str
                :param Targets: 后端服务的信息
        注意：此字段可能返回 null，表示取不到有效值。
                :type Targets: list of Backend
        """
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Targets = None

    def _deserialize(self, params):
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Backend()
                obj._deserialize(item)
                self.Targets.append(obj)


class RulesItems(AbstractModel):
    """七层规则对象"""

    def __init__(self):
        """
        :param LocationId: 规则id
        :type LocationId: str
        :param Domain: 域名
        :type Domain: str
        :param Url: uri
        :type Url: str
        :param Targets: 绑定的后端对象
        :type Targets: list of LbRsTargets
        """
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Targets = None

    def _deserialize(self, params):
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = LbRsTargets()
                obj._deserialize(item)
                self.Targets.append(obj)


class SetCustomizedConfigForLoadBalancerRequest(AbstractModel):
    """SetCustomizedConfigForLoadBalancer请求参数结构体"""

    def __init__(self):
        """
        :param OperationType: 操作类型：'ADD', 'DELETE', 'UPDATE', 'BIND', 'UNBIND'
        :type OperationType: str
        :param UconfigId: 除了创建个性化配置外，必传此字段，如：pz-1234abcd
        :type UconfigId: str
        :param ConfigContent: 创建个性化配置或修改个性化配置的内容时，必传此字段
        :type ConfigContent: str
        :param ConfigName: 创建个性化配置或修改个性化配置的名字时，必传此字段
        :type ConfigName: str
        :param LoadBalancerIds: 绑定解绑时，必传此字段
        :type LoadBalancerIds: list of str
        """
        self.OperationType = None
        self.UconfigId = None
        self.ConfigContent = None
        self.ConfigName = None
        self.LoadBalancerIds = None

    def _deserialize(self, params):
        self.OperationType = params.get("OperationType")
        self.UconfigId = params.get("UconfigId")
        self.ConfigContent = params.get("ConfigContent")
        self.ConfigName = params.get("ConfigName")
        self.LoadBalancerIds = params.get("LoadBalancerIds")


class SetCustomizedConfigForLoadBalancerResponse(AbstractModel):
    """SetCustomizedConfigForLoadBalancer返回参数结构体"""

    def __init__(self):
        """
        :param ConfigId: 个性化配置ID，如：pz-1234abcd
        :type ConfigId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ConfigId = None
        self.RequestId = None

    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.RequestId = params.get("RequestId")


class SetItem(AbstractModel):
    """集群参数。"""

    def __init__(self):
        """
                :param SetId: 集群Id
                :type SetId: int
                :param SetName: 集群名字
                :type SetName: str
                :param Type: 集群类型
                :type Type: str
                :param SetTag: 集群标签
        注意：此字段可能返回 null，表示取不到有效值。
                :type SetTag: str
                :param MaxConn: 最大连接数
                :type MaxConn: int
                :param MaxInFlow: 最大入带宽
                :type MaxInFlow: int
                :param MaxInPkg: 最大入包量
                :type MaxInPkg: int
                :param MaxOutFlow: 最大出带宽
                :type MaxOutFlow: int
                :param MaxOutPkg: 最大出包量
                :type MaxOutPkg: int
                :param MaxNewConn: 最大新建连接数
        注意：此字段可能返回 null，表示取不到有效值。
                :type MaxNewConn: int
                :param HTTPMaxNewConn: http最大新建连接数
        注意：此字段可能返回 null，表示取不到有效值。
                :type HTTPMaxNewConn: int
                :param HTTPSMaxNewConn: https最大新建连接数
        注意：此字段可能返回 null，表示取不到有效值。
                :type HTTPSMaxNewConn: int
                :param HTTPQps: http QPS
        注意：此字段可能返回 null，表示取不到有效值。
                :type HTTPQps: int
                :param HTTPSQps: https QPS
        注意：此字段可能返回 null，表示取不到有效值。
                :type HTTPSQps: int
                :param Vips: 集群已使用vip
        注意：此字段可能返回 null，表示取不到有效值。
                :type Vips: list of VipType
                :param ClusterId: 集群Id
        注意：此字段可能返回 null，表示取不到有效值。
                :type ClusterId: str
        """
        self.SetId = None
        self.SetName = None
        self.Type = None
        self.SetTag = None
        self.MaxConn = None
        self.MaxInFlow = None
        self.MaxInPkg = None
        self.MaxOutFlow = None
        self.MaxOutPkg = None
        self.MaxNewConn = None
        self.HTTPMaxNewConn = None
        self.HTTPSMaxNewConn = None
        self.HTTPQps = None
        self.HTTPSQps = None
        self.Vips = None
        self.ClusterId = None

    def _deserialize(self, params):
        self.SetId = params.get("SetId")
        self.SetName = params.get("SetName")
        self.Type = params.get("Type")
        self.SetTag = params.get("SetTag")
        self.MaxConn = params.get("MaxConn")
        self.MaxInFlow = params.get("MaxInFlow")
        self.MaxInPkg = params.get("MaxInPkg")
        self.MaxOutFlow = params.get("MaxOutFlow")
        self.MaxOutPkg = params.get("MaxOutPkg")
        self.MaxNewConn = params.get("MaxNewConn")
        self.HTTPMaxNewConn = params.get("HTTPMaxNewConn")
        self.HTTPSMaxNewConn = params.get("HTTPSMaxNewConn")
        self.HTTPQps = params.get("HTTPQps")
        self.HTTPSQps = params.get("HTTPSQps")
        if params.get("Vips") is not None:
            self.Vips = []
            for item in params.get("Vips"):
                obj = VipType()
                obj._deserialize(item)
                self.Vips.append(obj)
        self.ClusterId = params.get("ClusterId")


class SetLoadBalancerClsLogRequest(AbstractModel):
    """SetLoadBalancerClsLog请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param LogSetId: 日志服务(CLS)的日志集ID
        :type LogSetId: str
        :param LogTopicId: 日志服务(CLS)的日志主题ID
        :type LogTopicId: str
        """
        self.LoadBalancerId = None
        self.LogSetId = None
        self.LogTopicId = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LogSetId = params.get("LogSetId")
        self.LogTopicId = params.get("LogTopicId")


class SetLoadBalancerClsLogResponse(AbstractModel):
    """SetLoadBalancerClsLog返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetLoadBalancerExclusiveTagRequest(AbstractModel):
    """SetLoadBalancerExclusiveTag请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡的唯一ID
        :type LoadBalancerId: str
        :param ExclusiveValue: 负载均衡七层集群的独占标签，若要删除负载均衡七层集群的独占标签，可传入空字符串
        :type ExclusiveValue: str
        """
        self.LoadBalancerId = None
        self.ExclusiveValue = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ExclusiveValue = params.get("ExclusiveValue")


class SetLoadBalancerExclusiveTagResponse(AbstractModel):
    """SetLoadBalancerExclusiveTag返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetLoadBalancerLogRequest(AbstractModel):
    """SetLoadBalancerLog请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param OperationType: 操作类型，ADD | DEL | UPDATE
        :type OperationType: str
        :param BucketName: 如果用户开启日志访问，则此字段指定日志存放位置（COS的Bucket），OperationType 为ADD时，必须穿入此参数。
        :type BucketName: str
        :param Period: 日志导出到bucket的频率，单位：秒，有效取值范围为10分钟到12小时，建议取3600秒
        :type Period: int
        """
        self.LoadBalancerId = None
        self.OperationType = None
        self.BucketName = None
        self.Period = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.OperationType = params.get("OperationType")
        self.BucketName = params.get("BucketName")
        self.Period = params.get("Period")


class SetLoadBalancerLogResponse(AbstractModel):
    """SetLoadBalancerLog返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetLoadBalancerSecurityGroupsRequest(AbstractModel):
    """SetLoadBalancerSecurityGroups请求参数结构体"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param SecurityGroups: 安全组ID构成的数组，一个负载均衡实例最多可绑定50个安全组，如果要解绑所有安全组，可不传此参数，或传入空数组。
        :type SecurityGroups: list of str
        """
        self.LoadBalancerId = None
        self.SecurityGroups = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SecurityGroups = params.get("SecurityGroups")


class SetLoadBalancerSecurityGroupsResponse(AbstractModel):
    """SetLoadBalancerSecurityGroups返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetNameItem(AbstractModel):
    """集群中英文名"""

    def __init__(self):
        """
                :param SetName: 集群对外名字
                :type SetName: str
                :param SetChName: 集群对内名字
                :type SetChName: str
                :param ClusterId: 集群ID
        注意：此字段可能返回 null，表示取不到有效值。
                :type ClusterId: str
        """
        self.SetName = None
        self.SetChName = None
        self.ClusterId = None

    def _deserialize(self, params):
        self.SetName = params.get("SetName")
        self.SetChName = params.get("SetChName")
        self.ClusterId = params.get("ClusterId")


class SetNameVIP(AbstractModel):
    """集群名 vip"""

    def __init__(self):
        """
                :param SetName: 集群名
                :type SetName: str
                :param Vip: vip
                :type Vip: str
                :param Vport: 端口号
        注意：此字段可能返回 null，表示取不到有效值。
                :type Vport: int
        """
        self.SetName = None
        self.Vip = None
        self.Vport = None

    def _deserialize(self, params):
        self.SetName = params.get("SetName")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")


class SetSecurityGroupForLoadbalancersRequest(AbstractModel):
    """SetSecurityGroupForLoadbalancers请求参数结构体"""

    def __init__(self):
        """
                :param SecurityGroup: 安全组ID，如 sg-12345678
                :type SecurityGroup: str
                :param OperationType: ADD 绑定安全组；
        DEL 解绑安全组
                :type OperationType: str
                :param LoadBalancerIds: 负载均衡实例ID数组
                :type LoadBalancerIds: list of str
        """
        self.SecurityGroup = None
        self.OperationType = None
        self.LoadBalancerIds = None

    def _deserialize(self, params):
        self.SecurityGroup = params.get("SecurityGroup")
        self.OperationType = params.get("OperationType")
        self.LoadBalancerIds = params.get("LoadBalancerIds")


class SetSecurityGroupForLoadbalancersResponse(AbstractModel):
    """SetSecurityGroupForLoadbalancers返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetVip(AbstractModel):
    """独占集群中Vip的使用信息"""

    def __init__(self):
        """
                :param SetName: 集群名字
                :type SetName: str
                :param UsedVip: 已使用的vip
        注意：此字段可能返回 null，表示取不到有效值。
                :type UsedVip: list of str
                :param UnuseVip: 未使用vip
        注意：此字段可能返回 null，表示取不到有效值。
                :type UnuseVip: list of str
        """
        self.SetName = None
        self.UsedVip = None
        self.UnuseVip = None

    def _deserialize(self, params):
        self.SetName = params.get("SetName")
        self.UsedVip = params.get("UsedVip")
        self.UnuseVip = params.get("UnuseVip")


class SnatIp(AbstractModel):
    """SnatIp的信息结构"""

    def __init__(self):
        """
        :param SubnetId: 私有网络子网的唯一性id，如subnet-12345678
        :type SubnetId: str
        :param Ip: IP地址，如192.168.0.1
        :type Ip: str
        """
        self.SubnetId = None
        self.Ip = None

    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.Ip = params.get("Ip")


class TagInfo(AbstractModel):
    """负载均衡的标签信息"""

    def __init__(self):
        """
        :param TagKey: 标签的键
        :type TagKey: str
        :param TagValue: 标签的值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None

    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class Target(AbstractModel):
    """转发目标，即绑定在负载均衡上的后端服务"""

    def __init__(self):
        """
                :param Port: 后端服务的监听端口
        注意：此字段可能返回 null，表示取不到有效值。
                :type Port: int
                :param Type: 后端服务的类型，可取：CVM（云服务器）、ENI（弹性网卡）；作为入参时，目前本参数暂不生效。
        注意：此字段可能返回 null，表示取不到有效值。
                :type Type: str
                :param InstanceId: 绑定CVM时需要传入此参数，代表CVM的唯一 ID，可通过 DescribeInstances 接口返回字段中的 InstanceId 字段获取。
        注意：参数 InstanceId 和 EniIp 只能传入一个且必须传入一个。
        注意：此字段可能返回 null，表示取不到有效值。
                :type InstanceId: str
                :param Weight: 后端服务的转发权重，取值范围：[0, 100]，默认为 10。
                :type Weight: int
                :param EniIp: 绑定弹性网卡时需要传入此参数，代表弹性网卡的IP，
                弹性网卡必须先绑定至CVM，然后才能绑定到负载均衡实例。
                注意：参数 InstanceId 和 EniIp 只能传入一个且必须传入一个。注意：绑定弹性网卡需要先提交工单开白名单使用。
        注意：此字段可能返回 null，表示取不到有效值。
                :type EniIp: str
        """
        self.Port = None
        self.Type = None
        self.InstanceId = None
        self.Weight = None
        self.EniIp = None

    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        self.EniIp = params.get("EniIp")


class TargetCountForLoadBalancer(AbstractModel):
    """负载均衡实例及其绑定的后端服务总数"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡ID
        :type LoadBalancerId: str
        :param TargetCount: 负载均衡实例绑定的后端服务总数
        :type TargetCount: int
        """
        self.LoadBalancerId = None
        self.TargetCount = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.TargetCount = params.get("TargetCount")


class TargetGroupAssociation(AbstractModel):
    """规则与目标组的关联关系"""

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡ID
        :type LoadBalancerId: str
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param LocationId: 转发规则ID
        :type LocationId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.TargetGroupId = None
        self.LocationId = None

    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.TargetGroupId = params.get("TargetGroupId")
        self.LocationId = params.get("LocationId")


class TargetGroupBackend(AbstractModel):
    """目标组绑定的后端服务器"""

    def __init__(self):
        """
                :param TargetGroupId: 目标组ID
                :type TargetGroupId: str
                :param Type: 后端服务的类型，可取：CVM、ENI（即将支持）
                :type Type: str
                :param InstanceId: 后端服务的唯一 ID
                :type InstanceId: str
                :param Port: 后端服务的监听端口
                :type Port: int
                :param Weight: 后端服务的转发权重，取值范围：[0, 100]，默认为 10。
                :type Weight: int
                :param PublicIpAddresses: 后端服务的外网 IP
        注意：此字段可能返回 null，表示取不到有效值。
                :type PublicIpAddresses: list of str
                :param PrivateIpAddresses: 后端服务的内网 IP
        注意：此字段可能返回 null，表示取不到有效值。
                :type PrivateIpAddresses: list of str
                :param InstanceName: 后端服务的实例名称
        注意：此字段可能返回 null，表示取不到有效值。
                :type InstanceName: str
                :param RegisteredTime: 后端服务被绑定的时间
        注意：此字段可能返回 null，表示取不到有效值。
                :type RegisteredTime: str
                :param EniId: 弹性网卡唯一ID
        注意：此字段可能返回 null，表示取不到有效值。
                :type EniId: str
        """
        self.TargetGroupId = None
        self.Type = None
        self.InstanceId = None
        self.Port = None
        self.Weight = None
        self.PublicIpAddresses = None
        self.PrivateIpAddresses = None
        self.InstanceName = None
        self.RegisteredTime = None
        self.EniId = None

    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.InstanceName = params.get("InstanceName")
        self.RegisteredTime = params.get("RegisteredTime")
        self.EniId = params.get("EniId")


class TargetGroupInfo(AbstractModel):
    """目标组信息"""

    def __init__(self):
        """
                :param TargetGroupId: 目标组ID
                :type TargetGroupId: str
                :param VpcId: 目标组的vpcid
                :type VpcId: str
                :param TargetGroupName: 目标组的名字
                :type TargetGroupName: str
                :param Port: 目标组的默认端口
        注意：此字段可能返回 null，表示取不到有效值。
                :type Port: int
                :param CreatedTime: 目标组的创建时间
                :type CreatedTime: str
                :param UpdatedTime: 目标组的修改时间
                :type UpdatedTime: str
                :param AssociatedRule: 关联到的规则数组
        注意：此字段可能返回 null，表示取不到有效值。
                :type AssociatedRule: list of AssociationItem
        """
        self.TargetGroupId = None
        self.VpcId = None
        self.TargetGroupName = None
        self.Port = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.AssociatedRule = None

    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.VpcId = params.get("VpcId")
        self.TargetGroupName = params.get("TargetGroupName")
        self.Port = params.get("Port")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        if params.get("AssociatedRule") is not None:
            self.AssociatedRule = []
            for item in params.get("AssociatedRule"):
                obj = AssociationItem()
                obj._deserialize(item)
                self.AssociatedRule.append(obj)


class TargetGroupInstance(AbstractModel):
    """目标组实例"""

    def __init__(self):
        """
        :param BindIP: 目标组实例的内网IP
        :type BindIP: str
        :param Port: 目标组实例的端口
        :type Port: int
        :param Weight: 目标组实例的权重
        :type Weight: int
        :param NewPort: 目标组实例的新端口
        :type NewPort: int
        """
        self.BindIP = None
        self.Port = None
        self.Weight = None
        self.NewPort = None

    def _deserialize(self, params):
        self.BindIP = params.get("BindIP")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.NewPort = params.get("NewPort")


class TargetHealth(AbstractModel):
    """描述一个Target的健康信息"""

    def __init__(self):
        """
        :param IP: Target的内网IP
        :type IP: str
        :param Port: Target绑定的端口
        :type Port: int
        :param HealthStatus: 当前健康状态，true：健康，false：不健康（包括尚未开始探测、探测中、状态异常等几种状态）。只有处于健康状态（且权重大于0），负载均衡才会向其转发流量。
        :type HealthStatus: bool
        :param TargetId: Target的实例ID，如 ins-12345678
        :type TargetId: str
        :param HealthStatusDetial: 当前健康状态的详细信息。如：Alive、Dead、Unknown。Alive状态为健康，Dead状态为异常，Unknown状态包括尚未开始探测、探测中、状态未知。
        :type HealthStatusDetial: str
        """
        self.IP = None
        self.Port = None
        self.HealthStatus = None
        self.TargetId = None
        self.HealthStatusDetial = None

    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Port = params.get("Port")
        self.HealthStatus = params.get("HealthStatus")
        self.TargetId = params.get("TargetId")
        self.HealthStatusDetial = params.get("HealthStatusDetial")


class TargetRegionInfo(AbstractModel):
    """负载均衡实例所绑定的后端服务的信息，包括所属地域、所属网络。"""

    def __init__(self):
        """
        :param Region: Target所属地域，如 ap-guangzhou
        :type Region: str
        :param VpcId: Target所属网络，私有网络格式如 vpc-abcd1234，如果是基础网络，则为"0"
        :type VpcId: str
        """
        self.Region = None
        self.VpcId = None

    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")


class TestEzioRequest(AbstractModel):
    """TestEzio请求参数结构体"""

    def __init__(self):
        """
        :param Name: name
        :type Name: str
        """
        self.Name = None

    def _deserialize(self, params):
        self.Name = params.get("Name")


class TestEzioResponse(AbstractModel):
    """TestEzio返回参数结构体"""

    def __init__(self):
        """
        :param Hello: aa
        :type Hello: str
        :param World: aa
        :type World: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Hello = None
        self.World = None
        self.RequestId = None

    def _deserialize(self, params):
        self.Hello = params.get("Hello")
        self.World = params.get("World")
        self.RequestId = params.get("RequestId")


class VipAndVport(AbstractModel):
    """字典类型"""

    def __init__(self):
        """
        :param Vip: vip
        :type Vip: str
        :param Vport: 端口号
        :type Vport: int
        """
        self.Vip = None
        self.Vport = None

    def _deserialize(self, params):
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")


class VipType(AbstractModel):
    """vip所属负载均衡类型"""

    def __init__(self):
        """
        :param Vip: vip
        :type Vip: str
        :param Forward: 负载均衡类型。1 应用型，0 传统型。
        :type Forward: int
        """
        self.Vip = None
        self.Forward = None

    def _deserialize(self, params):
        self.Vip = params.get("Vip")
        self.Forward = params.get("Forward")


class ZoneInfo(AbstractModel):
    """可用区相关信息"""

    def __init__(self):
        """
                :param ZoneId: 可用区数值形式的唯一ID，如：100001
        注意：此字段可能返回 null，表示取不到有效值。
                :type ZoneId: int
                :param Zone: 可用区字符串形式的唯一ID，如：ap-guangzhou-1
        注意：此字段可能返回 null，表示取不到有效值。
                :type Zone: str
                :param ZoneName: 可用区名称，如：广州一区
        注意：此字段可能返回 null，表示取不到有效值。
                :type ZoneName: str
        """
        self.ZoneId = None
        self.Zone = None
        self.ZoneName = None

    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
