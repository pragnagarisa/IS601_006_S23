import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine, Patty, Topping
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
# this is an example test showing how to cascade fixtures to build up state


@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

# Bun first
def test_bun_first(machine):
    with pytest.raises(InvalidStageException) as exc_info:
        machine.handle_patty("turkey")

#UCID:vg473; Date: 19/03/2023


# Patty out of stock
def test_patty_outofstock(machine):
    machine.patties = [Patty(name="beef", quantity=1, cost=1)]

    with pytest.raises(OutOfStockException) as exc_info:
        machine.handle_bun("no bun")
        machine.handle_patty("beef")
        machine.handle_patty("beef")

    assert "beef" in str(exc_info.value)
    assert "Turkey" not in str(exc_info.value)

#UCID:vg473; Date: 19/03/2023

# Toppings out of stock
def test_toppings_outofstock(machine):
    machine.toppings = [Topping(name="Lettuce", quantity=0, cost=.25)]

    with pytest.raises(OutOfStockException) as exc_info:
        machine.handle_bun("no bun")
        machine.handle_patty("Turkey")
        machine.handle_patty("next")
        machine.handle_toppings("Lettuce")

    assert "Lettuce" in str(exc_info.value)

#UCID:vg473; Date: 19/03/2023

# Patty Exceeding choice
def test_patty_Exceedingchoice(machine):
    machine.patties = [Patty(name="Turkey", quantity=10, cost=1), Patty(
        name="Veggie", quantity=10, cost=1), Patty(name="beef", quantity=10, cost=1)]

    with pytest.raises(ExceededRemainingChoicesException) as exce_cho:
        machine.handle_bun("no bun")
        machine.handle_patty("Turkey")
        machine.handle_patty("beef")
        machine.handle_patty("veggie")
        machine.handle_patty("veggie")

    assert "veggie" in str(exce_cho.value)

#UCID:vg473; Date: 19/03/2023

# Toppings Exceeding choice
def test_toppings_Exceedingchoicetop(machine):
    machine.toppings = [Topping(name="Lettuce", quantity=10, cost=.25), Topping(name="Tomato", quantity=10, cost=.25),
                        Topping(name="Pickles", quantity=10, cost=.25),Topping(name="Cheese", quantity=10, cost=.25), Topping(
                    name="Ketchup", quantity=10, cost=.25),Topping(name="Mayo", quantity=10, cost=.25), 
                    Topping(name="Mustard", quantity=10, cost=.25), Topping(name="BBQ", quantity=10, cost=.25)]

    with pytest.raises(ExceededRemainingChoicesException) as exceed_info:
        machine.handle_bun("no bun")
        machine.handle_patty("Turkey")
        machine.handle_patty("next")
        machine.handle_toppings("Lettuce")
        machine.handle_toppings("bbq")
        machine.handle_toppings("Mustard")
        machine.handle_toppings("Ketchup")

    assert "Ketchup" in str(exceed_info.value)

#UCID:vg473; Date: 19/03/2023

#calculation
def test_order_one(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("bbq")
    machine.handle_toppings("done")
    machine.handle_pay(1.25, "1.25")
  

    machine.handle_bun("lettuce wrap")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("mayo")
    machine.handle_toppings("tomato")
    machine.handle_toppings("done")
    machine.handle_pay(2.75, "2.75")

   

    machine.handle_bun("lettuce wrap")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("mayo")
    machine.handle_toppings("tomato")
    machine.handle_toppings("done")
    machine.handle_pay(3.75, "3.75")
 
#UCID:vg473; Date: 19/03/2023

# total sales
def test_total_sales(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("turkey")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("mayo")
    machine.handle_toppings("done")
    burgerCost1 = machine.calculate_cost()
    machine.handle_pay(burgerCost1, str(burgerCost1))

    machine.handle_bun("lettuce wrap")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("mayo")
    machine.handle_toppings("tomato")
    machine.handle_toppings("done")
    burgerCost2 = machine.calculate_cost()
    machine.handle_pay(burgerCost2, str(burgerCost2))

    machine.handle_bun("White Burger Bun")
    machine.handle_patty("Veggie")
    machine.handle_patty("next")
    machine.handle_toppings("Pickles")
    machine.handle_toppings("Ketchup")
    machine.handle_toppings("done")
    burgerCost3 = machine.calculate_cost()
    machine.handle_pay(burgerCost3, str(burgerCost3))

    assert machine.total_sales == burgerCost1+burgerCost2+burgerCost3

#UCID:vg473; Date: 19/03/2023


# total burgers increment for each sale
def test_total_burgerscount(machine):
    assert machine.total_burgers == 0

    machine.handle_bun("no bun")
    machine.handle_patty("Turkey")
    machine.handle_patty("next")
    machine.handle_toppings("bbq")
    machine.handle_toppings("mayo")
    machine.handle_toppings("done")
    burgerCost1 = machine.calculate_cost()
    machine.handle_pay(burgerCost1, str(burgerCost1))

    machine.handle_bun("no bun")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("Pickles")
    machine.handle_toppings("Mustard")
    machine.handle_toppings("done")
    burgerCost2 = machine.calculate_cost()
    machine.handle_pay(burgerCost2, str(burgerCost2))

    machine.handle_bun("lettuce wrap")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("mayo")
    machine.handle_toppings("tomato")
    machine.handle_toppings("done")
    burgerCost3 = machine.calculate_cost()
    machine.handle_pay(burgerCost3, str(burgerCost3))

    assert machine.total_burgers == 3
    #UCID:vg473; Date: 19/03/2023


    