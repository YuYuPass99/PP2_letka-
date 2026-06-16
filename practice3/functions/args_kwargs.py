
def add_numbers(*args):
    return sum(args)
print(add_numbers(1,2,3,4))  # 10

def max_number(*args):
    return max(args)
print(max_number(5,3,9,1))  # 9

def print_info(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}: {v}")
print_info(name="Ali", grade=10)

def all_together(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
all_together(1,2,3, a=10, b=20)
