def main():
    x = int(input("Block size? "))
    draw_block(x)

def draw_block(n):
    for _ in range(n):
        print("#" * n)

main()
