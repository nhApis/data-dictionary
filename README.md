## analysis_asset_risk
#### 描述: 内部高风险网络行为
#### 字段总数: 22
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 自增长栏位 |
|network_catagory |varchar(50) |YES |None  | 僵尸网络类型 |
|c2_ip |varchar(50) |YES |None  | 控制主机服务器地址 |
|c2_url |varchar(50) |YES |None  | 控制主机URL或域名信息 |
|c2_area |varchar(50) |YES |None  | 控制主机所处地域、ISP等信息 |
|bot_ip |varchar(50) |YES |None  | 僵尸主机IP |
|bot_area |varchar(50) |YES |None  | 僵尸主机所处地域、ISP等信息 |
|asset_id |varchar(50) |YES |None  | 关联资产信息 |
|asset_risk_catagory |varchar(50) |YES |None  | 资产风险类型：bot主机还是控制主机 |
|threat_level |varchar(50) |YES |None  | 威胁级别高中低 |
|check_time |datetime |YES |None  | 检测发现的时间 |
|fb_time |datetime |YES |None  | 情报发布时间 |
|threat_source |varchar(50) |YES |None  | 情报来源机构 |
|threat_ioc |varchar(50) |YES |None  | IP、URL情报等 |
|log_start_time |varchar(50) |YES |None  | 此记录关联的日志最早时间 |
|log_end_time |varchar(50) |YES |None  | 此记录关联的日志最晚时间 |
|threat_id |varchar(50) |YES |None  | 情报ID |
|threat_name |varchar(100) |YES |None  |  |
|threat_catagory |varchar(50) |YES |None  | 1，内部情报 2，外部情报 |
|analysis_time |datetime |YES |None  | 分析时间 |
|asset_ip |varchar(50) |YES |None  | 源IP |
|target_ip |varchar(50) |YES |None  | 目标IP |
## analysis_asset_threat
#### 描述: 资产筛选
#### 字段总数: 30
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 自增长栏位 |
|asset_id |varchar(50) |YES |None  | 情报筛选出来的资产ID号 |
|asset_name |varchar(50) |YES |None  | 资产名 |
|asset_ip |varchar(50) |YES |None  | 资产IP |
|asset_domain |varchar(50) |YES |None  | 资产域名 |
|asset_manager |varchar(50) |YES |None  | 资产责任人 |
|asset_oper_sys |varchar(50) |YES |None  | 资产所在业务系统 |
|asset_system_info |varchar(50) |YES |None  | 情报涉及到的系统或应用信息 |
|url |varchar(50) |YES |None  | 匹配资产的情报的具体URL |
|fb_time |datetime |YES |None  | 情报发布时间 |
|check_time |datetime |YES |None  | 检测筛选资产时间 |
|warn_status |varchar(50) |YES |None  | 是否触发告警或预警操作 |
|threat_ioc |varchar(50) |YES |None  | 匹配资产的情报类型，如IP情报，URL情报等 |
|threat_source |varchar(50) |YES |None  | 情报来源机构 |
|threat_credit |varchar(50) |YES |None  | 情报信誉值 |
|threat_type |varchar(50) |YES |None  | 威胁类型 |
|vul_name |varchar(50) |YES |None  | 情报中涉及到的漏洞信息 |
|vul_type |varchar(50) |YES |None  | 漏洞的类别（如DDOS） |
|vul_target |varchar(50) |YES |None  | 漏洞的目标（如弱点或配置问题） |
|cve |varchar(50) |YES |None  | 漏洞CVE编号 |
|cnnvd |varchar(50) |YES |None  | 漏洞CNNVD编号 |
|vul_level |varchar(50) |YES |None  | 漏洞风险级别 |
|threat_actor |varchar(200) |YES |None  | 情报事件中技术和程序 |
|threat_link |varchar(200) |YES |None  | 外部地址 |
|patch |varchar(200) |YES |None  | 厂商或权威机构发布的修复措施 |
|threat_desc |varchar(200) |YES |None  | 情报内容描述 |
|threat_report |varchar(512) |YES |None  | 报告原文（如PDF、WORD、XML、HTML等格式文档） |
|threat_id |varchar(50) |YES |None  | 情报ID |
|threat_catagory |varchar(11) |YES |None  | 1，内部情报 2，外部情报 |
|analysis_time |datetime |YES |None  | 分析时间 |
## analysis_asset_vul
#### 描述: 漏洞情报
#### 字段总数: 27
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 自增长栏位 |
|asset_id |varchar(50) |YES |None  | 情报筛选出来的资产ID号s |
|asset_name |varchar(50) |YES |None  | 资产名 |
|asset_ip |varchar(50) |YES |None  | 资产IP |
|manager |varchar(50) |YES |None  | 资产责任人 |
|asset_oper_sys |varchar(50) |YES |None  | 资产所在业务系统 |
|asset_system_info |varchar(50) |YES |None  | 情报涉及到的系统或应用信息 |
|fb_time |datetime |YES |None  | 情报发布时间 |
|scan_time |datetime |YES |None  | 资产漏洞扫描时间 |
|warn_status |varchar(50) |YES |None  | 是否触发告警或预警操作 |
|threat_ioc |varchar(50) |YES |None  | 匹配资产的情报类型，这里是漏洞情报 |
|threat_source |varchar(50) |YES |None  | 情报来源机构 |
|vul_name |varchar(50) |YES |None  | 情报中涉及到的漏洞信息 |
|vul_catagory |varchar(50) |YES |None  | 漏洞的类别（如DDOS） |
|vul_target |varchar(50) |YES |None  | 漏洞的目标（如弱点或配置问题） |
|cve |varchar(50) |YES |None  | 漏洞CVE编号 |
|cnnvd |varchar(50) |YES |None  | 漏洞CNNVD编号 |
|vul_level |varchar(50) |YES |None  | 漏洞风险级别 |
|threat_type |varchar(200) |YES |None  | 情报事件中技术和程序 |
|threat_link |varchar(200) |YES |None  | 厂商或权威机构发布的修复措施 |
|threat_desc |varchar(200) |YES |None  | 情报内容描述 |
|threat_report |varchar(512) |YES |None  | 报告原文（如PDF、WORD、XML、HTML等格式文档） |
|threat_id |varchar(50) |YES |None  | 情报ID |
|hg_id |varchar(50) |YES |None  |  |
|threat_catagory |varchar(50) |YES |None  | 1，内部情报 2，外部情报 |
|asset_domain |varchar(50) |YES |None  | 资产域名 |
|analysis_time |datetime |YES |None  | 分析时间 |
## analysis_attack
#### 描述: 外部攻击
#### 字段总数: 26
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 自增长栏位 |
|log_id |varchar(50) |YES |None  | 原告警日志ID |
|src_ip |varchar(50) |YES |None  | 原日志源IP，对应情报IP |
|log_catagory |varchar(50) |YES |None  | 原日志类型 |
|warn_type |varchar(50) |YES |None  | 原日志告警类型 |
|warn_level |varchar(50) |YES |None  | 原日志告警级别 |
|log_time |varchar(50) |YES |None  | 日志产生时间 |
|log_detail |varchar(50) |YES |None  | 原日志详细信息 |
|asset_id |varchar(50) |YES |None  | 资产ID号 |
|asset_name |varchar(50) |YES |None  | 资产名 |
|asset_ip |varchar(50) |YES |None  | 资产IP ，对应原日志目标IP |
|manager |varchar(50) |YES |None  | 资产责任人 |
|system |varchar(50) |YES |None  | 资产所在业务系统 |
|fb_time |datetime |YES |None  | 情报发布时间 |
|warn_status |varchar(50) |YES |None  | 是否触发告警或预警操作（告警/预警分开表示） |
|threat_ioc |varchar(50) |YES |None  | 匹配日志的情报类型，如IP情报，URL情报等 |
|threat_source |varchar(50) |YES |None  | 情报来源机构 |
|threat_credit |varchar(50) |YES |None  | 情报信誉值 |
|threat_type |varchar(50) |YES |None  | 情报威胁类型 |
|threat_actor |varchar(200) |YES |None  | 行为特征 |
|threat_link |varchar(200) |YES |None  | 外部地址 |
|threat_desc |varchar(50) |YES |None  | 情报内容描述 |
|threat_report |varchar(50) |YES |None  | 报告原文（如PDF、WORD、XML、HTML等格式文档） |
|threat_id |varchar(50) |YES |None  | 情报ID |
|threat_catagory |varchar(50) |YES |None  | 1，内部情报 2，外部情报 |
|analysis_time |datetime |YES |None  | 分析时间 |
## analysis_event_threat
#### 描述: 情报关联
#### 字段总数: 21
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 自增长栏位 |
|event_id |varchar(50) |YES |None  | 事件ID |
|event_name |varchar(50) |YES |None  | 事件名称 |
|event_type |varchar(50) |YES |None  | 事件类型 |
|event_level |varchar(50) |YES |None  | 级别 |
|src_ip |varchar(50) |YES |None  | 源地址 |
|dst_ip |varchar(50) |YES |None  | 目的地址 |
|last_uptime |datetime |YES |None  | 最后更新时间 |
|event_desc |varchar(200) |YES |None  | 事件描述 |
|threat_id |varchar(50) |YES |None  | 情报ID |
|threat_ioc |varchar(50) |YES |None  | 1IP类2数字类3字符类 |
|threat_source |varchar(50) |YES |None  | 情报来源机构 |
|threat_credit |varchar(50) |YES |None  | 情报信誉值 |
|threat_type |varchar(50) |YES |None  | 威胁类型 |
|threat_actor |varchar(200) |YES |None  | 情报事件中技术和程序 |
|threat_link |varchar(200) |YES |None  | 外部地址 |
|threat_desc |varchar(200) |YES |None  | 情报内容描述 |
|threat_report |varchar(512) |YES |None  | 报告原文 |
|threat_catagory |varchar(11) |YES |None  | 1内部情报 2外部情报 |
|warn_status |varchar(50) |YES |None  | 是否触发告警或预警操作 |
|analysis_time |datetime |YES |None  | 分析时间 |
## analysis_history_attack
#### 描述: 历史攻击回溯
#### 字段总数: 28
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 自增长栏位 |
|log_id |varchar(50) |YES |None  | 历史日志ID |
|src_ip |varchar(50) |YES |None  | 原日志源IP，对应情报IP |
|log_catagory |varchar(50) |YES |None  | 原日志类型 |
|log_warn_type |varchar(50) |YES |None  | 原日志告警类型 |
|log_warn_level |varchar(50) |YES |None  | 原日志告警级别 |
|log_time |datetime |YES |None  | 日志产生时间 |
|log_detail |varchar(50) |YES |None  | 原日志详细信息 |
|asset_id |varchar(50) |YES |None  | 情报筛选出来的资产ID号 |
|asset_name |varchar(50) |YES |None  | 资产名 |
|asset_ip |varchar(50) |YES |None  | 资产IP ，对应原日志目标IP |
|manager |varchar(50) |YES |None  | 资产责任人 |
|asset_oper_sys |varchar(50) |YES |None  | 资产所在业务系统 |
|fb_time |varchar(50) |YES |None  | 情报发布时间 |
|warn_status |varchar(50) |YES |None  | 是否触发告警或预警操作（告警/预警分开表示） |
|threat_ioc |varchar(50) |YES |None  | 匹配日志的情报类型，如IP情报，URL情报等 |
|threat_source |varchar(50) |YES |None  | 情报来源机构 |
|threat_credit |varchar(50) |YES |None  | 情报信誉值 |
|threat_type |varchar(200) |YES |None  | 情报威胁类型 |
|threat_actor |varchar(200) |YES |None  | 行为特征 |
|threat_link |varchar(200) |YES |None  | 情报链接 |
|threat_desc |varchar(200) |YES |None  | 情报内容描述 |
|threat_report |varchar(512) |YES |None  | 报告原文（如PDF、WORD、XML、HTML等格式文档） |
|threat_id |varchar(50) |YES |None  | 情报ID |
|threat_catagory |varchar(50) |YES |None  | 1，内部情报 2，外部情报 |
|analysis_time |datetime |YES |None  | 分析时间 |
|process_status |int(11) |YES |None  | 处理状态 |
|asset_system_info |varchar(200) |YES |None  | 资产系统信息 |
## asset
#### 描述: 资产--杨鹏
#### 字段总数: 34
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|instanceid |varchar(50) |YES |None  | 主机ID |
|ipv4 |varchar(32) |YES |None  |  |
|ipv6 |varchar(32) |YES |None  |  |
|vip |varchar(32) |YES |None  |  |
|internet_ip |varchar(32) |YES |None  | 公网ip |
|domain |varchar(128) |YES |None  |  |
|hostname |varchar(32) |YES |None  |  |
|os_system |varchar(200) |YES |None  | 操作系统 |
|os_distro |varchar(200) |YES |None  | 操作系统详细 |
|os_version |varchar(100) |YES |None  | 操作系统版本 |
|mac_addr |varchar(31) |YES |None  |  |
|businesses_id |varchar(50) |YES |None  | 业务系统id |
|businesses_name |varchar(32) |YES |None  | 业务系统 |
|asset_type_id |bigint(20) |YES |None  | 对应property_tree表里的资产类型的id |
|department_id |varchar(32) |YES |None  | 所属部门id |
|important_asset_type |bit(1) |YES |b'1'  | 是否重要资产 |
|virtual_host |bit(1) |YES |b'0'  | 是否虚拟主机 |
|owner_name |varchar(32) |YES |None  | 负责人 |
|vendor |varchar(32) |YES |None  | 设备厂商 |
|known_assets_type |bit(1) |YES |b'0'  | 是否已知资产 |
|physical_position |varchar(100) |YES |None  | 物理位置 |
|security_domain_id |bigint(20) |YES |None  | 对应于property_tree里的资产域id |
|riskscore |int(3) |YES |None  | riskscore |
|asset_value |varchar(20) |YES |None  | 资产价值 |
|purpose |text |YES |None  | 用途 |
|manufacturer |varchar(32) |YES |None  | 设备维护厂商 |
|maintainer_name |varchar(32) |YES |None  | 设备维护联系人 |
|maintainer_phone |varchar(16) |YES |None  | 设备维护联系人电话 |
|maintainer_mail |varchar(32) |YES |None  | 设备维护联系人邮箱 |
|remark |text |YES |None  | 设备维护备注说明 |
|update_date |datetime |YES |None  |  |
|regenerator |varchar(32) |YES |None  | 更新人 |
|assets_src_type |tinyint(1) |YES |1  | 资产来源 1:批量导入 2:人工添加 3:流量解析 4:日志解析 |
## asset_service
#### 描述: 资产服务表--杨鹏
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|asset_id |bigint(20) |YES |None  |  |
|port |int(11) |YES |None  | 端口号 |
|protocol |varchar(256) |YES |None  | 协议 |
|version |varchar(60) |YES |None  |  |
|update_date |datetime |YES |None  |  |
|regenerator |varchar(32) |YES |None  |  |
## cmdb_hosts
#### 描述: 国信cmdb资产表-单吉祥
#### 字段总数: 13
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|instanceid |varchar(50) |NO |  | id/主机id |
|ip |varchar(20) |YES |None  | 主机ip |
|hostname |varchar(100) |YES |None  | 主机名称 |
|os_system |varchar(20) |YES |None  | 操作系统 |
|os_distro |varchar(200) |YES |None  | 操作系统详细 |
|os_version |varchar(200) |YES |None  | 操作系统版本 |
|owner_name |varchar(100) |YES |None  | 负责人（所属人）包含编号,一个人的信息用“，”分割。编号和名称用“#”分割 |
|businesses_id |varchar(50) |YES |None  | 业务系统id |
|businesses_name |varchar(100) |YES |None  | 业务系统 |
|network_domain |varchar(100) |YES |None  | 网络域(DMZ域/非DMZ域) |
|asset_value |varchar(20) |YES |None  | 资产价值 |
|nettype |varchar(100) |YES |None  |  |
|hostnmae |varchar(255) |YES |None  |  |
## custom_threshold
#### 描述: 前端界面单值图表-阈值控制表-单吉祥
#### 字段总数: 3
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|ct_name |varchar(200) |YES |None  |  |
|ct_value |int(11) |NO |None  |  |
## da_component
#### 描述: 大盘组件表-许瑛
#### 字段总数: 20
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(50) |NO |None  |  |
|name |varchar(20) |NO |None  | 组件名称 |
|table_name |varchar(2000) |NO |None  | 表名 |
|expression |varchar(10000) |YES |None  |  |
|expression_json |varchar(5000) |YES |None  |  |
|time_flag |int(1) |NO |None  | 时间标志 1：无 2 ：固定时间 3：最近时间 |
|start_time |bigint(20) |YES |None  | 开始时间(毫秒) 时间标志为2的场合必须有值，其他场合必须为空。 |
|end_time |bigint(20) |YES |None  |  |
|time_interval |int(11) |YES |None  | 间隔 时间标志为3的场合必须有值，其他场合必须为空。 |
|time_unit |varchar(1) |YES |None  | 间隔单位 时间标志为3的场合必须有值，其他场合必须为空。 s:秒 m:分 h:时 d:天 w:周 M:月 |
|graph_type |varchar(20) |NO |None  | 图表的类型 |
|is_dsp_Border |int(1) |NO |None  | 是否显示边框 0：不显示 1：显示 |
|opacity |double |NO |None  | 透明度的值 |
|x_axis |varchar(1000) |YES |None  | 选择出的表示字段 |
|y_axis |varchar(1000) |YES |None  | 数据的分组内容 |
|setting |varchar(1000) |YES |None  | 每个图表的具体特殊设置 |
|create_time |timestamp |YES |CURRENT_TIMESTAMP  |  |
|update_time |timestamp |YES |CURRENT_TIMESTAMP  |  |
|create_user |varchar(50) |YES |None  |  |
|update_user |varchar(50) |YES |None  |  |
## da_component_ref
#### 描述: 大盘主表-许瑛
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(50) |NO |None  | 大盘ID或者组件组ID |
|cid |varchar(50) |NO |  |  |
|status |int(1) |YES |None  | 1-大盘与组件组的关系 2-组件组与组件的关系 3-大盘与组件的关系 |
|create_time |timestamp |NO |CURRENT_TIMESTAMP  |  |
|update_time |timestamp |NO |CURRENT_TIMESTAMP  |  |
|create_user |varchar(50) |YES |None  |  |
|update_user |varchar(50) |YES |None  |  |
## da_component_task_ref
#### 描述: 
#### 字段总数: 3
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|component_id |varchar(255) |NO |  |  |
|task_id |varchar(255) |NO |None  |  |
|selected |varchar(1) |YES |None  | 当前任务是否是组件被选中任务 0 非选中 1 选中 |
## da_dashboard
#### 描述: 大盘主表-许瑛
#### 字段总数: 17
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(50) |NO |None  | 主键 uuid |
|name |varchar(255) |YES |None  | 大盘名称 |
|back_flag |int(11) |YES |None  | 背景传值标识 ，flag=0：无背景，flag=1：设置backcolor，flag=2：设置background |
|back_color |varchar(100) |YES |None  | 背景颜色 |
|background |varchar(255) |YES |None  | 背景图片 |
|time_unit |varchar(50) |YES |None  | 间隔单位 时间标志为3的场合必须有值，其他场合必须为空。 s:秒 m:分 h:时 d:天 w:周 M:月 |
|start_time |bigint(20) |YES |None  | 	开始时间,单位：毫秒 |
|end_time |bigint(20) |YES |None  | 结束时间,单位：毫秒 |
|refresh |int(10) |YES |None  | 动作时间间隔，单位：秒（S） |
|status |int(10) |YES |1  |  |
|create_time |timestamp |NO |CURRENT_TIMESTAMP  |  |
|time_flag |int(10) |YES |None  | 时间标志 1：无 2 ：固定时间 3：最近时间 |
|time_interval |int(10) |YES |None  | 	间隔 时间标志为3的场合必须有值，其他场合必须为空。 |
|update_time |timestamp |NO |CURRENT_TIMESTAMP  |  |
|create_user |varchar(50) |YES |None  | 创建者 |
|update_user |varchar(50) |YES |None  | 修改者 |
|layout |text |YES |None  | 大盘布局 |
## da_datasource_join
#### 描述: 用来表示联动关系的方式，该表中最多只会有一条记录 - 许瑛
#### 字段总数: 2
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(20) |NO |None  |  |
|join_type |varchar(1) |YES |None  | 1 左侧 2 交集 3 右侧 |
## da_datasource_relation
#### 描述: 联动处理- 许瑛
#### 字段总数: 9
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(20) |NO |  |  |
|main_datasource_id |varchar(2000) |NO |None  |  |
|main_column_name |varchar(255) |NO |None  |  |
|sub_datasource_id |varchar(2000) |NO |None  |  |
|sub_column_name |varchar(255) |NO |None  |  |
|update_time |timestamp |YES |None  |  |
|update_user |varchar(255) |YES |None  |  |
|create_time |timestamp |YES |None  |  |
|create_user |varchar(255) |YES |None  |  |
## da_dictionary
#### 描述: 大盘字典信息表-许瑛
#### 字段总数: 8
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|item_id |varchar(10) |NO |None  | 选项编码 |
|dict_id |varchar(20) |NO |000  | 字典ID |
|dict_name |varchar(20) |NO |None  | 字典名称 |
|comment |varchar(200) |YES |None  | 备考 |
|create_user |varchar(32) |NO |None  | 创建者 |
|create_time |datetime |NO |None  | 创建时间 |
|update_user |varchar(32) |NO |None  | 更新者 |
|update_time |datetime |NO |None  | 更新时间 |
## da_group
#### 描述: 大盘组件组表-许瑛
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(50) |NO |None  |  |
|name |varchar(255) |YES |None  | 组件组名称 |
|status |int(1) |YES |1  |  |
|create_time |timestamp |YES |CURRENT_TIMESTAMP  |  |
|update_time |timestamp |YES |CURRENT_TIMESTAMP  |  |
|create_user |varchar(50) |YES |None  |  |
|update_user |varchar(50) |YES |None  |  |
## da_sankey_test
#### 描述: 
#### 字段总数: 5
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |0  |  |
|to_test |varchar(255) |YES |None  |  |
|from_test |varchar(255) |YES |None  |  |
|value |int(11) |YES |None  |  |
|create_time |bigint(11) |YES |None  |  |
## da_task
#### 描述: 
#### 字段总数: 15
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(255) |NO |  |  |
|task_name |varchar(255) |YES |None  | 任务名称 |
|task_time_flag |int(1) |YES |None  | 1 最近一天 2最近一周 3 最近一年 |
|start_time |bigint(20) |YES |None  | 任务的统计开始时间 |
|end_time |bigint(20) |YES |None  | 任务的统计结束时间 |
|y_axis |varchar(255) |YES |None  | Y轴信息 |
|x_axis |varchar(255) |YES |None  | X轴信息 |
|task_type |int(11) |YES |None  | 任务类型 1 趋势 |
|status |varchar(1) |YES |None  | 任务状态 1 暂停 2 执行中 3 完成 |
|progress |double |YES |None  | 进度 |
|result |varchar(255) |YES |None  | 该任务的执行结果存放路径 |
|update_user |varchar(255) |YES |None  |  |
|update_time |timestamp |YES |CURRENT_TIMESTAMP  |  |
|create_user |varchar(255) |YES |None  |  |
|create_time |timestamp |YES |CURRENT_TIMESTAMP  |  |
## da_tree_test
#### 描述: 
#### 字段总数: 5
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) unsigned |NO |None  |  |
|child_name |varchar(255) |YES |None  |  |
|parent_id |bigint(20) |YES |None  |  |
|value |int(11) |YES |None  |  |
|create_time |bigint(20) |YES |None  |  |
## da_trend_task_data
#### 描述: 
#### 字段总数: 3
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|task_id |varchar(50) |NO |0  |  |
|position_x |double |NO |0  |  |
|position_y |double |NO |0  |  |
## dns_result
#### 描述: dns任务结果--杨鹏
#### 字段总数: 6
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|domain |varchar(255) |NO |None  |  |
|version |int(11) |NO |None  |  |
|dns_ips |varchar(1000) |NO |None  | dns服务器地址，以逗号分隔 |
|update_date |datetime |YES |None  |  |
|regenerator |varchar(32) |YES |None  | 更新人 |
## etl_conf_dateformat
#### 描述: ETL create_time 时间转换格式预定义-李国浩
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) unsigned |NO |None  |  |
|date_format |varchar(255) |YES |None  |  |
|date_example |varchar(255) |YES |None  |  |
|locale |varchar(255) |YES |None  |  |
## etl_dict_define
#### 描述: ETL 动态补字典基础表-李国浩
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) unsigned |NO |None  |  |
|dict_name |varchar(255) |NO |  |  |
|dict_ch_name |varchar(1024) |NO |  |  |
|dict_schema |text |NO |None  |  |
## etl_global_field
#### 描述: ETL 提取器全局字段信息-李国浩
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) unsigned |NO |None  |  |
|field_name |varchar(255) |YES |None  |  |
|field_type |varchar(255) |YES |None  |  |
|field_ch_name |varchar(1024) |YES |None  |  |
## etl_job
#### 描述: ETL 任务总表-李国浩
#### 字段总数: 10
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|job_serial_number |varchar(255) |NO |  | 作业流水号 |
|kafka_broker_Addr |varchar(255) |YES |None  | kafka连接地址 |
|kafka_input_topic |varchar(255) |YES |None  | 输入topic |
|kafka_output_topic |varchar(255) |YES |None  | 输出topic |
|kafka_error_topic |varchar(255) |YES |None  | 错误pic |
|job_description |varchar(255) |YES |None  | 任务描述 |
|job_status |int(1) |YES |0  | 状态 -1:已删除, 0:禁用, 1:启用 |
|create_time |datetime |YES |None  | 创建时间 |
|update_time |datetime |YES |None  | 更新时间 |
## etl_node_info
#### 描述: ETL keeperlive 节点上报信息-李国浩
#### 字段总数: 6
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) unsigned |NO |None  |  |
|cluster_name |varchar(255) |YES |None  |  |
|component_type |varchar(255) |YES |None  |  |
|host_ip |varchar(64) |YES |None  |  |
|host_name |varchar(1024) |YES |None  |  |
|host_port |int(11) |YES |None  |  |
## etl_node_workers
#### 描述: ETL 采集器，解析器节点信息-李国浩
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) unsigned |NO |None  |  |
|worker_host_name |varchar(1024) |YES |None  |  |
|worker_ip |varchar(255) |YES |None  |  |
|worker_type |varchar(255) |YES |None  |  |
|activity |tinyint(4) |YES |None  |  |
|create_time |timestamp |YES |CURRENT_TIMESTAMP  |  |
|update_time |timestamp |YES |CURRENT_TIMESTAMP  |  |
## etl_rules
#### 描述: ETL 解析规则配置信息-李国浩
#### 字段总数: 10
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|job_serial_number |varchar(50) |YES |  | job流水号 |
|extract_id |int(11) |YES |None  | 提取器id |
|field_en_name |varchar(100) |YES |  | 英文名 |
|field_cn_name |varchar(200) |YES |  | 中文名 |
|field_type |varchar(100) |YES |  | 字段类型 |
|field_source |varchar(100) |YES |  | 字段来源 |
|field_value |varchar(100) |YES |  | 值 |
|rules |varchar(1024) |YES |  | 规则 |
|status |varchar(1) |YES |1  | 状态，备用 |
## etl_task_collect
#### 描述: ETL 采集器采集任务信息-李国浩
#### 字段总数: 6
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|job_serial_number |varchar(50) |YES |None  | job流水号 |
|collect_node_ips |varchar(1000) |YES |None  | 采集器节点ip,多个逗号分隔 |
|collect_src_type |int(2) |YES |None  | 采集源类别 |
|conf_content |varchar(3000) |YES |None  | 采集器配置内容，存储json内容 |
|state |int(2) |YES |None  | 任务状态 |
## etl_task_extract
#### 描述: ETL 提取器配置信息-李国浩
#### 字段总数: 8
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 主键id |
|job_serial_number |varchar(50) |YES |None  | 任务流水号 |
|extract_name |varchar(255) |YES |None  | 提取器名字 |
|field_name |varchar(1000) |YES |None  | 字段名列表，逗号分隔 |
|extract_data |text |YES |None  | 提取器数据 |
|extract_data_catalog |varchar(50) |YES |None  | 日志分类 |
|extract_data_sample |text |YES |None  | 提取数据示例 |
|extract_type |varchar(20) |YES |None  | 类型regex/char |
## etl_task_output
#### 描述: ETL 解析任务数据存储-李国浩
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|job_serial_number |varchar(50) |YES |None  | job流水号 |
|conf_content |varchar(3000) |YES |None  | 配置内容 |
|state |int(2) |YES |None  | 状态 |
## etl_task_output_status
#### 描述: ETL 备用，暂不用-李国浩
#### 字段总数: 8
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|task_output_id |int(11) |YES |None  | 输出任务id |
|status |int(2) |YES |None  | 任务状态 |
|message |varchar(200) |YES |None  | 消息 |
|node_ip |varchar(20) |YES |None  | 服务ip |
|service_name |varchar(50) |YES |None  | 服务名称 |
|create_time |timestamp |YES |CURRENT_TIMESTAMP  |  |
|update_time |timestamp |YES |CURRENT_TIMESTAMP  | 更新时间 |
## event_action
#### 描述: 事件动作表
#### 字段总数: 3
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 自增id |
|action |varchar(50) |YES |None  | 动作 |
|url |text |YES |None  | 动作跳转界面 |
## event_alarm
#### 描述: 事件告警表-牛虹
#### 字段总数: 80
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(50) |NO |  | 日志编号 |
|create_time |bigint(20) |YES |None  | 事件发生时间 |
|severity |tinytext |YES |None  | 威胁等级(0:低1:中2:高3:危急)_ |
|src_ip |varchar(40) |YES |None  | 源IP |
|src_port |varchar(10) |YES |None  | 源端口 |
|src_country |varchar(20) |YES |None  | 源ip所属国家 |
|src_province |varchar(20) |YES |None  | 源IP所属省 |
|src_city |varchar(20) |YES |None  | 源IP所属市 |
|src_asset_name |varchar(50) |YES |None  | 源设备名 |
|src_business_system |varchar(50) |YES |None  | 设备业务系统 |
|src_network_domain |varchar(50) |YES |None  | 设备网络域 |
|src_asset_value |varchar(20) |YES |None  | 资产价值 |
|protocol |varchar(20) |YES |None  | 协议 |
|dst_ip |varchar(40) |YES |None  | 目的IP |
|dst_port |varchar(10) |YES |None  | 目的端口 |
|dst_country |varchar(20) |YES |None  | 目的IP所属国家 |
|dst_province |varchar(20) |YES |None  | 目的IP所属省 |
|dst_city |varchar(20) |YES |None  | 目的IP所属市 |
|dst_asset_name |varchar(50) |YES |None  | 目标设备名 |
|dst_business_system |varchar(50) |YES |None  | 设备业务系统 |
|dst_network_domain |varchar(50) |YES |None  | 设备网络域 |
|dst_asset_value |varchar(20) |YES |None  | 资产价值 |
|username |varchar(50) |YES |None  | 用户名称 |
|event_name |varchar(50) |YES |None  | 事件名称 |
|event_behavior_type |varchar(50) |YES |None  | 事件行为分类 |
|event_technique_type |varchar(50) |YES |None  | 事件技术分类 |
|event_model_source |varchar(50) |YES |None  | 事件来源 |
|rule_name |varchar(50) |YES |None  | 规则名称 |
|event_nums |varchar(20) |YES |None  | 原始日志条数 |
|alarm_first_time |bigint(20) |YES |None  | 原始日志首次时间 |
|alarm_last_time |bigint(20) |YES |None  | 原始日志最后时间 |
|org_log_id |text |YES |None  | 原始日志的ID |
|risk_level |tinytext |YES |None  | 风险等级 |
|warn_status |tinytext |YES |None  | 告警状态告警状态（1:派单,2:待处理,3:处理中,4:处理完毕,5:关闭） |
|event_description |varchar(2000) |YES |None  | 事件详细描述 |
|dst_owner |varchar(50) |YES |None  | 目的资产责任人 |
|src_owner |varchar(50) |YES |None  | 来源资产责任人 |
|url |varchar(2000) |YES |None  | URL |
|domain |varchar(50) |YES |None  | 域名 |
|cookie |text |YES |None  |  |
|focus_point |varchar(50) |YES |None  | 关注点 |
|focus_content |varchar(2000) |YES |None  | 关注内容 |
|ticket_id |varchar(50) |YES |None  | 工单号 |
|process_time |varchar(20) |YES |None  | 处置时间 |
|process_type |varchar(20) |YES |None  | 处置方式(0:忽略告警,1:转工单,2:自动响应) |
|tag |varchar(1000) |YES |None  | 标签(多个标签ID按逗号分隔) |
|event_device_type |varchar(50) |YES |None  | 事件设备类型 |
|rule_type |varchar(50) |YES |None  | 策略类型(离线、近实时) |
|risk_type |tinytext |YES |None  | 风险类型 |
|risk_score |varchar(50) |YES |None  | 风险分值 |
|vendor |varchar(50) |YES |None  | 品牌/厂商 |
|system |varchar(50) |YES |None  | 系统名称 |
|event_channel |varchar(50) |YES |None  | 事件渠道 |
|openid |varchar(50) |YES |None  | Openid |
|device_fingerprint_id |varchar(50) |YES |None  | 设备ID |
|browser_fingerprint_id |varchar(50) |YES |None  | 浏览器指纹 |
|cookieid |varchar(50) |YES |None  | Cookieid |
|risk_explain |varchar(3000) |YES |None  | 风险说明 |
|model_name |varchar(200) |YES |None  | 模型名称 |
|event_type |varchar(500) |YES |None  | 事件分类 |
|intelligence_id |varchar(50) |YES |None  | 情报ID |
|intelligence_type |varchar(50) |YES |None  | 情报类型 |
|internal_event |tinytext |YES |None  | 是否内部事件 |
|is_read |tinytext |YES |None  | 已读/未读(1:已读,2:未读) |
|ddos_att_type |varchar(50) |YES |None  | DDOS攻击类型 |
|ddos_total_flow |bigint(20) |YES |None  | DDOS攻击流量总值 |
|ddos_peak_flow |bigint(20) |YES |None  | DDOS攻击流量峰值 |
|biz_event_type |varchar(50) |YES |None  | 业务异常流量事件类型 |
|biz_up_flow |bigint(20) |YES |None  | 业务异常上行流量 |
|biz_down_flow |bigint(20) |YES |None  | 业务异常下行流量 |
|biz_now_flow |bigint(20) |YES |None  | 业务异常当前流量 |
|biz_now_base_flow |bigint(20) |YES |None  | 业务异常当前流量基线值 |
|biz_total_base_flow |bigint(20) |YES |None  | 业务异常总流量基线值 |
|eqpt_asset_type |varchar(300) |YES |None  | 设备资产类型 |
|src_asset_type |varchar(300) |YES |None  | 源地址资产类型 |
|dst_asset_type |varchar(300) |YES |None  | 目标地址资产类型 |
|aggregation_count |bigint(20) |YES |None  |  |
|src_asset_dept |varchar(50) |YES |None  | 来源IP地址资产所属部门名称 |
|dst_asset_dept |varchar(50) |YES |None  | 目的IP地址资产所属部门名称 |
|eqpt_asset_dept |varchar(50) |YES |None  | 设备IP地址资产所属部门名称 |
## event_disposal
#### 描述: 事件处置
#### 字段总数: 3
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 自增id |
|disposal_name |varchar(150) |YES |None  | 处置名称 |
|operation_field |varchar(150) |YES |None  | 操作字段 |
## event_field
#### 描述: 
#### 字段总数: 2
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 自增id |
|field |varchar(50) |YES |None  | 字段名称 |
## event_field_action
#### 描述: 
#### 字段总数: 2
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|field_id |int(11) |NO |None  |  |
|action_id |int(11) |NO |None  |  |
## event_investigation_task
#### 描述: 事件调查任务-杨祎
#### 字段总数: 8
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|task_id |int(11) |NO |None  | 事件调查任务自增id |
|task_name |varchar(250) |YES |None  | 事件调查任务名称 |
|task_describe |text |YES |None  | 事件调查任务描述 |
|operation_time |varchar(50) |YES |None  | 事件调查任务操作时间 |
|create_user |varchar(250) |YES |None  | 事件调查任务创建用户 |
|task_status |varchar(11) |YES |None  | 事件调查任务状态1开启2关闭 |
|create_time |varchar(50) |YES |None  | 创建时间 |
|new_task |tinyint(1) |YES |1  | 是否新建 默认true |
## event_investigation_users_middle
#### 描述: 事件调查任务分享用户中间表-杨祎
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 自增id |
|task_id |int(11) |YES |None  | 任务id |
|user_id |int(11) |YES |None  | 被分享用户id |
|user_name |varchar(255) |YES |None  | 被分享用户姓名 |
## event_tag
#### 描述: 事件标签表-杨祎
#### 字段总数: 2
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|tag_name |varchar(150) |NO |  | 标签名称 |
|tag_score |bigint(20) |YES |0  | 标签打分 |
## event_tag_middle
#### 描述: 
#### 字段总数: 2
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|event_id |varchar(50) |NO |None  |  |
|tag_name |varchar(150) |NO |  |  |
## event_task_relation
#### 描述: 事件调查任务关联细表-杨祎
#### 字段总数: 27
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|relation_id |int(11) |NO |None  | 任务关联表自增id |
|remark |text |YES |None  | 备注 |
|log_count |int(11) |YES |None  | 日志条数 |
|log_query_param |text |YES |None  | 日志查询条件 |
|upload_file_name |varchar(250) |YES |None  | 附件名称 |
|upload_file_size |varchar(250) |YES |None  | 附件大小 |
|download_file_url |time |YES |None  | 附件下载链接 |
|event_name |varchar(255) |YES |None  | 事件名称 |
|event_src_ip |varchar(150) |YES |None  | 事件源ip |
|event_dst_ip |varchar(150) |YES |None  | 事件目的ip |
|event_focus_content |varchar(250) |YES |None  | 事件关注内容 |
|event_severity |varchar(250) |YES |None  | 事件危险级别 |
|operation_time |varchar(50) |YES |None  | 加入任务时间 |
|log_start_time |varchar(50) |YES |None  | 日志开始时间 |
|log_end_time |varchar(50) |YES |None  | 日志结束时间 |
|event_focus_point |varchar(250) |YES |None  | 事件关注点 |
|relation_type |varchar(250) |YES |None  | 任务关联类型 |
|trace_task_name |varchar(500) |YES |None  | 溯源任务名称 |
|trace_condition |varchar(500) |YES |None  | 溯源任务条件/源信息 |
|trace_task_category |int(11) |YES |None  | 溯源任务分类 |
|trace_start_time |varchar(50) |YES |None  | 溯源开始时间 |
|trace_end_time |varchar(50) |YES |None  | 溯源结束时间 |
|trace_user_name |varchar(50) |YES |None  | 溯源创建人 |
|trace_task_desc |text |YES |None  | 溯源任务描述 |
|trace_status |int(11) |YES |None  | 溯源0未运行 1运行中 2已完成 |
|event_id |varchar(50) |YES |None  | 事件id |
|task_id |int(11) |YES |None  |  |
## excel_data
#### 描述: 
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|excel_id |int(11) |NO |None  |  |
|data_code |varchar(255) |YES |None  |  |
|excel_date |varchar(255) |YES |None  |  |
|excel_name |varchar(255) |YES |None  |  |
## excel_file
#### 描述: 
#### 字段总数: 5
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|excel_id |int(11) |NO |None  |  |
|excel_path |varchar(255) |YES |None  |  |
|excel_name |varchar(255) |YES |None  |  |
|table_id |varchar(255) |YES |None  |  |
|job_id |varchar(255) |YES |None  |  |
## excel_manager
#### 描述: 
#### 字段总数: 2
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|table_id |int(11) |NO |None  |  |
|table_name |varchar(255) |YES |None  |  |
## external_asset_task_detail
#### 描述: 外部资产扫描任务详细--杨鹏
#### 字段总数: 11
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|domain |varchar(255) |NO |None  | 域名 |
|call_back_keys |varchar(255) |YES |None  | 回调服务的key列表，以逗号分隔 |
|version |int(11) |NO |0  | 版本号，任务启动时进行+1更新 |
|status |tinyint(4) |NO |0  | 0:等待执行，1:执行中 |
|update_date |datetime |YES |None  |  |
|regenerator |varchar(32) |YES |None  | 更新人 |
|name |varchar(255) |YES |None  | 外部资产名称 |
|ip_address |varchar(15) |YES |None  | ip地址 |
|record_no |varchar(32) |YES |None  | 备案号 |
|is_external |tinyint(1) |YES |None  | 是否为外部资产 |
|is_info |tinyint(1) |YES |None  | 是否为情报 |
## external_asset_task_info
#### 描述: 外部资产扫描任务信息--杨鹏
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|task_type |tinyint(4) |NO |1  | 1:whois 2:子域名 3:DNS解析 |
|run_time |time |NO |00:00:00  | 执行时间 |
|run_type |tinyint(4) |NO |1  | 1:每天，2:每周，3:每月，4:每年 |
|run_days |varchar(1000) |YES |None  | 每天：NULL，每周：周一--周日的数字,每月:1-31,每年：日期列表（逗号分隔） |
|parms |varchar(1000) |YES |None  | 其他参数信息（DNS解析任务的DNS服务器） |
|update_date |datetime |YES |None  |  |
|regenerator |varchar(32) |YES |None  | 更新人 |
## festival
#### 描述: 趋势分析-节假日映射表-孙志收
#### 字段总数: 2
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|festival_day |varchar(8) |NO |None  |  |
|festival_comment |varchar(255) |YES |None  |  |
## fs_search_dictionary
#### 描述: 
#### 字段总数: 12
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(100) |NO |None  | 自增id |
|log_type |varchar(200) |NO |None  | 字段组对应日志类型 |
|log_type_name |varchar(100) |NO |None  | 字段组设备日志分类名称 |
|log_group_name |varchar(100) |NO |None  | 字段组名称 |
|log_column |varchar(100) |NO |None  | 列名 |
|log_column_name |varchar(200) |YES |None  | 列名对应名称 |
|log_column_type |varchar(10) |YES |String  | 字段类型 |
|is_check |int(2) |NO |0  | 是否被选为默认列（0：否，1：是） |
|create_user |varchar(50) |YES |None  | 创建者 |
|create_time |datetime |YES |None  |  |
|update_user |varchar(50) |YES |None  | 更新者 |
|update_time |datetime |YES |None  |  |
## fs_search_params
#### 描述: 全文检索-保存历史搜索-单吉祥
#### 字段总数: 15
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(100) |NO |None  | id |
|name |varchar(100) |NO |None  | 查询条件名称 |
|time_flag |int(2) unsigned |NO |1  | 时间标识（1：无，2：固定时间，3：相对时间） |
|start_time |varchar(20) |YES |None  | 查询起始时间 |
|end_time |varchar(20) |YES |None  | 查询结束时间 |
|time_interval |int(10) |YES |None  | 时间间隔 |
|time_unit |varchar(5) |YES |None  | 间隔单位（s:秒，m:分，h:小时，d:天，w:周，M：周） |
|param_indexs |varchar(500) |YES |None  | 查询索引，多个索引用“，”分割 |
|param_columns |varchar(500) |YES |None  | 查询列明，多列用“，”分割 |
|like_param |varchar(500) |YES |None  | 正则匹配，或模糊条件 |
|sort_column |varchar(20) |YES |None  | 所选排序列 |
|sort_flag |varchar(5) |YES |None  | 排序规则（正序：asc，倒序：desc） |
|user_name |varchar(500) |NO |None  | 条件可见的用户（多用户用逗好“，”隔开） |
|comment |varchar(500) |YES |None  | 注释说明 |
|search_type |varchar(2) |YES |None  |  |
## gamessage
#### 描述: 
#### 字段总数: 1
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
## gamessage_bean
#### 描述: 
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|mail_receiver |varchar(255) |YES |None  |  |
|text |varchar(255) |YES |None  |  |
|title |varchar(255) |YES |None  |  |
## ga_access_authority
#### 描述: 角色访问权限表-单吉祥
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|role_id |int(12) |NO |None  | 角色ID |
|node_list |text |NO |None  | 可访问菜单节点信息列表 |
|auth_list |text |NO |None  | 菜单权限列表 |
|create_user |varchar(32) |NO |None  | 创建者 |
|create_time |datetime |NO |None  | 创建时间 |
|update_user |varchar(32) |NO |None  | 更新者 |
|update_time |datetime |NO |None  | 更新时间 |
## ga_access_event_log
#### 描述: 系统访问日志表-单吉祥
#### 字段总数: 12
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|no |varchar(32) |NO |None  | 序号 |
|create_time |datetime |NO |None  | 创建时间 |
|log_type |char(1) |NO |None  | 日志类型（1：信息，2：告警，3：错误） |
|user_id |varchar(32) |YES |None  | 用户ID |
|user_name |varchar(32) |YES |None  | 用户名称 |
|org_name |varchar(32) |YES |None  | 组织机构名称 |
|role_name |varchar(32) |YES |None  | 角色名称 |
|ip |varchar(15) |YES |None  | IP地址 |
|url |varchar(300) |YES |None  | 访问URL |
|oper_target |varchar(100) |YES |None  | 操作对象（页面名称） |
|oper_type |varchar(50) |YES |None  | 操作类型（增加，删除，修改，下载，查询，登录，退出等） |
|oper_result |varchar(50) |YES |None  | 操作结果（登录成功，修改失败等） |
## ga_data_dictionary
#### 描述: 字典信息表-单吉祥
#### 字段总数: 8
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|item_id |varchar(10) |NO |None  | 选项编码 |
|dict_id |varchar(50) |NO |000  | 字典ID |
|dict_name |varchar(50) |NO |None  | 字典名称 |
|comment |varchar(200) |YES |None  | 备注 |
|create_user |varchar(32) |NO |None  | 创建者 |
|create_time |datetime |NO |None  | 创建时间 |
|update_user |varchar(32) |NO |None  | 更新者 |
|update_time |datetime |NO |None  | 更新时间 |
## ga_group
#### 描述: 用户组信息表-单吉祥
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|group_id |int(4) |NO |None  | 用户组ID |
|group_name |varchar(20) |NO |None  | 用户组名称 |
|comment |varchar(50) |YES |None  | 备考 |
|create_user |varchar(32) |NO |None  | 创建者 |
|create_time |datetime |NO |None  | 创建时间 |
|update_user |varchar(32) |NO |None  | 更新者 |
|update_time |datetime |NO |None  | 更新时间 |
## ga_knowledge_info
#### 描述: 安全运维 - 知识库管理表 - 许瑛
#### 字段总数: 19
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|knowledge_id |int(11) |NO |None  | 主键自增id |
|knowledge_name |varchar(100) |YES |None  | 知识库名称 |
|event_name |varchar(100) |YES |None  | 事件名称 |
|event_type |tinyint(2) |YES |None  | 类型 |
|event_level |tinyint(1) |YES |None  | 级别 |
|event_description |text |YES |None  | 描述 |
|knowledge_tag |varchar(255) |YES |None  | 标签 |
|disposal_suggestion |text |YES |None  | 处置建议 |
|disposal_suggestion_rich |text |YES |None  |  |
|effect_system |text |YES |None  | 影响系统 |
|effect_system_rich |text |YES |None  |  |
|knowledge_ref |text |YES |None  | 相关引用 |
|knowledge_ref_rich |text |YES |None  |  |
|cve_id |varchar(32) |YES |None  | CVE编码 |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新日期 |
|del_flag |tinyint(1) |YES |None  | 删除标识 |
## ga_menu
#### 描述: 菜单信息表-单吉祥
#### 字段总数: 11
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|menu_id |varchar(5) |NO |None  | 菜单ID |
|menu_name |varchar(50) |NO |None  | 菜单名称 |
|icon |varchar(50) |YES |None  | 展示图标 |
|router_path |varchar(100) |NO |None  | 点击后请求URL |
|normal |varchar(150) |YES |None  | 备考 |
|parent_menu_id |varchar(32) |YES |None  | 父菜单ID |
|disp_flag |char(1) |NO |0  | 菜单显示标识（0：显示，1：不显示） |
|create_user |varchar(32) |NO |None  | 创建者 |
|create_time |datetime |NO |None  | 创建时间 |
|update_user |varchar(32) |NO |None  | 更新者 |
|update_time |datetime |NO |None  | 更新时间 |
## ga_messages
#### 描述: 站内消息/邮件提醒表-牛虹
#### 字段总数: 9
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(50) |NO |None  | 消息ID |
|title |varchar(255) |YES |None  | 标题/邮件主题 |
|text |text |YES |None  | 内容/邮件正文 |
|mail_receiver |varchar(50) |YES |None  | 邮件接收人(邮件地址) |
|status |varchar(2) |YES |None  | 已读1/未读0(站内消息已读未读,如果有需求指定人员,需分细表) |
|send_type |varchar(2) |YES |None  | 发送源: 1规则引擎/2态势预警 |
|message_type |varchar(2) |YES |None  | 消息类型:1站内消息/2邮件消息/3站内和邮件 |
|send_time |datetime |YES |None  | 发送日期时间 |
|user_id |varchar(50) |YES |None  | 站内信指定某人(需确认是否有此需求) |
## ga_page_oper
#### 描述: 用户操作信息表-单吉祥
#### 字段总数: 8
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|url |varchar(255) |NO |None  | 操作URL |
|menu_id |varchar(20) |YES |None  |  |
|oper_type |varchar(32) |NO |None  | 操作类型名称 |
|oper_target |varchar(32) |NO |None  | 操作对象 |
|create_user |varchar(32) |NO |None  | 创建者 |
|create_time |datetime |NO |None  | 创建时间 |
|update_user |varchar(32) |NO |None  | 更新者 |
|update_time |datetime |NO |None  | 更新时间 |
## ga_pwd_policy
#### 描述: 用户策略表-单吉祥
#### 字段总数: 8
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|no |int(4) |NO |None  | 序号 |
|pwd_period |int(2) |NO |3  | 密码有效期限 |
|fail_count |int(1) |NO |5  | 失败登录次数 |
|lock_times |int(2) |NO |5  | 自动解锁时间 |
|create_user |varchar(32) |NO |None  | 创建者 |
|create_time |datetime |NO |None  | 创建时间 |
|update_user |varchar(32) |NO |None  | 更新者 |
|update_time |datetime |NO |None  | 更新时间 |
## ga_role
#### 描述: 角色信息表-单吉祥
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|role_id |int(4) |NO |None  | 用户角色ID |
|role_name |varchar(20) |NO |None  | 角色名称 |
|comment |varchar(50) |YES |None  | 备考 |
|create_user |varchar(32) |NO |None  | 创建者 |
|create_time |datetime |NO |None  | 创建时间 |
|update_user |varchar(32) |NO |None  | 更新者 |
|update_time |datetime |NO |None  | 更新时间 |
## ga_user
#### 描述: 用户信息表-单吉祥
#### 字段总数: 22
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|no |int(4) |NO |None  | 用户ID |
|role_id |int(4) |NO |None  | 用户角色ID |
|group_id |int(4) |NO |None  | 用户组ID |
|user_name |varchar(10) |NO |None  | 用户名称 |
|real_name |varchar(10) |NO |None  | 员工姓名 |
|department |varchar(20) |YES |None  | 所属部门 |
|director |varchar(10) |YES |None  | 直属领导 |
|sex |char(1) |YES |None  | 员工性别（0：男，1：女） |
|email |varchar(30) |YES |None  | 邮箱 |
|telphone |varchar(11) |YES |None  | 联系电话 |
|status |char(1) |NO |0  | 状态（0：正常，1：锁定） |
|user_pwd |varchar(255) |NO |None  | 用户密码 |
|user_pwd_old |varchar(255) |YES |None  | 用户旧密码 |
|user_pwd_salt |varchar(30) |NO |None  | 用户密码加盐 |
|period_from |date |NO |None  | 账号启用开始时间 |
|period_to |date |NO |None  | 账号启用结束时间 |
|lock_time |datetime |YES |None  | 账号锁定时间 |
|fail_count |int(1) |NO |0  | 登录失败次数 |
|create_user |varchar(32) |NO |None  | 创建者 |
|create_time |datetime |NO |None  | 创建时间 |
|update_user |varchar(32) |NO |None  | 更新者 |
|update_time |datetime |NO |None  | 更新时间 |
## ga_user_messages
#### 描述: 用户信息表-单吉祥
#### 字段总数: 11
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|no |int(4) |NO |None  | 序号 |
|send_date |date |NO |None  | 发送日期 |
|message_id |varchar(10) |NO |None  | 发送人 |
|send_user |varchar(10) |NO |None  | 发送人 |
|receive_user |varchar(10) |NO |None  | 接收人 |
|status |char(1) |NO |1  | 查看状态（1：未读，2：已读） |
|message |varchar(255) |NO |None  | 消息内容 |
|create_user |varchar(32) |NO |None  | 创建者 |
|create_time |datetime |NO |None  | 创建时间 |
|update_user |varchar(32) |NO |None  | 更新者 |
|update_time |datetime |NO |None  | 更新时间 |
## health_cofiguration_data
#### 描述: 数据质量监控配置表-秦霄飞
#### 字段总数: 8
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(32) |NO |None  | 数据质量监控配置 |
|job |varchar(64) |YES |None  |  |
|data_operator |tinyint(1) |YES |None  | 1：大于，2：大于等于，3：等于，4：小于，5：小于等于 |
|data_val |varchar(8) |YES |None  |  |
|data_flg |tinyint(1) |YES |None  | 0：不监控，1：监控 |
|show_flg |tinyint(1) |YES |None  | 0：关（不显示）1：开（显示） |
|create_user |varchar(64) |YES |None  |  |
|create_time |datetime |YES |None  |  |
## health_cofiguration_host
#### 描述: 服务器监控配置表-秦霄飞
#### 字段总数: 17
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(32) |NO |None  | 服务器监控配置表 |
|ip |varchar(15) |YES |None  |  |
|cpu_operator |tinyint(1) |YES |None  | 1:大于,2:大于等于,3:等于,4:小于,5:小于等于 |
|cpu_val |varchar(8) |YES |None  |  |
|cpu_flg |tinyint(1) |YES |None  | 0:不监控,1:监控 |
|mem_operator |tinyint(1) |YES |None  | 1:大于,2:大于等于,3:等于,4:小于,5:小于等于 |
|mem_val |varchar(8) |YES |None  |  |
|mem_flg |tinyint(1) |YES |None  | 0:不监控,1:监控 |
|disk_operator |tinyint(1) |YES |None  | 1:大于,2:大于等于,3:等于,4:小于,5:小于等于 |
|disk_val |varchar(8) |YES |None  |  |
|disk_flg |tinyint(1) |YES |None  | 0:不监控,1:监控 |
|network_operator |tinyint(1) |YES |None  | 1:大于,2:大于等于,3:等于,4:小于,5:小于等于 |
|network_val |varchar(64) |YES |None  |  |
|network_flg |tinyint(4) |YES |None  | 0:不监控,1:监控 |
|show_flg |tinyint(1) |YES |None  | 0:关（不显示）,1:开（显示) |
|create_user |varchar(64) |YES |None  |  |
|create_time |datetime |YES |None  |  |
## health_cofiguration_module
#### 描述: 平台组件监控配置表-秦霄飞
#### 字段总数: 13
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(32) |NO |None  | 服务器监控配置表 |
|module |varchar(32) |YES |None  |  |
|ip |text |YES |None  |  |
|cpu_operator |tinyint(1) |YES |None  | 1:大于,2:大于等于,3:等于,4:小于,5:小于等于 |
|cpu_val |varchar(8) |YES |None  |  |
|cpu_flg |tinyint(1) |YES |None  | 0:不监控,1:监控 |
|mem_operator |tinyint(1) |YES |None  | 1:大于,2:大于等于,3:等于,4:小于,5:小于等于 |
|mem_val |varchar(8) |YES |None  |  |
|mem_flg |tinyint(1) |YES |None  | 0:不监控,1:监控 |
|process_flg |tinyint(1) |YES |None  | 0:不监控,1:监控 |
|show_flg |tinyint(1) |YES |None  | 0:关（不显示）,1:开（显示) |
|create_user |varchar(64) |YES |None  |  |
|create_time |datetime |YES |None  |  |
## index_setting
#### 描述: 
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|uid |int(4) |NO |None  | 主键id |
|username |varchar(50) |NO |None  | 用户名 |
|layout |varchar(10000) |YES |None  |  |
|visible |varchar(10000) |YES |None  |  |
## job_task
#### 描述: 
#### 字段总数: 12
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|job_id |int(11) |NO |None  |  |
|job_day |varchar(255) |YES |None  |  |
|job_dsc |varchar(255) |YES |None  |  |
|job_cycle |varchar(255) |YES |None  |  |
|job_cycle_time |varchar(255) |YES |None  |  |
|job_frequency |varchar(255) |YES |None  |  |
|job_month |varchar(255) |YES |None  |  |
|job_name |varchar(255) |YES |None  |  |
|job_output_type |varchar(255) |YES |None  |  |
|job_start_time |varchar(255) |YES |None  |  |
|job_table_type |varchar(255) |YES |None  |  |
|job_week |varchar(255) |YES |None  |  |
## md_page_white_list
#### 描述: 
#### 字段总数: 8
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(12) |NO |None  | id |
|model_type |char(2) |YES |None  | 模型分类（1代表单页面模型，2代表单用户模型） |
|businesses_id |varchar(100) |YES |None  | 业务系统（与业务系统表对应） |
|white_url |varchar(512) |YES |None  | url白名单（单页面模型下model_type为1，存储某一具体业务系统下的白名单URL。） |
|white_ip |varchar(64) |YES |None  | IP白名单（单用户模型下model_type为2，存储某一具体业务系统下的白名单IP。若model_type值为1，此字段为空） |
|white_ip_describe |varchar(2048) |YES |None  | IP白名单描述（单用户模型下model_type为2，白名单IP描述信息。若model_type值为1，此字段为空） |
|state |char(2) |NO |0  | 白名单状态（1为已加白，0为未加白） |
|operation |char(2) |NO |0  | 操作（界面有两个按钮：“加白”、“去除”。点击“加白”按钮将state值置为1，点击“去除”按钮state值置为0。模型在进行算法算分时，读取相应业务系统相应模型的白名单列表，白名单不计算分值） |
## message_notice
#### 描述: 消息通知表
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|channel_id |varchar(250) |YES |None  | channel id |
|user_id |int(11) |YES |None  | 用户id |
|user_name |varchar(250) |YES |None  | 用户名 |
## model_monitoring
#### 描述: Spark模型名单表-陆建彬
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(12) |NO |None  | 主键 |
|app_business |varchar(100) |YES |None  | 业务系统名 |
|domain_name |varchar(512) |NO |None  | 域名 |
|model_type |int(2) |NO |None  | 模型类型, 1:单页面, 2:单用户 |
|model_status |int(2) |NO |None  | 模型运行状态, -1:运行异常 , 0:未运行, 1:运行中, 2:运行完成 |
|start_time |datetime |YES |None  | 模型运行开始时间 |
|end_time |datetime |YES |None  | 模型运行结束时间 |
## model_monitor_conf
#### 描述: Spark模型配置表-陆建彬
#### 字段总数: 5
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(12) |NO |None  | 主键 |
|domain_name |varchar(512) |NO |None  | 域名 |
|app_business |varchar(100) |YES |None  | 业务系统 |
|model_type |int(2) |NO |None  | 模型类型, 1:单页面, 2单用户 |
|status |int(2) |NO |0  | 状态, 0:禁用, 1:启用 |
## nhapis
#### 描述: 
#### 字段总数: 1
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
## nh_test
#### 描述: 
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|name |varchar(255) |YES |None  |  |
|age |int(11) |YES |None  |  |
|address |varchar(255) |YES |None  |  |
## property_tree
#### 描述: 树形属性--杨鹏
#### 字段总数: 6
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|type |tinyint(4) |NO |1  | 1:资产域 2:资产类型 |
|name |varchar(255) |NO |None  | 节点名称 |
|parent_id |bigint(20) |YES |0  | 父节点名称（根节点为空） |
|update_date |datetime |YES |None  |  |
|regenerator |varchar(32) |YES |None  | 更新人 |
## ss_date_cache
#### 描述: 
#### 字段总数: 3
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|no |bigint(20) |NO |None  |  |
|id |varchar(255) |YES |None  |  |
|import_time_ymd |varchar(255) |YES |None  |  |
## ss_scene_param
#### 描述: 
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|detect_id |varchar(255) |NO |None  |  |
|create_time |datetime |YES |None  |  |
|create_user |varchar(255) |YES |None  |  |
|detect_name |varchar(255) |YES |None  |  |
|param |varchar(255) |YES |None  |  |
|update_time |datetime |YES |None  |  |
|update_user |varchar(255) |YES |None  |  |
## subdomain_result
#### 描述: 子域名任务--杨鹏
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|domain |varchar(255) |YES |None  |  |
|sub_domain |varchar(255) |NO |None  |  |
|alive |tinyint(1) |NO |0  | 是否存活 0:否，1：是 |
|version |int(11) |NO |None  |  |
|update_date |datetime |YES |None  |  |
|regenerator |varchar(32) |YES |None  | 更新人 |
## system_keyword
#### 描述: 
#### 字段总数: 5
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) unsigned |NO |None  |  |
|module_id |varchar(255) |YES |None  | 模块标志 |
|keyword |varchar(255) |YES |None  | 关键字内容 |
|search_cnt |int(11) |YES |None  | 查询次数 |
|update_user |varchar(255) |YES |None  | 更新者 |
## sys_connectiontest
#### 描述: 
#### 字段总数: 1
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|a |char(1) |YES |None  |  |
## ta_eqpt_patch
#### 描述: 威胁分析-补丁漏洞表-单吉祥
#### 字段总数: 32
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(50) |NO |None  | id同esid相同 |
|collect_ip |varchar(20) |YES |None  | 采集IP-日志采集机IP |
|vendor |varchar(20) |YES |None  | 厂商-设备所属厂商 |
|eqpt_ip |varchar(20) |YES |None  | 设备IP-日志设备IP |
|eqpt_name |varchar(20) |YES |None  | 设备名-日志来源设备的资产名 |
|eqpt_business_system |varchar(20) |YES |None  | 设备业务系统-日志来源设备所属的业务系统 |
|eqpt_network_domain |varchar(20) |YES |None  | 设备网络域-日志来源设备所属的网络域 |
|eqpt_asset_value |varchar(5) |YES |None  | 资产价值-日志来源设备的资产价值 |
|create_time |varchar(20) |YES |None  | 日志发生时间-日志发生的时间 转换成到毫秒级的长整型数字字符串 |
|dst_ip |varchar(20) |YES |None  | 客户端主机IP-客户端主机IP |
|dst_country |varchar(20) |YES |None  | 客户端ip所属国家-日志的客户端地址所属国家 |
|dst_province |varchar(20) |YES |None  | 客户端P所属省-客户端地址所属省份 |
|dst_city |varchar(20) |YES |None  | 客户端P所属市-客户端地址所属市区 |
|dst_asset_name |varchar(20) |YES |None  | 客户端设备名-客户端地址设备的资产名 |
|dst_business_system |varchar(20) |YES |None  | 客户端设备业务系统-客户端地址设备所属的业务系统 |
|dst_network_domain |varchar(20) |YES |None  | 客户端设备网络域-客户端地址设备所属的网络域 |
|dst_asset_value |varchar(5) |YES |None  | 客户端资产价值-客户端设备的资产价值 |
|patch_name |varchar(255) |YES |None  | 补丁名称-补丁名称（补丁编号检索时需要使用like条件检索补丁名称字段） |
|patch_description |varchar(500) |YES |None  | 补丁描述-补丁详细描述 |
|solution |varchar(200) |YES |None  | 补丁用途-补丁解决问题 |
|fit_asset |varchar(20) |YES |None  | 适用资产类型-补丁适用资源 |
|severity |varchar(5) |YES |None  | 补丁级别-补丁级别 |
|status |varchar(50) |YES |None  | 补丁状态-已安装、未安装、安装失败 |
|eqpt_device_type |varchar(50) |YES |None  | 日志源分类-日志分类，日志来源设备分类 |
|event_category_object |varchar(50) |YES |None  | 日志目标对象分类-日志目标对象分类 |
|event_category_behavior |varchar(50) |YES |None  | 日志行为分类-日志行为分类 |
|event_category_technique |varchar(50) |YES |None  | 日志技术分类-日志技术分类 |
|action_result |varchar(20) |YES |None  | 行为结果-任务操作结果，如成功、失败、未知。 |
|dst_owner |varchar(20) |YES |None  | 目的资产责任人-目的资产责任人 |
|eqpt_owner |varchar(20) |YES |None  | 日志源资产责任人-日志源资产责任人 |
|collect_time |varchar(20) |YES |None  | 日志采集时间-日志采集时间 转换成到毫秒级的长整型数字字符串 |
|occurrence |int(10) unsigned zerofill |YES |0000000000  | 数量 |
## tb_analyzer
#### 描述: 关联规则表-唐笑于
#### 字段总数: 17
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 主键 |
|name |varchar(50) |NO |None  | 策略名称 |
|number |varchar(50) |NO |None  | 编号 |
|category_id |int(11) |YES |None  | 策略分类 |
|status |tinyint(1) |YES |0  | 状态 |
|event_name |varchar(255) |YES |None  | 事件名称 |
|severity |varchar(6) |YES |None  | 事件级别 |
|event_action_type |varchar(50) |YES |None  | 事件行为分类 |
|event_technique_type |varchar(50) |YES |None  | 事件技术分类 |
|description |varchar(200) |YES |None  | 描述 |
|src_ip |int(1) |YES |None  |  |
|dst_ip |int(1) |YES |None  |  |
|create_user |int(11) |YES |None  | 创建人 |
|create_time |datetime |YES |None  | 创建时间 |
|update_user |int(11) |YES |None  | 更新人 |
|update_time |datetime |YES |None  | 更新时间 |
|eqpt_device_type |varchar(50) |NO |None  |  |
## tb_analyzer_category
#### 描述: 关联规则分类-唐笑于
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(10) |NO |None  | 主键 |
|name |varchar(50) |NO |None  | 分类名称 |
|description |varchar(200) |YES |None  | 描述 |
|create_user |int(11) |YES |None  | 创建人 |
|create_time |datetime |YES |None  | 创建时间 |
|update_user |int(11) |YES |None  | 修改人 |
|update_time |datetime |YES |None  | 修改时间 |
## tb_analyzer_condition
#### 描述: 规则条件表-唐笑于
#### 字段总数: 5
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|analyzer_id |int(11) |NO |None  |  |
|filter_id |int(11) |NO |None  |  |
|count |int(4) |NO |1  |  |
|timewindow |int(4) |NO |None  | 单位 秒 |
## tb_analyzer_desc
#### 描述: 关联事件描述表-唐笑于
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|analyzer_id |int(11) |YES |None  |  |
|analyzer_field |varchar(20) |YES |None  |  |
|filter_id |int(11) |YES |None  |  |
|filter_field |varchar(20) |YES |None  |  |
|filter_text_front |varchar(50) |YES |None  |  |
|filter_text_end |varchar(50) |YES |None  |  |
## tb_analyzer_group
#### 描述: 关联规则归并表-唐笑于
#### 字段总数: 5
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|type |int(1) |NO |0  | 0相同 1不同 |
|analyzer_id |int(11) |NO |None  |  |
|filter_id |int(11) |NO |None  |  |
|field |varchar(20) |NO |None  |  |
## tb_analyzer_join
#### 描述: 关联规则条件关联表-唐笑于
#### 字段总数: 10
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|analyzer_id |int(11) |NO |0  |  |
|node_id |char(11) |NO |  | 预留字段 |
|parent_id |char(11) |NO |  | 预留字段 |
|node_type |varchar(20) |NO |None  | 节点类型 |
|filter_id |int(11) |YES |None  | 过滤器 |
|field |varchar(20) |YES |None  | 字段 |
|logic |varchar(10) |YES |None  | 逻辑符 |
|join_filter_id |int(11) |YES |None  | 关联过滤器 |
|join_field |varchar(20) |YES |None  | 关联字段 |
## tb_filter
#### 描述: 过滤器-唐笑于
#### 字段总数: 11
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(8) |NO |None  | 主键 |
|filter_category_id |int(11) |NO |None  | 分类ID |
|number |varchar(50) |NO |None  | 编号 |
|status |tinyint(1) |NO |1  | 状态，0:禁用，1:启用 |
|name |varchar(50) |NO |None  | 过滤器名称 |
|description |varchar(200) |YES |None  | 描述 |
|rule_show |text |YES |None  |  |
|create_user |char(32) |YES |None  | 创建人 |
|create_time |datetime |YES |None  | 创建时间 |
|update_user |char(32) |YES |None  | 修改人 |
|update_time |datetime |YES |None  | 修改时间 |
## tb_filter_category
#### 描述: 过滤器分类-唐笑于
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(10) |NO |None  | 主键 |
|name |varchar(50) |NO |None  | 分类名称 |
|description |varchar(200) |YES |None  | 描述 |
|create_user |int(11) |YES |None  | 创建人 |
|create_time |datetime |YES |None  | 创建时间 |
|update_user |int(11) |YES |None  | 修改人 |
|update_time |datetime |YES |None  | 修改时间 |
## tb_filter_details
#### 描述: 过滤器明细表-唐笑于
#### 字段总数: 9
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 主键 |
|filter_id |int(11) |NO |None  | 过滤器ID |
|node_id |char(11) |NO |None  | 预留字段 |
|parent_id |char(11) |NO |None  | 预留字段 |
|node_type |char(10) |NO |None  | 节点类型 |
|conditional |varchar(50) |YES |None  | 条件 |
|logic |varchar(10) |YES |None  | 逻辑符号 |
|value |text |YES |None  | 值 |
|list_id |int(11) |YES |None  | 名单ID，只有node_type是list时才可以选择名单 |
## tb_list
#### 描述: 名单表-唐笑于
#### 字段总数: 8
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 主键 |
|status |tinyint(1) |NO |0  | 状态，默认未启用 |
|name |varchar(50) |NO |None  | 名单名字 |
|description |varchar(500) |YES |None  | 描述 |
|create_user |int(11) |YES |None  | 创建人 |
|create_time |datetime |YES |None  | 创建时间 |
|update_user |int(11) |YES |None  | 修改人 |
|update_time |datetime |YES |None  | 修改时间 |
## tb_list_details
#### 描述: 名单详细信息-唐笑于
#### 字段总数: 9
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 主键 |
|status |tinyint(1) |NO |1  | 状态，默认启用 |
|list_id |int(11) |NO |None  | 名单ID |
|value |text |NO |None  | 名单值 |
|description |varchar(200) |YES |None  | 描述 |
|create_user |int(11) |YES |None  | 创建人 |
|create_time |datetime |YES |None  | 创建时间 |
|update_user |int(11) |YES |None  | 修改人 |
|update_time |datetime |YES |None  | 修改时间 |
## ti_antivirus
#### 描述: 
#### 字段总数: 9
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|antiviru_file_id |int(11) |NO |None  | 主键自增id |
|intelligence_file_id |int(11) |NO |None  | 情报ID |
|antivirus_name |varchar(100) |NO |None  | 反病毒软件名称 |
|antivirus_result |varchar(255) |NO |None  | 反病毒软件结果 |
|del_flag |tinyint(1) |YES |0  | 删除标识 0:未删 1:已删 |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新时间 |
## ti_file
#### 描述: 
#### 字段总数: 41
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|intelligence_file_id |int(11) |NO |None  | 主键自增id |
|intelligence_id |varchar(32) |NO |None  | 情报ID |
|intelligence_name |varchar(32) |YES |None  | 情报名称 |
|intelligence_ref |text |YES |None  | 情报链接 |
|intelligence_rep |varchar(255) |YES |None  | 情报报告 |
|intelligence_describe |varchar(255) |YES |None  | 情报描述 |
|intelligence_src |varchar(100) |YES |None  | 情报来源 |
|intelligence_publish_time
intelligence_publish_time |datetime |YES |None  | 情报发布时间 |
|intelligence_update_time |datetime |NO |0000-00-00 00:00:00  | 情报更新时间 |
|intelligence_patch |varchar(255) |YES |None  | 补丁 |
|file_name |varchar(255) |NO |None  | 文件名称 |
|file_size |varchar(32) |YES |None  | 文件大小 |
|filehash_sha256 |varchar(128) |YES |None  | 文件哈希sha256 |
|filehash_sha1 |varchar(128) |YES |None  | 文件哈希sha1 |
|filehash_md5 |varchar(128) |YES |None  | 文件哈希md5 |
|intelligence_type |tinyint(1) |YES |2  | 1为战略，2为战术，3为预警，4为通告 |
|alive |tinyint(1) |YES |0  | 是否启用，0:启用，1:禁用 |
|remark |varchar(255) |YES |None  | 备注标注 |
|last_analysis |datetime |YES |None  | 最后一次检测时间 |
|malware_family |varchar(255) |YES |None  | 恶意软件家族 |
|malware_type |varchar(255) |YES |None  | 恶意软件类型 |
|risk_score |tinyint(3) |YES |None  | 风险评分 |
|stat_net_scan |text |YES |None  | 静态网络监测结果 |
|acitve_net_scan |text |YES |None  | 动态网络监测结果 |
|stat_reg_scan |text |YES |None  | 静态注册表监测结果 |
|acitve_reg_scan |text |YES |None  | 动态注册表监测结果 |
|stat_file_scan |text |YES |None  | 静态监测文件系统结果 |
|acitve_file_scan |text |YES |None  | 动态监测文件系统结果 |
|file_ico |text |YES |None  | 文件IOC信息 |
|bevelscore |tinyint(3) |YES |None  | 可信度 |
|is_ransomware |tinyint(1) |YES |0  | 是否为勒索软件 0:否，1:是 |
|is_malware |tinyint(1) |YES |0  | 是否为蠕虫 0:否，1:是 |
|is_white |tinyint(1) |YES |0  | 是否为白名单文件 0:否，1:是 |
|is_trojans |tinyint(1) |YES |0  | 是否为木马 0:否，1:是 |
|rel_ip |text |YES |None  | 关联ip |
|rel_url |text |YES |None  | 关联url |
|del_flag |tinyint(1) |YES |0  | 删除标识 0:未删 1:已删 |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新时间 |
## ti_file_malicious_action
#### 描述: 
#### 字段总数: 10
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|action_file_id |int(11) |NO |None  | 主键自增id |
|intelligence_id |varchar(32) |NO |None  | 情报ID |
|action_name |varchar(32) |NO |None  | 恶意行为中文名称 |
|relation_date |datetime |YES |None  | 关联日期 |
|is_alive |tinyint(1) |YES |0  | 0：存活 1：未存活 |
|del_flag |tinyint(1) |YES |0  | 删除标识 0:未删 1:已删 |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新时间 |
## ti_ipaddr
#### 描述: 
#### 字段总数: 38
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|intelligence_ipaddr_id |int(11) |NO |None  | 主键自增id 对应ti_ipaddr_malicious_action.intelligence_ipaddr_id |
|intelligence_id |varchar(32) |NO |None  | 情报ID |
|intelligence_name |varchar(32) |YES |None  | 情报名称 |
|intelligence_ref |text |YES |None  | 情报链接 |
|intelligence_rep |varchar(255) |YES |None  | 情报报告 |
|intelligence_describe |varchar(255) |YES |None  | 情报描述 |
|intelligence_src |varchar(100) |YES |观安  | 情报来源 |
|intelligence_publish_time |datetime |YES |None  | 情报发布时间 |
|intelligence_update_time |datetime |NO |1970-01-01 00:00:00  | 情报更新时间 |
|intelligence_patch |varchar(255) |YES |None  | 补丁 |
|ipaddr |varchar(32) |YES |None  | IP地址(UNIQUE) |
|ipaddr_type |tinyint(4) |YES |None  | IP类型(0:IPv4类型,1:IPv6类型) |
|asn |varchar(150) |YES |None  | 与IP地址相关的自治系统号 |
|isp |varchar(32) |YES |None  | IP地址注册机构 |
|country_code |varchar(5) |YES |None  | 国家代码 |
|country |varchar(32) |YES |None  | 国家 |
|city |varchar(32) |YES |None  | 与IP地址相关的城市 |
|area |varchar(100) |YES |None  | 与IP地址相关的区域 |
|zipcode |varchar(32) |YES |None  | 邮编 |
|longitude |float |YES |None  | 经度 |
|latitude |float |YES |None  | 纬度 |
|analysis_to_domain |varchar(255) |YES |None  | 域名反向解析记录 |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新日期 |
|del_flag |tinyint(4) |YES |None  | 删除标识 |
|intelligence_type |tinyint(4) |YES |None  | 类型(1为战略，2为战术，3为预警，4为通告  默认为2) |
|alive |tinyint(4) |YES |0  | 是否启用(0 启用 1 不启用) |
|remark |varchar(255) |YES |None  | 备注 |
|risk_score |tinyint(4) |YES |None  | 风险评分(0-100) |
|bevel_score |tinyint(4) |YES |None  | 可信度(0-100) |
|c2_addr |text |YES |None  | C2服务器地址(域名或IP) |
|c2_type |varchar(32) |YES |None  | C2僵尸网络类型 |
|c2_port |int(11) |YES |None  | C2端口号 |
|c2_protocol |varchar(32) |YES |None  | C2协议 |
|rel_url |text |YES |None  | 关联域名 |
|rel_file |text |YES |None  | 关联文件 |
## ti_ipaddr_malicious_action
#### 描述: 
#### 字段总数: 10
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|action_ipaddr_id |int(11) |NO |None  |  |
|intelligence_id |varchar(32) |NO |None  | 情报ID |
|action_name |varchar(32) |NO |None  | 恶意行为中文名称 |
|date |datetime |YES |None  | 关联日期 |
|is_alive |tinyint(4) |YES |0  | 是否存活(0：存活 1：未存活 默认:0) |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(32) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新日期 |
|del_flag |tinyint(4) |YES |0  | 删除标识(0 未删，1:已删 默认:0) |
## ti_phone
#### 描述: 
#### 字段总数: 24
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|intelligence_id |int(11) |NO |None  | 主键自增id |
|intelligence_phone_id |varchar(32) |NO |None  | 情报ID |
|intelligence_name |varchar(32) |YES |None  | 情报名称 |
|intelligence_ref |text |YES |None  | 情报链接 |
|intelligence_rep |varchar(255) |YES |None  | 情报报告 |
|intelligence_description |varchar(255) |YES |None  | 情报描述 |
|intelligence_src |varchar(100) |YES |None  | 情报来源 |
|intelligence_publish_time |datetime |YES |None  | 情报发布时间 |
|intelligence_update_time |datetime |YES |0000-00-00 00:00:00  | 情报更新时间 |
|intelligence_patch |varchar(255) |YES |None  | 补丁 |
|phone_number |varchar(32) |NO |None  | 电话号码 |
|number_attribution |varchar(32) |YES |None  | 号码归属地 |
|phone_number_type |tinyint(1) |YES |None  | 0:真实运营商号码，1:虚拟运营商，2:阿里小号等 |
|action |text |YES |None  | 保留字段 |
|action_history |text |YES |None  | 保留字段 |
|risk_score |tinyint(3) |YES |None  |  |
|intelligence_type |tinyint(1) |YES |2  | 1为战略，2为战术，3为预警，4为通告 |
|alive |tinyint(1) |YES |0  | 是否启用，0:启用，1:禁用 |
|remark |varchar(255) |YES |None  | 备注标注 |
|del_flag |tinyint(1) |YES |0  | 0为未删，1为已删 |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新时间 |
## ti_url
#### 描述: 
#### 字段总数: 59
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|intelligence_url_id |int(11) |NO |None  | 主键自增id, |
|intelligence_id |varchar(32) |YES |None  | 情报ID, |
|intelligence_name |varchar(32) |YES |None  | 情报名称, |
|intelligence_ref |text |YES |None  | 情报链接, |
|intelligence_rep |varchar(255) |YES |None  | 情报报告, |
|intelligence_describe |varchar(255) |YES |None  | 情报描述, |
|intelligence_src |varchar(100) |YES |None  | 情报来源,情报机构名称：初始化数据默认观安 |
|intelligence_publish_time |datetime |YES |None  | 情报发布时间, |
|intelligence_update_time |datetime |YES |None  | 情报更新时间, |
|intelligence_patch |varchar(255) |YES |None  | 补丁, |
|url |text |YES |None  | url地址,url |
|isp |varchar(32) |YES |None  | ISP信息,根据IP地址查询注册机构 |
|country_code |int(5) |YES |None  | 国家代码,国家代码 |
|country |varchar(32) |YES |None  | 国家,与IP地址相关的国家 |
|city |varchar(32) |YES |None  | 城市,与IP地址相关的城市 |
|area |varchar(100) |YES |None  | 区域,与IP地址相关的区域 |
|zipcode |varchar(32) |YES |None  | 邮编,与IP地址相关的邮政编码 |
|longitude |float |YES |None  | 经度, |
|latitude |float |YES |None  | 纬度, |
|whois |text |YES |None  | whois记录,whois信息，信息不覆盖，保存历史记录 |
|sub_domains |text |YES |None  | 子域名,获取此域名包含的子域名 |
|page_snapshot |tinyint(4) |YES |None  | 页面快照,0为是,1为否 |
|hot |tinyint(4) |YES |None  | 热度, |
|analysis_to_ipaddr |varchar(255) |YES |None  | 解析地址, |
|create_user |varchar(100) |YES |None  | 创建者,创建者 |
|create_date |datetime |YES |None  | 创建日期,创建日期 |
|update_user |varchar(100) |YES |None  | 更新者,更新者 |
|update_date |datetime |YES |None  | 更新日期,更新日期 |
|domain_name |varchar(255) |YES |None  | 根域名名称,跟域名名称，用来关联whois表 |
|domain_type |tinyint(4) |YES |None  | 根域名类型,0为cn后缀，1为com，net后缀，2为org后缀，3为xyz后缀 |
|del_flag |tinyint(4) |YES |None  | 删除标识,逻辑删除 |
|alexa_rank |int(11) |YES |None  | Alexa排名信息, |
|domain_server |varchar(255) |YES |None  | 域名服务器, |
|CA |text |YES |None  | 数字证书,预留字段 |
|intelligence_type |tinyint(4) |YES |2  | 类型,1为战略，2为战术，3为预警，4为通告 |
|alive |tinyint(4) |YES |None  | 是否启用, |
|remark |varchar(255) |YES |None  | 备注,备注，标注字段 |
|risk_score |tinyint(4) |YES |None  | 风险评分,评分1-100 |
|bevel_score |tinyint(4) |YES |None  | 可信度,评分1-100 |
|c2_addr |text |YES |None  | C2服务器地址,域名或IP |
|c2_type |varchar(32) |YES |None  | C2僵尸网络类型, |
|c2_port |int(5) |YES |None  | C2端口号, |
|c2_protocol |varchar(32) |YES |None  | C2协议,端口对应协议 |
|is_idc |tinyint(4) |YES |None  | 是否为idc, |
|is_proxy |tinyint(4) |YES |None  | 是否为代理, |
|is_dynamic_ip |tinyint(4) |YES |None  | 是否为动态ip, |
|is_spam |tinyint(4) |YES |None  | 是否为恶意邮件, |
|is_gateway |tinyint(4) |YES |None  | 是否为网关, |
|is_whitelist |tinyint(4) |YES |None  | 是否为白名单, |
|is_bogon |tinyint(4) |YES |None  | 是否为bogon主机, |
|is_tor |tinyint(4) |YES |None  | 是否为洋葱网络, |
|is_gambling |tinyint(4) |YES |None  | 是否为赌博网站, |
|is_ransomware |tinyint(4) |YES |None  | 是否为勒索阮家, |
|is_scanner |tinyint(4) |YES |None  | 是否为扫描器, |
|is_malware |tinyint(4) |YES |None  | 是否为蠕虫, |
|is_porn |tinyint(4) |YES |None  | 是否为色情网站, |
|is_phishing |tinyint(4) |YES |None  | 是否为钓鱼网站, |
|is_edu |tinyint(4) |YES |None  | 是否为教育网站, |
|rel_ip |text |YES |None  | 关联域名,数组形式，解析后逗号分隔 |
## ti_url_malicious_action
#### 描述: 
#### 字段总数: 10
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|action_url_id |int(11) |NO |None  | 主键自增id, |
|intelligence_id |varchar(32) |NO |None  | 情报ID, |
|action_name |varchar(32) |NO |None  | 恶意行为中文名称, |
|date |datetime |YES |None  | 关联日期, |
|is_alive |tinyint(4) |YES |None  | 是否存活, |
|create_user |varchar(100) |YES |None  | 创建者, |
|create_date |datetime |YES |None  | 创建日期, |
|update_user |varchar(100) |YES |None  | 更新者, |
|update_date |datetime |YES |None  | 更新日期, |
|del_flag |tinyint(1) |YES |None  |  |
## ti_vul_info
#### 描述: 
#### 字段总数: 38
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|intelligence_vul_id |int(11) |NO |None  |  |
|intelligence_id |varchar(32) |YES |None  | 情报ID |
|intelligence_name |varchar(32) |YES |None  | 情报名称 |
|intelligence_ref |text |YES |None  | 情报链接 |
|intelligence_rep |varchar(255) |YES |None  | 情报报告 |
|intelligence_describe |varchar(255) |YES |None  | 情报描述 |
|intelligence_src |varchar(100) |YES |None  | 情报来源 |
|intelligence_publish_time |datetime |YES |None  | 情报发布时间 |
|intelligence_update_name |datetime |YES |None  | 情报更新时间 |
|intelligence_patch |varchar(255) |YES |None  | 补丁 |
|gsvd_id |varchar(32) |YES |None  | 观安漏洞编号 |
|cve_id |varchar(32) |YES |None  | CVE编号 |
|bugtraq_id |varchar(200) |YES |None  | BugTraq编号 |
|cnvd_id |varchar(32) |YES |None  | CNVD编号 |
|cnvd_level |tinyint(4) |YES |None  | CNVD等级 |
|cnnvd_id |varchar(32) |YES |None  | CNNVD编号 |
|cnnvd_level |tinyint(4) |YES |None  | CNNVD等级 |
|vul_type |tinyint(4) |YES |None  | 漏洞类型 |
|vul_sub_type |tinyint(4) |YES |None  | 漏洞子类型 |
|vul_source |varchar(32) |YES |None  | 漏洞来源 |
|vul_name |varchar(255) |YES |None  | 漏洞名称 |
|vul_detail |longtext |YES |None  | 漏洞描述 |
|vul_range |text |YES |None  | 漏洞影响范围 |
|vul_effect_version |varchar(255) |YES |None  | 漏洞 影响版本 |
|vul_solution |text |YES |None  | 漏洞解决方案 |
|vul_rank |tinyint(4) |YES |None  | 漏洞风险等级(0：高危1：中危2：低危) |
|vul_publish_date |datetime |YES |None  | 漏洞发布日期 |
|vul_patch |text |YES |None  | 补丁信息 |
|vul_ref |text |YES |None  | 参考链接 |
|create_user |varchar(255) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新日期 |
|del_flag |tinyint(4) |YES |None  | 删除标识 |
|file_name |varchar(255) |YES |None  | 文件名 |
|intelligence_type |tinyint(4) |YES |None  | 类型(1为战略，2为战术，3为预警，4为通告) |
|alive |tinyint(4) |YES |None  | 是否启用 |
|remark |varchar(255) |YES |None  | 备注 |
## ti_whois_cn
#### 描述: 
#### 字段总数: 14
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|cn_id |int(11) |NO |None  | 自增长编号, |
|domain_name |varchar(255) |YES |None  | 域名名称,查询的域名地址 |
|registrar_addr |text |YES |None  | 域名归属,域名所有人姓名 |
|registrar_email |varchar(255) |YES |None  | 联系人信箱,域名所有人邮箱 |
|creation_date |datetime |YES |None  | 注册时间,域名注册时间 |
|expiry_date |datetime |YES |None  | 过期时间,域名逾期时间 |
|domain_id |varchar(100) |YES |None  | 域名注册编号, |
|status |text |YES |None  | 域名当前状态, |
|name_server |text |YES |None  | 域名解析服务器, |
|is_dbssec |tinyint(4) |YES |None  | 是否保护,DNSSEC是否开启 |
|whois_src |tinyint(4) |YES |None  | whois信息来源,0手动新增，1导入，2同步，3自动发现 |
|create_user |varchar(100) |YES |None  | 创建者,创建者 |
|create_date |datetime |YES |None  | 创建日期,创建日期 |
|update_user |varchar(100) |YES |None  | 更新者,更新者 |
## ti_whois_cn_history
#### 描述: 
#### 字段总数: 14
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|cn_history_id |int(11) |NO |None  | 自增长编号, |
|domain_name |varchar(255) |YES |None  | 域名名称,查询的域名地址 |
|registrar_addr |text |YES |None  | 域名归属,域名所有人姓名 |
|registrar_email |varchar(255) |YES |None  | 联系人信箱,域名所有人邮箱 |
|creation_date |datetime |YES |None  | 注册时间,域名注册时间 |
|expiry_date |datetime |YES |None  | 过期时间,域名逾期时间 |
|domain_id |varchar(100) |YES |None  | 域名注册编号, |
|status |text |YES |None  | 域名当前状态, |
|name_server |text |YES |None  | 域名解析服务器, |
|is_dbssec |tinyint(4) |YES |None  | 是否保护,DNSSEC是否开启 |
|whois_src |tinyint(4) |YES |None  | whois信息来源,0手动新增，1导入，2同步，3自动发现 |
|create_user |varchar(100) |YES |None  | 创建者,创建者 |
|create_date |datetime |YES |None  | 创建日期,创建日期 |
|update_user |varchar(100) |YES |None  | 更新者,更新者 |
## ti_whois_com_net
#### 描述: 
#### 字段总数: 65
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|com_net_id |int(11) |NO |None  | 自增长编号, |
|domain_name |varchar(255) |YES |None  | 域名,查询的域名地址 |
|registrar_addr |text |YES |None  | 域名归属,域名所有人姓名 |
|registrar_email |varchar(255) |YES |None  | 联系人信箱,域名所有人邮箱 |
|creation_date |datetime |YES |None  | 注册时间,域名注册时间 |
|expiry_date |datetime |YES |None  | 过期时间,域名逾期时间 |
|domain_id |varchar(100) |YES |None  | 域名注册编号, |
|status |text |YES |None  | 域名当前状态, |
|name_server |text |YES |None  | 域名解析服务器, |
|is_dbssec |tinyint(4) |YES |None  | 是否保护,DNSSEC是否开启 |
|admin_city |varchar(100) |YES |None  | 管理员城市, |
|admin_country |varchar(100) |YES |None  | 管理员国家, |
|admin_email |varchar(255) |YES |None  | 管理员邮箱, |
|admin_fax |varchar(100) |YES |None  | 管理员传真, |
|admin_fax_ext |varchar(100) |YES |None  | 管理员传真分机号, |
|admin_name |varchar(100) |YES |None  | 管理员姓名, |
|admin_organization |varchar(100) |YES |None  | 管理员组织, |
|admin_phone |varchar(100) |YES |None  | 管理员电话, |
|admin_phone_ext |varchar(100) |YES |None  | 管理员电话分机号, |
|admin_postal_code |varchar(100) |YES |None  | 管理员邮政编码, |
|admin_state_province |varchar(100) |YES |None  | 管理员省份, |
|admin_street |varchar(100) |YES |None  | 管理员街道, |
|is_dnssec |tinyint(1) |YES |None  | DNS保护, |
|domain_status |varchar(255) |YES |None  | 域名状态, |
|registrant_city |varchar(100) |YES |None  | 注册人城市, |
|registrant_country |varchar(100) |YES |None  | 注册人国家, |
|registrant_email |varchar(255) |YES |None  | 注册人邮箱, |
|registrant_fax |varchar(100) |YES |None  | 注册人传真, |
|registrant_fax_ext |varchar(100) |YES |None  | 注册人传真分机号, |
|registrant_name |varchar(100) |YES |None  | 注册人姓名, |
|registrant_organization |varchar(255) |YES |None  | 注册人组织, |
|registrant_phone |varchar(100) |YES |None  | 注册人电话, |
|registrant_phone_ext |varchar(100) |YES |None  | 注册人电话分机号, |
|registrant_postal_code |varchar(100) |YES |None  | 注册人邮编, |
|registrant_state_province |varchar(100) |YES |None  | 注册人省份, |
|registrant_street |varchar(100) |YES |None  | 注册人街道, |
|registrar |varchar(100) |YES |None  | 注册人, |
|registrar_abuse_contact_email |varchar(255) |YES |None  | 注册人显示邮箱, |
|registra_abuse_contact_phone |varchar(100) |YES |None  | 注册人显示电话, |
|registra_iana _id |varchar(255) |YES |None  | IANA编号, |
|registrar_registration_expiration _date |datetime |YES |None  | 域名注册截止时间, |
|registrar_url |varchar(255) |YES |None  | 注册地址, |
|registrar_whois_server |varchar(255) |YES |None  | 注册Whois服务器地址 , |
|registry_admin_id |varchar(100) |YES |None  | 管理员ID, |
|registry_domain_id |varchar(100) |YES |None  | 域名iD, |
|registry_registrant_id |varchar(100) |YES |None  | 注册人编号, |
|registry_tech_id |varchar(100) |YES |None  | 技术人员编号, |
|reseller |varchar(100) |YES |None  | 销售者, |
|tech_city |varchar(100) |YES |None  | 技术人员城市, |
|tech_country |varchar(100) |YES |None  | 技术人员国家, |
|tech_email |varchar(255) |YES |None  | 技术人员邮箱, |
|tech_fax |varchar(100) |YES |None  | 技术人员传真, |
|tech_fax_ext |varchar(100) |YES |None  | 技术人员传真分机号, |
|tech_name |varchar(100) |YES |None  | 技术人员姓名, |
|tech_organization |varchar(255) |YES |None  | 技术人员组织, |
|tech_phone |varchar(100) |YES |None  | 技术人员电话, |
|tech_phone_ext |varchar(100) |YES |None  | 技术人员电话分机号, |
|tech_postal_code |varchar(100) |YES |None  | 技术人员邮编, |
|tech_state_province |varchar(100) |YES |None  | 技术人员省份, |
|tech_street |varchar(100) |YES |None  | 技术人员街道, |
|updated_date |datetime |YES |None  | 状态更新时间, |
|whois_src |tinyint(4) |YES |None  | whois信息来源,0手动新增，1导入，2同步，3自动发现 |
|create_user |varchar(100) |YES |None  | 创建者,创建者 |
|create_date |datetime |YES |None  | 创建日期,创建日期 |
|update_user |varchar(100) |YES |None  | 更新者,更新者 |
## ti_whois_com_net_history
#### 描述: 
#### 字段总数: 65
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|com_net_history_id |int(11) |NO |None  | 自增长编号, |
|domain_name |varchar(255) |YES |None  | 域名名称,查询的域名地址 |
|registrar_addr |text |YES |None  | 域名归属,域名所有人姓名 |
|registrar_email |varchar(255) |YES |None  | 联系人信箱,域名所有人邮箱 |
|creation_date |datetime |YES |None  | 注册时间,域名注册时间 |
|expiry_date |datetime |YES |None  | 过期时间,域名逾期时间 |
|domain_id |varchar(100) |YES |None  | 域名注册编号, |
|status |text |YES |None  | 域名当前状态, |
|name_server |text |YES |None  | 域名解析服务器, |
|is_dbssec |tinyint(4) |YES |None  | 是否保护,DNSSEC是否开启 |
|admin_city |varchar(100) |YES |None  | 管理员城市, |
|admin_country |varchar(100) |YES |None  | 管理员国家, |
|admin_email |varchar(255) |YES |None  | 管理员邮箱, |
|admin_fax |varchar(100) |YES |None  | 管理员传真, |
|admin_fax_ext |varchar(100) |YES |None  | 管理员传真分机号, |
|admin_name |varchar(100) |YES |None  | 管理员姓名, |
|admin_organization |varchar(100) |YES |None  | 管理员组织, |
|admin_phone |varchar(100) |YES |None  | 管理员电话, |
|admin_phone_ext |varchar(100) |YES |None  | 管理员电话分机号, |
|admin_postal_code |varchar(100) |YES |None  | 管理员邮政编码, |
|admin_state_province |varchar(100) |YES |None  | 管理员省份, |
|admin_street |varchar(100) |YES |None  | 管理员街道, |
|is_dnssec |tinyint(1) |YES |None  | DNS保护, |
|domain_status |varchar(255) |YES |None  | 域名状态, |
|registrant_city |varchar(100) |YES |None  | 注册人城市, |
|registrant_country |varchar(100) |YES |None  | 注册人国家, |
|registrant_email |varchar(255) |YES |None  | 注册人邮箱, |
|registrant_fax |varchar(100) |YES |None  | 注册人传真, |
|registrant_fax_ext |varchar(100) |YES |None  | 注册人传真分机号, |
|registrant_name |varchar(100) |YES |None  | 注册人姓名, |
|registrant_organization |varchar(255) |YES |None  | 注册人组织, |
|registrant_phone |varchar(100) |YES |None  | 注册人电话, |
|registrant_phone_ext |varchar(100) |YES |None  | 注册人电话分机号, |
|registrant_postal_code |varchar(100) |YES |None  | 注册人邮编, |
|registrant_state_province |varchar(100) |YES |None  | 注册人省份, |
|registrant_street |varchar(100) |YES |None  | 注册人街道, |
|registrar |varchar(100) |YES |None  | 注册人, |
|registrar_abuse_contact_email |varchar(255) |YES |None  | 注册人显示邮箱, |
|registra_abuse_contact_phone |varchar(100) |YES |None  | 注册人显示电话, |
|registra_iana _id |varchar(255) |YES |None  | IANA编号, |
|registrar_registration_expiration _date |datetime |YES |None  | 域名注册截止时间, |
|registrar_url |varchar(255) |YES |None  | 注册地址, |
|registrar_whois_server |varchar(255) |YES |None  | 注册Whois服务器地址 , |
|registry+admin_id |varchar(100) |YES |None  | 管理员ID, |
|registry_domain_id |varchar(100) |YES |None  | 域名iD, |
|registry_registrant_id |varchar(100) |YES |None  | 注册人编号, |
|registry_tech_id |varchar(100) |YES |None  | 技术人员编号, |
|reseller |varchar(100) |YES |None  | 销售者, |
|tech_city |varchar(100) |YES |None  | 技术人员城市, |
|tech_country |varchar(100) |YES |None  | 技术人员国家, |
|tech_email |varchar(255) |YES |None  | 技术人员邮箱, |
|tech_fax |varchar(100) |YES |None  | 技术人员传真, |
|tech_fax_ext |varchar(100) |YES |None  | 技术人员传真分机号, |
|tech_name |varchar(100) |YES |None  | 技术人员姓名, |
|tech_organization |varchar(255) |YES |None  | 技术人员组织, |
|tech_phone |varchar(100) |YES |None  | 技术人员电话, |
|tech_phone_ext |varchar(100) |YES |None  | 技术人员电话分机号, |
|tech_postal_code |varchar(100) |YES |None  | 技术人员邮编, |
|tech_state_province |varchar(100) |YES |None  | 技术人员省份, |
|tech_street |varchar(100) |YES |None  | 技术人员街道, |
|updated_date |datetime |YES |None  | 状态更新时间, |
|whois_src |tinyint(4) |YES |None  | whois信息来源,0手动新增，1导入，2同步，3自动发现 |
|create_user |varchar(100) |YES |None  | 创建者,创建者 |
|create_date |datetime |YES |None  | 创建日期,创建日期 |
|update_user |varchar(100) |YES |None  | 更新者,更新者 |
## ti_whois_org
#### 描述: 
#### 字段总数: 66
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|org_id |int(11) |NO |None  | 自增长编号, |
|domain_name |varchar(255) |YES |None  | 域名,查询的域名地址 |
|registrar_addr |text |YES |None  | 域名归属,域名所有人姓名 |
|registrar_email |varchar(255) |YES |None  | 联系人信箱,域名所有人邮箱 |
|creation_date |datetime |YES |None  | 注册时间,域名注册时间 |
|expiry_date |datetime |YES |None  | 过期时间,域名逾期时间 |
|domain_id |varchar(100) |YES |None  | 域名注册编号, |
|status |text |YES |None  | 域名当前状态, |
|name_server |text |YES |None  | 域名解析服务器, |
|is_dbssec |tinyint(4) |YES |None  | 是否保护,DNSSEC是否开启 |
|admin_city |varchar(100) |YES |None  | 管理员城市, |
|admin_country |varchar(100) |YES |None  | 管理员国家, |
|admin_email |varchar(255) |YES |None  | 管理员邮箱, |
|admin_fax |varchar(100) |YES |None  | 管理员传真, |
|admin_fax_ext |varchar(100) |YES |None  | 管理员传真分机号, |
|admin_name |varchar(100) |YES |None  | 管理员姓名, |
|admin_organization |varchar(100) |YES |None  | 管理员组织, |
|admin_phone |varchar(100) |YES |None  | 管理员电话, |
|admin_phone_ext |varchar(100) |YES |None  | 管理员电话分机号, |
|admin_postal_code |varchar(100) |YES |None  | 管理员邮政编码, |
|admin_state_province |varchar(100) |YES |None  | 管理员省份, |
|admin_street |varchar(100) |YES |None  | 管理员街道, |
|is_dnssec |tinyint(1) |YES |None  | DNS保护, |
|domain_status |varchar(255) |YES |None  | 域名状态, |
|registrant_city |varchar(100) |YES |None  | 注册人城市, |
|registrant_country |varchar(100) |YES |None  | 注册人国家, |
|registrant_email |varchar(255) |YES |None  | 注册人邮箱, |
|registrant_fax |varchar(100) |YES |None  | 注册人传真, |
|registrant_fax_ext |varchar(100) |YES |None  | 注册人传真分机号, |
|registrant_name |varchar(100) |YES |None  | 注册人姓名, |
|registrant_organization |varchar(255) |YES |None  | 注册人组织, |
|registrant_phone |varchar(100) |YES |None  | 注册人电话, |
|registrant_phone_ext |varchar(100) |YES |None  | 注册人电话分机号, |
|registrant_postal_code |varchar(100) |YES |None  | 注册人邮编, |
|registrant_state_province |varchar(100) |YES |None  | 注册人省份, |
|registrant_street |varchar(100) |YES |None  | 注册人街道, |
|registrar |varchar(100) |YES |None  | 注册人, |
|registrar_abuse_contact_email |varchar(255) |YES |None  | 注册人显示邮箱, |
|registra_abuse_contact_phone |varchar(100) |YES |None  | 注册人显示电话, |
|registra_iana _id |varchar(255) |YES |None  | IANA编号, |
|registrar_registration_expiration _date |datetime |YES |None  | 域名注册截止时间, |
|registrar_url |varchar(255) |YES |None  | 注册地址, |
|registrar_whois_server |varchar(255) |YES |None  | 注册Whois服务器地址 , |
|registry_admin_id |varchar(100) |YES |None  | 管理员ID, |
|registry_domain_id |varchar(100) |YES |None  | 域名iD, |
|registry_expiry_date |varchar(100) |YES |None  | 注册逾期时间, |
|registry_registrant_id |varchar(100) |YES |None  | 注册人编号, |
|registry_tech_id |varchar(100) |YES |None  | 技术人员编号, |
|reseller |varchar(100) |YES |None  | 销售者, |
|tech_city |varchar(100) |YES |None  | 技术人员城市, |
|tech_country |varchar(100) |YES |None  | 技术人员国家, |
|tech_email |varchar(255) |YES |None  | 技术人员邮箱, |
|tech_fax |varchar(100) |YES |None  | 技术人员传真, |
|tech_fax_ext |varchar(100) |YES |None  | 技术人员传真分机号, |
|tech_name |varchar(100) |YES |None  | 技术人员姓名, |
|tech_organization |varchar(255) |YES |None  | 技术人员组织, |
|tech_phone |varchar(100) |YES |None  | 技术人员电话, |
|tech_phone_ext |varchar(100) |YES |None  | 技术人员电话分机号, |
|tech_postal_code |varchar(100) |YES |None  | 技术人员邮编, |
|tech_state_province |varchar(100) |YES |None  | 技术人员省份, |
|tech_street |varchar(100) |YES |None  | 技术人员街道, |
|updated_date |datetime |YES |None  | 状态更新时间, |
|whois_src |tinyint(4) |YES |None  | whois信息来源,0手动新增，1导入，2同步，3自动发现 |
|create_user |varchar(100) |YES |None  | 创建者,创建者 |
|create_date |datetime |YES |None  | 创建日期,创建日期 |
|update_user |varchar(100) |YES |None  | 更新者,更新者 |
## ti_whois_org_history
#### 描述: 
#### 字段总数: 66
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|org_history_id |int(11) |NO |None  | 自增长编号, |
|domain_name |varchar(255) |YES |None  | 域名,查询的域名地址 |
|registrar_addr |text |YES |None  | 域名归属,域名所有人姓名 |
|registrar_email |varchar(255) |YES |None  | 联系人信箱,域名所有人邮箱 |
|creation_date |datetime |YES |None  | 注册时间,域名注册时间 |
|expiry_date |datetime |YES |None  | 过期时间,域名逾期时间 |
|domain_id |varchar(100) |YES |None  | 域名注册编号, |
|status |text |YES |None  | 域名当前状态, |
|name_server |text |YES |None  | 域名解析服务器, |
|is_dbssec |tinyint(4) |YES |None  | 是否保护,DNSSEC是否开启 |
|admin_city |varchar(100) |YES |None  | 管理员城市, |
|admin_country |varchar(100) |YES |None  | 管理员国家, |
|admin_email |varchar(255) |YES |None  | 管理员邮箱, |
|admin_fax |varchar(100) |YES |None  | 管理员传真, |
|admin_fax_ext |varchar(100) |YES |None  | 管理员传真分机号, |
|admin_name |varchar(100) |YES |None  | 管理员姓名, |
|admin_organization |varchar(100) |YES |None  | 管理员组织, |
|admin_phone |varchar(100) |YES |None  | 管理员电话, |
|admin_phone_ext |varchar(100) |YES |None  | 管理员电话分机号, |
|admin_postal_code |varchar(100) |YES |None  | 管理员邮政编码, |
|admin_state_province |varchar(100) |YES |None  | 管理员省份, |
|admin_street |varchar(100) |YES |None  | 管理员街道, |
|is_dnssec |tinyint(1) |YES |None  | DNS保护, |
|domain_status |varchar(255) |YES |None  | 域名状态, |
|registrant_city |varchar(100) |YES |None  | 注册人城市, |
|registrant_country |varchar(100) |YES |None  | 注册人国家, |
|registrant_email |varchar(255) |YES |None  | 注册人邮箱, |
|registrant_fax |varchar(100) |YES |None  | 注册人传真, |
|registrant_fax_ext |varchar(100) |YES |None  | 注册人传真分机号, |
|registrant_name |varchar(100) |YES |None  | 注册人姓名, |
|registrant_organization |varchar(255) |YES |None  | 注册人组织, |
|registrant_phone |varchar(100) |YES |None  | 注册人电话, |
|registrant_phone_ext |varchar(100) |YES |None  | 注册人电话分机号, |
|registrant_postal_code |varchar(100) |YES |None  | 注册人邮编, |
|registrant_state_province |varchar(100) |YES |None  | 注册人省份, |
|registrant_street |varchar(100) |YES |None  | 注册人街道, |
|registrar |varchar(100) |YES |None  | 注册人, |
|registrar_abuse_contact_email |varchar(255) |YES |None  | 注册人显示邮箱, |
|registra_abuse_contact_phone |varchar(100) |YES |None  | 注册人显示电话, |
|registra_iana _id |varchar(255) |YES |None  | IANA编号, |
|registrar_registration_expiration _date |datetime |YES |None  | 域名注册截止时间, |
|registrar_url |varchar(255) |YES |None  | 注册地址, |
|registrar_whois_server |varchar(255) |YES |None  | 注册Whois服务器地址 , |
|registry+admin_id |varchar(100) |YES |None  | 管理员ID, |
|registry_domain_id |varchar(100) |YES |None  | 域名iD, |
|registry_expiry_date |varchar(100) |YES |None  | 注册逾期时间, |
|registry_registrant_id |varchar(100) |YES |None  | 注册人编号, |
|registry_tech_id |varchar(100) |YES |None  | 技术人员编号, |
|reseller |varchar(100) |YES |None  | 销售者, |
|tech_city |varchar(100) |YES |None  | 技术人员城市, |
|tech_country |varchar(100) |YES |None  | 技术人员国家, |
|tech_email |varchar(255) |YES |None  | 技术人员邮箱, |
|tech_fax |varchar(100) |YES |None  | 技术人员传真, |
|tech_fax_ext |varchar(100) |YES |None  | 技术人员传真分机号, |
|tech_name |varchar(100) |YES |None  | 技术人员姓名, |
|tech_organization |varchar(255) |YES |None  | 技术人员组织, |
|tech_phone |varchar(100) |YES |None  | 技术人员电话, |
|tech_phone_ext |varchar(100) |YES |None  | 技术人员电话分机号, |
|tech_postal_code |varchar(100) |YES |None  | 技术人员邮编, |
|tech_state_province |varchar(100) |YES |None  | 技术人员省份, |
|tech_street |varchar(100) |YES |None  | 管理员街道, |
|updated_date |datetime |YES |None  | 状态更新时间, |
|whois_src |tinyint(4) |YES |None  | whois信息来源,0手动新增，1导入，2同步，3自动发现 |
|create_user |varchar(100) |YES |None  | 创建者,创建者 |
|create_date |datetime |YES |None  | 创建日期,创建日期 |
|update_user |varchar(100) |YES |None  | 更新者,更新者 |
## ti_whois_xyz
#### 描述: 
#### 字段总数: 69
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|xyz_id |int(11) |NO |None  | 自增长编号, |
|domain_name |varchar(255) |YES |None  | 域名,查询的域名地址 |
|registrar_addr |text |YES |None  | 域名归属,域名所有人姓名 |
|registrar_email |varchar(255) |YES |None  | 联系人信箱,域名所有人邮箱 |
|creation_date |datetime |YES |None  | 注册时间,域名注册时间 |
|expiry_date |datetime |YES |None  | 过期时间,域名逾期时间 |
|domain_id |varchar(100) |YES |None  | 域名注册编号, |
|status |text |YES |None  | 域名当前状态, |
|name_server |text |YES |None  | 域名解析服务器, |
|is_dbssec |tinyint(4) |YES |None  | 是否保护,DNSSEC是否开启 |
|admin_city |varchar(100) |YES |None  | 管理员城市, |
|admin_country |varchar(100) |YES |None  | 管理员国家, |
|admin_email |varchar(255) |YES |None  | 管理员邮箱, |
|admin_fax |varchar(100) |YES |None  | 管理员传真, |
|admin_name |varchar(100) |YES |None  | 管理员姓名, |
|admin_organization |varchar(100) |YES |None  | 管理员组织, |
|admin_phone |varchar(100) |YES |None  | 管理员电话, |
|admin_postal_code |varchar(100) |YES |None  | 管理员邮政编码, |
|admin_state_province |varchar(100) |YES |None  | 管理员省份, |
|admin_street |varchar(100) |YES |None  | 管理员街道, |
|billing_City |varchar(100) |YES |None  | 付费者城市, |
|billing_country |varchar(100) |YES |None  | 付费者国家, |
|billing_email |varchar(255) |YES |None  | 付费者邮箱, |
|billing_fax |varchar(100) |YES |None  | 付费者传真, |
|billing_name |varchar(100) |YES |None  | 付费者姓名, |
|billing_organization |varchar(100) |YES |None  | 付费者组织, |
|billing_phone |varchar(100) |YES |None  | 付费者电话, |
|billing_postal_code |varchar(100) |YES |None  | 付费者邮编, |
|billing_state_province |varchar(100) |YES |None  | 付费者省份, |
|Billing Street |varchar(100) |YES |None  | 付费者街道, |
|is_dnssec |tinyint(1) |YES |None  | DNS保护, |
|domain_status |varchar(255) |YES |None  | 域名状态, |
|registrant_city |varchar(100) |YES |None  | 注册人城市, |
|registrant_country |varchar(100) |YES |None  | 注册人国家, |
|registrant_email |varchar(255) |YES |None  | 注册人邮箱, |
|registrant_fax |varchar(100) |YES |None  | 注册人传真, |
|registrant_name |varchar(100) |YES |None  | 注册人姓名, |
|registrant_organization |varchar(255) |YES |None  | 注册人组织, |
|registrant_phone |varchar(100) |YES |None  | 注册人电话, |
|registrant_postal_code |varchar(100) |YES |None  | 注册人邮编, |
|registrant_state_province |varchar(100) |YES |None  | 注册人省份, |
|registrant_street |varchar(100) |YES |None  | 注册人街道, |
|registrar |varchar(100) |YES |None  | 注册人, |
|registrar_abuse_contact_email |varchar(255) |YES |None  | 注册人显示邮箱, |
|registra_abuse_contact_phone |varchar(100) |YES |None  | 注册人显示电话, |
|registra_iana _id |varchar(255) |YES |None  | IANA编号, |
|registrar_url |varchar(255) |YES |None  | 注册地址, |
|registrar_whois_server |varchar(255) |YES |None  | 注册Whois服务器地址 , |
|registry_admin_id |varchar(100) |YES |None  | 管理员ID, |
|registry_domain_id |varchar(100) |YES |None  | 域名iD, |
|registry_expiry_date |varchar(100) |YES |None  | 注册逾期时间, |
|registry_registrant_id |varchar(100) |YES |None  | 注册人编号, |
|registry_tech_id |varchar(100) |YES |None  | 技术人员编号, |
|reseller |varchar(100) |YES |None  | 销售者, |
|tech_city |varchar(100) |YES |None  | 技术人员城市, |
|tech_country |varchar(100) |YES |None  | 技术人员国家, |
|tech_email |varchar(255) |YES |None  | 技术人员邮箱, |
|tech_fax |varchar(100) |YES |None  | 技术人员传真, |
|tech_name |varchar(100) |YES |None  | 技术人员姓名, |
|tech_organization |varchar(255) |YES |None  | 技术人员组织, |
|tech_phone |varchar(100) |YES |None  | 技术人员电话, |
|tech_postal_code |varchar(100) |YES |None  | 技术人员邮编, |
|tech_state_province |varchar(100) |YES |None  | 技术人员省份, |
|tech_street |varchar(100) |YES |None  | 管理员街道, |
|updated_date |datetime |YES |None  | 状态更新时间, |
|whois_src |tinyint(4) |YES |None  | whois信息来源,0手动新增，1导入，2同步，3自动发现 |
|create_user |varchar(100) |YES |None  | 创建者,创建者 |
|create_date |datetime |YES |None  | 创建日期,创建日期 |
|update_user |varchar(100) |YES |None  | 更新者,更新者 |
## ti_whois_xyz_history
#### 描述: 
#### 字段总数: 69
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|xyz_id |int(11) |NO |None  | 自增长编号, |
|domain_name |varchar(255) |YES |None  | 域名,查询的域名地址 |
|registrar_addr |text |YES |None  | 域名归属,域名所有人姓名 |
|registrar_email |varchar(255) |YES |None  | 联系人信箱,域名所有人邮箱 |
|creation_date |datetime |YES |None  | 注册时间,域名注册时间 |
|expiry_date |datetime |YES |None  | 过期时间,域名逾期时间 |
|domain_id |varchar(100) |YES |None  | 域名注册编号, |
|status |text |YES |None  | 域名当前状态, |
|name_server |text |YES |None  | 域名解析服务器, |
|is_dbssec |tinyint(4) |YES |None  | 是否保护,DNSSEC是否开启 |
|admin_city |varchar(100) |YES |None  | 管理员城市, |
|admin_country |varchar(100) |YES |None  | 管理员国家, |
|admin_email |varchar(255) |YES |None  | 管理员邮箱, |
|admin_fax |varchar(100) |YES |None  | 管理员传真, |
|admin_name |varchar(100) |YES |None  | 管理员姓名, |
|admin_organization |varchar(100) |YES |None  | 管理员组织, |
|admin_phone |varchar(100) |YES |None  | 管理员电话, |
|admin_postal_code |varchar(100) |YES |None  | 管理员邮政编码, |
|admin_state_province |varchar(100) |YES |None  | 管理员省份, |
|admin_street |varchar(100) |YES |None  | 管理员街道, |
|billing_City |varchar(100) |YES |None  | 付费者城市, |
|billing_country |varchar(100) |YES |None  | 付费者国家, |
|billing_email |varchar(255) |YES |None  | 付费者邮箱, |
|billing_fax |varchar(100) |YES |None  | 付费者传真, |
|billing_name |varchar(100) |YES |None  | 付费者姓名, |
|billing_organization |varchar(100) |YES |None  | 付费者组织, |
|billing_phone |varchar(100) |YES |None  | 付费者电话, |
|billing_postal_code |varchar(100) |YES |None  | 付费者邮编, |
|billing_state_province |varchar(100) |YES |None  | 付费者省份, |
|Billing Street |varchar(100) |YES |None  | 付费者街道, |
|is_dnssec |tinyint(1) |YES |None  | DNS保护, |
|domain_status |varchar(255) |YES |None  | 域名状态, |
|registrant_city |varchar(100) |YES |None  | 注册人城市, |
|registrant_country |varchar(100) |YES |None  | 注册人国家, |
|registrant_email |varchar(255) |YES |None  | 注册人邮箱, |
|registrant_fax |varchar(100) |YES |None  | 注册人传真, |
|registrant_name |varchar(100) |YES |None  | 注册人姓名, |
|registrant_organization |varchar(255) |YES |None  | 注册人组织, |
|registrant_phone |varchar(100) |YES |None  | 注册人电话, |
|registrant_postal_code |varchar(100) |YES |None  | 注册人邮编, |
|registrant_state_province |varchar(100) |YES |None  | 注册人省份, |
|registrant_street |varchar(100) |YES |None  | 注册人街道, |
|registrar |varchar(100) |YES |None  | 注册人, |
|registrar_abuse_contact_email |varchar(255) |YES |None  | 注册人显示邮箱, |
|registra_abuse_contact_phone |varchar(100) |YES |None  | 注册人显示电话, |
|registra_iana _id |varchar(255) |YES |None  | IANA编号, |
|registrar_url |varchar(255) |YES |None  | 注册地址, |
|registrar_whois_server |varchar(255) |YES |None  | 注册Whois服务器地址 , |
|registry+admin_id |varchar(100) |YES |None  | 管理员ID, |
|registry_domain_id |varchar(100) |YES |None  | 域名iD, |
|registry_expiry_date |varchar(100) |YES |None  | 注册逾期时间, |
|registry_registrant_id |varchar(100) |YES |None  | 注册人编号, |
|registry_tech_id |varchar(100) |YES |None  | 技术人员编号, |
|reseller |varchar(100) |YES |None  | 销售者, |
|tech_city |varchar(100) |YES |None  | 技术人员城市, |
|tech_country |varchar(100) |YES |None  | 技术人员国家, |
|tech_email |varchar(255) |YES |None  | 技术人员邮箱, |
|tech_fax |varchar(100) |YES |None  | 技术人员传真, |
|tech_name |varchar(100) |YES |None  | 技术人员姓名, |
|tech_organization |varchar(255) |YES |None  | 技术人员组织, |
|tech_phone |varchar(100) |YES |None  | 技术人员电话, |
|tech_postal_code |varchar(100) |YES |None  | 技术人员邮编, |
|tech_state_province |varchar(100) |YES |None  | 技术人员省份, |
|tech_street |varchar(100) |YES |None  | 管理员街道, |
|updated_date |datetime |YES |None  | 状态更新时间, |
|whois_src |tinyint(4) |YES |None  | whois信息来源,0手动新增，1导入，2同步，3自动发现 |
|create_user |varchar(100) |YES |None  | 创建者,创建者 |
|create_date |datetime |YES |None  | 创建日期,创建日期 |
|update_user |varchar(100) |YES |None  | 更新者,更新者 |
## topo_line
#### 描述: 拓扑线--杨鹏
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|security_domain_id |bigint(20) |YES |None  |  |
|source |bigint(20) |YES |None  | 源资产ID |
|target |bigint(20) |YES |None  | 目的资产ID |
|points |varchar(1000) |YES |None  | 线的中间坐标点集合 |
|update_date |datetime |YES |None  |  |
|regenerator |varchar(32) |YES |None  | 更新人 |
## topo_node_pos
#### 描述: 拓扑节点--杨鹏
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|security_domain_id |bigint(20) |YES |None  |  |
|asset_id |bigint(20) |NO |None  | 资产id |
|x |double |YES |None  | x坐标点 |
|y |double |YES |None  | y坐标点 |
|update_date |datetime |YES |None  |  |
|regenerator |varchar(32) |YES |None  | 更新人 |
## ts_result
#### 描述: 溯源结果表
#### 字段总数: 5
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(50) |NO |None  |  |
|task_id |varchar(20) |YES |None  | 溯源任务ID |
|keyword |varchar(20) |YES |None  | 溯源关键字 ip ipc vpn |
|serial_number |int(11) |YES |None  | 数据展现序号 |
|data |text |YES |None  | 数据 |
## ts_tasks
#### 描述: 溯源任务表-陆建彬
#### 字段总数: 12
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(50) |NO |None  | ID |
|task_name |varchar(500) |YES |None  | 任务名称 |
|condition |varchar(500) |YES |None  | 条件/源信息 |
|task_category |int(11) |YES |None  | 任务分类 0：ip溯源 1：IPC段溯源 2：VPN溯源 |
|data_sources |varchar(500) |YES |None  | 数据源 多个数据源用逗号隔开 |
|start_time |datetime |YES |None  | 开始时间 |
|end_time |datetime |YES |None  | 结束时间 |
|user_name |varchar(50) |YES |None  | 创建人 |
|task_describe |varchar(500) |YES |None  | 任务描述 |
|notification |varchar(500) |YES |None  | 消息通知 1：消息通知，2邮件通知，3消息邮件都通知  即：01   10  11 |
|personnel_list |varchar(1000) |YES |None  | 通知人员列表 多个人员用，逗号隔开 |
|status |int(11) |YES |None  | 执行状态 0未运行 1运行中 2已完成 |
## ueba_account
#### 描述: 人员信息表
#### 字段总数: 42
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|account_id |int(11) |NO |None  | 自增id |
|account |varchar(255) |YES |None  | 账号 |
|age |int(11) |YES |None  | 年龄 |
|city |varchar(255) |YES |None  | 市/县 |
|common_browsers_fingerprints |varchar(255) |YES |None  | 常用浏览器指纹 |
|common_device |varchar(255) |YES |None  | 常用设备 |
|common_openid |varchar(255) |YES |None  | 常用Openid |
|common_url |varchar(255) |YES |None  | 常用地址 |
|country |varchar(255) |YES |None  | 国家/地区 |
|create_time |datetime |YES |None  | 创建时间 |
|create_user |varchar(255) |YES |None  | 创建用户 |
|department |varchar(255) |YES |None  | 部门 |
|edu_level |varchar(255) |YES |None  | 教育程度 |
|first_order_time |varchar(255) |YES |None  | 首单时间 |
|identity_card_no |varchar(255) |YES |None  | 身份证 |
|last_login_position |varchar(255) |YES |None  | 最后一次登录时间 |
|last_login_time |varchar(255) |YES |None  | 最后一次登录位置 |
|location |varchar(255) |YES |None  |  |
|menber_level |int(11) |YES |None  | 会员等级 |
|name |varchar(255) |YES |None  | 姓名 |
|org_id |int(11) |YES |None  | 账号组织机构ID |
|organization |varchar(255) |YES |None  | 账号组织机构名称 |
|pay_account |varchar(255) |YES |None  | 支付账号 |
|position |varchar(255) |YES |None  | 职务 |
|postal_code |varchar(255) |YES |None  | 邮政编码 |
|province |varchar(255) |YES |None  | 省/自治区 |
|register_position |varchar(255) |YES |None  | 注册地理位置 |
|register_time |varchar(255) |YES |None  | 注册时间 |
|status |varchar(255) |YES |None  | 账户状态 |
|street |varchar(255) |YES |None  | 街道 |
|tag |varchar(255) |YES |None  | 机器行为标签 |
|telephone_no |varchar(255) |YES |None  | 电话号码 |
|type |varchar(255) |YES |None  | 账号类型名称 |
|type_id |int(11) |YES |None  | 账号类型ID |
|update_time |datetime |YES |None  | 更新时间 |
|update_user |varchar(255) |YES |None  | 更新用户 |
|company |varchar(255) |YES |None  | 公司 |
|mobilephone_no |varchar(255) |YES |None  | 手机号码 |
|e_mail |varchar(255) |YES |None  | 邮箱 |
|user_id |varchar(255) |YES |None  | 用户id |
|user_integra |int(11) |YES |None  | 用户积分 |
|user_addr |varchar(255) |YES |None  | 用户地址 |
## ueba_area_ip
#### 描述: 
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|area_id |varchar(10) |NO |  |  |
|area_name |varchar(50) |YES |None  |  |
|area_ip |varchar(20) |YES |None  |  |
|area_type |varchar(50) |YES |None  |  |
## ueba_asset
#### 描述: 
#### 字段总数: 35
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|os_distro |varchar(200) |YES |None  |  |
|os_system |varchar(200) |YES |None  |  |
|os_version |varchar(100) |YES |None  |  |
|asset_value |varchar(20) |YES |None  |  |
|assets_src |varchar(32) |YES |None  |  |
|businesses_id |varchar(50) |YES |None  |  |
|businesses_name |varchar(32) |YES |None  |  |
|departments |varchar(32) |YES |None  |  |
|domain |varchar(128) |YES |None  |  |
|hostname |varchar(32) |YES |None  |  |
|important_asset_type |bit(1) |YES |None  |  |
|instanceid |varchar(50) |YES |None  |  |
|ip |varchar(32) |YES |None  |  |
|known_assets_type |bit(1) |YES |None  |  |
|macaddr |varchar(31) |YES |None  |  |
|maintainer_mail |varchar(32) |YES |None  |  |
|maintainer_name |varchar(32) |YES |None  |  |
|maintainer_phone |varchar(16) |YES |None  |  |
|manufacturer |varchar(32) |YES |None  |  |
|network_domain |varchar(100) |YES |None  |  |
|owner_email |varchar(32) |YES |None  |  |
|owner_name |varchar(32) |YES |None  |  |
|owner_phone |varchar(32) |YES |None  |  |
|public_ip |varchar(32) |YES |None  |  |
|regenerator |varchar(32) |YES |None  |  |
|remark |text |YES |None  |  |
|riskscore |int(11) |YES |None  |  |
|update_date |datetime |YES |None  |  |
|vendor |varchar(32) |YES |None  |  |
|create_time |datetime |YES |None  |  |
|create_user |varchar(255) |YES |None  |  |
|ip_address |varchar(255) |YES |None  |  |
|update_time |datetime |YES |None  |  |
|update_user |varchar(255) |YES |None  |  |
## ueba_baseline
#### 描述: 
#### 字段总数: 5
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|frequency |varchar(255) |YES |None  |  |
|generated_date |datetime |YES |None  |  |
|name |varchar(255) |YES |None  |  |
|quantity |bigint(20) |NO |None  |  |
## ueba_baseline_details
#### 描述: 
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|baseline_id |bigint(20) |NO |None  |  |
|key |varchar(45) |YES |None  |  |
|value |varchar(45) |YES |None  |  |
## ueba_danger_list
#### 描述: 名单信息表
#### 字段总数: 13
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  | 自增id |
|create_time |datetime |YES |None  | 创建时间 |
|create_user |varchar(255) |YES |None  | 创建用户 |
|effective_end_date |datetime |YES |None  | 失效日期 |
|effective_start_date |datetime |YES |None  | 生效日期 |
|name |varchar(255) |YES |None  | 名单值 |
|update_time |datetime |YES |None  | 更新时间 |
|update_user |varchar(255) |YES |None  | 更新用户 |
|tag_list |varchar(20) |YES |None  | 标签 |
|type |varchar(20) |YES |None  | 类型 |
|comment |varchar(255) |YES |None  | 备注 |
|content_type |int(20) |YES |None  | 子类型 |
|source |int(20) |YES |None  | 来源 |
## ueba_dept
#### 描述: 
#### 字段总数: 6
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|create_time |datetime |YES |None  |  |
|create_user |varchar(255) |YES |None  |  |
|name |varchar(255) |YES |None  |  |
|update_time |datetime |YES |None  |  |
|update_user |varchar(255) |YES |None  |  |
## ueba_dictionary_category
#### 描述: 
#### 字段总数: 8
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(255) |NO |None  |  |
|name |varchar(255) |YES |None  |  |
|comment |varchar(255) |YES |None  |  |
|parent_category_id |varchar(255) |NO |0  |  |
|create_user |varchar(255) |YES |None  |  |
|create_time |datetime |YES |None  |  |
|update_user |varchar(255) |YES |None  |  |
|update_time |datetime |YES |None  |  |
## ueba_dictionary_data
#### 描述: 
#### 字段总数: 18
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|alias |varchar(255) |YES |None  |  |
|category_id |varchar(255) |NO |None  |  |
|comment |varchar(255) |YES |None  |  |
|create_time |datetime |YES |None  |  |
|data_type |varchar(255) |YES |None  |  |
|name |varchar(255) |YES |None  |  |
|parent_dict_id |bigint(20) |NO |0  |  |
|update_time |datetime |YES |None  |  |
|update_user |varchar(255) |YES |None  |  |
|create_user |varchar(255) |YES |None  |  |
|argument |varchar(255) |YES |None  |  |
|seg1 |varchar(255) |YES |None  |  |
|seg1desc |varchar(255) |YES |None  |  |
|seg2 |varchar(255) |YES |None  |  |
|seg2desc |varchar(255) |YES |None  |  |
|seg3 |varchar(255) |YES |None  |  |
|seg3desc |varchar(255) |YES |None  |  |
## ueba_filter_agg
#### 描述: 
#### 字段总数: 6
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|data_collection1 |bigint(20) |NO |None  |  |
|data_collection2 |bigint(20) |NO |None  |  |
|key_by1 |varchar(255) |YES |None  |  |
|key_by2 |varchar(255) |YES |None  |  |
|rule_config_id |bigint(20) |NO |None  |  |
## ueba_filter_config
#### 描述: 
#### 字段总数: 6
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|create_time |datetime |YES |None  |  |
|create_user |varchar(255) |YES |None  |  |
|strategy_id |bigint(20) |NO |None  |  |
|update_time |datetime |YES |None  |  |
|update_user |varchar(255) |YES |None  |  |
## ueba_filter_rule
#### 描述: 
#### 字段总数: 5
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|double_data_flow |varchar(255) |YES |None  |  |
|relation |varchar(255) |YES |None  |  |
|rule_config_id |bigint(20) |NO |None  |  |
|rules |varchar(2048) |YES |None  |  |
## ueba_list_tag
#### 描述: 
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|create_time |datetime |YES |None  |  |
|create_user |varchar(255) |YES |None  |  |
|name |varchar(255) |YES |None  |  |
|update_time |datetime |YES |None  |  |
|update_user |varchar(255) |YES |None  |  |
|list_id |varchar(255) |YES |None  |  |
## ueba_list_type
#### 描述: 
#### 字段总数: 6
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|create_time |datetime |YES |None  |  |
|create_user |varchar(255) |YES |None  |  |
|name |varchar(255) |YES |None  |  |
|update_time |datetime |YES |None  |  |
|update_user |varchar(255) |YES |None  |  |
## ueba_main_account
#### 描述: 
#### 字段总数: 13
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|main_account_id |varchar(10) |NO |  |  |
|user_name |varchar(20) |YES |None  |  |
|lock_status |varchar(10) |YES |None  |  |
|effect_time |datetime |YES |None  |  |
|exprie_time |datetime |YES |None  |  |
|last_login_time |datetime |YES |None  |  |
|person_name |varchar(20) |YES |None  |  |
|org_id |varchar(10) |YES |None  |  |
|org_name |varchar(100) |YES |None  |  |
|main_role_id |varchar(10) |YES |None  |  |
|main_role_name |varchar(100) |YES |None  |  |
|main_account_tel |varchar(20) |YES |None  |  |
|main_account_email |varchar(50) |YES |None  |  |
## ueba_netloc
#### 描述: 
#### 字段总数: 6
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|create_time |datetime |YES |None  |  |
|create_user |varchar(255) |YES |None  |  |
|name |varchar(255) |YES |None  |  |
|update_time |datetime |YES |None  |  |
|update_user |varchar(255) |YES |None  |  |
## ueba_org_tag
#### 描述: 
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|tag_name |varchar(50) |YES |None  |  |
|tag_org_id |varchar(10) |YES |None  |  |
|tag_create_time |datetime |YES |None  |  |
## ueba_port
#### 描述: 
#### 字段总数: 13
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|ip_address |varchar(255) |YES |None  |  |
|open_port |varchar(255) |YES |None  |  |
|port_type |varchar(255) |YES |None  |  |
|service_app_banner |varchar(255) |YES |None  |  |
|service_app_name |varchar(255) |YES |None  |  |
|service_app_version |varchar(255) |YES |None  |  |
|service_type |varchar(255) |YES |None  |  |
|port_id |int(11) |NO |None  |  |
|ipaddr |varchar(255) |YES |None  |  |
|port |int(11) |YES |None  |  |
|service |varchar(255) |YES |None  |  |
|service_v |varchar(255) |YES |None  |  |
## ueba_salve_account
#### 描述: 
#### 字段总数: 6
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|slacct_id |varchar(10) |NO |  |  |
|slacct_account_name |varchar(50) |YES |None  |  |
|main_account_id |varchar(10) |YES |None  |  |
|domain_id |varchar(10) |YES |None  |  |
|domian_name |varchar(50) |YES |None  |  |
|slacct_person_name |varchar(50) |YES |None  |  |
## ueba_strategy
#### 描述: 
#### 字段总数: 17
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|action_condition_id |int(11) |YES |None  |  |
|action_config_id |int(11) |YES |None  |  |
|create_time |datetime |YES |None  |  |
|create_user |varchar(255) |YES |None  |  |
|dataset_one_id |int(11) |YES |None  |  |
|dataset_two_id |int(11) |YES |None  |  |
|edit_status |int(11) |YES |None  |  |
|filter_id |int(11) |YES |None  |  |
|job_id |varchar(255) |YES |None  |  |
|name |varchar(255) |YES |None  |  |
|risk_type |int(11) |YES |None  |  |
|scene |varchar(255) |YES |  |  |
|status |int(11) |YES |None  |  |
|time_window_id |int(11) |YES |None  |  |
|type |varchar(255) |YES |None  |  |
|description |varchar(255) |YES |None  |  |
## ueba_strategy_action
#### 描述: 
#### 字段总数: 11
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|alarm_condition |varchar(255) |YES |None  |  |
|kill_chain_stage |int(255) |YES |None  |  |
|mail_address |varchar(255) |YES |None  |  |
|mail_notice |bit(1) |YES |None  |  |
|risk_score |int(11) |YES |None  |  |
|risk_type |int(11) |YES |None  |  |
|strategy_id |int(11) |YES |None  |  |
|internal_event |bit(1) |YES |None  |  |
|risk_level |int(11) |YES |None  |  |
|event_type |int(11) |YES |None  |  |
## ueba_strategy_dataset
#### 描述: 
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|condition_relation |text |YES |None  |  |
|name |varchar(255) |YES |None  |  |
|data_source |varchar(255) |YES |None  |  |
## ueba_strategy_output
#### 描述: 
#### 字段总数: 6
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|add_list |bit(1) |YES |None  |  |
|filed |varchar(11) |YES |None  |  |
|list_id |int(11) |YES |None  |  |
|strategy_id |int(11) |YES |None  |  |
|value_type |varchar(255) |YES |None  |  |
## ueba_strategy_repeat
#### 描述: 
#### 字段总数: 6
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|repace_time |varchar(255) |YES |None  |  |
|repace_type |varchar(255) |YES |None  |  |
|repace_value |varchar(255) |YES |None  |  |
|strategy_id |int(11) |YES |None  |  |
|timer_cron |varchar(255) |YES |None  |  |
## ueba_strategy_timewindow
#### 描述: 
#### 字段总数: 9
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|type |varchar(255) |YES |None  |  |
|step |int(11) |YES |None  |  |
|step_type |varchar(255) |YES |None  |  |
|strategy_id |int(11) |YES |None  |  |
|time_end |datetime |YES |None  |  |
|time_start |datetime |YES |None  |  |
|window |int(11) |YES |None  |  |
|window_type |varchar(255) |YES |None  |  |
## ueba_user_organization
#### 描述: 
#### 字段总数: 3
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|org_id |varchar(10) |NO |  | 组织机构ID |
|parent_id |varchar(10) |YES |None  | 组织机构父ID |
|org_name |varchar(50) |YES |None  | 组织机构名 |
## ueba_user_tag
#### 描述: 
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|user_tag_id |varchar(10) |NO |  |  |
|tag_name |varchar(100) |YES |None  |  |
|tag_main_account_id |varchar(10) |YES |None  |  |
|tag_create_time |datetime |YES |None  |  |
## ueba_webservice
#### 描述: 
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|ip_address |varchar(255) |YES |None  |  |
|open_port |varchar(255) |YES |None  |  |
|service_app_banner |varchar(255) |YES |None  |  |
|service_app_name |varchar(255) |YES |None  |  |
|service_app_version |varchar(255) |YES |None  |  |
|web_finger_print |varchar(255) |YES |None  |  |
## ums_com_email
#### 描述: 
#### 字段总数: 11
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|email_id |varchar(10) |NO |None  | 邮件序号 |
|name |varchar(255) |YES |None  | 配置名称 |
|smtp |varchar(255) |YES |None  | 邮件smtp服务器 |
|smtp_port |varchar(10) |YES |None  | 发送端口 |
|user_name |varchar(96) |NO |None  | 邮件用户名 |
|password |varchar(32) |NO |None  | 邮件密码 |
|encryption |tinyint(1) |YES |None  | 是否SSL加密:
0:普通发送
1:SSL加密发送 |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新日期 |
## ums_com_email_content
#### 描述: 
#### 字段总数: 14
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|email_id |varchar(10) |NO |None  | 邮件序号 |
|content_id |varchar(10) |NO |None  | 内容序号 |
|from_person |varchar(100) |YES |None  | 发信人 |
|title |varchar(500) |NO |None  | 邮件标题 |
|content1 |text |YES |None  | 内容1 |
|content2 |text |YES |None  | 内容2 |
|content3 |text |YES |None  | 内容3 |
|content4 |text |YES |None  | 内容4 |
|content5 |text |YES |None  | 内容5 |
|content6 |text |YES |None  | 内容6 |
|content7 |text |YES |None  | 内容7 |
|content8 |text |YES |None  | 内容8 |
|content9 |text |YES |None  | 内容9 |
|content10 |text |YES |None  | 内容10 |
## ums_sys_dept
#### 描述: 
#### 字段总数: 10
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|dept_id |varchar(32) |NO |None  | 部门编号 |
|parent_dept_id |varchar(32) |NO |None  | 上级部门编号 |
|dept_name |varchar(32) |NO |None  | 部门名称 |
|dept_describe |varchar(255) |YES |None  | 部门描述 |
|dept_sort |int(3) |YES |None  | 部门排序 |
|del_flag |tinyint(1) |NO |None  | 删除标识
0:未删除
1:已删除 |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新日期 |
## ums_sys_function_url
#### 描述: 
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|function_url_id |int(11) |NO |None  | 功能url编号 |
|function_id |char(32) |NO |None  | 功能编号 |
|url_id |char(32) |NO |None  | url编号 |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新日期 |
## ums_sys_permission_data
#### 描述: 
#### 字段总数: 10
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|data_id |varchar(32) |NO |None  | 数据权限编号 |
|parent_data_id |varchar(32) |NO |None  | 上级数据权限编号 |
|external_id |varchar(100) |NO |None  | 外部权限编号 |
|data_name |varchar(32) |NO |None  | 数据权限名称 |
|data_describe |varchar(255) |YES |None  | 数据权限描述 |
|perms |varchar(100) |YES |None  | 数据权限标识 |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新日期 |
## ums_sys_permission_function
#### 描述: 
#### 字段总数: 9
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|function_id |varchar(32) |NO |None  | 功能分类 |
|parent_function_id |varchar(32) |NO |None  | 上级功能编号 |
|function_name |varchar(100) |NO |None  | 功能名称 |
|function_describe |varchar(255) |YES |None  | 功能描述 |
|function_type |tinyint(1) |YES |None  | 操作权限类型：0:页面,1:普通api,2:特殊通道api |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新日期 |
## ums_sys_role
#### 描述: 
#### 字段总数: 9
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|role_id |varchar(32) |NO |None  | 角色编号 |
|role_name |varchar(32) |NO |None  | 角色名称 |
|role_describe |varchar(255) |YES |None  | 角色描述 |
|builtin |tinyint(1) |NO |None  | 是否预置
 0：预置
 1：未预置 |
