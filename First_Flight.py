captain_name = 'Rashaad'
captain_phone = '206-351-4856'
captain_confirm = 'C)NF!Rm'
captain_value = 100

copilot_1_name = 'Sahara'
copilot_1_phone = '206-214-7979'
copilot_1_confirm = 'C)NF!Rm#)^$E'
copilot_1_value = 100
copilot_2_name = 'Shea'
copilot_2_phone = '206-701-1400'
copilot_2_confirm = 'C)NF!RmDJNN**SS'
copilot_2_value = 100

crew_1_name = 'James'
crew_1_phone = '206-544-765'
crew_1_confirm = 'C)NF!Rm#dDWW)^$E'
crew_1_value = 100
crew_2_name = 'Jess'
crew_2_phone = '206-851-1400'
crew_2_confirm = 'C)NF!RmDJNN**SS'
crew_2_value = 100
crew_3_name = 'Steven'
crew_3_phone = '206-214-6579'
crew_3_confirm = 'C)NF!GEERm#)^$E'
crew_3_value = 100
crew_4_name = 'Michael'
crew_4_phone = '206-751-1550'
crew_4_confirm = 'C)NFGE!RmDJNN**SS'
crew_4_value = 100

pass_1_name = 'JZ'
pass_1_phone = '946-544-765'
pass_1_confirm = 'C)NFGEE#dDWW)^$E'
pass_1_value = 100
pass_2_name = 'JSwag'
pass_2_phone = '206-935-1400'
pass_2_confirm = 'C)NF!RmDJN'
pass_2_value = 100
pass_3_name = 'Ted'
pass_3_phone = '745-214-6579'
pass_3_confirm = 'C)gggEERm#)^$E'
pass_3_value = 100
pass_4_name = 'Jordan'
pass_4_phone = '206-751-9830'
pass_4_confirm = 'C)NDJNN**SS'
pass_4_value = 100
pass_5_name = 'JD'
pass_5_phone = '506-544-765'
pass_5_confirm = 'C)NdddDWW)^$E'
pass_5_value = 100
pass_6_name = 'Mike T'
pass_6_phone = '206-851-4832'
pass_6_confirm = 'C)NF!dddf((SS'
pass_6_value = 100
pass_7_name = 'Hank'
pass_7_phone = '206-921-6579'
pass_7_confirm = 'C)NFm#)^$E'
pass_7_value = 100
pass_8_name = 'Harold'
pass_8_phone = '206-751-0293'
pass_8_confirm = 'C)NFGE!RmD8222S'
pass_8_value = 100


def create_captain(captain_name, captain_phone, captain_confirm, captain_value):
    captain = {'Captain': [captain_name, captain_phone, captain_confirm, captain_value]
               }
    '''get value of captain'''
    captain_total = (captain['Captain'][3])
    print(captain_total)
    return captain_name


def create_copilot(copilot_name, copilot_phone, copilot_confirm, copilot_value):
    copilot = {'Copilot_1': [copilot_name, copilot_phone, copilot_confirm, copilot_value],
               'Copilot_2': [copilot_name, copilot_phone, copilot_confirm, copilot_value]
               }
    '''Get sum of value of copilots'''
    copilot_total = 0
    for value in copilot.values():
        copilot_total += value[3]


def create_crew(crew_name, crew_phone, crew_confirm, crew_value):
    crew_member = {'Crew_1': [crew_name, crew_phone, crew_confirm, crew_value],
                   'Crew_2': [crew_name, crew_phone, crew_confirm, crew_value],
                   'Crew_3': [crew_name, crew_phone, crew_confirm, crew_value],
                   'Crew_4': [crew_name, crew_phone, crew_confirm, crew_value]
                   }
    '''Get sum of value of crew'''
    crew_total = 0
    for value in crew_member.values():
        crew_total += value[3]


def create_pass(pass_name, pass_phone, pass_confirm, pass_value):
    passenger = {'Passenger_1': [pass_name, pass_phone, pass_confirm, pass_value],
                 'Passenger_2': [pass_name, pass_phone, pass_confirm, pass_value],
                 'Passenger_3': [pass_name, pass_phone, pass_confirm, pass_value],
                 'Passenger_4': [pass_name, pass_phone, pass_confirm, pass_value],
                 'Passenger_5': [pass_name, pass_phone, pass_confirm, pass_value],
                 'Passenger_6': [pass_name, pass_phone, pass_confirm, pass_value],
                 'Passenger_7': [pass_name, pass_phone, pass_confirm, pass_value],
                 'Passenger_8': [pass_name, pass_phone, pass_confirm, pass_value]
                 }
    '''Get sum of value of passengers'''
    pass_total = 0
    for value in passenger.values():
        pass_total += value[3]
    '''Sum all total to get total value of plane.'''
def sum_plane_total():
    plane_total = str(captain_total + copilot_total + crew_total)

    print('The total value of the plane is ${}'.format(plane_total))
    print('The name of the captain is {}'.format(captain_name))
    print('The 2 copilots of the plane are {} and {}'.format(copilot_1_name, copilot_2_name))


name_of_captain = create_captain(captain_name, captain_phone, captain_confirm, captain_value)
print('The name of the captain is {}'.format(name_of_captain))


