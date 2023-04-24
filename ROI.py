class ROI():
        
    def __init__(self):
        self.cash_flow = 0
        self.property_value = 0
        self.income = {}
        self.total_income = 0
        self.expenses = {}
        self.total_expenses = 0
        self.ROI = {}
        self.total_investment = 0
        self.total_expenses = 0
        self.ROI_percent = 0

    def driver(self):
        driver_switch = True
        while driver_switch:
            command_prompt = input("what do you want to do, you can say 'show cash flow'  'show ROI'  'show expenses'  'show income'  'input expenses'  'input income'.").lower()
            if command_prompt == "show cash flow":
                self.cal_total_expenses()
                self.cal_total_income()
                self.cal_cash_flow()
                print(f"your annual cash income is ${self.cash_flow}")
                self.driver()
            elif command_prompt == "show roi":
                self.cal_total_expenses()
                self.cal_total_income()
                self.cal_cash_flow()
                self.input_down_payment()
                print(f"your ROI is {self.ROI_percent}%")
            elif command_prompt == "show expenses":
                pass
            elif command_prompt == "show income":
                pass
            elif command_prompt == "input expenses":
                self.input_property_value()
            elif command_prompt == "input income":
                self.input_rental()
            else:
                print("ERROR please input a valid command")
                self.driver()

    def input_property_value(self):
        property_value = input("what did you purchase the property for? You can say 'back' to return to main menu")
        if property_value.isdigit():
            self.property_value = float(property_value)
            self.input_tax()
        elif property_value.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_property_value()

    def input_tax(self):
        tax_input = input("what is the monthly tax on the property? You can say 'back' to return to main menu")
        if tax_input.isdigit():
            self.expenses["tax"] = float(tax_input)
            self.input_insurance()
        elif tax_input.lower() == "back":
            self.driver()
        else:
                print("ERROR please input a valid command")
                self.input_tax()

    def input_insurance(self):
        insurance_input = input("what do you pay on insurance? You can say 'back' to return to main menu")   
        if insurance_input.isdigit():
            self.expenses["insurance"] = float(insurance_input)
            self.input_utilities()
        elif insurance_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_insurance()

    def input_utilities(self):
        #utilities (electric water garbage sewer gas misc)
        utilities_Q = input("are you paying for the utilities or is the renter? you can say 'yes'  'no'  'back'")
        if utilities_Q.lower() == "yes":
            self.input_electricity()
        elif utilities_Q.lower() == "no":
            self.input_hoa()
        elif utilities_Q.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_utilities()

    def input_electricity(self):
        electric_input = input("what is the monthly electric bill? You can say 'back' to return to main menu")
        if electric_input.isdigit():
            self.expenses["electric"] = float(electric_input)
            self.input_water()
        elif electric_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_electricity()
        
    def input_water(self):
        water_input = input("what is the monthly water bill? You can say 'back' to return to main menu")
        if water_input.isdigit():
            self.expenses["water"] = float(water_input)
            self.input_garbage()
        elif water_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_water()

    def input_garbage(self):
        garbage_input = input("what is the monthly garbage bill? You can say 'back' to return to main menu")
        if garbage_input.isdigit():
            self.expenses["garbage"] = float(garbage_input)
            self.input_sewer()
        elif garbage_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_garbage()

    def input_sewer(self):
        sewer_input = input("what is the monthly sewer bill? You can say 'back' to return to main menu")
        if sewer_input.isdigit():
            self.expenses["sewer"] = float(sewer_input)
            self.input_gas()
        elif sewer_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_sewer()

    def input_gas(self):
        gas_input = input("what is the monthly gas bill? You can say 'back' to return to main menu")
        if gas_input.isdigit():
            self.expenses["gas"] = float(gas_input)
            self.input_misc_utility()
        elif gas_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_gas()

    def input_misc_utility(self):
        misc_input = input("if you have any misc utilities please enter the total here? You can say 'back' to return to main menu")
        if misc_input.isdigit():
            self.expenses["misc_utilities"] = float(misc_input)
            self.input_hoa()
        elif misc_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_misc_utility()

    def input_hoa(self):
        hoa_input = input("what is your monthly cost for your HOA? You can say 'back' to return to main menu")
        if hoa_input.isdigit():
            self.expenses["HOA"] = float(hoa_input)
            self.input_lawn_snow()
        elif hoa_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_hoa()

    def input_lawn_snow(self):
        lawn_snow_input = input("what is your monthly cost for lawn/snow care? You can say 'back' to return to main menu")
        if lawn_snow_input.isdigit():
            self.expenses["lawn/snow"] = float(lawn_snow_input)
            self.input_vacancy()
        elif lawn_snow_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_lawn_snow()

    def input_vacancy(self):
        vacancy_input = input("what is your monthly savings cost for future vacancy? You can say 'back' to return to main menu")
        if vacancy_input.isdigit():
            self.expenses["vacancy"] = float(vacancy_input)
            self.input_repairs()
        elif vacancy_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_vacancy()

    def input_repairs(self):
        repairs_input = input("what is your monthly savings cost for future repairs? You can say 'back' to return to main menu")
        if repairs_input.isdigit():
            self.expenses["repairs"] = float(repairs_input)
            self.input_capEx()
        elif repairs_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_repairs()

    def input_capEx(self):
        capEx_input = input("what is your monthly savings cost for large expenses? You can say 'back' to return to main menu")
        if capEx_input.isdigit():
            self.expenses["capEx"] = float(capEx_input)
            self.input_management()
        elif capEx_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_capEx()

    def input_management(self):
        management_input = input("what is your monthly cost for property management? You can say 'back' to return to main menu")
        if management_input.isdigit():
            self.expenses["management"] = float(management_input)
            self.input_morgage()
        elif management_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_management()

    def input_morgage(self):
        morgage_input = input("what is your monthly morgage payment? You can say 'back' to return to main menu")
        if morgage_input.isdigit():
            self.expenses["morgage"] = float(morgage_input)
            self.input_misc()
        elif morgage_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_morgage()

    def input_misc(self):
        misc_input = input("if you have any aditional charges please add them up and input them here. You can say 'back' to return to main menu")
        if misc_input.isdigit():
            self.expenses["misc"] = float(misc_input)
            self.driver()
        elif misc_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_misc()

    def cal_total_expenses(self):
        for value in self.expenses.values():
            self.total_expenses += value
            return self.total_expenses
    
    def input_rental(self):
        rental_input = input("what are you charging per month on rent? You can say 'back' to return to main menu")
        if rental_input.isdigit():
            self.income["rental"] = float(rental_input)
            self.input_laundry()
        elif rental_input.lower() == "back":
            self.input_laundry()
        else:
            print("ERROR please input a valid command")
            self.input_rental()

    def input_laundry(self):
        laundry_input = input("what are you charging per month for laundry? You can say 'back' to return to main menu")
        if laundry_input.isdigit():
            self.income["laundry"] = float(laundry_input)
            self.input_storage()
        elif laundry_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_laundry()

    def input_storage(self):
        storage_input = input("what are you charging per month for storage? You can say 'back' to return to main menu")
        if storage_input.isdigit():
            self.income["storage"] = float(storage_input)
            self.input_misc()
        elif storage_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_storage()

    def input_misc(self):
        misc_input = input("if you have any additional charges you can input them here? You can say 'back' to return to main menu")
        if misc_input.isdigit():
            self.income["misc'"] = float(misc_input)
            self.driver()
        elif misc_input.lower() == "back":
            self.driver()
        else:
            print("ERROR please input a valid command")
            self.input_misc()
        
    def cal_total_income(self):
        for value in self.income.values():
            self.total_income += value
            return self.total_income
            
    def cal_cash_flow(self):
        self.cash_flow = self.total_expenses - self.total_income
        self.cash_flow = self.cash_flow * 12
        return self.cash_flow

    def input_down_payment(self):
        down_payment_input = input("what did you put down on the house?")
        if down_payment_input.isdigit():
            self.ROI["down_payment"] = float(down_payment_input)
            self.input_closing_cost()
        else:
            print("ERROR please input a valid command")
            self.input_down_payment()

    def input_closing_cost(self):
        closing_cost_input = input("what was the closing cost?")
        if closing_cost_input.isdigit():
            self.ROI["closing_cost"] = float(closing_cost_input)
            self.input_rehab
        else:
            print("ERROR please input a valid command")
            self.input_closing_cost()

    def input_rehab(self):
        rehab_input = input("what did it cost to repair the building?")
        if rehab_input.isdigit():
            self.ROI["rehab"] = float(rehab_input)
            self.input_misc_costs
        else:
            print("ERROR please input a valid command")
            self.input_rehab()

    def input_misc_costs(self):
        misc_cost_input = input("are there any aditional costs")
        if misc_cost_input.isdigit():
            self.ROI["misc_costs"] = float(misc_cost_input)
            self.cal_ROI()
        else:
            print("ERROR please input a valid command")
            self.input_misc_costs()


    def cal_ROI(self):
        for value in self.ROI.values():
            self.total_investment += value
            return self.total_investment
        self.finish_ROI()

    def finish_ROI(self):
        self.ROI_percent = self.total_investment // self.cash_flow
        return self.ROI_percent

roi = ROI()

roi.driver()
