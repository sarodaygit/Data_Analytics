import mymodule
from stringmodule import stringoperations

if __name__ == '__main__':

    sumoftwo = mymodule.add(2,3)
    print(sumoftwo)

    constr = stringoperations.strconcat("Hello", "World")
    print(constr)

    