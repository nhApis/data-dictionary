#git pull
python getDataDictionary.py
git add .
DATE=`date "+%Y-%m-%d %H:%M:%S"`
git commit -m "更新数据字典_${DATE}"
git push
scp getDataDictionary.py /idss/tools/gitLab/gitProject/0.55/data-dictionary
cd /idss/tools/gitLab/gitProject/0.55/data-dictionary/ && sh git.sh
scp getDataDictionary.py /idss/tools/gitLab/gitProject/10.8/doc/04.详细设计/data-dictionary
cd /idss/tools/gitLab/gitProject/10.8/doc/04.详细设计/data-dictionary/ && sh git.sh
