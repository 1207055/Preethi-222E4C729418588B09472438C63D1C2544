def linearSearchProduct(productList, targetProduct):
    indices = []

    for index, product in enumerate(productList):
        if product == targetProduct:
            indices.append(index)
    
    return indices

products = ["tree", "branches", "fruits", "tree", "root", "tree"]
target = "tree"
result = linearSearchProduct(products, target)
print(result)
