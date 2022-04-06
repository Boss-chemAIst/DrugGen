"""
Transforms raw omics data to desired format and saves to csv file.
"""


def main():
    import pandas as pd
    import os
    from cmapPy.pandasGEXpress.parse_gctx import parse

    # Checks working directory and reads csv file with raw omics data
    path = os.getcwd()
    omics_df = parse(path + '\\data\\example.gctx')

    # Gets gene names from dataframe column names (define range in square brackets)
    list_of_genes = omics_df.columns.values.tolist()[:]

    '... dataframe processing ...'

    # Sets column names
    column_names = ['Disease_ID', 'Trivial_names'] + list_of_genes

    # Saves processed dataframe to csv file with pre-defined columns
    final_omics_df = pd.DataFrame(data=omics_df,
                                  columns=column_names)
    final_omics_df.to_csv(path + '\\data\\all\\All_Diseases.csv')


if __name__ == '__main__':
    main()
