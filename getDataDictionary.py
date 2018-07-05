#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
db = MySQLdb.connect("localhost", "root", "idss@123!@#", "cyber", charset='utf8' )
cursor = db.cursor()
sql_table = "SELECT	\
	TABLE_NAME,TABLE_COMMENT	\
	FROM	\
	information_schema.`TABLES`	\
	WHERE	\
	table_schema = 'cyber' and TABLE_TYPE = 'BASE TABLE'	\
	order by TABLE_NAME"
f = open("README.md", "w")
#try:
# 执行SQL语句,查询所有表名
cursor.execute(sql_table)
# 获取所有表名记录
results_table = cursor.fetchall()
for row in results_table:
	TABLE_NAME = row[0]
	TABLE_COMMENT = row[1]
	# 打印结果
	f.write("## %s\n" % (TABLE_NAME))
	f.write("#### 描述: %s\n" % (TABLE_COMMENT))
	sql = "SELECT	\
        	count(*) \
	FROM  \
		information_schema. COLUMNS  \
	WHERE  \
		table_schema = 'cyber' and TABLE_NAME='%s' \
	ORDER BY  \
		TABLE_SCHEMA,  \
		TABLE_NAME,  \
		ORDINAL_POSITION" % (TABLE_NAME)
	# 执行sql,查询当前表的所有字段
	cursor.execute(sql)
	# 获取当前表的所有字段
	cnt = cursor.fetchone()
	f.write("#### 字段总数: %s\n" % (cnt))
	sql = "SELECT	\
        TABLE_SCHEMA AS 数据库名,  \
		TABLE_NAME AS 表名,  \
		COLUMN_NAME AS 字段,  \
		COLUMN_TYPE AS 类型,  \
		IS_NULLABLE AS 允许空,  \
		COLUMN_DEFAULT AS 默认值,  \
		COLUMN_COMMENT AS 注释  \
	FROM  \
		information_schema. COLUMNS  \
	WHERE  \
		table_schema = 'cyber' and TABLE_NAME='%s' \
	ORDER BY  \
		TABLE_SCHEMA,  \
		TABLE_NAME,  \
		ORDINAL_POSITION" % (TABLE_NAME)
	# 执行sql,查询当前表的所有字段
	cursor.execute(sql)
	# 获取当前表的所有字段
	results = cursor.fetchall()
	f.write("|字段|类型|允许空|默认|注释|\n")
	f.write("|:----    |:-------    |:--- |----|------      |\n")
	for row in results:
		COLUMN_NAME = row[2]
		COLUMN_TYPE = row[3]
		IS_NULLABLE = row[4]
		COLUMN_DEFAULT = row[5]
		COLUMN_COMMENT = row[6]
		f.write("|%s |%s |%s |%s  | %s |\n" % (COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT, COLUMN_COMMENT))

#except:
#   print "Error: unable to fecth data"

# 关闭数据库连接
db.close()
