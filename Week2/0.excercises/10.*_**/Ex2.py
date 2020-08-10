# Napisz funkcję, która przyjmie dowolną liczbę argumentów nazwanych 
# i wypisze sposób w jaki została wywołana, 
# tzn. poszczególne nazwy argumentów, znak równa się i wartość (np. first_name=Mikołaj, age=134).


def personal_information(**info):
    for first_name, age in info.items():
        print(f"first_name = {first_name}, age = {age}")


def run_example():
    personal_information(
        Adam=27,
        Juliet = 26,
        Kasia = 34
        )

print(run_example())
