import time


#def validate_schedule(hour_validator):
#    signal = False
#    while True:
#        t = time.asctime()
#        hour_listener = t.split(' ')[4][0:5]
#        if hour_listener == "2023":
#            hour_listener = t.split(' ')[3][0:5]
#        time.sleep(30)
#        if hour_listener not in hour_validator:
#            print(f"awaiting for signal\nSignal is {signal}\n@ {hour_listener}")

#        else:
#            signal = True
#            print(f"awaiting for signal\nSignal is {signal}\n@ {hour_listener}")
#            return signal
            
            
            
def validate_schedule(hour_validator):
    """
        function that take two string as attribute , start and end check time with time module 
        return True when time hit the start attribute or back to default False if end attribute is hit.
    """
    start_signal = False
#    print('awaiting starts schedule')
    while start_signal == False:
        t = time.asctime()
        hour_listener = t.split(' ')[4][0:5]
        if hour_listener == "2023":
            hour_listener = t.split(' ')[3][0:5]
        time.sleep(30)
#        print(f'waiting for schedule time at: {hour_listener}')
        if hour_listener in hour_validator:
            print(hour_listener)
            start_signal = True
    return start_signal
