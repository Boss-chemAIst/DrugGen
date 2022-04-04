from models.molecule_constructor import construct_molecule

Process_data = True  # State true if data was not processed yet
Train_encoders = True  # State true if encoders were not trained yet

Disease_name = ''  # Disease to generate the drug for
Number_of_neighbors = None

# Loads all the data and saves to csv files in 'data' directory
if Process_data:
    import run_data_loading
    run_data_loading.main()

if Train_encoders:
    import run_encoders_training
    run_encoders_training.main()

molecule = construct_molecule(disease_name=Disease_name,
                              number_of_neighbors=Number_of_neighbors,
                              weighting_type='linear')
