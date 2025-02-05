import simplemathlib
from mylib import stroperations
from mylib.sublib import substroperations


if __name__ == "__main__":
    a = 2
    b = 3
    outputoftwonumbers = simplemathlib.add(a, b)
    print(f"Adding {a} and {b} gives {outputoftwonumbers}")
    pivalue = simplemathlib.PI
    print(f"Value of PI is {pivalue}")

    strname = "John Doe"
    lastname = "Doe"
    test = substroperations.stringtoupper(strname)
    outputofstring = stroperations.concatenate(strname, lastname)
    print(f"Concatenating {strname} and {lastname} gives {outputofstring}")
    print("strname in uppercase is", substroperations.stringtoupper(strname))