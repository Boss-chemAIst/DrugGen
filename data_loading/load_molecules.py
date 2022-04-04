"""
Parses molecules from PubChem (or chembl database) and saves desired data to csv file.
"""


def main():
    import pandas as pd
    import os

    final_df = pd.DataFrame(columns=['Molecule_ID',
                                     'Canonical_SMILES',
                                     'Trivial_names'])

    path = os.getcwd()
    final_df.to_csv(path + '\\data\\all\\All_Molecules.csv')


if __name__ == '__main__':
    main()
