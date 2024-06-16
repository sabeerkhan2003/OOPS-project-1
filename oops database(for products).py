

import sqlite3
v1=sqlite3.connect("data3.db")
print("connected successfully")

v2=v1.cursor()

'''statement="""create table products(
        product id int,
        name varchar,
        description varchar,
        prize varchar2,
        category varchar);"""'''
    
'''v2.execute(statement)
print("table created")'''

v2.execute('''insert into products values(1,"Wireless Mouse","Ergonomic wireless mouse with adjustable DPI",500,"Electronics")''')
v2.execute('''insert into products values(2,"Bluetooth headphones","Noise-cancelling over-ear headphones with Bluetooth 5.0",2500,"Electronics")''')
v2.execute('''insert into products values(3,"Mechanical keyboard"," Mechanical keyboard with customizable RGB lighting",900,"Electronics")''')
v2.execute('''insert into products values(4,"Smart watch","Fitness tracking smartwatch with heart rate monitor",3000,"wearbles")''')
v2.execute('''insert into products values(5,"Running Shoes","Lightweight running shoes with breathable mesh",2000,"Footwear")''')
v2.execute('''insert into products values(6,"Coffee maker","12-cup programmable coffee maker with built-in grinder",1300,"Home Appliances")''')
v2.execute('''insert into products values(7,"Vacuum Cleaner","Cordless vacuum cleaner with powerful suction",3000,"Home Appliances")''')
v2.execute('''insert into products values(8,"Yoga Mat","Non-slip yoga mat with carrying strap",1000,"Fitness")''')
v2.execute('''insert into products values(9,"Water Bottle","Insulated stainless steel water bottle",500,"Accessories")''')
v2.execute('''insert into products values(10,"Smartphone","Latest model smartphone with 128GB storage",20000,"Electronics")''')
print("Inserted")


v1.commit()