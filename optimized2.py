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


def find_best_investment_dynamic(actions, max_budget):
    # Tri des actions par ordre décroissant en fonction du profit (=action les plus rentable sont analysées en premier)
    sorted_actions = sorted(actions, key=lambda x: x["rendement"], reverse=True)
    # longueur total du Nombre d'actions stockée dans une variable
    num_actions = len(sorted_actions)

    # création d'une liste pour stocker les résultats intermédiaires
    # dp[i][j] représente le meilleur rendement pour les i premières actions avec un budget j
    dp = [[0.0] * (max_budget + 1) for _ in range(num_actions + 1)]

    for i in range(1, num_actions + 1):
        for budget in range(max_budget + 1):
            # Ne pas inclure l'action i
            dp[i][budget] = dp[i - 1][budget]

            # Inclure l'action i si elle respecte le budget
            if (
                sorted_actions[i - 1]["price"] <= budget
                and sorted_actions[i - 1]["profit"] != 0
            ):
                dp[i][budget] = max(
                    dp[i][budget],
                    dp[i - 1][int(budget - sorted_actions[i - 1]["price"])]
                    + sorted_actions[i - 1]["profit"]
                    * sorted_actions[i - 1]["price"]
                    / 100,
                )

    # Reconstruction de la liste des meilleures actions
    best_investment_dynamic = []
    i, budget = num_actions, max_budget
    while i > 0 and budget > 0:
        if dp[i][int(budget)] != dp[i - 1][int(budget)]:
            best_investment_dynamic.append(sorted_actions[i - 1])
            budget -= sorted_actions[i - 1]["price"]
        i -= 1

    # Valeur du meilleur retour sur investissement arrondi à deux chiffres après la virgule
    best_return_dynamic = round(dp[num_actions][max_budget], 2)

    return best_investment_dynamic, best_return_dynamic


def display_result_optimized(best_investment, best_return):
    print("Meilleure combinaison d'actions: ")
    for action in best_investment:
        print(
            f"{action['action']}- Coût: {action['price']} euros - Bénéfices: {action['profit']}% - Rendement: {action['rendement']}€"
        )
    print(f"\nRendement total: {best_return}€")
