employee_name = input("Please Enter your name: ")
monthly_sales = input("Enter your monthly sales: ")
monthly_sales = int(monthly_sales)

commission  = round(((13 / 100) * monthly_sales), 2)

print(f"Ok {employee_name}, This month you won ${commission}")
