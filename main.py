# Program for One Stop Insurance Company to create new insurance policy information.
# Written on July 17 2023
# Written by Marlanna Ryan

# Import required libraries
import datetime
import time
from tqdm import tqdm


# Open the defaults file and read the values into variables.
f = open('OSICDef.dat', 'r')
NXT_POLICY_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
DIS_ADD_CARS = float(f.readline())
COST_EXT_LIABILITY = float(f.readline())
COST_GLASS = float(f.readline())
COST_LOANER = float(f.readline())
HST_RATE = float(f.readline())
PROCESS_FEE = float(f.readline())
f.close()

# Main program
while True:
    CustFirName = input("Enter the customer's first name: ").title()
    CustLasName = input("Enter the customer's last name: ").title()
    StrAdd = input("Enter the customer's address: ")
    City = input("Enter the customer's city: ").title()

    while True:

        Prov = input("Enter the customer's province (LL): ").upper()

        ProvLst = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]

        if Prov == "":
            print("Error - Province cannot be blank.")
        elif len(Prov) != 2:
            print("Error - Province must contain 2 characters only.")
        else:
            break

    Postal = input("Enter the customer's postal code: ")
    PhoneNum = input("Enter the customer's phone number: ")
    NumCarsIns = int(input("Enter the number of cars to be insured: "))

    CostExtLiability = input("Would the customer like extra liability (Y/N): ").upper()
    if CostExtLiability == "Y":
        Liability = COST_EXT_LIABILITY * NumCarsIns
    elif CostExtLiability == "N":
        Liability = 0

    CostGlass = input("Would the customer like glass coverage? (Y/N): ").upper()
    if CostGlass == "Y":
        Glass = COST_GLASS * NumCarsIns
    elif CostExtLiability == "N":
        Glass = 0

    CostLoaner = input("Would the customer like to receive a loaner car? (Y/N): ").upper()
    if CostLoaner == "Y":
        Loaner = COST_LOANER * NumCarsIns
    elif CostExtLiability == "N":
        Loaner = 0

    while True:

        PayMethod = input("Is the customer paying in full or monthly installments? (Full/Monthly): ").title()

        PayMethodLst = ["Full", "Monthly"]

        if PayMethod == "":
            print("Error - Payment method cannot be blank.")
        elif PayMethod not in PayMethodLst:
            print("Error - Payment method must be in either full or monthly installments.")
        else:
            break

# Calculations
    InsPremiums = BASIC_PREMIUM + ((BASIC_PREMIUM * (NumCarsIns - 1)) * (1 - DIS_ADD_CARS))
    TotExtCost = Liability + Glass + Loaner
    TotInsPremium = InsPremiums + TotExtCost
    HST = TotInsPremium * HST_RATE
    TotCost = TotInsPremium + HST
    MonPayment = (PROCESS_FEE + TotCost) / 8

    InvDate = datetime.datetime.now()
    InvDateDsp = InvDate.strftime("%Y-%m-%d")

    NxtPayDate = (datetime.date(InvDate.year, InvDate.month + 1, 1))
    NxtPayDateDsp = NxtPayDate.strftime("%Y-%m-%d")

# Progress bar
    print()
    print()
    for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=100, bar_format="{desc}  {bar}"):
        time.sleep(.1)
    print("Policy information processed and saved.")
    time.sleep(1)
    print()

# Concatenations
    CustName = CustFirName + " " + CustLasName
    CustAdd = StrAdd + " " + City + " " + Prov + " " + Postal

# Display
    print()
    print("           ONE STOP INSURANCE COMPANY")
    print("==================  RECEIPT  ==================")
    print(f"Date: {InvDateDsp:>41s}")
    print(f"Policy Number: {NXT_POLICY_NUM:>32d}")
    print("-----------------------------------------------")
    print("Customer Information:")
    print("----------------------")
    print(f"Name: {CustName:>41s}")
    print(f"Address: {CustAdd:>38s}")
    print(f"Phone Number: {PhoneNum:>33s}")
    print("-----------------------------------------------")
    print("Insurance Information:")
    print("----------------------")
    print(f"Number of Cars Insured: {NumCarsIns:>23d}")
    BasicPremiumDSP = "${:,.2f}".format(BASIC_PREMIUM)
    print(f"Basic Premium: {BasicPremiumDSP:>32s}")
    LiabilityDsp = "${:,.2f}".format(Liability)
    print(f"Basic Premium: {LiabilityDsp:>32s}")
    GlassDsp = "${:,.2f}".format(Glass)
    print(f"Basic Premium: {GlassDsp:>32s}")
    LoanerDsp = "${:,.2f}".format(Loaner)
    print(f"Basic Premium: {LoanerDsp:>32s}")
    TotInsPremiumDsp = "${:,.2f}".format(TotInsPremium)
    print(f"Basic Premium: {TotInsPremiumDsp:>32s}")
    print("-----------------------------------------------")
    print("Taxes and Fees:")
    print("----------------------")
    HSTDsp = "${:,.2f}".format(HST)
    print(f"Basic Premium: {HSTDsp:>32s}")
    ProcessFeeDSP = "${:,.2f}".format(PROCESS_FEE)
    print(f"Basic Premium: {ProcessFeeDSP:>32s}")
    TotCostDsp = "${:,.2f}".format(TotCost)
    print(f"Basic Premium: {TotCostDsp:>32s}")
    print("-----------------------------------------------")
    print("Payment Information:")
    print("----------------------")
    print(f"Payment Method: {PayMethod:>31s}")
    print(f"Next Payment Date: {NxtPayDateDsp:>28s}")
    MonPaymentDsp = "${:,.2f}".format(MonPayment)
    print(f"Basic Premium: {MonPaymentDsp:>32s}")
    print("===============================================")
    print()

# Crate new policy number or end
    Continue = input("Would you like to crate a new insurance policy? (Y/N): ").upper()
    if Continue == "Y":
        NXT_POLICY_NUM += 1
    if Continue == "N":
        print("Thank you for using this program.")
        print()
        break

# Write the values to a file for future reference.
f = open('Policies.dat', 'a')
f.write(f"{NXT_POLICY_NUM},")
f.write(f"{InvDateDsp},")
f.write(f"{CustFirName},")
f.write(f"{CustLasName},")
f.write(f"{StrAdd},")
f.write(f"{City},")
f.write(f"{Prov},")
f.write(f"{Postal},")
f.write(f"{PhoneNum},")
f.write(f"{NumCarsIns},")
f.write(f"{Liability},")
f.write(f"{Glass},")
f.write(f"{Loaner},")
f.write(f"{PayMethod},")
f.write(f"{TotInsPremium}\n")
f.close()

# Write the current values back to the defaults file.
f = open('OSICDef.dat', 'w')
f.write(f"{NXT_POLICY_NUM}\n")
f.write(f"{BASIC_PREMIUM}\n")
f.write(f"{DIS_ADD_CARS}\n")
f.write(f"{COST_EXT_LIABILITY}\n")
f.write(f"{COST_GLASS}\n")
f.write(f"{COST_LOANER}\n")
f.write(f"{HST_RATE}\n")
f.write(f"{PROCESS_FEE}\n")
f.close()










