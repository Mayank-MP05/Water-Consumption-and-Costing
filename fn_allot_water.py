from constant import daily_use_per_person,no_of_peoples_2BHK,no_of_peoples_3BHK,no_of_days_in_month,corporation_rate_per_ltr,borewell_rate_per_ltr

def calculate_for_allot_water(apartment_type,corporation_to_bore_ration):
    """[summary] - Return the Net Water consumed and Associated Cost with it 

    Args:
        apartment_type `int`: [2 | 3] - Represents the 2BHK or 3BHK apartment
        corporation_to_bore_ration `float`: - Ration of Corporation to Borewell water

    Returns:
        [Net water in litres `int`,net cost in rs `float` ]
    """
    
    net_water_litres = 0
    net_cost_in_rs = 0
    
    if(apartment_type == 2):
        net_water_litres = daily_use_per_person * no_of_peoples_2BHK * no_of_days_in_month 
    
    elif(apartment_type == 3):
        net_water_litres = daily_use_per_person * no_of_peoples_3BHK * no_of_days_in_month
    
    # Cost Calculation
    cost_factor_bore = corporation_to_bore_ration / (1 + corporation_to_bore_ration)
    take_from_coporation = net_water_litres * cost_factor_bore
    take_from_borewell = net_water_litres * (1 - cost_factor_bore)
    
    net_cost_in_rs = (take_from_coporation * corporation_rate_per_ltr) + (take_from_borewell * borewell_rate_per_ltr)
    return net_water_litres,net_cost_in_rs