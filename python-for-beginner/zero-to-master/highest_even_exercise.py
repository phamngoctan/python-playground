def highest_even(li):
    import sys
    res = -sys.maxsize - 1
    for i in range(len(li)):
        if li[i] % 2 == 0 and li[i] > res:
            res = li[i]
    return res

def main():
    res = highest_even([10,2,3,4,8,11])
    assert res == 10, 'expect 10 but'.format(res)
    print(res)

if __name__ == '__main__':
    main()