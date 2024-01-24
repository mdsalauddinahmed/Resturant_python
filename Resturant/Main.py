from Menu import Pizza,Burger,Drinks,Menu
from Resturant import Resturant
from User import chef,Manager,Server,Customer
from order import Order

def main():
    menu=Menu()
    burger_1=Burger('Beef Burger',1000,'beef',['goru','haddi'])
    menu.add_menu_item('burger',burger_1)

    pizza_1=Pizza('chiken pizza',500,'large',['potato','onion','oil'])
    menu.add_menu_item('pizza',pizza_1)

    coke =Drinks('Coke',50,True)
    menu.add_menu_item('drinks',coke)



    #show menu item
    menu.show_menu()

    resturant=Resturant('kacchi bhai',2000,menu)

    manager=Manager('kalo shaheb Manager',343,'kalo@gmail.com','kaliyapor',1500,'24 jannuary,2024','Manager')
    baburchi=chef('lalo shaheb baburchi',343,'kalo@gmail.com','kaliyapor',1500,'24 jannuary,2024','Manager','Everything')
    server=Server('waiter',545,'waiter@.com','resturant',300,'23 januarry,2024','server')
    
    # print(manager)
    resturant.add_employee('Manager', manager)
    resturant.add_employee('chef', baburchi)
    resturant.add_employee('server', server)
   
  #show employers

    resturant.show_employee()

    #customer

    customer_1=Customer('salauddin',3456,'amirsalauddin@f.com','gazipur',100000)

    order_1=Order(customer_1,[pizza_1,coke])
    customer_1.pay_for_order(order_1)
    resturant.add_oreders(order_1)

    resturant.received_payment(order_1,2000,customer_1)

    print('Revenue :',resturant.revenue,'Balance :',resturant.balance)



#call the main function
if __name__ == '__main__':
    main()