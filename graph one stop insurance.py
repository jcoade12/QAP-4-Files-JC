#jack coady one stopinsurance, QAP4

#import my formats
import datetime
import FormatValues as FV

#.dat file
f = open ('OSICDEF.dat')
#constants
Next_policy_num = int(f.readline())
Basic_premium = (f.readline())
Additional_carsdiscount= (f.readline())
Extra_liability_coverage = (f.readline())
Glass_coverage = (f.readline())
Loaner_car_coverage= (f.readline())
HST= (f.readline())
Processing_fee_for_monthly= (f.readline())

#my inputs
customer_first=input("Enter customer name: ").title()
customer_last=input("Enter customer last name: ").title()
adress=input("Enter customer adress: ")
city=input("Enter customer city: ").title()


#confirmation of province
list=["Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Nova Scotia", "Ontario", "Prince Edward Island" ,"Quebec", "Saskatchewan"]
   
while True:
   province=input("please enter chosen province: ")
   if province in list:
    break
else:
    print("error not a valid province")

postal_code=input("Enter postal code: ")
phone_numb=input("Enter customer phone number: ")
numbers_of_cars_being_insured=input("Enter number of cars being insured: ")
#option for liability
while True:
    extra_ility=input("would customer like extra liabilty? Y for yes N for no: ").upper()

    if extra_ility:=("Y"):
        extra_libilty=input("please enter amount chosen")
        break
    else: 
        extra_libilty=()
        break
#option for glass covrage
while True:
    glass_option=input("would you like glass covrage Y for yes N for no: ").upper()
    
    if glass_option==("Y"):
       break
    
    else:
       break
#loner car validation
    
while True:
    lonercar_pref=input("would they like a loner car? Y for yes N for no: ").upper()
    if lonercar_pref==("Y"):
        lonercar=("Yes") 
        (Loaner_car_coverage)*(numbers_of_cars_being_insured)
        break
    if lonercar_pref==("N"):
        lonercar=("No")
        break
    
    while True:
        payment_prefrance=input("would they like to pay in monthly or full M or F: ").title()
        if payment_prefrance==("M"):
            payment_choice=("Monthly")
            break
        if payment_prefrance==("F"):
            payment_choice=("Full")
            break

#my calculations
discount=Additional_carsdiscount*Basic_premium
primum_for_extra_car=discount*numbers_of_cars_being_insured
insurance_primums=Basic_premium+primum_for_extra_car





#the recept and fromatting

print("--------------------------------------------------------")
print()
print(f"customer name:     {customer_first}{customer_last:>10s}")
print()