|del_flag |tinyint(1) |NO |None  | 删除标识
0:未删除
1:已删除 |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新日期 |
## ums_sys_role_data
#### 描述: 
#### 字段总数: 8
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|role_data_id |int(11) |NO |None  | 角色数据权限编号 |
|role_id |varchar(32) |NO |None  | 角色编号 |
|data_id |varchar(32) |NO |None  | 数据权限编号 |
|mode |tinyint(1) |YES |None  | 暂不使用 |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新日期 |
## ums_sys_role_function
#### 描述: 
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|role_function_id |int(11) |NO |None  | 角色操作权限编号 |
|role_id |varchar(32) |NO |None  | 角色编号 |
|function_id |varchar(32) |NO |None  | 功能编号 |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新日期 |
## ums_sys_url
#### 描述: 
#### 字段总数: 9
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|url_id |varchar(32) |NO |None  | url编号 |
|url_name |varchar(100) |NO |None  | url名称 |
|url_path |varchar(255) |NO |None  | url路径 |
|url_method |varchar(10) |NO |None  | 请求方式 |
|url_describe |varchar(255) |YES |None  | url描述 |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(199) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新日期 |
## ums_sys_user
#### 描述: 
#### 字段总数: 26
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|user_id |varchar(32) |NO |None  | 用户编号 |
|dept_id |varchar(32) |YES |None  | 部门编号 |
|user_name |varchar(100) |NO |None  | 用户名 |
|password |varchar(32) |NO |None  | 密码 |
|password_old |varchar(32) |YES |None  | 旧密码 |
|period_from |date |NO |None  | 账号使用开始日 |
|period_to |date |NO |None  | 账号使用结束日 |
|status |tinyint(1) |NO |None  | 状态
0：正常
1：锁定 |
|real_name |varchar(32) |YES |None  | 员工姓名 |
|code |varchar(100) |YES |None  | 员工工号 |
|sex |varchar(1) |YES |None  | 员工性别
0:男
1:女 |
|telephone |varchar(11) |YES |None  | 联系电话 |
|email |varchar(100) |NO |None  | 电子邮箱 |
|leader |varchar(100) |YES |None  | 直属领导 |
|login_voucher |varchar(100) |YES |None  | 单点登录凭证 |
|fail_count |int(11) |YES |None  | 失败次数 |
|lock_date |datetime |YES |None  | 锁定日期 |
|final_login_ip |varchar(15) |YES |None  | 最后登录ip |
|final_login_date |date |YES |None  | 最后登录时间 |
|builtin |tinyint(1) |NO |None  | 是否预置
0：预置
1：未预置 |
|security_code |varchar(128) |YES |None  |  |
|del_flag |tinyint(1) |NO |None  | 删除标识
0:未删除
1:已删除 |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新日期 |
## ums_sys_user_role
#### 描述: 
#### 字段总数: 7
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|user_role_id |int(11) |NO |None  | 人员角色编号 |
|user_id |varchar(32) |NO |None  | 用户编号 |
|role_id |varchar(32) |NO |None  | 角色编号 |
|create_user |varchar(100) |YES |None  | 创建者 |
|create_date |datetime |YES |None  | 创建日期 |
|update_user |varchar(100) |YES |None  | 更新者 |
|update_date |datetime |YES |None  | 更新日期 |
## weak_analysis
#### 描述: 
#### 字段总数: 12
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  | 唯一标识 |
|dst_ip |varchar(15) |YES |None  | 资产名或者资产ip |
|alarm_id |varchar(200) |YES |None  | 告警编号 |
|alarm_name |varchar(200) |YES |None  | 告警名称 |
|alarm_event_name |varchar(200) |YES |None  | 告警事件 |
|src_hostname |varchar(200) |YES |None  | 主机名 |
|src_ip |varchar(15) |YES |None  | 源ip |
|alarm_type |varchar(200) |YES |None  | 告警类型 |
|alarm_content |varchar(200) |YES |None  | 告警内容 |
|create_time |bigint(20) |NO |None  | 事件发生时间 |
|weak_type |varchar(1) |NO |None  | 1:漏洞利用，2：配置不合规，3：弱口令 |
|weak_num |int(11) |NO |None  | 记录攻击了多少次 |
## web_shell_history
#### 描述: 历史累计维度存储表
#### 字段总数: 9
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(200) |NO |None  |  |
|domain |varchar(200) |YES |None  | 域名 |
|business_system |varchar(200) |YES |None  | 业务系统 |
|url |varchar(8000) |YES |None  | 请求url |
|first_interview |bigint(20) |YES |None  | 页面初次访问时间 |
|latest_visit_time |bigint(20) |YES |None  | 页面最新访问时间 |
|exposure_days |int(11) |YES |None  | 页面曝光天数（如页面第一次1月1号访问，最后一次1月25号访问过，则计数为25） |
|history_days |int(11) |YES |None  | 如页面只在1月1号，1月25号访问过，则计数为2） |
|update_time |bigint(20) |YES |None  | 记录更新时间 |
## whois_result
#### 描述: whois任务结果--杨鹏
#### 字段总数: 14
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|domain |varchar(255) |YES |None  |  |
|version |int(11) |YES |None  |  |
|regist_id |varchar(255) |YES |None  | 注册号 |
|whois_server |varchar(255) |YES |None  |  |
|registrar |varchar(255) |YES |None  | 域名归属 |
|regist_date |datetime |YES |None  | 注册时间 |
|expiry_date |datetime |YES |None  | 到期时间 |
|update_date |datetime |YES |None  | 更新时间 |
|contact_email |varchar(255) |YES |None  | 邮箱 |
|contact_phone |varchar(255) |YES |None  | 联系电话 |
|status |varchar(50) |YES |None  | 域名状态 |
|record |varchar(255) |YES |None  | 备案号 |
|regenerator |varchar(32) |YES |None  | 更新人 |
