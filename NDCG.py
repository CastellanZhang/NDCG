import sys, math

topK = int(sys.argv[1])

def DCG(label_list):
    dcgsum = 0
    for i in range(len(label_list)):
        dcg = (2**label_list[i] - 1)/math.log(i+2, 2)
        dcgsum += dcg
    return dcgsum

def NDCG(label_list):
    global topK
    dcg = DCG(label_list[0:topK])
    ideal_list = sorted(label_list, reverse=True)
    ideal_dcg = DCG(ideal_list[0:topK])
    if ideal_dcg == 0:
        return 0
    return dcg/ideal_dcg

def queryNDCG(label_qid_score):
    tmp = sorted(label_qid_score, key = lambda x:-x[2])
    label_list = []
    for label,q,s in tmp:
        label_list.append(label)
    return NDCG(label_list)
    
last_qid = ""
l_q_s = []

ndcg = 0
cnt = 0

for line in sys.stdin:
    label, qid, score = line.rstrip().split(" ")
    if last_qid != "" and qid != last_qid:
        ndcg += queryNDCG(l_q_s)
        cnt += 1
        l_q_s= []
    last_qid = qid
    l_q_s.append([int(label),qid, float(score)])

if last_qid != "":
    ndcg += queryNDCG(l_q_s)
    cnt += 1

#print cnt
print ndcg/cnt

