# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


class AssignProjectRequest(AbstractModel):
    """AssignProject请求参数结构体"""

    def __init__(self):
        """
        :param InstanceIds: 实例ID列表，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceIds: list of str
        :param ProjectId: 项目ID
        :type ProjectId: int
        """
        self.InstanceIds = None
        self.ProjectId = None

    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProjectId = params.get("ProjectId")


class AssignProjectResponse(AbstractModel):
    """AssignProject返回参数结构体"""

    def __init__(self):
        """
        :param FlowIds: 返回的异步任务ID列表
        :type FlowIds: list of int non-negative
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: strDestroy
        """
        self.FlowIds = None
        self.RequestId = None

    def _deserialize(self, params):
        self.FlowIds = params.get("FlowIds")
        self.RequestId = params.get("RequestId")


class BackupFile(AbstractModel):
    """备份文件存储信息"""

    def __init__(self):
        """
        :param ReplicateSetId: 备份文件所属的副本集/分片ID
        :type ReplicateSetId: str
        :param File: 备份文件保存路径
        :type File: str
        """
        self.ReplicateSetId = None
        self.File = None

    def _deserialize(self, params):
        self.ReplicateSetId = params.get("ReplicateSetId")
        self.File = params.get("File")


class BackupInfo(AbstractModel):
    """备份信息"""

    def __init__(self):
        """
                :param InstanceId: 实例ID
                :type InstanceId: str
                :param BackupType: 备份方式，0-自动备份，1-手动备份
                :type BackupType: int
                :param BackupName: 备份名称
                :type BackupName: str
                :param BackupDesc: 备份备注
        注意：此字段可能返回 null，表示取不到有效值。
                :type BackupDesc: str
                :param BackupSize: 备份文件大小，单位KB
        注意：此字段可能返回 null，表示取不到有效值。
                :type BackupSize: int
                :param StartTime: 备份开始时间
        注意：此字段可能返回 null，表示取不到有效值。
                :type StartTime: str
                :param EndTime: 备份结束时间
        注意：此字段可能返回 null，表示取不到有效值。
                :type EndTime: str
                :param Status: 备份状态，1-备份中，2-备份成功
                :type Status: int
                :param BackupMethod: 备份方法，0-逻辑备份，1-物理备份
                :type BackupMethod: int
        """
        self.InstanceId = None
        self.BackupType = None
        self.BackupName = None
        self.BackupDesc = None
        self.BackupSize = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.BackupMethod = None

    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupType = params.get("BackupType")
        self.BackupName = params.get("BackupName")
        self.BackupDesc = params.get("BackupDesc")
        self.BackupSize = params.get("BackupSize")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.BackupMethod = params.get("BackupMethod")


class ClientConnection(AbstractModel):
    """客户端连接信息，包括客户端IP和连接数"""

    def __init__(self):
        """
        :param IP: 连接的客户端IP
        :type IP: str
        :param Count: 对应客户端IP的连接数
        :type Count: int
        """
        self.IP = None
        self.Count = None

    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Count = params.get("Count")


