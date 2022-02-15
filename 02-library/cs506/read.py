import pandas as pd 


def read_csv(csv_file_path):
    csv = pd.read_csv(csv_file_path, header=None)
    list_of_list = [list(row) for row in csv.values]
    return list_of_list 
   # return pd.read_csv(csv_file_path, header=None).to_numpy()
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
