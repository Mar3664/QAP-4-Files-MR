# Program that allows the user to enter the total amount of sales each month and graphs data.
# Written on July 17 2023
# Written by Marlanna Ryan

# Required imported libraries
import matplotlib.pyplot as plt

# Lists
MonthsLst = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
MonthSalesLst = []

# Program and Graph
for month in MonthsLst:
    MonthSales = float(input(f"Enter Total Amount of Sales for {month}: "))
    MonthSalesLst.append(MonthSales)

MonthLstFormated = [month[:3] for month in MonthsLst]

plt.title("Sales over 12 months")
plt.plot(MonthLstFormated, MonthSalesLst, color="green", marker="x")

plt.xlabel("Time (months)")
plt.ylabel("Sales ($)")

plt.ylim(bottom=0)

plt.grid(True)

plt.show()




