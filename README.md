#WordSeg

Chinese Word Segmentation using [CRF++][link1].

[link1]:http://sourceforge.net/projects/crfpp/files/

[link2]:https://github.com/isnowfy/snowseg/blob/master/unigram_add_one.py

##主要流程

1. 对训练集进行字标注   
`python tag.py pku_training.utf8`
2. 训练模型
`crf_learn template pku_training.utf8.data model`
3. 对测试集进行字标注   
`python tag.py pku_test.utf8`
4. 预测测试集中每个字对应的字标号   
`crf_test -m model pku_test_gold.utf`
5. 根据字标注得到分词结果   
`python back_new.py pku_test_gold.utf linefile temp newtemp re-sult_new`

##测试

`perl score training_file gold_file result_file > score_file`