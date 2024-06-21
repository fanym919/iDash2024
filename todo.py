def solution(local_updates, num_clients, total_number_of_samples):
    # Aggregation step
    aggregated_delta_weights = [
        None for _ in range(len(local_updates[0]["updates"]))
    ]
    for idx_weight in range(len(local_updates[0]["updates"])):
        aggregated_delta_weights[idx_weight] = sum(
            [
                local_updates[idx_client]["updates"][idx_weight]
                * local_updates[idx_client]["n_samples"]
                for idx_client in range(num_clients)
            ]
        )
        aggregated_delta_weights[idx_weight] /= float(total_number_of_samples)

    return aggregated_delta_weights