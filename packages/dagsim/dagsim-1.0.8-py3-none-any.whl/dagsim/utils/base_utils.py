import numpy as np


def get_args_str(doc_string, n):
    start = doc_string.find("(")
    end = doc_string.find(",")
    while end >= 0 and n > 1:
        end = doc_string.find(",", end + 1)
        n -= 1
    if end == -1:
        end = doc_string.find(")")
    return doc_string[start + 1:end]


def get_args_list(args_str):
    pass


def check_for_numeric_type(string: str):
    num = float(string)
    if num == int(num):
        num = int(num)
    return num


def is_numeric(string: str):
    try:
        float(string)
        return True
    except ValueError:
        return False


def get_args_st(doc, n):
    start = doc.find("(")
    end = doc.find(")")
    doc = doc[doc.find("("): doc.find(")")]
    feq = doc.find("=")
    print(doc[:feq])


if __name__ == "__main__":
    # doc = "fds(dasd,dasd dasd) dasd sdaftqwe "
    # doc = np.add.__doc__
    # args = get_args_st(doc, 2)
    # print(args)
    is_numeric("2")
    is_numeric("2a")
    is_numeric("-2")
    is_numeric("-2.2")
    is_numeric("23.")
