import my_functions
import outer_package.my_package.helpers as h
import outer_package.my_package.constants as c

if __name__ == '__main__':

    h.print_greeting_message(c.GRETTINGS)

    a= my_functions.get_valid_integer()
    b=my_functions.get_valid_integer()
    result= my_functions.my_sum(a,b)



    print(f'{a}+{b} = {result}')


