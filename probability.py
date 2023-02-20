import pandas as pd
import math

class Probability:
    """
    A class which contains the tools to work out the probability of certain
    outcomes in a normal distribution, using a z-chart.

    ...

    Attributes
    ----------
    path : str
        path for the z-chart in csv format
    z_number : float
        z-number which, used to find the corresponding probability from z-chart

    Methods
    -------
    create_dataframe():
        Takes in a file path for a csv file, reads and returns it
        as a dataframe.
    split_z_score_into_2_numbers(z_number):
        Takes in a z-number and splits it into two numbers.
    get_probability(large_num, small_num, file):
        Takes in the split z-number and finds the corresponding probability value from the z-chart
    run_all(path, z_number):
        Runs all methods in the Probability class sequentially.
    """
    
    def __init__(self, path, z_number):
        self.path =  path
        self.z_number = z_number

    def create_dataframe(self, path):
        """
        Takes in a file path for a csv file, reads and returns it
        as a dataframe.
        """
        csv_file = pd.read_csv(filepath_or_buffer=path, index_col=1)
        return csv_file

    def split_z_score_into_2_numbers(self, z_number):
        """
        Takes in a z-number and splits it into two numbers. 
        These numbers are the first and second decimal places
        for use with the z-chart
        """
        z_number_string = str(z_number)
        if len(z_number_string)==3:
            large_num, small_num = z_number, '0.00'
        elif len(z_number_string) == 1:
            large_num, small_num = float(z_number), '0.00'
        elif len(z_number_string) == 4:
            last_digit = int(z_number_string[-1])
            small_num = last_digit/100
            large_num = z_number - small_num
        else:
            print('z-number must be <= 3 and have 2 decimal places or less')
        
        return large_num, small_num

    def get_probability(self, large_num, small_num, file):
        """
        Takes in the split z-number and finds the corresponding
        probability value from the z-chart
        """
        probability_from_z_chart = file.loc[large_num, str(small_num)]
        return probability_from_z_chart

    def run_all(self, path, z_number):
        """
        Runs all methods in the Probability class sequentially.
        """
        z_chart = self.create_dataframe(path=self.path)
        large_num, small_num = self.split_z_score_into_2_numbers(z_number)
        probability_from_z_chart = self.get_probability(large_num,
                                                        small_num,
                                                        z_chart)
        return z_chart, large_num, small_num, probability_from_z_chart