parking = []

while True:

    choice = input("""
=================================================
        QUẢN LÝ BÃI XE - SMART PARKING
=================================================
1. Check-in (Thêm xe vào bãi)
2. Báo cáo tồn kho
3. Tìm kiếm xe theo ID
4. Check-out (Xóa xe khỏi bãi)
5. Thoát chương trình
=================================================
Mời bạn nhập lựa chọn (1-5):
""").strip()

    match choice:

        case '1':

            plate = input("Nhập biển số xe: ").strip()

            if plate == "":
                print("[Lỗi] Biển số không được để trống!")
                continue

            check_plate = False

            for xe in parking:
                if xe["plate"] == plate:
                    check_plate = True
                    break

            if check_plate:
                print("[Lỗi] Biển số đã tồn tại trong bãi!")
                continue

            while True:

                vehicle_type = input("""
Loại xe:
1. Xe máy
2. Ô tô
Nhập lựa chọn: """).strip()

                if vehicle_type == "1":
                    vehicle_type = "Xe máy"
                    break

                elif vehicle_type == "2":
                    vehicle_type = "Ô tô"
                    break

                else:
                    print("[Lỗi] Chỉ được nhập 1 hoặc 2!")

            entry_time = input("Nhập giờ vào: ").strip()

            if entry_time == "":
                print("[Lỗi] Giờ vào không được để trống!")
                continue

            new_vehicle = {
                "id": len(parking) + 1,
                "plate": plate,
                "type": vehicle_type,
                "entry_time": entry_time
            }

            parking.append(new_vehicle)

            print("Check-in thành công!")


        case '2':

            if len(parking) == 0:
                print("\n[Thông báo] Bãi xe hiện đang trống!")
            else:

                print("\n================ DANH SÁCH XE ================\n")

                print(
                    f"{'ID':<5} | {'Biển số':<15} | {'Loại xe':<10} | {'Giờ vào':<10}"
                )

                print("-" * 55)

                for xe in parking:
                    print(
                        f"{xe['id']:<5} | "
                        f"{xe['plate']:<15} | "
                        f"{xe['type']:<10} | "
                        f"{xe['entry_time']:<10}"
                    )

 
        case '3':

            id_input = input("Nhập ID cần tìm: ").strip()

            found = False

            for xe in parking:

                if str(xe["id"]) == id_input:
                    print("\nThông tin chi tiết:")

                    print(xe)

                    found = True
                    break

            if not found:
                print("[Lỗi] Không tìm thấy xe trong hệ thống!")

        case '4':

            id_input = input("Nhập ID xe cần ra: ").strip()

            found = False

            for xe in parking:

                if str(xe["id"]) == id_input:

                    found = True

                    exit_time = input("Nhập giờ ra: ").strip()

                    if exit_time == "":
                        print("[Lỗi] Giờ ra không được để trống!")
                        break

                    fee = 0

                    if xe["type"] == "Xe máy":
                        fee = 5000
                    else:
                        fee = 10000

                    print("\n===== PHIẾU THANH TOÁN =====")
                    print("Biển số :", xe["plate"])
                    print("Loại xe :", xe["type"])
                    print("Phí gửi :", fee, "VNĐ")

                    parking.remove(xe)

                    print("\nCheck-out thành công!")
                    break

            if not found:
                print("[Lỗi] Không tìm thấy xe trong hệ thống!")

        case '5':

            print("Đã thoát chương trình!")
            break


        case _:

            print("[Lỗi] Vui lòng chọn từ 1 đến 5!")