def read_file_optimized(file_path):
    data = []
    with open(file_path, "r") as file:
        next(file)
        for line in file:
            action, price, profit = line.strip().split(",")
            # Convertir en float
            price = float(price)
            profit = float(profit)

            # Vérifier que le profit n'est pas égal à zéro avant d'ajouter les données
            if profit != 0 and price > 0:
                data.append(
                    {
                        "action": action.strip(),
                        "price": float(price),
                        "profit": float(profit),
                        "rendement": float((profit * price) / 100),
                    }
                )
    return data


def find_best_investment_optimized(actions, max_budget):
    # tri des actions par ordre décroissant en fonction du profit
    sorted_actions = sorted(actions, key=lambda y: y["rendement"], reverse=True)
    # budget actuel
    current_budget = 0.0
    # liste des meilleurs actions
    best_investment_optimized = []
    # valeur total du rendement
    best_return_optimized = 0.0
    # parcour chaque action
    for action in sorted_actions:
        # vérifie si l'ajout d'une action respecte le budget max et que le profit n'est pas égal à zéro
        if current_budget + action["price"] <= max_budget and action["profit"] != 0:
            # ajout du prix de l'action au budget en cours
            current_budget += action["price"]
            # ajout de l'action à la liste des meilleurs actions
            best_investment_optimized.append(action)
            # valeur meilleur investissement mise à jour en ajoutant le profit de l'action et son prix divisé par 100
            best_return_optimized += action["profit"] * action["price"] / 100
    # valeur du retour sur investissement est arrondi à deux chiffres après la virgule
    best_return_optimized = round(best_return_optimized, 2)
    # renvoi de la liste des meilleurs actions sélectionnées et de la valeur du meilleur retour sur investissement
    return best_investment_optimized, best_return_optimized


def display_result_optimized(best_investment, best_return):
    print("Meilleure combinaison d'actions: ")
    for action in best_investment:
        print(
            f"{action['action']}- Coût: {action['price']} euros - Bénéfices: {action['profit']}% - Rendement: {action['rendement']}€"
        )
    print(f"\nRendement total: {best_return}€")
