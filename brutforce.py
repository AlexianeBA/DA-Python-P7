import itertools


def read_file(file_path):
    data = []
    with open(file_path, "r") as file:
        next(file)
        for line in file:
            action, price, profit = line.strip().split(",")
            data.append(
                {
                    "action": action.strip(),
                    "price": float(price),
                    "profit": float(profit),
                }
            )
    print("Ouverture du document ok: ", data)
    return data


def find_best_investment(actions, max_budget):
    best_investment = None
    best_return = 0.0
    # boucle qui parcourt toutes les actions
    for r in range(1, len(actions) + 1):
        # génère toutes les combinaisons possible des éléments dans la liste des actions
        for subset in itertools.combinations(actions, r):
            # calcul du cout total en additionnant les prix de chaque action
            total_price = sum(action["price"] for action in subset)
            # calcul le rendement total en mutlipliant le profit par le prix pour chaque actions et additionne ces valeurs
            total_return = sum(
                (action["profit"] * action["price"]) / 100 for action in subset
            )

            if total_price <= max_budget and total_return > best_return:
                best_return = round(total_return, 2)
                best_investment = subset
    # retourne le meilleur investissement trouvé
    return best_investment, best_return


def display_result(best_investment, best_return):
    print("Meilleure combinaison d'actions:")
    for action in best_investment:
        print(
            f"{action['action']}- Coût: {action['price']} euros - Bénéfices: {action['profit']}%"
        )
    print(f"\nRendement total: {best_return}€")
