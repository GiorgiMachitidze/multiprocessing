import concurrent.futures
import requests
import json


def req(link):
    s = requests.get(link)
    return s.json()


def thread_function(counter):
    products = []
    with concurrent.futures.ThreadPoolExecutor() as ex:
        for cnt in range(1, 21):
            res = ex.submit(req, f"https://dummyjson.com/products/{cnt + counter}")
            products.append(res.result())
    return products


if __name__ == "__main__":
    all_products = []
    with concurrent.futures.ProcessPoolExecutor() as process:
        c = 0
        for i in range(5):
            r = process.submit(thread_function, c)
            all_products.extend(r.result())
            c += 20

    with open("product_file.json", "w") as file:
        for product in all_products:
            json.dump(product, file)
            file.write('\n')
