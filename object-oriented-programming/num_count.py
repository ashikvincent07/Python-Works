class NumberCount:

    def solution(*args, **kwargs):
        value = int(kwargs.get("value"))

        if value not in args:
            print(f"{value} not in the list")
        else:
            print(f"count of {value} = {args.count(value)}")

numb_count_instance = NumberCount()

numb_count_instance.solution(12, 10, 10, 10, 12, 11, 8, value= 11)
