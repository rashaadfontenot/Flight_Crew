


def create_captain(captain_name, captain_phone, captain_confirm, captain_value):
    captain = {'Captain': {'Captain_Name': captain_name, 'Captain Phone': captain_phone, 'Captain Confirm': captain_confirm, 'Captain Value': captain_value}
               }
    '''get value of captain'''
    captain_total = captain['Captain']['Captain Value']
    return captain_total



def create_copilot(copilot_name, copilot_phone, copilot_confirm, copilot_value):
    copilot = {'Copilot_1': {'Copilot Name': copilot_name, 'Copilot Phone': copilot_phone, 'Copilot Confirm': copilot_confirm, 'Copilot Value': copilot_value},
               'Copilot_2': {'Copilot Name': copilot_name, 'Copilot Phone': copilot_phone, 'Copilot Confirm': copilot_confirm, 'Copilot Value': copilot_value}
               }
    '''Get sum of value of copilots'''
    copilot_total = 0
    for value in copilot.values():
        print(value)


def create_crew(crew_name, crew_phone, crew_confirm, crew_value):
    crew_member = {'Crew_1': {'Crew Name': crew_name, 'Crew Phone': crew_phone, 'Crew Confirm': crew_confirm, 'Crew Value': crew_value},
                   'Crew_2': {'Crew Name': crew_name, 'Crew Phone': crew_phone, 'Crew Confirm': crew_confirm, 'Crew Value': crew_value},
                   'Crew_3': {'Crew Name': crew_name, 'Crew Phone': crew_phone, 'Crew Confirm': crew_confirm, 'Crew Value': crew_value},
                   'Crew_4': {'Crew Name': crew_name, 'Crew Phone': crew_phone, 'Crew Confirm': crew_confirm, 'Crew Value': crew_value}
                   }
    '''Get sum of value of crew'''
    crew_total = 0
    for value in crew_member.values():
        crew_total += value[3]
    return crew_total


def create_pass(pass_name, pass_phone, pass_confirm, pass_value):
    passenger = {'Passenger_1': {'Passenger Name': pass_name, 'Passenger Phone': pass_phone, 'Passenger Confirm': pass_confirm, 'Passenger Value': pass_value},
                 'Passenger_2': {'Passenger Name': pass_name, 'Passenger Phone': pass_phone, 'Passenger Confirm': pass_confirm, 'Passenger Value': pass_value},
                 'Passenger_3': {'Passenger Name': pass_name, 'Passenger Phone': pass_phone, 'Passenger Confirm': pass_confirm, 'Passenger Value': pass_value},
                 'Passenger_4': {'Passenger Name': pass_name, 'Passenger Phone': pass_phone, 'Passenger Confirm': pass_confirm, 'Passenger Value': pass_value},
                 'Passenger_5': {'Passenger Name': pass_name, 'Passenger Phone': pass_phone, 'Passenger Confirm': pass_confirm, 'Passenger Value': pass_value},
                 'Passenger_6': {'Passenger Name': pass_name, 'Passenger Phone': pass_phone, 'Passenger Confirm': pass_confirm, 'Passenger Value': pass_value},
                 'Passenger_7': {'Passenger Name': pass_name, 'Passenger Phone': pass_phone, 'Passenger Confirm': pass_confirm, 'Passenger Value': pass_value},
                 'Passenger_8': {'Passenger Name': pass_name, 'Passenger Phone': pass_phone, 'Passenger Confirm': pass_confirm, 'Passenger Value': pass_value}
                 }
    '''Get sum of value of passengers'''
    pass_total = 0
    for value in passenger.values():
        pass_total += value[3]
    return pass_total


create_copilot('Rashaad', '2034443223', 22333, 100)


