
def test_gosh(command):
    #command.run('param list 0')
    #print("Hello World!")
    #print(command.run_check('param list 0'))
    #print(command.check_ram_image('param list 0'))
    #command.run('param get ram_image')
    
    print("State = " + str(command.get_status()))
    
    if command.get_param_state('ram_image', 1):
        print("Succes!")
        
    else:
        print("Failure..")
    
    
    #print(string_read)
    
    