class CreateDBInstanceHourRequest(AbstractModel):
    """CreateDBInstanceHour请求参数结构体"""

    def __init__(self):
        """
        :param Memory: 实例内存大小，单位：GB
        :type Memory: int
        :param Volume: 实例硬盘大小，单位：GB
        :type Volume: int
        :param ReplicateSetNum: 副本集个数，创建副本集实例时，该参数必须设置为1；创建分片实例时，具体参照查询云数据库的售卖规格返回参数
        :type ReplicateSetNum: int
        :param NodeNum: 每个副本集内节点个数，当前副本集节点数固定为3，分片从节点数可选，具体参照查询云数据库的售卖规格返回参数
        :type NodeNum: int
        :param MongoVersion: 版本号，具体支持的售卖版本请参照查询云数据库的售卖规格
        （DescribeSpecInfo）返回结果。参数与版本对应关系是MONGO_3_WT：MongoDB 3.2 WiredTiger存储引擎版本，
        MONGO_3_ROCKS：MongoDB 3.2 RocksDB存储引擎版本，MONGO_36_WT：MongoDB 3.6 WiredTiger存储引擎版本
        :type MongoVersion: str
        :param MachineCode: 机器类型，HIO：高IO型；HIO10G：高IO万兆
        :type MachineCode: str
        :param GoodsNum: 实例数量，最小值1，最大值为10
        :type GoodsNum: int
        :param Zone: 可用区信息，格式如：ap-guangzhou-2
        :type Zone: str
        :param ClusterType: 实例类型，REPLSET-副本集，SHARD-分片集群
        :type ClusterType: str
        :param VpcId: 私有网络ID，如果不设置该参数则默认选择基础网络
        :type VpcId: str
        :param SubnetId: 私有网络下的子网ID，如果设置了 VpcId，则 SubnetId必填
        :type SubnetId: str
        :param Password: 实例密码，不设置该参数则需要在创建完成后通过设置密码接口初始化实例密码。密码必须是8-16位字符，且至少包含字母、数字和字符 !@#%^*() 中的两种
        :type Password: str
        :param ProjectId: 项目ID，不设置为默认项目
        :type ProjectId: int
        :param Tags: 实例标签信息
        :type Tags: list of TagInfo
        """
        self.Memory = None
        self.Volume = None
        self.ReplicateSetNum = None
        self.NodeNum = None
        self.MongoVersion = None
        self.MachineCode = None
        self.GoodsNum = None
        self.Zone = None
        self.ClusterType = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.ProjectId = None
        self.Tags = None

    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.NodeNum = params.get("NodeNum")
        self.MongoVersion = params.get("MongoVersion")
        self.MachineCode = params.get("MachineCode")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.ClusterType = params.get("ClusterType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")
        self.ProjectId = params.get("ProjectId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateDBInstanceHourResponse(AbstractModel):
    """CreateDBInstanceHour返回参数结构体"""

    def __init__(self):
        """
        :param DealId: 订单ID
        :type DealId: str
        :param InstanceIds: 创建的实例ID列表
        :type InstanceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.InstanceIds = None
        self.RequestId = None

    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance请求参数结构体"""

    def __init__(self):
        """
        :param NodeNum: 每个副本集内节点个数，当前副本集节点数固定为3，分片从节点数可选，具体参照查询云数据库的售卖规格返回参数
        :type NodeNum: int
        :param Memory: 实例内存大小，单位：GB
        :type Memory: int
        :param Volume: 实例硬盘大小，单位：GB
        :type Volume: int
        :param MongoVersion: 版本号，具体支持的售卖版本请参照查询云数据库的售卖规格（DescribeSpecInfo）返回结果。
        参数与版本对应关系是MONGO_3_WT：MongoDB 3.2 WiredTiger存储引擎版本，MONGO_3_ROCKS：MongoDB 3.2
        RocksDB存储引擎版本，MONGO_36_WT：MongoDB 3.6 WiredTiger存储引擎版本
        :type MongoVersion: str
        :param GoodsNum: 实例数量, 最小值1，最大值为10
        :type GoodsNum: int
        :param Zone: 实例所属区域名称，格式如：ap-guangzhou-2
        :type Zone: str
        :param Period: 实例时长，单位：月，可选值包括 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]
        :type Period: int
        :param MachineCode: 机器类型，HIO：高IO型；HIO10G：高IO万兆型
        :type MachineCode: str
        :param ClusterType: 实例类型，REPLSET-副本集，SHARD-分片集群
        :type ClusterType: str
        :param ReplicateSetNum: 副本集个数，创建副本集实例时，该参数必须设置为1；创建分片实例时，具体参照查询云数据库的售卖规格返回参数
        :type ReplicateSetNum: int
        :param ProjectId: 项目ID，不设置为默认项目
        :type ProjectId: int
        :param VpcId: 私有网络 ID，如果不传则默认选择基础网络，请使用 查询私有网络列表
        :type VpcId: str
        :param SubnetId: 私有网络下的子网 ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用 查询子网列表
        :type SubnetId: str
        :param Password: 实例密码，不设置该参数则需要在创建完成后通过设置密码接口初始化实例密码。密码必须是8-16位字符，且至少包含字母、数字和字符 !@#%^*() 中的两种
        :type Password: str
        :param Tags: 实例标签信息
        :type Tags: list of TagInfo
        :param AutoRenewFlag: 自动续费标记，可选值为：0 - 不自动续费；1 - 自动续费。默认为不自动续费
        :type AutoRenewFlag: int
        """
        self.NodeNum = None
        self.Memory = None
        self.Volume = None
        self.MongoVersion = None
        self.GoodsNum = None
        self.Zone = None
        self.Period = None
        self.MachineCode = None
        self.ClusterType = None
        self.ReplicateSetNum = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.Tags = None
        self.AutoRenewFlag = None

    def _deserialize(self, params):
        self.NodeNum = params.get("NodeNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.MongoVersion = params.get("MongoVersion")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.Period = params.get("Period")
        self.MachineCode = params.get("MachineCode")
        self.ClusterType = params.get("ClusterType")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoRenewFlag = params.get("AutoRenewFlag")


class CreateDBInstanceResponse(AbstractModel):
    """CreateDBInstance返回参数结构体"""

    def __init__(self):
        """
        :param DealId: 订单ID
        :type DealId: str
        :param InstanceIds: 创建的实例ID列表
        :type InstanceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.InstanceIds = None
        self.RequestId = None

    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class DBInstanceInfo(AbstractModel):
    """实例信息"""

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Region: 地域信息
        :type Region: str
        """
        self.InstanceId = None
        self.Region = None

    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Region = params.get("Region")


class DescribeBackupAccessRequest(AbstractModel):
    """DescribeBackupAccess请求参数结构体"""

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param BackupName: 需要获取下载授权的备份文件名
        :type BackupName: str
        """
        self.InstanceId = None
        self.BackupName = None

    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupName = params.get("BackupName")


class DescribeBackupAccessResponse(AbstractModel):
    """DescribeBackupAccess返回参数结构体"""

    def __init__(self):
        """
        :param Region: 实例所属地域
        :type Region: str
        :param Bucket: 备份文件所在存储桶
        :type Bucket: str
        :param Files: 备份文件的存储信息
        :type Files: list of BackupFile
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Region = None
        self.Bucket = None
        self.Files = None
        self.RequestId = None

    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        if params.get("Files") is not None:
            self.Files = []
            for item in params.get("Files"):
                obj = BackupFile()
                obj._deserialize(item)
                self.Files.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClientConnectionsRequest(AbstractModel):
    """DescribeClientConnections请求参数结构体"""

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        """
        self.InstanceId = None

    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeClientConnectionsResponse(AbstractModel):
    """DescribeClientConnections返回参数结构体"""

    def __init__(self):
        """
        :param Clients: 客户端连接信息，包括客户端IP和对应IP的连接数量
        :type Clients: list of ClientConnection
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Clients = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("Clients") is not None:
            self.Clients = []
            for item in params.get("Clients"):
                obj = ClientConnection()
                obj._deserialize(item)
                self.Clients.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBBackupsRequest(AbstractModel):
    """DescribeDBBackups请求参数结构体"""

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        """
        self.InstanceId = None

    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDBBackupsResponse(AbstractModel):
    """DescribeDBBackups返回参数结构体"""

    def __init__(self):
        """
        :param BackupList: 备份列表
        :type BackupList: list of BackupInfo
        :param TotalCount: 备份总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BackupList = None
        self.TotalCount = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("BackupList") is not None:
            self.BackupList = []
            for item in params.get("BackupList"):
                obj = BackupInfo()
                obj._deserialize(item)
                self.BackupList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体"""

    def __init__(self):
        """
        :param InstanceIds: 实例ID列表，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceIds: list of str
        :param InstanceType: 实例类型，取值范围：0-所有实例,1-正式实例，2-临时实例, 3-只读实例，-1-正式实例+只读+灾备实例
        :type InstanceType: int
        :param ClusterType: 集群类型，取值范围：0-副本集实例，1-分片实例，-1-所有实例
        :type ClusterType: int
        :param Status: 实例状态，取值范围：0-待初始化，1-流程执行中，2-实例有效，-2-实例已过期
        :type Status: list of int
        :param VpcId: 私有网络的ID，基础网络则不传该参数
        :type VpcId: str
        :param SubnetId: 私有网络的子网ID，基础网络则不传该参数。入参设置该参数的同时，必须设置相应的VpcId
        :type SubnetId: str
        :param PayMode: 付费类型，取值范围：0-按量计费，1-包年包月，-1-按量计费+包年包月
        :type PayMode: int
        :param Limit: 单次请求返回的数量，最小值为1，最大值为100，默认值为20
        :type Limit: int
        :param Offset: 偏移量，默认值为0
        :type Offset: int
        :param OrderBy: 返回结果集排序的字段，目前支持："ProjectId", "InstanceName", "CreateTime"，默认为升序排序
        :type OrderBy: str
        :param OrderByType: 返回结果集排序方式，目前支持："ASC"或者"DESC"
        :type OrderByType: str
        :param ProjectIds: 项目 ID
        :type ProjectIds: list of int non-negative
        :param SearchKey: 搜索关键词，支持实例Id、实例名称、完整IP
        :type SearchKey: str
        """
        self.InstanceIds = None
        self.InstanceType = None
        self.ClusterType = None
        self.Status = None
        self.VpcId = None
        self.SubnetId = None
        self.PayMode = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None
        self.ProjectIds = None
        self.SearchKey = None

    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceType = params.get("InstanceType")
        self.ClusterType = params.get("ClusterType")
        self.Status = params.get("Status")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.PayMode = params.get("PayMode")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.ProjectIds = params.get("ProjectIds")
        self.SearchKey = params.get("SearchKey")


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回参数结构体"""

    def __init__(self):
        """
        :param TotalCount: 符合查询条件的实例总数
        :type TotalCount: int
        :param InstanceDetails: 实例详细信息列表
        :type InstanceDetails: list of InstanceDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceDetails = None
        self.RequestId = None

    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceDetails") is not None:
            self.InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = InstanceDetail()
                obj._deserialize(item)
                self.InstanceDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSpecInfoRequest(AbstractModel):
    """DescribeSpecInfo请求参数结构体"""

    def __init__(self):
        """
        :param Zone: 待查询可用区
        :type Zone: str
        """
        self.Zone = None

    def _deserialize(self, params):
        self.Zone = params.get("Zone")


class DescribeSpecInfoResponse(AbstractModel):
    """DescribeSpecInfo返回参数结构体"""

    def __init__(self):
        """
        :param SpecInfoList: 实例售卖规格信息列表
        :type SpecInfoList: list of SpecificationInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SpecInfoList = None
        self.RequestId = None

    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self.SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecificationInfo()
                obj._deserialize(item)
                self.SpecInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class InstanceDetail(AbstractModel):
    """实例详情"""

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param PayMode: 付费类型，可能的返回值：1-包年包月；0-按量计费
        :type PayMode: int
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param ClusterType: 集群类型，可能的返回值：0-副本集实例，1-分片实例，
        :type ClusterType: int
        :param Region: 地域信息
        :type Region: str
        :param Zone: 可用区信息
        :type Zone: str
        :param NetType: 网络类型，可能的返回值：0-基础网络，1-私有网络
        :type NetType: int
        :param VpcId: 私有网络的ID
        :type VpcId: str
        :param SubnetId: 私有网络的子网ID
        :type SubnetId: str
        :param Status: 实例状态，可能的返回值：0-待初始化，1-流程处理中，2-运行中，-2-实例已过期
        :type Status: int
        :param Vip: 实例IP
        :type Vip: str
        :param Vport: 端口号
        :type Vport: int
        :param CreateTime: 实例创建时间
        :type CreateTime: str
        :param DeadLine: 实例到期时间
        :type DeadLine: str
        :param MongoVersion: 实例版本信息
        :type MongoVersion: str
        :param Memory: 实例内存规格，单位为MB
        :type Memory: int
        :param Volume: 实例磁盘规格，单位为MB
        :type Volume: int
        :param CpuNum: 实例CPU核心数
        :type CpuNum: int
        :param MachineType: 实例机器类型
        :type MachineType: str
        :param SecondaryNum: 实例从节点数
        :type SecondaryNum: int
        :param ReplicationSetNum: 实例分片数
        :type ReplicationSetNum: int
        :param AutoRenewFlag: 实例自动续费标志，可能的返回值：0-手动续费，1-自动续费，2-确认不续费
        :type AutoRenewFlag: int
        :param UsedVolume: 已用容量，单位MB
        :type UsedVolume: int
        :param MaintenanceStart: 维护窗口起始时间
        :type MaintenanceStart: str
        :param MaintenanceEnd: 维护窗口结束时间
        :type MaintenanceEnd: str
        :param ReplicaSets: 分片信息
        :type ReplicaSets: list of ShardInfo
        :param ReadonlyInstances: 只读实例信息
        :type ReadonlyInstances: list of DBInstanceInfo
        :param StandbyInstances: 灾备实例信息
        :type StandbyInstances: list of DBInstanceInfo
        :param CloneInstances: 临时实例信息
        :type CloneInstances: list of DBInstanceInfo
        :param RelatedInstance: 关联实例信息，对于正式实例，该字段表示它的临时实例信息；对于临时实例，则表示它的正式实例信息;如果为只读/灾备实例,则表示他的主实例信息
        :type RelatedInstance: :class:`tencentcloud.mongodb.v20190725.models.DBInstanceInfo`
        :param Tags: 实例标签信息集合
        :type Tags: list of TagInfo
        :param InstanceVer: 实例版本标记
        :type InstanceVer: int
        :param ClusterVer: 实例版本标记
        :type ClusterVer: int
        :param Protocol: 协议信息，可能的返回值：1-mongodb，2-dynamodb
        :type Protocol: int
        :param InstanceType: 实例类型，可能的返回值，1-正式实例，2-临时实例，3-只读实例，4-灾备实例
        :type InstanceType: int
        :param InstanceStatusDesc: 实例状态描述
        :type InstanceStatusDesc: str
        :param RealInstanceId: 实例对应的物理实例id，回档并替换过的实例有不同的InstanceId和RealInstanceId，从barad获取监控数据等场景下需要用物理id获取
        :type RealInstanceId: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.PayMode = None
        self.ProjectId = None
        self.ClusterType = None
        self.Region = None
        self.Zone = None
        self.NetType = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.Vip = None
        self.Vport = None
        self.CreateTime = None
        self.DeadLine = None
        self.MongoVersion = None
        self.Memory = None
        self.Volume = None
        self.CpuNum = None
        self.MachineType = None
        self.SecondaryNum = None
        self.ReplicationSetNum = None
        self.AutoRenewFlag = None
        self.UsedVolume = None
        self.MaintenanceStart = None
        self.MaintenanceEnd = None
        self.ReplicaSets = None
        self.ReadonlyInstances = None
        self.StandbyInstances = None
        self.CloneInstances = None
        self.RelatedInstance = None
        self.Tags = None
        self.InstanceVer = None
        self.ClusterVer = None
        self.Protocol = None
        self.InstanceType = None
        self.InstanceStatusDesc = None
        self.RealInstanceId = None

    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.PayMode = params.get("PayMode")
        self.ProjectId = params.get("ProjectId")
        self.ClusterType = params.get("ClusterType")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.NetType = params.get("NetType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.CreateTime = params.get("CreateTime")
        self.DeadLine = params.get("DeadLine")
        self.MongoVersion = params.get("MongoVersion")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.CpuNum = params.get("CpuNum")
        self.MachineType = params.get("MachineType")
        self.SecondaryNum = params.get("SecondaryNum")
        self.ReplicationSetNum = params.get("ReplicationSetNum")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.UsedVolume = params.get("UsedVolume")
        self.MaintenanceStart = params.get("MaintenanceStart")
        self.MaintenanceEnd = params.get("MaintenanceEnd")
        if params.get("ReplicaSets") is not None:
            self.ReplicaSets = []
            for item in params.get("ReplicaSets"):
                obj = ShardInfo()
                obj._deserialize(item)
                self.ReplicaSets.append(obj)
        if params.get("ReadonlyInstances") is not None:
            self.ReadonlyInstances = []
            for item in params.get("ReadonlyInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self.ReadonlyInstances.append(obj)
        if params.get("StandbyInstances") is not None:
            self.StandbyInstances = []
            for item in params.get("StandbyInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self.StandbyInstances.append(obj)
        if params.get("CloneInstances") is not None:
            self.CloneInstances = []
            for item in params.get("CloneInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self.CloneInstances.append(obj)
        if params.get("RelatedInstance") is not None:
            self.RelatedInstance = DBInstanceInfo()
            self.RelatedInstance._deserialize(params.get("RelatedInstance"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceVer = params.get("InstanceVer")
        self.ClusterVer = params.get("ClusterVer")
        self.Protocol = params.get("Protocol")
        self.InstanceType = params.get("InstanceType")
        self.InstanceStatusDesc = params.get("InstanceStatusDesc")
        self.RealInstanceId = params.get("RealInstanceId")


class IsolateDBInstanceRequest(AbstractModel):
    """IsolateDBInstance请求参数结构体"""

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        """
        self.InstanceId = None

    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class IsolateDBInstanceResponse(AbstractModel):
    """IsolateDBInstance返回参数结构体"""

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None

    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSpecRequest(AbstractModel):
    """ModifyDBInstanceSpec请求参数结构体"""

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param Memory: 实例配置变更后的内存大小，单位：GB。内存和磁盘必须同时升配或同时降配
        :type Memory: int
        :param Volume: 实例配置变更后的硬盘大小，单位：GB。内存和磁盘必须同时升配或同时降配。降配时，新的磁盘参数必须大于已用磁盘容量的1.2倍
        :type Volume: int
        :param OplogSize: 实例配置变更后oplog的大小，单位：GB，默认为磁盘空间的10%，允许设置的最小值为磁盘的10%，最大值为磁盘的90%
        :type OplogSize: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None

    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")


class ModifyDBInstanceSpecResponse(AbstractModel):
    """ModifyDBInstanceSpec返回参数结构体"""

    def __init__(self):
        """
        :param DealId: 订单ID
        :type DealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None

    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class OfflineIsolatedDBInstanceRequest(AbstractModel):
    """OfflineIsolatedDBInstance请求参数结构体"""

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        """
        self.InstanceId = None

    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class OfflineIsolatedDBInstanceResponse(AbstractModel):
    """OfflineIsolatedDBInstance返回参数结构体"""

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None

    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class RenameInstanceRequest(AbstractModel):
    """RenameInstance请求参数结构体"""

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param NewName: 实例名称
        :type NewName: str
        """
        self.InstanceId = None
        self.NewName = None

    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NewName = params.get("NewName")


class RenameInstanceResponse(AbstractModel):
    """RenameInstance返回参数结构体"""

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None

    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ShardInfo(AbstractModel):
    """实例分片详情"""

    def __init__(self):
        """
        :param UsedVolume: 分片已使用容量
        :type UsedVolume: float
        :param ReplicaSetId: 分片ID
        :type ReplicaSetId: str
        :param ReplicaSetName: 分片名
        :type ReplicaSetName: str
        :param Memory: 分片内存规格，单位为MB
        :type Memory: int
        :param Volume: 分片磁盘规格，单位为MB
        :type Volume: int
        :param OplogSize: 分片Oplog大小，单位为MB
        :type OplogSize: int
        :param SecondaryNum: 分片从节点数
        :type SecondaryNum: int
        :param RealReplicaSetId: 分片物理id
        :type RealReplicaSetId: str
        """
        self.UsedVolume = None
        self.ReplicaSetId = None
        self.ReplicaSetName = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None
        self.SecondaryNum = None
        self.RealReplicaSetId = None

    def _deserialize(self, params):
        self.UsedVolume = params.get("UsedVolume")
        self.ReplicaSetId = params.get("ReplicaSetId")
        self.ReplicaSetName = params.get("ReplicaSetName")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")
        self.SecondaryNum = params.get("SecondaryNum")
        self.RealReplicaSetId = params.get("RealReplicaSetId")


class SpecItem(AbstractModel):
    """mongodb售卖规格"""

    def __init__(self):
        """
        :param SpecCode: 规格信息标识
        :type SpecCode: str
        :param Status: 规格有效标志，取值：0-停止售卖，1-开放售卖
        :type Status: int
        :param Cpu: 规格有效标志，取值：0-停止售卖，1-开放售卖
        :type Cpu: int
        :param Memory: 内存规格，单位为MB
        :type Memory: int
        :param DefaultStorage: 默认磁盘规格，单位MB
        :type DefaultStorage: int
        :param MaxStorage: 最大磁盘规格，单位MB
        :type MaxStorage: int
        :param MinStorage: 最小磁盘规格，单位MB
        :type MinStorage: int
        :param Qps: 可承载qps信息
        :type Qps: int
        :param Conns: 连接数限制
        :type Conns: int
        :param MongoVersionCode: 实例mongodb版本信息
        :type MongoVersionCode: str
        :param MongoVersionValue: 实例mongodb版本号
        :type MongoVersionValue: int
        :param Version: 实例mongodb版本号（短）
        :type Version: str
        :param EngineName: 存储引擎
        :type EngineName: str
        :param ClusterType: 集群类型，取值：1-分片集群，0-副本集集群
        :type ClusterType: int
        :param MinNodeNum: 最小副本集从节点数
        :type MinNodeNum: int
        :param MaxNodeNum: 最大副本集从节点数
        :type MaxNodeNum: int
        :param MinReplicateSetNum: 最小分片数
        :type MinReplicateSetNum: int
        :param MaxReplicateSetNum: 最大分片数
        :type MaxReplicateSetNum: int
        :param MinReplicateSetNodeNum: 最小分片从节点数
        :type MinReplicateSetNodeNum: int
        :param MaxReplicateSetNodeNum: 最大分片从节点数
        :type MaxReplicateSetNodeNum: int
        :param MachineType: 机器类型，取值：0-HIO，4-HIO10G
        :type MachineType: str
        """
        self.SpecCode = None
        self.Status = None
        self.Cpu = None
        self.Memory = None
        self.DefaultStorage = None
        self.MaxStorage = None
        self.MinStorage = None
        self.Qps = None
        self.Conns = None
        self.MongoVersionCode = None
        self.MongoVersionValue = None
        self.Version = None
        self.EngineName = None
        self.ClusterType = None
        self.MinNodeNum = None
        self.MaxNodeNum = None
        self.MinReplicateSetNum = None
        self.MaxReplicateSetNum = None
        self.MinReplicateSetNodeNum = None
        self.MaxReplicateSetNodeNum = None
        self.MachineType = None

    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.Status = params.get("Status")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.DefaultStorage = params.get("DefaultStorage")
        self.MaxStorage = params.get("MaxStorage")
        self.MinStorage = params.get("MinStorage")
        self.Qps = params.get("Qps")
        self.Conns = params.get("Conns")
        self.MongoVersionCode = params.get("MongoVersionCode")
        self.MongoVersionValue = params.get("MongoVersionValue")
        self.Version = params.get("Version")
        self.EngineName = params.get("EngineName")
        self.ClusterType = params.get("ClusterType")
        self.MinNodeNum = params.get("MinNodeNum")
        self.MaxNodeNum = params.get("MaxNodeNum")
        self.MinReplicateSetNum = params.get("MinReplicateSetNum")
        self.MaxReplicateSetNum = params.get("MaxReplicateSetNum")
        self.MinReplicateSetNodeNum = params.get("MinReplicateSetNodeNum")
        self.MaxReplicateSetNodeNum = params.get("MaxReplicateSetNodeNum")
        self.MachineType = params.get("MachineType")


class SpecificationInfo(AbstractModel):
    """实例规格信息"""

    def __init__(self):
        """
        :param Region: 地域信息
        :type Region: str
        :param Zone: 可用区信息
        :type Zone: str
        :param SpecItems: 售卖规格信息
        :type SpecItems: list of SpecItem
        """
        self.Region = None
        self.Zone = None
        self.SpecItems = None

    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        if params.get("SpecItems") is not None:
            self.SpecItems = []
            for item in params.get("SpecItems"):
                obj = SpecItem()
                obj._deserialize(item)
                self.SpecItems.append(obj)


class TagInfo(AbstractModel):
    """实例标签信息"""

    def __init__(self):
        """
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None

    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
