from customer import Customer
from coffee import Coffee
from order import Order

def main():
    try:
        
        customer = Customer("Alice")
        coffee = Coffee("Espresso")

        
        print(f"Customer: {customer.name}")

        
        order = customer.create_order(coffee, 5.0)

        
        print(f"Order: Coffee={order.coffee.name}, Price={order.price}")

        
        print(f"Customer coffees: {[c.name for c in customer.coffees]}")
        print(f"Coffee customers: {[c.name for c in coffee.customers]}")

        
        print(f"Espresso orders: {coffee.num_orders()}")

        
        print(f"Most aficionado: {Customer.most_aficionado(coffee).name}")

        empty_coffee = Coffee("Cappuccino")
        print(f"Cappuccino orders: {empty_coffee.num_orders()}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()