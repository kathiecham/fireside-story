def get_country_codes(prices):
    prices_list = prices.split(', ')
    #print(prices_list)
    x = 0
    country_codes = []
    for codes in prices_list:      
        code = prices_list[x][:2]
        country_codes.append(code)
        x += 1
    code_str = ", ".join(country_codes)
    return code_str
    #print(code_str)


def main():
    get_country_codes(prices)


if __name__ == "__main__":
    main()