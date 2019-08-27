import datetime

def time_this(org_function):
    def new_function(*args, **kwargs):
        before = datetime.datetime.now()
        x = org_function(*args, **kwargs)
        after = datetime.datetime.now()
        print("Elapsed Time = {0}".format(after-before))
        return x
    return new_function
