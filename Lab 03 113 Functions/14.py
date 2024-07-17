price_a=30
price_b=20
price_c=10
price_o=30
price_s=10
weight_a=1
weight_b=2
weight_c=3
weight_o=6
distance_oa=100
distance_ab=100
distance_bc=200
distance_co=50
def read_input():
    """read input and store in global variable"""
    # need to declare variables as global variables because we need to assign their values
    global price_a, price_b, price_c, price_s,price_o
    global weight_a, weight_b, weight_c,weight_o
    global distance_oa, distance_ab, distance_bc, distance_co
    weight_a = float(input("weight of cargo to A: "))
    weight_b = float(input("weight of cargo to B: "))
    weight_c = float(input("weight of cargo to C: "))
    weight_o = float(input("weight of cargo to O: "))
    price_a = float(input("price of cargo to A: "))
    price_b = float(input("price of cargo to B: "))
    price_c = float(input("price of cargo to C: "))
    price_o = float(input("price of cargo to O: "))
    price_s = float(input("price of supply: "))
    distance_oa = float(input("distance O to A: "))
    distance_ab = float(input("distance A to B: "))
    distance_bc = float(input("distance B to C: "))
    distance_co = float(input("distance C to O: "))
def travel_speed(w):
    """calculate traveling speed using a formular that is given in the problem"""
    return 90/(30+w)+5

from math import ceil

def travel_time(s, d):
    """calculate total days to travel distance d using speed s.
       A fraction of day is roundup to full day """
    hours = d/s
    day = ceil(hours/24)
    return day

def cal_sub_profit(distance, net_weight, sell_weight, cargo_price_per_ton, supply_price_per_day):
    """calculate profit that is received when travel from a town to a next town"""
    speed = travel_speed(net_weight)
    cargo_price = sell_weight*cargo_price_per_ton
    supply_price = travel_time(speed,distance)*supply_price_per_day
    return cargo_price - supply_price
    
def calculate_profit():
    """calculate and return result profit from input data"""
    #step 1: from o to a
    w_net = weight_a+weight_b+weight_c
    profit = cal_sub_profit(distance_oa,w_net,weight_a,price_a,price_s)
    #step 2: from a to b
    w_net = weight_b+weight_c
    profit = profit + cal_sub_profit(distance_ab,w_net,weight_b,price_b,price_s)
    #step 3: from b to c
    w_net = weight_c
    profit = profit + cal_sub_profit(distance_bc,w_net,weight_c,price_c,price_s)
    #step 4: from c to 0
    w_net = weight_o
    profit = profit + cal_sub_profit(distance_co,w_net,weight_o,price_o,price_s)
    return profit

read_input()
profit = calculate_profit()
print("result profit is %.3f"%profit)