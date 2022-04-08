import glob
import os
import re
import xml.etree.ElementTree as ET
import pandas as pd

files = glob.glob(os.getcwd() + "/xin_eng_200410.xml", recursive=True)
# files = glob.glob(os.getcwd() + "/webnlg-dataset/webnlg_challenge_2017/test/testdata_no_lex.xml", recursive=True)
# print(files)
# triple_re=re.compile('(\d)triples')
# # print(triple_re)
# data_dct={}
# for file in files:
#     tree = ET.parse(file)
#     root = tree.getroot()
#     # print(root.tag)
#     # print(root[0].tag)
#     triples_num=triple_re.findall(file)
#     print(triples_num)
#     for sub_root in root:
#         for ss_root in sub_root:
#             strutured_master=[]
#             unstructured=[]
#             for entry in ss_root:
#                 unstructured.append(entry.text)
#                 strutured=[triple.text for triple in entry]
#                 strutured_master.extend(strutured)
#             unstructured=[i for i in unstructured if i.replace('\n','').strip()!='' ]
#             strutured_master=strutured_master[-triples_num:]
#             strutured_master_str=(' && ').join(strutured_master)
#             data_dct[strutured_master_str]=unstructured
# mdata_dct={"prefix":[], "input_text":[], "target_text":[]}
# for st,unst in data_dct.items():
#     for i in unst:
#         mdata_dct['prefix'].append('webNLG')
#         mdata_dct['input_text'].append(st)
#         mdata_dct['target_text'].append(i)


# df=pd.DataFrame(mdata_dct)
# df.to_csv('webNLG2020_train.csv')


tree = ET.parse(os.getcwd() + "/xin_eng_200410.xml")
# tree = ET.parse(os.getcwd() + "/nyt_eng_199909.xml")

root = tree.getroot()
text = ET.tostring(root, encoding="utf8").decode("utf8")
# print(root[0][1].text)

for description in root.iter("description"):
    print(description.text)

# for child in root:
#     print(child.tag, child.attrib)


