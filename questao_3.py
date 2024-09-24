import sys
import json

def find_lowest(data):
    lowest = float('inf')

    for value in data:
        if(not value):
            continue

        if(value < lowest):
            lowest = value

    return lowest

def find_highest(data):
    highest = 0

    for value in data:
        if(not value):
            continue 

        if(value > highest):
            highest = value

    return highest

def lowest_revenue(data):
    for month, days in data.items():
        for day,revenues in enumerate(days):
            print(f"menor faturamento em {month}/{day+1} = {find_lowest(revenues)}")

def highest_revenue(data):
    for month, days in data.items():
        for day,revenues in enumerate(days):
            print(f"maior faturamento em {month}/{day+1} = {find_highest(revenues)}")

def get_month_mean(days):
    total = 0
    for day in days:
        total += sum(day)
    return total/len(days)


def days_with_superior_mean(data):
    for month, days in data.items():
        month_mean = get_month_mean(days)
        total_days_with_superior_mean = 0

        for revenues in days:
            day_mean = sum(revenues)/len(revenues)
            if(day_mean > month_mean):
                total_days_with_superior_mean+=1

        print(f"{month} teve {total_days_with_superior_mean} dias com a média superior a media mensal")


if __name__ == '__main__':
    total_params = len(sys.argv)

    if(total_params < 2):
        print("Usage: python3 questao_3.py data.json")
        sys.exit(1)

    data_file = sys.argv[1]
    data = None

    with open(data_file, 'r') as json_file:
        data = json.load(json_file)
    
    lowest_revenue(data)
    print("-"*30)
    highest_revenue(data)
    print("-"*30)
    days_with_superior_mean(data)
