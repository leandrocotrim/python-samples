try:
    #r = 0/0
    raise Exception('cotrim')
except ZeroDivisionError as ee:
    print(ee)
except Exception as e:
    print(e)