def main():
    name = input()
    fixed_salary = float(input())
    sales = float(input())

    commission = sales * 0.15
    total = fixed_salary + commission
    
    print("TOTAL = R$ {:.2f}".format(total))

if __name__ == '__main__':
    main()
