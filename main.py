from brutforce import read_file, find_best_investment, display_result


def main():
    print("1 : Dataset 20 lignes \n2 : Dataset 1 \n3: Dataset 2")
    dataset_choice = input("Choissez le dataset à explorer : ")
    if dataset_choice == "2":
        file_path = "dataset1"
    elif dataset_choice == "3":
        file_path = "dataset2"
    else:
        file_path = "index"

    # Lire les données à partir du fichier
    actions = read_file("datasets/" + file_path + ".csv")

    max_budget_per_client = 500

    # Trouver la meilleure combinaison d'actions
    best_investment, best_return = find_best_investment(actions, max_budget_per_client)

    # Afficher les résultats
    display_result(best_investment, best_return)


if __name__ == "__main__":
    main()
