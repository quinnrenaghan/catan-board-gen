import Board_Utility as Util
import Balanced_Utility as Balanced
import time

min_harbor_score = 1000000
max_harbor_score = 0

min_number_clustering = 1000000
max_number_clustering = 0

min_probability_distribution = 1000000
max_probability_distribution = 0

min_resource_probability = 1000000
max_resource_probability = 0

min_resource_clustering = 1000000
max_resource_clustering = 0

min_resource_distribution = 1000000
max_resource_distribution = 0

start_time = time.time()
for i in range(50000000):
    board = Util.Board()

    harbor_score = Balanced.harbor_score(board)
    if harbor_score > max_harbor_score:
        max_harbor_score = harbor_score
    if harbor_score < min_harbor_score:
        min_harbor_score = harbor_score

    number_clustering = Balanced.number_clustering(board)
    if number_clustering > max_number_clustering:
        max_number_clustering = number_clustering
    if number_clustering < min_number_clustering:
        min_number_clustering = number_clustering

    probability_distribution = Balanced.probability_distribution(board)
    if probability_distribution > max_probability_distribution:
        max_probability_distribution = probability_distribution
    if probability_distribution < min_probability_distribution:
        min_probability_distribution = probability_distribution

    resource_probability = Balanced.resource_probability(board)
    if resource_probability > max_resource_probability:
        max_resource_probability = resource_probability
    if resource_probability < min_resource_probability:
        min_resource_probability = resource_probability

    resource_clustering = Balanced.resource_clustering(board)
    if resource_clustering > max_resource_clustering:
        max_resource_clustering = resource_clustering
    if resource_clustering < min_resource_clustering:
        min_resource_clustering = resource_clustering

    resource_distribution = Balanced.resource_distribution(board)
    if resource_distribution > max_resource_distribution:
        max_resource_distribution = resource_distribution
    if resource_distribution < min_resource_distribution:
        min_resource_distribution = resource_distribution


print(f"harbor score: max: {max_harbor_score} min: {min_harbor_score} \n")
print(f"number clustering max: {max_number_clustering} min: {min_number_clustering} \n")
print(f"probability distribution max: {max_probability_distribution} min: {min_probability_distribution} \n")
print(f"resource probability max: {max_resource_probability} min: {min_resource_probability} \n")
print(f"resource clustering max: {max_resource_clustering} min: {min_resource_clustering} \n")
print(f"resource distribution max: {max_resource_distribution} min: {min_resource_distribution} \n")



