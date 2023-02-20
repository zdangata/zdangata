from probability import Probability
path = './z-chart.csv'
z_number = 2

probability = Probability(path=path, z_number=z_number)
z_chart, large_num, small_num, probability_from_z_chart = probability.run_all(path=path,
                                                                              z_number=z_number)
large_num, small_num = probability.split_z_score_into_2_numbers(z_number)
print(f'Probability from z-chart at {large_num} and {small_num} is: ', probability_from_z_chart)