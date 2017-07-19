# NDCG
计算排序模型预测结果的NDCG@k

执行方法：

cat label_qid_score.txt | python NDCG.py k

输入文件每一行的格式：

label qid score

注意，这里算出的NDCG@k和RankLib的“NDCG@k”一致，和xgboost的“ndcg@n”不一致，和xgboost的"ndcg@n-"一致。
