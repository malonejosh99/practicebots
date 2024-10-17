
#coffee bot, started from an idea from learning and built on top of it. 
#will use as practice and a starting point for all future projects
#will add new features and enhance it as my knowledge increases and my skill set

#holds the menu, works out each items cost, gives each item its cost depensing on customers choices.
class Menu:
    def __init__(self):
        self.base_menu = {"Brewed Coffee": 2.50, "Mocha": 3.00, "Latte": 3.50}
        self.size_multiplier = {'Small': 0.50, 'Medium': 1.00, "Large": 1.50}
        
    
    def display_menu(self):
        print('Menu:')
        for item, base_price in self.base_menu.items():
            prices = [f"{size.title()}: £{float(base_price) * float(multiplier):.2f}" for size, multiplier in self.size_multiplier.items()]
            print(f"{item.title()}, " + ", ".join(prices))

    def calculate_item_cost(self, drink_type, size):
        drink_type = drink_type
        size = size  
        if drink_type not in self.base_menu:
            raise ValueError(f"Invalid drink type: {drink_type}")
        if size not in self.size_multiplier:
            raise ValueError(f"Invalid size: {size}")
        
        base_price = self.base_menu[drink_type]
        size_multiplier = self.size_multiplier[size]
        return float(base_price) * float(size_multiplier)
#parts of the order are done here. that includes price/adding to the order
class Order:
    def __init__(self):
        self.menu = Menu()
        self.orders = []

    def add_order(self, size, drink_type):
            for order in self.orders:
                if order[0] == drink_type and order[1] == size:
                    order[2] +=1
                    return
            self.orders.append([drink_type, size, 1])
            
    def calculate_total(self):
            """calculating the current cost based on current orders."""
            total = 0
            for drink_type, size, quantity in self.orders:
                try:
                    item_total = self.menu.calculate_item_cost(drink_type, size) * quantity


                #if isinstance(item_total, (float,int)):
                    print(f"{drink_type} ({size}) x {quantity}: £{item_total:.2f}")
                    total += item_total
                #else:
                    #raise ValueError(f'Item total is not a numeric value: {item_total}')
                    
                except ValueError as e:
                    print(f'Error calculating total: {e}')
                    return 0
            return float(total)

#starting point of the bot. it all starts from here, it inititates the menu view, and health and safety 
class CoffeeBot:
    def __init__(self):
        self.menu = Menu()
        self.order = Order()
        self.health_risk_assessment = HealthRiskAssessment()
        self.make_order = MakeOrder()
          
    user_input = input("Please touch screen to start \n>")
    def run(self):
        try:
            self.menu.display_menu()
            #asking customer a safety question. allergies
            introduction = input(
            '''Welcome to the cafe!, before I take your order do you 
            have any allergies or health issues I need to be made 
            aware of? Please Push - (y/n) \n> ''').lower()
            
            if introduction == 'y':
                HealthRiskAssessment().run()  #customers response yes or no
            elif introduction == 'n':         #no carries on the order process
                MakeOrder().run()             #yes returns the health and safety assesment 
            else:
                print("Invalid input. Please enter 'y' or 'n. ")
                self.run()

        except (EOFError, KeyboardInterrupt):
            print("/Input interrupted. Exiting. ")
        except Exception as e:
            print(f'An error occurred: {e}')

