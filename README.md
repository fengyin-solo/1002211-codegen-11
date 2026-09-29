# 消防设施维保管理平台

面向灭火器、消火栓、报警主机、消防泵房、防火分隔、疏散通道与消防演练的一体化消防设施维保管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 灭火器管理 | `extinguisher` | 灭火器 | 编号、规格型号、灭火剂类型 |
| 消火栓管理 | `hydrant` | 消火栓 | 栓号、安装位置、栓口数量 |
| 报警主机管理 | `alarmhost` | 火灾报警主机 | 主机编号、主机型号、安装位置 |
| 探测器管理 | `detector` | 火灾探测器 | 探测器编号、探测器类型、安装位置 |
| 消防泵房管理 | `pumphouse` | 消防水泵 | 泵号、水泵类型、额定流量 |
| 消防水池管理 | `watertank` | 消防水池 | 水池编号、水池容积、当前水位 |
| 防火门管理 | `door` | 防火门 | 门号、安装位置、门体类型 |
| 防火卷帘管理 | `shutter` | 防火卷帘 | 卷帘编号、安装位置、卷帘面积 |
| 疏散通道管理 | `exit` | 疏散通道 | 通道编号、所在楼层、通道宽度 |
| 喷淋系统管理 | `sprinkler` | 喷淋系统 | 系统编号、保护区域、喷头数量 |
| 气体灭火系统 | `gas` | 气体灭火装置 | 装置编号、保护区域、灭火剂种类 |
| 消防演练管理 | `drill` | 消防演练 | 演练编号、演练类型、参与部门 |
| 消防培训管理 | `training` | 消防培训 | 培训编号、培训主题、培训讲师 |
| 动火审批 | `change` | 动火证 | 动火证编号、申请部门、动火地点 |
| 故障报修 | `fault` | 故障报修单 | 报修编号、报修设施、故障现象 |
| 消防许可证件管理 | `cert` | 消防证件 | 证件编号、证件类型、持证单位 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
