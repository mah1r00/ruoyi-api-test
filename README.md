# 若依（RuoYi）企业级后台接口自动化测试

## 项目简介
针对若依企业级后台管理系统（RuoYi-Vue v3.9.2），对用户管理、角色管理、部门管理等核心模块进行接口自动化测试，基于 Python + Pytest + Requests 搭建自动化测试框架，并使用 JMeter 完成基础性能测试。

## 技术栈
| 工具 | 用途 |
|------|------|
| Python 3.12 | 编程语言 |
| Pytest | 测试框架 |
| Requests | HTTP 请求库 |
| YAML | 测试数据管理 |
| Allure | 测试报告生成 |
| JMeter 5.6.3 | 性能测试 |
| Apifox | 接口调试与自动化 Runner |

## 测试范围
| 模块 | 接口数 | 用例数 | 测试重点 |
|------|--------|--------|---------|
| 登录认证 | 3 | 6 | 登录鉴权、Token获取、用户信息 |
| 用户管理 | 8 | 18 | 用户增删改查、重复名校验、状态切换、密码重置 |
| 角色管理 | 5 | 10 | 角色增删查、权限分配 |
| 部门管理 | 4 | 8 | 部门增删查 |
| **合计** | **20** | **42** | 正向21条 + 反向21条 |

## 项目结构
```
ruoyi-test/
├── config/                  # 配置文件
│   └── settings.yaml        # 环境配置（URL、账号）
├── common/                  # 公共模块
│   ├── api_client.py        # HTTP 请求封装（GET/POST/PUT/DELETE）
│   └── token_manager.py     # Token 获取与自动刷新
├── testcases/               # 测试用例
│   ├── conftest.py          # pytest 全局配置
│   ├── test_login.py        # 登录模块测试
│   ├── test_user.py         # 用户管理测试
│   ├── test_role.py         # 角色管理测试
│   └── test_dept.py         # 部门管理测试
├── data/                    # 测试数据
│   ├── user_data.yaml
│   └── role_data.yaml
├── aggregate.csv            # JMeter 聚合报告
├── summary.csv              # JMeter 汇总报告
├── requirements.txt         # Python 依赖
└── README.md
```

## 运行方式
```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行所有测试
pytest -v

# 3. 生成 Allure 报告
pytest --alluredir=./reports
allure serve ./reports
```

## 测试环境
- 被测系统：若依（RuoYi-Vue v3.9.2）
- 部署方式：本地部署（MySQL + Redis + 前后端分离）
- 后端地址：http://localhost:8080
- 认证方式：Bearer Token

## 性能测试结果（JMeter）
| 指标 | 值 |
|------|-----|
| 测试场景 | 登录接口并发 |
| 线程数 | 50 |
| 总请求数 | 500 |
| 平均响应时间 | 581ms |
| 90% 响应时间 | 950ms |
| 99% 响应时间 | 1325ms |
| 最快响应时间 | 143ms |
| 最慢响应时间 | 1425ms |
| 异常率 | 0% |
| 吞吐量 | 47.5 req/s |

## 项目收获
- 掌握了从零搭建接口自动化测试框架的能力，理解数据驱动、依赖处理、断言封装等核心设计思想
- 熟悉企业级后台系统（若依）的 RBAC 权限模型，积累了多角色权限测试经验
- 具备将 Swagger 文档转化为自动化用例的能力，实现接口测试体系化落地
- 掌握 JMeter 性能测试基础方法，能够独立完成接口并发测试与结果分析
