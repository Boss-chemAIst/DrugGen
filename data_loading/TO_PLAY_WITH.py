import os
from cmapPy.pandasGEXpress.parse_gctx import parse

path = os.getcwd()
upper_path = '\\'.join(path.split('\\')[0:-1])
omics_df = parse(upper_path + '\\data\\raw_data\\example.gctx')

print(omics_df.data_df)
print(omics_df.col_metadata_df)