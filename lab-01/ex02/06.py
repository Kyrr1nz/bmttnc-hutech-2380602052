def tao_mang(hang, cot):
    if hang < 0 or cot < 0:
        raise ValueError("Số hàng và số cột phải không âm.")
    return [[i * j for j in range(cot)] for i in range(hang)]


def main():
    hang = int(input("Nhập X (số hàng): "))
    cot = int(input("Nhập Y (số cột): "))
    print(tao_mang(hang, cot))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, EOFError) as loi:
        raise SystemExit(f"Dữ liệu không hợp lệ: {loi}")
