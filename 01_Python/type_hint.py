# def add_numbers(a:int, b:int, c:int) -> int:
#     return a+b+c

# x = add_numbers(1,2,3)
# print(x)



# def add_numbers(a:int, b:int, c:int) -> None:
#     return a+b+c

# add_numbers(1,2,3)



# from typing import List
# x:List[List[int]] = [[1,2],[3,4]]



# from typing import Dict
# x:Dict[str,str] = {"a":"b"}



# from typing import Set
# x:Set[float] = {"a","b"}



# from typing import Tuple
# x: Tuple[int,int,int] = (1,2,3)



from typing import Callable
def fun() -> Callable[[int,int],int]:
    def add(x:int, y:int) -> int:
        return x+y

    return add

fun()