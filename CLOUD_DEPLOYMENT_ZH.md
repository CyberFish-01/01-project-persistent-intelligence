# 01 Core 云端部署

英文镜像：[CLOUD_DEPLOYMENT.md](./CLOUD_DEPLOYMENT.md)

01 Core 更适合运行在云服务器上。

原因很简单：Persistent Intelligence 需要持续的 state home。如果它只在本地电脑运行，关机、断网、睡觉、出门都会打断连续性。

第一版推荐部署形态：

```text
AstrBot
  ↓ localhost
01 Core API
  ↓
/root/01_state
```

## 服务器目录

推荐：

```text
/root/01-project-persistent-intelligence  # 代码仓库
/root/01_state                            # 01 Core 状态
/root/01_imports                          # 一次性记忆导入中间产物
/root/data/plugins/astrbot_plugin_01_core # AstrBot adapter
```

## 拉取仓库

```bash
git clone https://github.com/CyberFish-01/01-project-persistent-intelligence.git /root/01-project-persistent-intelligence
```

更新：

```bash
cd /root/01-project-persistent-intelligence
git pull --ff-only
```

## 初始化状态

```bash
cd /root/01-project-persistent-intelligence
python3 -m one_core.cli --state-dir /root/01_state init
```

如果需要从 AstrBot / Angel Memory 导入旧记忆：

```bash
mkdir -p /root/01_imports
find /root/data/plugin_data/astrbot_plugin_angel_memory /root/data/plugin_data/astrbot_plugin_01_dreams \
  -type f \
  \( -name '*.db' -o -name '*.sqlite' -o -name '*.sqlite3' -o -name '*.json' -o -name '*.jsonl' -o -name '*.md' -o -name '*.txt' \) \
  > /root/01_imports/source_files.txt

python3 -m one_core.cli clean-memory $(cat /root/01_imports/source_files.txt) \
  -o /root/01_imports/astrbot_angel_memory_cleaned.txt

python3 -m one_core.cli --state-dir /root/01_state import-text \
  /root/01_imports/astrbot_angel_memory_cleaned.txt \
  --source-label astrbot_angel_memory_cloud_seed \
  --source-system astrbot_angel_memory

python3 -m one_core.cli --state-dir /root/01_state dream --limit 1000
```

## systemd 常驻服务

仓库内提供 service 模板：

```text
deploy/systemd/01-core.service
```

安装：

```bash
cp /root/01-project-persistent-intelligence/deploy/systemd/01-core.service /etc/systemd/system/01-core.service
systemctl daemon-reload
systemctl enable --now 01-core.service
```

检查：

```bash
systemctl status 01-core.service --no-pager -l
curl http://127.0.0.1:8765/health
curl http://127.0.0.1:8765/v1/status
```

## 安装 AstrBot Adapter

```bash
rm -rf /root/data/plugins/astrbot_plugin_01_core
cp -R /root/01-project-persistent-intelligence/adapters/astrbot/astrbot_plugin_01_core \
  /root/data/plugins/astrbot_plugin_01_core
systemctl restart astrbot.service
```

然后在 AstrBot 使用：

```text
/01 ping
/01 status
/01 context
/01 chat <内容>
/01 dream [limit]
```

## 安全边界

第一版 API 默认只监听：

```text
127.0.0.1:8765
```

不要直接暴露到公网。

远程访问应该等后续加入：

- token；
- TLS；
- 路径白名单；
- adapter 身份；
- 审计日志。

## 当前服务器验证记录

2026-06-03 已完成一次云端部署验证：

```text
01 Core service: active, enabled
01 Core API: http://127.0.0.1:8765
state dir: /root/01_state
imported memories: 1005
semantic memories after dream: 9
pending dream jobs: 0
AstrBot service: active
AstrBot adapter import under AstrBot runtime: ok
```
