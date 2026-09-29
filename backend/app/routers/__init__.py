"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import extinguisher as router_extinguisher
from app.routers import hydrant as router_hydrant
from app.routers import alarmhost as router_alarmhost
from app.routers import detector as router_detector
from app.routers import pumphouse as router_pumphouse
from app.routers import watertank as router_watertank
from app.routers import door as router_door
from app.routers import shutter as router_shutter
from app.routers import exit as router_exit
from app.routers import sprinkler as router_sprinkler
from app.routers import gas as router_gas
from app.routers import drill as router_drill
from app.routers import training as router_training
from app.routers import change as router_change
from app.routers import fault as router_fault
from app.routers import cert as router_cert

ROUTERS = [router_extinguisher, router_hydrant, router_alarmhost, router_detector, router_pumphouse, router_watertank, router_door, router_shutter, router_exit, router_sprinkler, router_gas, router_drill, router_training, router_change, router_fault, router_cert]