#Class where the order is created and finalized. too difficult to do seperate
class MakeOrder:
    def __init__(self):
        self.menu = Menu()   #instantiates from the menu and order class to be able to use the functions them classes provide
        self.order = Order() #as they are important in maintaining orders, prices
    
    def get_cup(self): #asks if the customer wants to use their own cup or not (enviromentally friendly)
        while True:
            self.cup_used = input('Would you like to use your own cup/s or our own? (y/n) \n >').lower()
            if self.cup_used == 'y': 
                print('''
                If yes, we thank you for caring about the environment ! 
                Our own cups arent re-usable, i would advise find a cup you love,
                and let us use it to make your coffee!!
                ''')
                return 'Yes'
            elif self.cup_used == 'n':  #just returns yes or no
                return 'No'
            else:
                print("Invalid option. Please enter (y/n) ")
    
    def get_size(self): #function used to collect sizes of each drink ordered
        while True:     #has an affect on price, so important function, each size has a different price depending on which coffee is chosen due to base price 
            self.size = input('''What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n >''').lower()
            if self.size == 'a':
                return 'Small'
            elif self.size == 'b':  #returns small, medium, large for the drink sizes
                return 'Medium'     #uses a b or c to pick 
            elif self.size == 'c':
                return 'Large'
            else:
                print("Invalid size option, please enter (a/b/c)")
                
        
    def get_drink_type(self): #function used to decide what drink the customer would like
        while True:           #important functions, has an affect on the prize, also depending on size. due to calculations being done on the individual prices and sizes
            self.drink_type = input('''What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n >''').lower()
            if self.drink_type == 'a':
                return 'Brewed Coffee'
            elif self.drink_type == 'b':  #uses an a, b,c method to decide
                return 'Mocha'            #returns names of the coffees
            elif self.drink_type == 'c':  #all coffees have a base price, sizes price varies, makes each coffee price different 
                return 'Latte'
            else:
                print('Invalid drink option, please try (a/b/c)')
        
    def order_milk(self): #this is an extra function, just for addtional user interaction.
        while True:       #this gets the type of milk the customer wants just to add when the names of the drinks get printed out
            self.milk = input(f'And what kind of milk for your {self.drink_type}? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n[d] Almond \n[e] No Milk \n > ').lower()
            if self.milk == 'a':
                return f'2% milk'
            elif self.milk == 'b':   #this uses the same a,b,d,d,e, in a while loop, if,elif,else method
                return f'non-fat'    #returns the names of the milk 
            elif self.milk == 'c':
                return f'soy'
            elif self.milk == 'd':
                return "Almond"
            elif self.milk == 'e':
                return "no milk"
            else:
                print('Invalid milk option, please try ')
                
        
    def run (self): #runs the make order class. gathers information from functions above
                    #also instantiates from parent classes 
        input('Push the screen to start, how can we help....')

        print(f'Using own cup: {self.get_cup()}') #message printed get cup function has been returned 

        more_items = 'y' #boolean to keep the order open as long as they want to add more 
        drinks = [] #lists drink to allow us to print out a itemized bill
        while more_items == 'y':
            size = self.get_size() #function above
            drink_type = self.get_drink_type() #function above
            milk_type = self.order_milk() #function above
          
            drink = (f"{size} {drink_type}")
            print(f'We have a: {milk_type} {drink.lower()}') #an additional message printed when each order has been collected

            while True:
                confirmation = input('Can we confirm that is part of/ or your order please? (y/n) \n >').lower().strip()
                if confirmation == 'y':
                    self.order.add_order(size, drink_type) #function from menu class
                    drinks.append(drink)
                    break                 #while loop, allows you to restart the order from the drink selection if a mistake was made
                elif confirmation == "n": #if yes, it break and continue the bot 
                    print("Restarting the drink order")
                    return self.run()  #restarts if a mistake was made


            print('Order:')
            for drink in drinks:
                print("-", milk_type, drink)   #prints out the drinks after theyre confirmed in the order

            
            more_items = input('Is there anything else you would like to add? (y/n) \n > ').lower().strip()
            if more_items == 'n':
                #final = FinalizeOrder(self.order)
                return self.confirm_and_finalize()  #if no more items are to be added, the order is confirmed and finalized


    def confirm_and_finalize(self):  #function used to calculated the total of the bill and print out an itemized bill
        self.total = self.order.calculate_total()  #using function from the order class
        while True: #while loop used to be more robust in regard to user input- incorrect input will not break it until its something the bot requires
            tip_choice = input("Would you like to add a tip? (yes/no or y/n)").lower()
            #gives the customer a choice to add a tip and will be used in the final receipt 
            if tip_choice in ['yes', 'y']: #allows multiple inputs

                while True: #while loop used for robustness against invalid inputs. 
                    try:   #try-except block extra layer- wont break entire bot until numerical value is entered
                        tip_amount = float(input('Please enter amount: £0.00 \n>'))
                        break #breaks loop once correct input is inputted--- asks specficially in the format that it requires
                    except ValueError:
                        print('Invalid response. Please enter a total amount.')  #message printed if incorrect input is detected
                       
                break
            elif tip_choice in ['no', 'n']:
                tip_amount = 0.0   #if no is selected, tip amount is sent a 0.0
                break
            else:
                print("invalid response. please use instructions")

        name = input("Can I get your name please? ").title() #name before order is finalised
        print('\nYour Total:') #message printed before receipt is printed

        vat_rate = float(0.20)
        vat_amount = float(self.total) * float(vat_rate)
        total_with_vat = float(self.total) + float(vat_amount)
        final_amount = float(total_with_vat) + float(tip_amount)  #working out amounts now tip and tax is involved

        #name = input("Can I get your name please? ").title()
        print(f"\nSubtotal: £{self.total:.2f}")
        print(f"VAT (20%): £{vat_amount:.2f}")
        print(f"Total with VAT: £{total_with_vat:.2f}")   #prints out the bill 
        print(f"Tip: £{tip_amount:.2f}")
        print(f"Final Total: £{final_amount:.2f}")
        print(f"\n{name}, your drinks will be ready shortly. Thank you for your order!")

