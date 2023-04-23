文件夹解释
Extract --> 从SQuAD(中文)中提取出全部的paragraphs
    cmrc2018_dev.json --> 包含848条paragraphs
    cmrc2018_train.json --> 包含2403条paragraphs
    cmrc2018_trail.json --> 包含256条paragraphs
    data.txt  --> dev, train, trail的数据合并
    main.py --> 主程序
    rescource.txt --> 结果(从SQuAD(中文)中提取出的全部的paragraphs),共3507条paragraphs

分词 --> 使用pyhanlp对从SQuAD(中文)中提取出全部的paragraphs进行分词
    ans.txt --> 分词结果
    config.txt --> 使用anaconda环境运行的cmd命令
    main.py --> 主程序
    rescource.txt --> 来自./Extract/rescource.txt
    word_character.txt --> pyhanlp的分词类型表

database --> 将分词结果清洗并存到数据库中，最后筛出64970条有效entity
    ans.txt --> 来自./分词/ans.txt
    main.py --> 主程序
    main.sql --> 去除掉重复的，以及数词，数量词，名词性语素

28W数据处理 --> 对百度百科爬取的28w条数据进行处理
    data.txt --> 对相同id合并后的数据
    main.py --> 将data.txt, raw.txt数据储存到数据库中
    main.sql --> 对286350条百度百科数据与64970条SQuAD(中文)数据进行匹配
    raw.txt --> 源数据

最终匹配出28290条，覆盖率约43%

