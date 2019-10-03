import pandas as pd
import xlrd


data = pd.read_excel('data.xlsx')
fcetc = pd.read_excel('fcetc.xlsx')

# print(data)
# print(fcetc)

# cd = fcetc.loc[(fcetc['CAP_TY_CD']=='AR')]
# print(cd)
#
# for i in data:
#     SRC_SYS_CD = data['SRC_SYS_CD'][0]
#     # ACCT_NUM = data['ACCT_NUM']
#     # CAP_TY_CD = data['CAP_TY_CD']
#     # AMT_TYPE = data['AMT_TYPE']
#     # FAT = data['FAT']
#     # LE = data['LE']
#     # aAMT = data['AMT']
#     print(SRC_SYS_CD)
SRC_SYS_CD_count = 0
SRC_SYS_CD = (data['SRC_SYS_CD'][SRC_SYS_CD_count])
print(SRC_SYS_CD)


ACCT_NUM = (data['ACCT_NUM'][SRC_SYS_CD_count])
CAP_TY_CD = (data['CAP_TY_CD'][SRC_SYS_CD_count])
AMT_TYPE = (data['AMT_TYPE'][SRC_SYS_CD_count])
FAT = (data['FAT'][SRC_SYS_CD_count])
LE = (data['LE'][SRC_SYS_CD_count])
AMT = (data['AMT'][SRC_SYS_CD_count])

# print(AMT,ACCT_NUM,AMT_TYPE)

# (fcetc.loc[(fcetc['SRC_SYS_CD'] == SRC_SYS_CD) & (fcetc['LE'] == '520')])
y = fcetc.loc[(fcetc['SRC_SYS_CD'] == SRC_SYS_CD) & (fcetc['LE'] == LE)]
print(y)