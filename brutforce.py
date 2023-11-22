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
    print("entrer dans la méthode de trouvaille meilleur investissement")
    for r in range(1, len(actions) + 1):
        for subset in itertools.combinations(actions, r):
            total_price = sum(action["price"] for action in subset)
            total_return = sum(action["profit"] * action["price"] for action in subset)

            if total_price <= max_budget and total_return > best_return:
                best_return = total_return
                best_investment = subset
    print("fin boucle")
    return best_investment, best_return


def display_result(best_investment, best_return):
    print("Meilleur combinaison d'actions:")
    for action in best_investment:
        print(
            f"{action['action']}- Coût: {action['price']} euros - Bénéfices: {action['profit']}%"
        )
    print(f"\nRendement total: {best_return}€")
