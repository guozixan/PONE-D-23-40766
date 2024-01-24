import random
from data_loader import load_data
from logistics_model import LogisticsPoint, LogisticsRoute
from optimizer import PathOptimizer
import time
from consensus import Blockchain, CPBFTConsensus, PBFTConsensus



def simulate_consensus_process(optimizer_class, consensus_class, demand_points, supply_points, routes, num_plans=10):
    results = []

    for plan_id in range(1, num_plans + 1):
        optimizer = optimizer_class(demand_points, supply_points, routes)
        optimized_solution = optimizer.optimize()
        total_time, total_cost = optimizer.calculate_total_time_and_cost(optimized_solution)

        blockchain = Blockchain()
        consensus_mechanism = consensus_class(blockchain, node_id=0, num_nodes=5)
        start_time = time.time()
        fairness_index = calculate_fairness_index(optimized_solution, demand_points)
        consensus_mechanism.apply_consensus(optimized_solution)
        end_time = time.time()
        consensus_time = end_time - start_time

        if consensus_time == 0:
            consensus_time = 0.0001  # Setting a small non-zero value

        throughput = len(optimized_solution) / consensus_time
        blockchain_length = len(blockchain.chain)

        results.append((f"B{plan_id}", total_time, total_cost, fairness_index, consensus_time, throughput, blockchain_length))

    return results

def main():
    demand_points, supply_points, routes = load_data()

    pbft_results = simulate_consensus_process(PathOptimizer, PBFTConsensus, demand_points, supply_points, routes)

    cpbft_results = simulate_consensus_process(PathOptimizer, CPBFTConsensus, demand_points, supply_points, routes)

    print("PBFT Results (Plan ID | Total Time | Total Cost | Consensus Time | Throughput | Blockchain Length)")
    for result in pbft_results:
        print(result)

    print("\nC-PBFT Results (Plan ID | Total Time | Total Cost| Consensus Time | Throughput | Blockchain Length)")
    for result in cpbft_results:
        print(result)

if __name__ == "__main__":
    main()
