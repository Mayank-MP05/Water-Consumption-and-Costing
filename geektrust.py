from debugger import debug
import sys

from constant import ALLOT_WATER,ADD_GUESTS,BILL

# Cost and Consumption calculations functions
from fn_allot_water import calculate_for_allot_water
from fn_add_guest import calculate_for_add_guests

def main():
    input_file = sys.argv[1]
    opened_file_ptr = open(input_file,'r')

    net_water_consumed = 0
    cost_of_water_consumed = 0
    
    no_of_guests = 0

    while True:
        command = opened_file_ptr.readline()
        # FIXME: Removing newline from raw readline
        command = command.replace("\n", "")
        if not command:
            break
        parsed_commands_with_args = command.split(" ")
        debug("parsed_commands_with_args: ",parsed_commands_with_args)
        command_alias = parsed_commands_with_args[0]
        
        if( command_alias == ALLOT_WATER ):
            apartment_type = int(parsed_commands_with_args[1])
            ratio_extraction_string = parsed_commands_with_args[2].split(":")
            corporation_to_bore_ration = int(ratio_extraction_string[0])/int(ratio_extraction_string[1])
            debug("corporation_to_bore_ration",corporation_to_bore_ration)
            water_ALLOT_WATER,cost_ALLOT_WATER = calculate_for_allot_water(apartment_type,corporation_to_bore_ration)
            net_water_consumed += water_ALLOT_WATER
            cost_of_water_consumed += cost_ALLOT_WATER
            debug("water_ALLOT_WATER",water_ALLOT_WATER)
            debug("cost_ALLOT_WATER",cost_ALLOT_WATER)
        elif( command_alias == ADD_GUESTS ):
            # Just Keep on counting net No Of Guest don't calculate values each time
            no_of_guests += int(parsed_commands_with_args[1])
        elif( command_alias == BILL):
            # Calculate and Print Net Cost and Consumption
            water_ADD_GUEST,cost_ADD_GUEST = calculate_for_add_guests(no_of_guests)
            debug("water_ADD_GUEST",water_ADD_GUEST)
            debug("cost_ADD_GUEST",cost_ADD_GUEST)
            net_water_consumed += water_ADD_GUEST
            cost_of_water_consumed += cost_ADD_GUEST
            print(round(net_water_consumed),round(cost_of_water_consumed))
            break

if __name__ == "__main__":
    main()