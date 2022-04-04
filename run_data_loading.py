# Import scripts for data loading
from data_loading import load_molecules, \
                         load_omics


def main():
    load_molecules.main()  # Saves all molecules to csv files
    load_omics.main()  # Saves all omics data to csv files


if __name__ == '__main__':
    main()
