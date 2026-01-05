def operation(*args, **kwargs):
    if kwargs.get("key") == "max":
        print("MAX : " ,max(args))

    elif kwargs.get("key") == "min":
        print("MIN : ",min(args))

operation(12, 34, 45, 23, key= "max")
operation(12, 34, 45, 23, key= "min")