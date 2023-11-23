from optimized import (
    read_file_optimized,
    find_best_investment_optimized,
    display_result_optimized,
)
import time


def main_optimized():
    print("1 : Dataset 20 lignes \n2 : Dataset 1 \n3: Dataset 2")
    dataset_choice = input("Choissez le dataset à explorer : ")
    if dataset_choice == "2":
        file_path = "dataset1"
    elif dataset_choice == "3":
        file_path = "dataset2"
    else:
        file_path = "index"
    start_time = time.time()
    # Lire les données à partir du fichier
    actions = read_file_optimized("datasets/" + file_path + ".csv")

    max_budget_per_client = 500

    # Trouver la meilleure combinaison d'actions
    best_investment, best_return = find_best_investment_optimized(
        actions, max_budget_per_client
    )

    # Afficher les résultats
    display_result_optimized(best_investment, best_return)
    end_time = time.time()

    total_execution_time = round(end_time - start_time, 2)
    print(f"Temps total d'exécution: {total_execution_time} secondes")


if __name__ == "__main__":
    main_optimized()
