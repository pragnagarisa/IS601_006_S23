from enum import Enum
import sys
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, NeedsCleaningException, OutOfStockException
from BurgerMachineExceptions import InvalidPaymentException


class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity=10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if (self.quantity < 0):
            raise OutOfStockException(self.name)
        return self.quantity

    def in_stock(self):
        return self.quantity > 0

    def __repr__(self) -> str:
        return self.name


class Bun(Usable):
    pass


class Patty(Usable):
    pass


class Topping(Usable):
    pass


class STAGE(Enum):
    Bun = 1
    Patty = 2
    Toppings = 3
    Pay = 4


class BurgerMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 15
    MAX_PATTIES = 3
    MAX_TOPPINGS = 3

    buns = [Bun(name="No Bun", cost=0), Bun(name="White Burger Bun", cost=1), Bun(
        "Wheat Burger Bun", cost=1.25), Bun("Lettuce Wrap", cost=1.5)]
    patties = [Patty(name="Turkey", quantity=10, cost=1), Patty(
        name="Veggie", quantity=10, cost=1), Patty(name="Beef", quantity=10, cost=1)]
    toppings = [Topping(name="Lettuce", quantity=10, cost=.25), Topping(name="Tomato", quantity=10, cost=.25), Topping(name="Pickles", quantity=10, cost=.25),
                Topping(name="Cheese", quantity=10, cost=.25), Topping(
                    name="Ketchup", quantity=10, cost=.25),
                Topping(name="Mayo", quantity=10, cost=.25), Topping(name="Mustard", quantity=10, cost=.25), Topping(name="BBQ", quantity=10, cost=.25)]

    # variables
    remaining_uses = USES_UNTIL_CLEANING
    remaining_patties = MAX_PATTIES
    remaining_toppings = MAX_TOPPINGS
    total_sales = 0
    total_burgers = 0

    inprogress_burger = []
    currently_selecting = STAGE.Bun

    # rules
    # 1 - bun must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - patties can't exceed max
    # 4 - toppings can't exceed max
    # 5 - proper cost must be calculated and shown to the user
    # 6 - cleaning must be done after certain number of uses before any more burgers can be made
    # 7 - total sales should calculate properly based on cost calculation
    # 8 - total_burgers should increment properly after a payment

    def pick_bun(self, choice):
        if self.currently_selecting != STAGE.Bun:
            raise InvalidStageException
        for c in self.buns:
            if c.name.lower() == choice.lower():
                c.use()
                self.inprogress_burger.append(c)
                return
        raise InvalidChoiceException(choice)

    def pick_patty(self, choice):
        if self.currently_selecting != STAGE.Patty:
            raise InvalidStageException
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_patties <= 0:
            self.currently_selecting = STAGE.Toppings
            raise ExceededRemainingChoicesException(choice)
        for f in self.patties:
            if f.name.lower() == choice.lower():
                f.use()
                self.inprogress_burger.append(f)
                self.remaining_patties -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException(choice)

    def pick_toppings(self, choice):
        if self.currently_selecting != STAGE.Toppings:
            raise InvalidStageException
        if self.remaining_toppings <= 0:
            self.currently_selecting = STAGE.Pay
            raise ExceededRemainingChoicesException(choice)
        for t in self.toppings:
            if t.name.lower() == choice.lower():
                t.use()
                self.inprogress_burger.append(t)
                self.remaining_toppings -= 1
                return
        raise InvalidChoiceException(choice)

    def reset(self):
        self.remaining_patties = self.MAX_PATTIES
        self.remaining_toppings = self.MAX_TOPPINGS
        self.inprogress_burger = []
        self.currently_selecting = STAGE.Bun

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING

    def handle_bun(self, bun):
        self.pick_bun(bun)
        self.currently_selecting = STAGE.Patty

    def handle_patty(self, patty):
        if patty == "next":
            self.currently_selecting = STAGE.Toppings
        else:
            self.pick_patty(patty)

    def handle_toppings(self, toppings):
        if toppings == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_toppings(toppings)

    def handle_pay(self, expected, total):
        if self.currently_selecting != STAGE.Pay:
            raise InvalidStageException
        if total == str(expected):
            print("Thank you! Enjoy your burger!")
            self.total_burgers += 1
            self.total_sales += expected  # only if successful
            print(f"Total sales so far {self.total_sales}")
            self.reset()
        else:
            raise InvalidPaymentException(total)

    def print_current_burger(self):
        # print(self.inprogress_burger)
        print(
            f"Current Burger: {','.join([x.name for x in self.inprogress_burger])}")

    def calculate_cost(self):
        # TODO add the calculation expression/logic for the inprogress_burger
        total_cost = sum(x.cost for x in self.inprogress_burger)
        return total_cost

    #UCID:vg473; Date: 19/03/2023
    #calculate_cost function calculates the total cost of burger, inprogress_burger list have all the user added data and
    #the cost of bun,patty and toppings are added to total_cost and return total_cost

    def run(self):
        try:
            if self.currently_selecting == STAGE.Bun:
                bun = input(
                    f"What type of bun would you like {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.buns))))}?\n")
                self.handle_bun(bun)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Patty:
                patty = input(
                    f"Would type of patty would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.patties))))}? Or type next.\n")
                self.handle_patty(patty)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Toppings:
                toppings = input(
                    f"What topping would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.toppings))))}? Or type done.\n")
                self.handle_toppings(toppings)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Pay:
                expected = self.calculate_cost()
                total = input(
                    f'Your total is {"${:,.2f}".format(expected)} please enter the exact value.\n')
                self.handle_pay(expected, total)
                choice = input("What would you like to do? (order or quit)\n")
                if choice == "quit":
                    print("Quitting the burger machine")
                    return 1
        except KeyboardInterrupt:
            # quit
            print("Quitting the burger machine")
            sys.exit()

        # handle OutOfStockException
        except OutOfStockException as ie:

            print(f'Sorry, {self.currently_selecting}: {ie} is Out of Stock') # show an appropriate message of what stage/category was out of stock
        
        #UCID:vg473; Date: 19/03/2023
        # At any stage, if an item goes out of stock, it will be handled with OutOfStockException.
        # Inside OutofStockException, We print the message mentioning at which stage and what item (passed in as exception argument 'ie') went out of stock.

        # handle NeedsCleaningException
        except NeedsCleaningException as ne:
          
            clean_input = input(f"Type CLEAN to start cleaning\n") # prompt user to type "clean" to trigger clean_machine()
            
            if clean_input == 'clean':
                self.clean_machine()
                print("Machine Cleaned..... please Continue")# print a message whether or not the machine was cleaned
                
            else:
                print("Machine not cleaned yet") # print a message whether or not the machine was cleaned
                exit()
                
        #UCID:vg473; Date: 19/03/2023
        #NeedsCleaningException is raised at stage patty, when remaining_uses = USES_UNTIL_CLEANING user needs to type the word CLEAN , them clean_machine function is called
        #and cleans the machine and prints machine clean, if user input is not cleaned it clean_machin function isn't called
        #and prints message machine not cleaned yet

        
        # handle InvalidChoiceException
        except InvalidChoiceException as ce:
            
            print('invalid choice:', self.currently_selecting,ce)  # show an appropriate message of what stage/category was the invalid choice was in
    
        #UCID:vg473; Date: 19/03/2023
        # At any stage, if an item name is invalid, it will be handled with InvalidChoiceException.
        # Inside InvalidChoiceException, We print the message mentioning at which stage and what item (passed in as exception argument 'ce') name is invalid.


        # handle ExceededRemainingChoicesException
        except ExceededRemainingChoicesException as ee:
           
            print('exceeding choices:',self.currently_selecting,ee)
            
        #UCID:vg473; Date: 19/03/2023
        # At any stage, selecting choices are exceeding , it will be handled with ExceededRemainingChoicesException.
        # Inside ExceededRemainingChoicesException, We print the message mentioning at which stage choices are exceeding (passed in as exception argument 'ee')

        # handle InvalidPaymentException
        except InvalidPaymentException as pe:
            
            print('Invalid Value:', pe)# show an appropriate message

        #UCID:vg473; Date: 19/03/2023
        #If user enter data is not matching with valid calculation at handle_pay function  InvalidPaymentException exception is raised
        #We print the Invalid payment message (passed is an exception argument 'pe')

        except:
            # this is a default catch all, follow the steps above
            print("Something went wrong")

        self.run()

    def start(self):
        while True:
            self.run()


if __name__ == "__main__":
    bm = BurgerMachine()
    bm.start()
