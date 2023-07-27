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
if numbers_of_cars_being_insured==1 :
    discount=1
#option for glass covrage
while True:
    glass_option=input("would you like glass covrage Y for yes N for no: ").upper()
    
    if glass_option==("Y"):
      glass_cov=("Yes")
    break
else:   
    glass_cov=(No)

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
extras=0
#my extras
extras_list=[lonercar,glass_cov,]
if ("yes") in extras_list:
    Extra_liability_coverage+extras

if lonercar==("yes"):
    loner_extra=Loaner_car_coverage*numbers_of_cars_being_insured

if glass_cov==("yes"):
   glass_extra=Glass_coverage*numbers_of_cars_being_insured
#my calculations
discount=Additional_carsdiscount*Basic_premium
extra_cars_cost=numbers_of_cars_being_insured*discount
insurance_primums=Basic_premium+extra_cars_cost
total_cost=insurance_primums+HST
monthly_pay=(total_cost+Processing_fee_for_monthly)/8
cur_date=datetime.date.today()
inv_date=cur_date.strftime("%m/%d/%y")
first_day_month=datetime.date(cur_date.year, cur_date.month % 12 + 1, 1)
pay_date=first_day_month.strftime("%m/%d/%Y")

#the recept and fromatting

print("-------------------------------------------------------------")
print()
print("                One Stop Insurance")
print("             Insurance Policy Information")
print(f"              invoice date:{inv_date}")
print()
print(f"customer name:          {customer_first}{customer_last:>10s}")
print(f"customer adress:        {adress}, {city}, {province}")
print(f"customer postal code:   {postal_code}")
print(f"customer phone number:  {phone_numb}")
print()
print(f"choice of payment:      {payment_choice}")
print(f"number of cars insured: {numbers_of_cars_being_insured}")
print(f"car loned:              {lonercar}")
print(f"glass insurance:        {glass_cov}")
print("-------------------------------------------------------------")
print(f"basic premium:          ${FV.FDollar2(Basic_premium):>10s}")
print(f"multi car discount:     ${FV.FDollar2(discount):>10s}")
print(f"multi car fees:         ${FV.FDollar2(extra_cars_cost):>10s}")
print(f"insurance premiums:     ${FV.FDollar2(insurance_primums):>10s}")
print()
print(f"Total Cost:             ${FV.FDollar2(total_cost):>10s}") 
print(f"monthly amount:         ${FV.FDollar2(monthly_pay):>10s}")
print(f"Next Payment Date:      ${FV.FDollar2(pay_date):>10s}")
print("_____________________________________________________________")
