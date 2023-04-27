from re import L
import pandas as pd 


def mainmenu():
    print("Welcome to the dashbaord")
    print("1) All data") 
    print("2) Specific Date range")
    print("3) Specific Car brand")
    print("4) Specifc Car model")

    return int(input("Enter (1-3) :"))

def get_start_date():
    Flag = True 
    while Flag:
        start_date = input("Enter start date (DD/MM/YY) :")
        if start_date == "":
            print("Please enter the date\n")
        else:
            try:
                pd.to_datetime(start_date,dayfirst=True)
            except:
                print("ERROR: Check your format\n")
                Flag = True
            else:
                print("-  Data entered successfully\n")
                return start_date

def get_end_date():
    Flag = True 
    while Flag:
        end_date = input("Enter end date (DD/MM/YY) :")
        if end_date == "":
            print("Please enter the date\n")
        else:
            try:
                pd.to_datetime(end_date,dayfirst=True)
            except:
                print("ERROR: Check your format\n")
                Flag = True
            else:
                print("-  Data entered successfully\n")
                return end_date


def all_date():
    df = pd.read_csv("CarsSold.csv")
    df["Date Bought"] = pd.to_datetime(df["Date Bought"],dayfirst=True)
    df = df.sort_values(by="Date Bought")
    print("\n\n\n\n\n\n")
    print(df)



def specific_date_range():
    start_date = get_start_date()
    end_date = get_end_date()


    print("- - - - DATA VIEWER 0.01V - - - -\n")

    df = pd.read_csv("CarsSold.csv")
    df["Date Bought"] = pd.to_datetime(df["Date Bought"],dayfirst=True)
    df = df.sort_values(by="Date Bought")

    viewer = (df["Date Bought"] >= start_date) & (df["Date Bought"] <= end_date)
    df_2 = df.loc[viewer]
    print(df_2)

def specific_car_brand():
    brand_input = str(input("Please enter what car brand you want to view? :")).upper()

    df = pd.read_csv("CarsSold.csv")
    df["Date Bought"] = pd.to_datetime(df["Date Bought"],dayfirst=True)
    df = df.sort_values(by="Date Bought")
    df2 = df.where(df["Car brand"] == brand_input)
    df2.dropna(inplace=True)
    print(df2)

def specific_car_model():
    carmodel_input = str(input("Please enter what car model you want to veiw? :")).upper()

    df = pd.read_csv("CarsSold.csv")
    df["Date Bought"] = pd.to_datetime(df["Date Bought"],dayfirst=True)
    df = df.sort_values(by="Date Bought")
    df2 = df.where(df["MODEL"] == carmodel_input)
    df2.dropna(inplace=True)
    print(df2)



def selection():
    if x == 1:
        all_date()
    elif x == 2: 
        specific_date_range()
    elif x == 3:
        specific_car_brand()
    elif x == 4:
        specific_car_model()








x = mainmenu()
selection()



