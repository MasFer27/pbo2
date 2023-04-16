def my_generator():
    for i in range(3):
        yield i

def main():
    g = my_generator()
    while True:
        try:
            value = next(g)
            print(value)
        except StopIteration:
            print("Generator is exhausted")
            break

main()
