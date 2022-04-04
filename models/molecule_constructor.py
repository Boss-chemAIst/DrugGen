def construct_molecule(disease_name=None,
                       number_of_neighbors=None,
                       weighting_type='linear'):

    """... search for a disease in All_Diseases.csv ..."""

    """... send omics to Biological_VAE and get vector representation ..."""

    """... determine disease proximity to all other diseases and choose number_of_neighbors diseases ..."""

    """... rank number_of_neighbors molecules against these diseases according to weighting_type ..."""

    """... calculate a new molecule as a weighted sum of number_of_neighbors diseases ..."""

    """... send a new molecule to Molecular_VAE decoder ..."""