#Class made specifically to ask safety questions if trigerred in the inital question.
class HealthRiskAssessment:
    def __init__(self):
        self.make = MakeOrder()

    def run(self):

        while True:
            allergies = input('''Can you tell me which allergies you have so I can help advise 
                                on your decision today and inform the baristas for your safety? 
                                (e.g., Dairy, Seeds) ''').lower().strip()
            if not allergies:
                print('Please enter your allergies or type "none" if no allergies')
                continue
            if allergies == 'none':
                print('No health risks identified. lets continue witht the order!')
                return self.make.run()

            while True:
                if 'dairy' in allergies:
                        response = input('''We offer these alternatives: Oat, Almond, and Soy. Are any of these okay? (y/n) ''').lower()

                        if response == 'y':
                            print("Great, youll be able to choose your alternative when making your order")
                            return self.make.run()
                        elif response == 'n':
                            print("We offer no safe alternatives, we do apologise.")
                            return bot.run()
                        else:
                            print("Invalid response, please use (y/n)")
                            continue

                elif 'seeds' in allergies:
                    print('''Seeds are only found in our sandwhiches and wraps. Please check the label or ask us.
                            seeds contained in our products are: Poppy, Sunflower, sessame''')
                    
                    response = input("Do any of these seeds affect you? (y/n) \n>").lower()

                    if response == 'n':
                        res2 = input("We advise to be cautious when ordering food, would you like to continue with a drink? (y/n) \n> ").lower()
                        if res2 == 'y':
                            print('We can safely proceed. All alternatives are offered on the menu.')
                            return self.make.run()
                        elif res2 == 'n':
                            print("Im sorry we couldnt find an alternative for you. We will learn and ensure this doesnt happen again")
                            return bot.run()
                        else:
                            print("Invalid reponse. Please use (y/n)")
                            continue
                        
                    if response == 'y':
                        res2 = input("We advise not to order any of our food items. Would you like to continue with a drink? (y/n) \n>")
                        if res2 == 'n':
                            print("Sorry we have no alternatives for this. We will learn and make sure to fix this.")
                            return bot.run()
                        elif res2 == 'y':
                            print('We can safely proceed. All alternatives are offered on the menu.')
                            return self.make.run()
                        else:
                            print("Invalid response. Please respond with (y/n)")
                            continue
                else:
                    print("Invalid response, please try again.")
                    continue

            
#survery to be conducted when the order is finalised and receipt has been printed
class SurveyBot():
    
    def __init__(self):
        self.rating = None #ratings and feedback are empty until input. 
        self.feedback = None

    def survey_intro(self):
        survey_choice = input('''
                            Would you like to take a survey for us (y/n) ?
                            We politey ask for you to take the time so we can 
                            improve the service ! Your feedback is highly valuable  \n >
                            ''').lower()
        if survey_choice == 'y':
            self.survey_questions() #proceeding to survey function
        elif survey_choice == 'n':
            print("Thank you for using us today ! have a great day !")
            return bot.run()
        else:
            print('Invalid input please use (y/n)')
            return self.survey_intro()
        
    def survey_questions(self):
        #asking for a rating
        try:
            self.rating = int(input("On a scale of 1-5, how would you rate this experience? \n>"))

            if self.rating < 1 or self.rating > 5:
                print("Please provide a rating between 1 and 5.")
                return self.survey_questions()
            
        except ValueError:
            print("please provide a rating between 1-5")
            return self.survey_questions()
        #reinforcing the rating the customer has given. thanking them. 
        print(f"Thank you for the {self.rating}-star rating! be sure to follow us on social media for a chance to win exclusive prizes")
        self.ask_for_feedback()
    
    def ask_for_feedback(self):
        #asking if feedback wants to be left. 
        feedback_choice = input("Would you like to leave us feedback (y/n) ?: \n>").lower()
        print("Thank you for your valuable feedback!")

        if feedback_choice == 'y':
            self.feedback = input("Please leave your feedback below: \n>")
            print("Thank you for your feedback!")
        elif feedback_choice == 'n':
            print("Thank you for using us today ! ")
            return bot.run()
        else:
            print("Invalid input, please use (y\n)")
            return self.ask_for_feedback()
        
        self.end_survey()

    def end_survey(self):
        print("You have successfully completed the survey. Have a great day!")
        return self.quit_survey()

    def quit_survey(self):
        print("Finished.")
        exit()
        bot.run()

        
#run the chat bot from here
bot = CoffeeBot()
bot.run()
bot1 = SurveyBot()
bot1.survey_intro()