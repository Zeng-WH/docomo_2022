import csv
import json
csv_reader = csv.reader(open("/mnt/dolphinfs/ssd_pool/docker/user/hadoop-aipnlp/zengweihao02/EMNLP2022/TODSum/mt-seq2seq/TODSum_Data/docomo_data/test.csv"))
train_json = []
count = 0
for line in csv_reader:
    if count == 0:
        pass
    else:
        temp_dict = {}
        temp_dict["text"] = line[0]
        temp_dict["summary"] = line[1]
        train_json.append(temp_dict)
    count = count + 1

with open("/mnt/dolphinfs/ssd_pool/docker/user/hadoop-aipnlp/zengweihao02/EMNLP2022/TODSum/mt-seq2seq/TODSum_Data/docomo_data/test.json", "w") as w:
    for item in train_json:
        w.write(json.dumps(item))
        w.write("\n")
    
print("bupt")
