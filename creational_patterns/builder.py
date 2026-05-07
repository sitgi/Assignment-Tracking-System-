class Pizza:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_cheese(self):
        self.pizza.add("cheese")
        return self

    def add_toppings(self):
        self.pizza.add("toppings")
        return self

    def build(self):
        return self.pizza
