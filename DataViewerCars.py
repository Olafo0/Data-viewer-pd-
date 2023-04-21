import pandas as pd 

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


def main():
    print("- - - - DATA VIEWER 0.01V - - - -\n")

    df = pd.read_csv("CarsSold.csv")
    df["Date Bought"] = pd.to_datetime(df["Date Bought"],dayfirst=True)
    df = df.sort_values(by="Date Bought")

    viewer = (df["Date Bought"] >= start_date) & (df["Date Bought"] <= end_date)
    df_2 = df.loc[viewer]
    print(df_2)







start_date = get_start_date()
end_date = get_end_date()
main()