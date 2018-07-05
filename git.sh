git pull
python /idss/tools/showdoc/getDataDictionary.py
git add .
DATE=`date "+%Y-%m-%d %H:%M:%S"`
git commit -m "更新数据字典_${DATE}"
git push
