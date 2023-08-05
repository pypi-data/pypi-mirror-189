# textanalyze4sc

中文文本分析库，可对文本进行词频统计、情绪分析、话题分析等

- [github地址](https://github.com/martin6336/textanalyze4sc) ``https://github.com/hidadeng/cntext``
- [pypi地址](https://pypi.org/project/textanalyze4sc/)  ``https://pypi.org/project/cntext/``


功能模块含


- **word_cloud**  文本统计,可读性等
- **get_keyword**  获取文本关键词
- **get_entity** 获取文本实体
- **get_emotion**  获取文本情绪
- **get_cosemantic**  获取词语共现语义图
- **get_topic**  获取话题
- **visualization** 可视化，如词云图



<br>

## 安装

```
pip install textanalyze4sc
```


<br><br>

## 一、读取数据



```python
from texttool import analyze

df_data = analyze.load_data(the path of your data)
```




<br><br>

## 二、提取关键词


```python


df_data_key=analyze.get_keyword(df_data)
```


<br>

## 三、提取实体

```python
df_data_entity=analyze.get_entity(df_data)

```




## 四、情感分析
这里提供两种粒度的情感分析。

1，这里分为三种“积极”，“负面”，“中立”
```python
analyze.get_emotion('我很开心，你是这么认为的吗')

```

结果

```
'pos'
```

2，这里进行更为细粒度的区分，分为“好”，“乐”，“哀”，“怒”，“惧”，“恶”，“惊” 七类情绪。
```python
analyze.get_emotion_sp('我很开心，你是这么认为的吗')

```

结果

```
{'words': 10,
 'sentences': 1,
 '好': 0,
 '乐': 1,
 '哀': 0,
 '怒': 0,
 '惧': 0,
 '恶': 0,
 '惊': 0}
```


## 五、词语共现图

本文使用筛选出现频率出现前50的实体，并作出共现图
<br>

```

analyze.get_cosemantic(df_data,top50_all)
```




## 六、可视化
本文提供各类可视化工具，柱状图，趋势图，词云图等。

