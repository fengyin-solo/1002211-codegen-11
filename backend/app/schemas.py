"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class ExtinguisherEntry(BaseModel):
    """灭火器明细结构。"""

    field_0: str | None = None  # 编号
    field_1: str | None = None  # 规格型号
    field_2: str | None = None  # 灭火剂类型
    field_3: str | None = None  # 放置位置
    field_4: str | None = None  # 充装日期
    field_5: str | None = None  # 下次检验日期
    field_6: str | None = None  # 责任人
    field_7: str | None = None  # 使用状态

class HydrantEntry(BaseModel):
    """消火栓明细结构。"""

    field_0: str | None = None  # 栓号
    field_1: str | None = None  # 安装位置
    field_2: str | None = None  # 栓口数量
    field_3: str | None = None  # 供水来源
    field_4: str | None = None  # 出水压力
    field_5: str | None = None  # 上次试水日期
    field_6: str | None = None  # 维护人员
    field_7: str | None = None  # 使用状态

class AlarmhostEntry(BaseModel):
    """火灾报警主机明细结构。"""

    field_0: str | None = None  # 主机编号
    field_1: str | None = None  # 主机型号
    field_2: str | None = None  # 安装位置
    field_3: str | None = None  # 回路数量
    field_4: str | None = None  # 探测器数量
    field_5: str | None = None  # 上次巡检日期
    field_6: str | None = None  # 维护厂家
    field_7: str | None = None  # 运行状态

class DetectorEntry(BaseModel):
    """火灾探测器明细结构。"""

    field_0: str | None = None  # 探测器编号
    field_1: str | None = None  # 探测器类型
    field_2: str | None = None  # 安装位置
    field_3: str | None = None  # 所属回路
    field_4: str | None = None  # 安装日期
    field_5: str | None = None  # 清洗日期
    field_6: str | None = None  # 灵敏度
    field_7: str | None = None  # 运行状态

class PumphouseEntry(BaseModel):
    """消防水泵明细结构。"""

    field_0: str | None = None  # 泵号
    field_1: str | None = None  # 水泵类型
    field_2: str | None = None  # 额定流量
    field_3: str | None = None  # 额定扬程
    field_4: str | None = None  # 电机功率
    field_5: str | None = None  # 上次启动测试日期
    field_6: str | None = None  # 控制方式
    field_7: str | None = None  # 运行状态

class WatertankEntry(BaseModel):
    """消防水池明细结构。"""

    field_0: str | None = None  # 水池编号
    field_1: str | None = None  # 水池容积
    field_2: str | None = None  # 当前水位
    field_3: str | None = None  # 补水方式
    field_4: str | None = None  # 上次清洗日期
    field_5: str | None = None  # 水质量检测日期
    field_6: str | None = None  # 管理人员
    field_7: str | None = None  # 水池状态

class DoorEntry(BaseModel):
    """防火门明细结构。"""

    field_0: str | None = None  # 门号
    field_1: str | None = None  # 安装位置
    field_2: str | None = None  # 门体类型
    field_3: str | None = None  # 耐火等级
    field_4: str | None = None  # 安装日期
    field_5: str | None = None  # 上次检修日期
    field_6: str | None = None  # 闭门器状态
    field_7: str | None = None  # 使用状态

class ShutterEntry(BaseModel):
    """防火卷帘明细结构。"""

    field_0: str | None = None  # 卷帘编号
    field_1: str | None = None  # 安装位置
    field_2: str | None = None  # 卷帘面积
    field_3: str | None = None  # 耐火极限
    field_4: str | None = None  # 控制方式
    field_5: str | None = None  # 上次测试日期
    field_6: str | None = None  # 联动状态
    field_7: str | None = None  # 使用状态

class ExitEntry(BaseModel):
    """疏散通道明细结构。"""

    field_0: str | None = None  # 通道编号
    field_1: str | None = None  # 所在楼层
    field_2: str | None = None  # 通道宽度
    field_3: str | None = None  # 照明方式
    field_4: str | None = None  # 指示标志数量
    field_5: str | None = None  # 上次检查日期
    field_6: str | None = None  # 检查人员
    field_7: str | None = None  # 通道状态

class SprinklerEntry(BaseModel):
    """喷淋系统明细结构。"""

    field_0: str | None = None  # 系统编号
    field_1: str | None = None  # 保护区域
    field_2: str | None = None  # 喷头数量
    field_3: str | None = None  # 末端压力
    field_4: str | None = None  # 水流指示器状态
    field_5: str | None = None  # 上次试水日期
    field_6: str | None = None  # 管网压力
    field_7: str | None = None  # 系统状态

class GasEntry(BaseModel):
    """气体灭火装置明细结构。"""

    field_0: str | None = None  # 装置编号
    field_1: str | None = None  # 保护区域
    field_2: str | None = None  # 灭火剂种类
    field_3: str | None = None  # 钢瓶数量
    field_4: str | None = None  # 上次充装日期
    field_5: str | None = None  # 驱动压力
    field_6: str | None = None  # 控制方式
    field_7: str | None = None  # 装置状态

class DrillEntry(BaseModel):
    """消防演练明细结构。"""

    field_0: str | None = None  # 演练编号
    field_1: str | None = None  # 演练类型
    field_2: str | None = None  # 参与部门
    field_3: str | None = None  # 演练日期
    field_4: str | None = None  # 演练时长
    field_5: str | None = None  # 参与人数
    field_6: str | None = None  # 演练评估
    field_7: str | None = None  # 演练状态

class TrainingEntry(BaseModel):
    """消防培训明细结构。"""

    field_0: str | None = None  # 培训编号
    field_1: str | None = None  # 培训主题
    field_2: str | None = None  # 培训讲师
    field_3: str | None = None  # 培训日期
    field_4: str | None = None  # 培训对象
    field_5: str | None = None  # 参训人数
    field_6: str | None = None  # 考核方式
    field_7: str | None = None  # 培训状态

class ChangeEntry(BaseModel):
    """动火证明细结构。"""

    field_0: str | None = None  # 动火证编号
    field_1: str | None = None  # 申请部门
    field_2: str | None = None  # 动火地点
    field_3: str | None = None  # 动火作业类型
    field_4: str | None = None  # 申请日期
    field_5: str | None = None  # 动火时间起
    field_6: str | None = None  # 动火时间止
    field_7: str | None = None  # 审批状态

class FaultEntry(BaseModel):
    """故障报修单明细结构。"""

    field_0: str | None = None  # 报修编号
    field_1: str | None = None  # 报修设施
    field_2: str | None = None  # 故障现象
    field_3: str | None = None  # 报修人
    field_4: str | None = None  # 报修时间
    field_5: str | None = None  # 维修人员
    field_6: str | None = None  # 修复时间
    field_7: str | None = None  # 修理状态

class CertEntry(BaseModel):
    """消防证件明细结构。"""

    field_0: str | None = None  # 证件编号
    field_1: str | None = None  # 证件类型
    field_2: str | None = None  # 持证单位
    field_3: str | None = None  # 发证机关
    field_4: str | None = None  # 签发日期
    field_5: str | None = None  # 有效期至
    field_6: str | None = None  # 证件状态
