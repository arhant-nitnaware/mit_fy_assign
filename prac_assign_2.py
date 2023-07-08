#link to dataset https://drive.google.com/file/d/1-LbO5q4TEu1no9gkgYMx0rkM3VJSXLkw/view?usp=sharing
with open('Sales.csv', 'r') as file:
    data = file.readlines()

data = [row.strip() for row in data[1:]]
#print(data)

product_id = [row.split(',')[0] for row in data]
product_details = [row.split(',')[1] for row in data]
supplier_details = [row.split(',')[2] for row in data]
customer_details = [row.split(',')[3] for row in data]
gender = [row.split(',')[4] for row in data]

def find_frequent(a_list):
    count, product_list = 0, []
    for product in set(a_list):
        if a_list.count(product) > count:
            count = a_list.count(product)
            product_list = []
            product_list.append(product)
        elif a_list.count(product) == count:
            product_list.append(product)
    return product_list

print('most popular prodcut:', find_frequent(product_details))
print('best supplier:',find_frequent(supplier_details))
print('best customer',find_frequent(customer_details))
print('most frequent gender is:',find_frequent(gender))