from debugger import debug
import sys

from constant import ALLOT_WATER,ADD_GUESTS,BILL

# Cost and Consumption calculations functions
from fn_allot_water import calculate_for_allot_water

def main():
    input_file = sys.argv[1]
    opened_file_ptr = open(input_file,'r')

    net_water_consumed = 0
    cost_of_water_consumed = 0

    while True:
        command = opened_file_ptr.readline()
        if not command:
            break
        parsed_commands_with_args = command.split(" ")
        command_alias = parsed_commands_with_args[0]
        
        if( command_alias == ALLOT_WATER ):
            apartment_type = int(parsed_commands_with_args[1])
            ratio_extraction_string = parsed_commands_with_args[2].split(":")
            corporation_to_bore_ration = int(ratio_extraction_string[0])/int(ratio_extraction_string[1])
            debug(corporation_to_bore_ration)
            water_ALLOT_WATER,cost_ALLOT_WATER = calculate_for_allot_water(apartment_type,corporation_to_bore_ration)
            net_water_consumed += water_ALLOT_WATER
            cost_of_water_consumed += cost_ALLOT_WATER
        elif( command_alias == ALLOT_WATER ):
            pass
        elif( command_alias == BILL):
            pass
            

if __name__ == "__main__":
    main()