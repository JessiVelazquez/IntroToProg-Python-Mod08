# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# JVelazquez,12.5.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strChoice = ""  # User choice from menu options


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's name
        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JVelazquez,12.5.2020,Modified code to complete assignment 8
    """

    # Fields
    # Constructors
    def __init__(self, product_name, product_price):
        # Attributes
        try:
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception("Error setting initial values")

    # Properties
    # product_name
    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    # product_price
    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if str(value).isnumeric() == True:
            self.__product_price = value
        else:
            raise Exception("Names cannot be numbers")

    # Methods
    def __str__(self):
        return self.__product_name + "," + str(self.__product_price)

    # -- End of Class


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            name, price = line.split(",")
            Obj = Product(name, price)
            list_of_rows.append(Obj)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, Product):
        """

        :param file_name: Text file to be opened and written to by program.
        :param list_of_rows: (list) Task list data table
        :return: (list) of dictionary tows
        """
        file_name = open(file_name, "w")
        for objProd in Product:
            file_name.write(str(objProd) + "\n")
        file_name.close()

    @staticmethod
    def add_data_to_list(name, price, list_of_rows):
        """ Adds a row of data to item list data table

        :param product: (string)
        :param price: (float)
        :param list_of_rows: (list)
        :return: (list) of dictionary rows
        """
        obj = Product(name, price)
        list_of_rows.append(obj)
        return list_of_rows, 'Success'


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data in list of product objects
        2) Add data to list of product objects
        3) Save data to file and exit program        
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    def print_current_list_of_products(Product):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current products in list are: *******")
        for objProd in Product:
            print(objProd)
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_product_and_price(optional_message=''):
        """ Collects task and priority values from user

        :param optional_message: optional message to be displayed
        :return: (string) product
        :return: (float) price
        """
        product = str(input("Enter a product: "))
        price = float(input("Enter its price: "))
        return product, price

    @staticmethod
    def print_entry_to_user(optional_message=''):
        """
        :param optional_message:
        :return:
        """
        print(str(objProd) + " has been added to list.")
        print()  # add line for looks

    @staticmethod
    def print_user_message(optional_message=''):
        """
        :param optional_message:
        :return:
        """
        print(optional_message)
        print()  # add line for looks


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

try:
    # Load data from file into a list of product objects when script starts
    FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)

except FileNotFoundError as e:
    print(e)
    print("No existing 'products.txt' found. New file will be automatically created "
          "when new data is saved.")
    print()

while (True):
    try:
        # Show user a menu of options
        IO.print_menu_Tasks()

        # Get user's menu option choice
        strChoice = IO.input_menu_choice()

        # Show user current data in the list of product objects
        if strChoice == "1":
            IO.print_current_list_of_products(lstOfProductObjects)
            IO.input_press_to_continue()
            continue

        # Let user add data to the list of product objects
        elif strChoice == "2":
            name, price = IO.input_new_product_and_price()
            objProd = Product(name, price)
            IO.print_entry_to_user()
            FileProcessor.add_data_to_list(name, str(price), lstOfProductObjects)
            IO.input_press_to_continue()
            continue

        # let user save current data to file and exit program
        elif strChoice == "3":
            FileProcessor.write_data_to_file(strFileName, lstOfProductObjects)
            IO.print_user_message("Data saved to file. Program closed!")
            break

        else:
            IO.print_user_message("Not a valid entry, please enter a choice 1-3.")
            continue

    except ValueError as e:
        print(e)
        print("Price must be a numeric value. Item not added to list. "
              "Please enter numeric value for 'Price'.")
        print()
        continue

# Main Body of Script  ---------------------------------------------------- #
