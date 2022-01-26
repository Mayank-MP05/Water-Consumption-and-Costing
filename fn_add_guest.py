from debugger import debug
from constant import monthly_use_per_person

"""
Tanker Water - Slab rate:

- 0 to 500L - Rs. 2 per litre
- 501L to 1500L - Rs. 3 per litre
- 1501 to 3000L - Rs. 5 per litre
- 3001L+ - Rs. 8 per litre

Tanker water has a slab rate similar to income tax slabs, which means you pay different amounts for each slab. For e.g if you have consumed 2000L of tanker water then your cost is 500*2 + 1000*3 + 500*5 = Rs. 6500
"""

def calculate_for_add_guests(no_of_guests):
    """Gives the Cost and Consumption of the Water for Guest 

    Args:
        no_of_guests `int`: take the No of Guests as input parameter

    Returns:
        `net_monthly_use,net_monthly_cost` 
    """
    net_monthly_use = no_of_guests * monthly_use_per_person
    net_monthly_cost = 0

    step_wise_capacity = [0,500,1500,3000]
    step_wise_unit_costs = [2,3,5,8]
    
    min_complete_idx = -1
    new_step_wise_capacity = []
    add_in_list_flag = False
    
    for itr in step_wise_capacity:
        if(itr < net_monthly_use):
            new_step_wise_capacity.append(itr)
        else: 
            new_step_wise_capacity.append(net_monthly_use) 
            add_in_list_flag = True
            break
            
    if not add_in_list_flag:
        new_step_wise_capacity.append(net_monthly_use) 
    
    debug("new_step_wise_capacity",new_step_wise_capacity)
        
    # FIXME: Zero Guests are there Edge Case
    if len(new_step_wise_capacity) == 1:
        return 0,0
    
    for itr in range(len(new_step_wise_capacity)):
        if itr != 0:
            slab_length = new_step_wise_capacity[itr] - new_step_wise_capacity[itr-1]
            slab_cost = slab_length * step_wise_unit_costs[itr-1]
            net_monthly_cost += slab_cost
            
    return net_monthly_use,net_monthly_cost
        