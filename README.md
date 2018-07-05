## asset
#### 描述: 
#### 字段总数: 34
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|instanceid |varchar(50) |YES |None  | 主机ID |
|ipv4 |varchar(32) |YES |None  |  |
|ipv6 |varchar(32) |YES |None  |  |
|vip |varchar(32) |YES |None  |  |
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
|important_asset_type |tinyint(1) |YES |1  | 是否重要资产 |
|virtual_host |tinyint(1) |YES |0  | 是否虚拟主机 |
|owner_name |varchar(32) |YES |None  | 负责人 |
|vendor |varchar(32) |YES |None  | 设备厂商 |
|known_assets_type |tinyint(1) |YES |0  | 是否已知资产 |
|physical_position |varchar(100) |YES |None  | 物理位置 |
|network_domain_id |bigint(20) |YES |None  | 对应于property_tree里的资产域id |
|riskscore |int(3) |YES |None  | riskscore |
|asset_value |varchar(20) |YES |None  | 资产价值 |
|purpose |text |YES |None  | 用途 |
|gj_yj |tinyint(1) |YES |None  | 是否告警/预警 0：告警 1：未告警 2：预警 3.未预警 |
|manufacturer |varchar(32) |YES |None  | 设备维护厂商 |
|maintainer_name |varchar(32) |YES |None  | 设备维护联系人 |
|maintainer_phone |varchar(16) |YES |None  | 设备维护联系人电话 |
|maintainer_mail |varchar(32) |YES |None  | 设备维护联系人邮箱 |
|remark |text |YES |None  | 设备维护备注说明 |
|update_date |datetime |YES |None  |  |
|regenerator |varchar(32) |YES |None  | 更新人 |
|assets_src_type |tinyint(1) |YES |1  | 资产来源 1:批量导入 2:人工添加 3:流量解析 4:日志解析 |
## cmdb_hosts
#### 描述: 国信cmdb资产表-牛虹
#### 字段总数: 12
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
## custom_threshold
#### 描述: 
#### 字段总数: 3
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|ct_name |varchar(200) |YES |None  |  |
|ct_value |int(11) |NO |None  |  |
## da_component
#### 描述: 
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
#### 描述: 大盘主表
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
## da_dashboard
#### 描述: 大盘主表
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
## da_dictionary
#### 描述: 字典信息表
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
#### 描述: 组件组表
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
## dns_result
#### 描述: 
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
#### 描述: 
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) unsigned |NO |None  |  |
|date_format |varchar(255) |YES |None  |  |
|date_example |varchar(255) |YES |None  |  |
|locale |varchar(255) |YES |None  |  |
## etl_dict_define
#### 描述: 
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) unsigned |NO |None  |  |
|dict_name |varchar(255) |NO |  |  |
|dict_ch_name |varchar(1024) |NO |  |  |
|dict_schema |text |NO |None  |  |
## etl_global_field
#### 描述: 
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) unsigned |NO |None  |  |
|field_name |varchar(255) |YES |None  |  |
|field_type |varchar(255) |YES |None  |  |
|field_ch_name |varchar(1024) |YES |None  |  |
## etl_job
#### 描述: 
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
#### 描述: 
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
#### 描述: 
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
#### 描述: 
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
#### 描述: 
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
#### 描述: 
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
#### 描述: 
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|job_serial_number |varchar(50) |YES |None  | job流水号 |
|conf_content |varchar(3000) |YES |None  | 配置内容 |
|state |int(2) |YES |None  | 状态 |
## etl_task_output_status
#### 描述: 
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
## event_investigation_task
#### 描述: 事件调查任务
#### 字段总数: 5
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|task_id |int(11) |NO |None  | 事件调查任务自增id |
|task_name |varchar(250) |YES |None  | 事件调查任务名称 |
|task_describe |text |YES |None  | 事件调查任务描述 |
|operation_time |date |YES |None  | 事件调查任务创建时间 |
|operation_name |varchar(250) |YES |None  | 事件调查任务创建用户 |
## event_investigation_users_middle
#### 描述: 事件调查任务分享用户中间表
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 自增id |
|task_id |int(11) |YES |None  | 任务id |
|user_id |int(11) |YES |None  | 被分享用户id |
|user_name |varchar(255) |YES |None  | 被分享用户姓名 |
## event_tag
#### 描述: 事件标签表
#### 字段总数: 3
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|tag_id |int(11) |NO |None  | 标签自增id |
|tag_name |varchar(150) |YES |None  | 标签名称 |
|tag_score |bigint(20) |YES |None  | 标签打分 |
## event_tag_middle
#### 描述: 事件标签与事件中间表
#### 字段总数: 4
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  | 自增id |
|event_id |int(11) |YES |None  | 事件id |
|tag_id |int(11) |YES |None  | 标签id |
|tag_name |varchar(250) |YES |None  | 标签名称 |
## event_task_relation
#### 描述: 事件调查任务关联细表
#### 字段总数: 26
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
|event_severity |int(11) |YES |None  | 事件危险级别 |
|task_id |int(11) |YES |None  | 事件所属任务id |
|operatiom_time |datetime |YES |None  | 事件加入任务时间 |
|log_start_time |datetime |YES |None  | 日志开始时间 |
|log_end_time |datetime |YES |None  | 日志结束时间 |
|event_focus_point |varchar(250) |YES |None  | 时间关注点 |
|relation_type |varchar(250) |YES |None  | 任务关联类型 |
|trace_task_name |varchar(500) |YES |None  | 溯源任务名称 |
|trace_condition |varchar(500) |YES |None  | 溯源任务条件/源信息 |
|trace_task_category |int(11) |YES |None  | 溯源任务分类 |
|trace_start_time |datetime |YES |None  | 溯源开始时间 |
|trace_end_time |datetime |YES |None  | 溯源结束时间 |
|trace_user_name |varchar(50) |YES |None  | 溯源创建人 |
|trace_task_desc |text |YES |None  | 溯源任务描述 |
|trace_status |int(11) |YES |None  | 溯源0未运行 1运行中 2已完成 |
## external_asset_task_detail
#### 描述: 
#### 字段总数: 8
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|domain |varchar(255) |NO |None  | 域名 |
|task_type |tinyint(4) |NO |None  |  |
|call_back_keys |varchar(255) |YES |None  | 回调服务的key列表，以逗号分隔 |
|version |int(11) |NO |0  | 版本号，任务启动时进行+1更新 |
|status |tinyint(4) |NO |0  | 0:等待执行，1:执行中 |
|update_date |datetime |YES |None  |  |
|regenerator |varchar(32) |YES |None  | 更新人 |
## external_asset_task_info
#### 描述: 
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
#### 描述: 
#### 字段总数: 2
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|festival_day |varchar(8) |NO |None  |  |
|festival_comment |varchar(255) |YES |None  |  |
## fs_search_params
#### 描述: 
#### 字段总数: 10
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(100) |NO |None  | id |
|name |varchar(100) |NO |None  | 查询条件名称 |
|start_time |varchar(20) |NO |None  | 查询起始时间 |
|end_time |varchar(20) |NO |None  | 查询结束时间 |
|param_indexs |varchar(500) |YES |None  | 查询索引，多个索引用“，”分割 |
|param_colums |varchar(500) |YES |None  | 查询列明，多列用“，”分割 |
|like_param |varchar(500) |YES |None  | 正则匹配，或模糊条件 |
|user_name |varchar(100) |NO |None  | 当前登录用户 |
|comment |varchar(500) |YES |None  | 注释说明 |
|search_type |varchar(2) |YES |None  |  |
## ga_access_authority
#### 描述: 角色访问权限表
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
#### 描述: 系统访问日志表
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
#### 描述: 字典信息表
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
#### 描述: 用户组信息表
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
## ga_menu
#### 描述: 菜单信息表
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
#### 描述: 站内消息/邮件提醒表
#### 字段总数: 9
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|message_id |varchar(50) |NO |None  | 消息ID |
|title |varchar(255) |YES |None  | 标题/邮件主题 |
|text |text |YES |None  | 内容/邮件正文 |
|mail_receiver |varchar(50) |YES |None  | 邮件接收人(邮件地址) |
|status |varchar(2) |YES |None  | 已读1/未读0(站内消息已读未读,如果有需求指定人员,需分细表) |
|send_type |varchar(2) |YES |None  | 发送源: 1规则引擎/2态势预警 |
|message_type |varchar(2) |YES |None  | 消息类型:1站内消息/2邮件消息/3站内和邮件 |
|send_time |datetime |YES |None  | 发送日期时间 |
|user_id |varchar(50) |YES |None  | 站内信指定某人(需确认是否有此需求) |
## ga_page_oper
#### 描述: 用户操作信息表
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
#### 描述: 用户策略表
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
#### 描述: 角色信息表
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
#### 描述: 用户信息表
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
#### 描述: 用户信息表
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
## health_cofiguration_host
#### 描述: 
#### 字段总数: 17
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(32) |NO |None  | 服务器监控配置表 |
|ip |varchar(15) |YES |None  |  |
|cpu_operator |tinyint(1) |YES |None  | 1:大于
2:大于等于
3:等于
4:小于
5:小于等于 |
|cpu_val |varchar(8) |YES |None  |  |
|cpu_flg |tinyint(1) |YES |None  | 0:不监控
1:监控 |
|mem_operator |tinyint(1) |YES |None  | 1:大于
2:大于等于
3:等于
4:小于
5:小于等于 |
|mem_val |varchar(8) |YES |None  |  |
|mem_flg |tinyint(1) |YES |None  | 0:不监控
1:监控 |
|disk_operator |tinyint(1) |YES |None  | 1:大于
2:大于等于
3:等于
4:小于
5:小于等于 |
|disk_val |varchar(8) |YES |None  |  |
|disk_flg |tinyint(1) |YES |None  | 0:不监控
1:监控 |
|network_operator |tinyint(1) |YES |None  | 1:大于
2:大于等于
3:等于
4:小于
5:小于等于 |
|network_val |varchar(64) |YES |None  |  |
|network_flg |tinyint(4) |YES |None  | 0:不监控
1:监控 |
|show_flg |tinyint(1) |YES |None  | 0:关（不显示）
1:开（显示 |
|create_user |varchar(64) |YES |None  |  |
|create_time |datetime |YES |None  |  |
## health_cofiguration_module
#### 描述: 
#### 字段总数: 13
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |varchar(32) |NO |None  | 服务器监控配置表 |
|module |varchar(32) |YES |None  |  |
|ip |text |YES |None  |  |
|cpu_operator |tinyint(1) |YES |None  | 1:大于
2:大于等于
3:等于
4:小于
5:小于等于 |
|cpu_val |varchar(8) |YES |None  |  |
|cpu_flg |tinyint(1) |YES |None  | 0:不监控
1:监控 |
|mem_operator |tinyint(1) |YES |None  | 1:大于
2:大于等于
3:等于
4:小于
5:小于等于 |
|mem_val |varchar(8) |YES |None  |  |
|mem_flg |tinyint(1) |YES |None  | 0:不监控
1:监控 |
|process_flg |tinyint(1) |YES |None  | 0:不监控
1:监控 |
|show_flg |tinyint(1) |YES |None  | 0:关（不显示）
1:开（显示 |
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
#### 描述: 
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
#### 描述: 
#### 字段总数: 5
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(12) |NO |None  | 主键 |
|domain_name |varchar(512) |NO |None  | 域名 |
|app_business |varchar(100) |YES |None  | 业务系统 |
|model_type |int(2) |NO |None  | 模型类型, 1:单页面, 2单用户 |
|status |int(2) |NO |0  | 状态, 0:禁用, 1:启用 |
## property_tree
#### 描述: 
#### 字段总数: 6
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|type |int(11) |NO |1  | 1:资产域 2:资产类型 |
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
#### 描述: 
#### 字段总数: 6
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|sub_domain |varchar(255) |NO |None  |  |
|alive |tinyint(1) |NO |0  | 是否存活 0:否，1：是 |
|version |int(11) |NO |None  |  |
|update_date |datetime |YES |None  |  |
|regenerator |varchar(32) |YES |None  | 更新人 |
## sys_connectiontest
#### 描述: 
#### 字段总数: 1
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|a |char(1) |YES |None  |  |
## ta_eqpt_patch
#### 描述: 
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
#### 描述: 关联规则表
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
#### 描述: 关联规则分类
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
#### 描述: 规则条件表
#### 字段总数: 5
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|analyzer_id |int(11) |NO |None  |  |
|filter_id |int(11) |NO |None  |  |
|count |int(4) |NO |1  |  |
|timewindow |int(4) |NO |None  | 单位 秒 |
## tb_analyzer_desc
#### 描述: 关联事件描述表
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
#### 描述: 关联规则归并表
#### 字段总数: 5
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |int(11) |NO |None  |  |
|type |int(1) |NO |0  | 0相同 1不同 |
|analyzer_id |int(11) |NO |None  |  |
|filter_id |int(11) |NO |None  |  |
|field |varchar(20) |NO |None  |  |
## tb_analyzer_join
#### 描述: 关联规则条件关联表
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
#### 描述: 过滤器
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
#### 描述: 过滤器分类
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
#### 描述: 过滤器明细表
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
#### 描述: 名单表
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
#### 描述: 名单详细信息
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
## topo_line
#### 描述: 
#### 字段总数: 6
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|source |bigint(20) |YES |None  | 源资产ID |
|target |bigint(20) |YES |None  | 目的资产ID |
|points |varchar(1000) |YES |None  | 线的中间坐标点集合 |
|update_date |datetime |YES |None  |  |
|regenerator |varchar(32) |YES |None  | 更新人 |
## topo_node_pos
#### 描述: 
#### 字段总数: 6
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|asset_id |bigint(20) |NO |None  | 资产id |
|x |double |YES |None  | x坐标点 |
|y |double |YES |None  | y坐标点 |
|update_date |datetime |YES |None  |  |
|regenerator |varchar(32) |YES |None  | 更新人 |
## trace_source_tasks
#### 描述: 
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
#### 描述: 
#### 字段总数: 10
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|id |bigint(20) |NO |None  |  |
|create_time |datetime |YES |None  |  |
|create_user |varchar(255) |YES |None  |  |
|effective_end_date |datetime |YES |None  |  |
|effective_start_date |datetime |YES |None  |  |
|name |varchar(255) |YES |None  |  |
|update_time |datetime |YES |None  |  |
|update_user |varchar(255) |YES |None  |  |
|tag_id |bigint(20) |YES |None  |  |
|type_id |bigint(20) |YES |None  |  |
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
## ueba_list_tag
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
## ueba_port
#### 描述: 
#### 字段总数: 8
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
## ueba_staff
#### 描述: 
#### 字段总数: 40
|字段|类型|允许空|默认|注释|
|:----    |:-------    |:--- |----|------      |
|user_id |int(11) |NO |None  |  |
|account |varchar(255) |YES |None  |  |
|age |int(11) |YES |None  |  |
|city |varchar(255) |YES |None  |  |
|common_browsers_fingerprints |varchar(255) |YES |None  |  |
|common_device |varchar(255) |YES |None  |  |
|common_openid |varchar(255) |YES |None  |  |
|common_url |varchar(255) |YES |None  |  |
|country |varchar(255) |YES |None  |  |
|create_time |datetime |YES |None  |  |
|create_user |varchar(255) |YES |None  |  |
|department |varchar(255) |YES |None  |  |
|e_mail |varchar(255) |YES |None  |  |
|edu_level |varchar(255) |YES |None  |  |
|employee_type |varchar(255) |YES |None  |  |
|first_order_time |varchar(255) |YES |None  |  |
|follow_user_list |varchar(255) |YES |None  |  |
|icon |varchar(255) |YES |None  |  |
|identity_card_no |varchar(255) |YES |None  |  |
|last_login_position |varchar(255) |YES |None  |  |
|last_login_time |varchar(255) |YES |None  |  |
|location |varchar(255) |YES |None  |  |
|menber_level |varchar(255) |YES |None  |  |
|org_id |int(11) |YES |None  |  |
|organization |varchar(255) |YES |None  |  |
|pay_account |varchar(255) |YES |None  |  |
|position |varchar(255) |YES |None  |  |
|postal_code |varchar(255) |YES |None  |  |
|province |varchar(255) |YES |None  |  |
|register_position |varchar(255) |YES |None  |  |
|register_time |varchar(255) |YES |None  |  |
|status |varchar(255) |YES |None  |  |
|street |varchar(255) |YES |None  |  |
|tag |varchar(255) |YES |None  |  |
|telephone_no |varchar(255) |YES |None  |  |
|type |int(11) |YES |None  |  |
|type_id |int(11) |YES |None  |  |
|update_time |datetime |YES |None  |  |
|update_user |varchar(255) |YES |None  |  |
|user_name |varchar(255) |YES |None  |  |
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
## whois_result
#### 描述: 
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
