from brutforce import read_file, find_best_investment, display_result
import time
import psutil
import datetime


def main():
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
    actions = read_file("datasets/" + file_path + ".csv")

    max_budget_per_client = 500

    # Trouver la meilleure combinaison d'actions
    best_investment, best_return = find_best_investment(actions, max_budget_per_client)
    end_time = time.time()
    # Afficher les résultats
    display_result(best_investment, best_return)
    total_execution_time = round(end_time - start_time, 2)
    print(f"Temps total d'exécution: {total_execution_time} secondes")

    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Utilisation du processeur: {cpu_usage}%")
    memory_info = psutil.virtual_memory()

    total_memory = memory_info.total
    used_memory = memory_info.used
    available_memory = memory_info.available

    print(f"Mémoire totale: {total_memory} octets")
    print(f"Mémoire utilisée: {used_memory} octets")
    print(f"Mémoire disponible: {available_memory} octets")


if __name__ == "__main__":
    main()
