parking_list = []
id_index = 1
while True:
    choice = input("""|===== QUẢN LÝ BAI XE - SMART PARKING ===== |
==========================================
1. Check-in (Đăng ký xe vào)
2. Báo cáo tôn kho (Hiển thị danh sách)
3. Tìm kiêm xe (Theo bien sô)
4. Check-out (Xử lý xe ra & Tính phí)
5. Thoat chưong trinh
==========================================
Mời bạn chọn chức năng (1-5): """)
    match choice:
        case "1":
            while True:
                license_plate = input("Nhập biển số xe cần đăng ký:").strip()
                if license_plate == "":
                    print("Hãy nhập biển số xe muốn đăng ký")
                    continue
                found = False
                for car in parking_list:
                    if car['license_plate'] == license_plate:
                        found = True
                        break
                if found:
                    print("Xe đã được đăng ký vui lòng không đăng ký lại")
                    continue
                while True:
                    type_car = input("Nhập loại xe (1-Xe máy | 2-Ô tô): ").strip()
                    if not type_car.isdigit():
                        print("Loại xe phải là số")
                        continue
                    if type_car not in ["1", "2"]:
                        print("Loại xe chỉ được nhập 1 hoặc 2")
                        continue
                    if type_car == "1":
                        type_car = "Xe máy"
                    else:
                        type_car = "Ô tô"
                    break
                while True:
                    start_hour = input("Nhập giờ vào: ").strip()
                    if not start_hour.isdigit():
                        print("Giờ chỉ được là số")
                        continue
                    start_hour = int(start_hour)
                    if start_hour < 0 or start_hour > 24:
                        print("Giờ bắt đầu gửi phải trong khoảng 0-24h")
                        continue
                    break
                new_dict_car = {"id": id_index, 
                               "license_plate": license_plate,  
                               "type_car":type_car,
                               "start_hour": start_hour
                            }
                parking_list.append(new_dict_car)
                print("Đã thêm thành công")
                id_index += 1
                break
        case "2":
            if parking_list == []:
                print("Bãi đỗ xe hiện đang trống")
                continue
            print(f"ID | {'Biển số xe':<20} |{'Loại xe':<10} | {'Giờ vào'}")
            print("-"*55)
            for car in parking_list:
                print(f"{car['id']:<2} | {car['license_plate']:<20} |{car['type_car']:<10} | {car['start_hour']}")
        case "3":
            while True:
                license_plate_search = input("Nhập biển số xe cần tìm: ").strip()
                if license_plate_search == "":
                    print("Biển số không được để trống!")
                    continue
                found = False
                for car in parking_list:
                    if car['license_plate'] == license_plate_search:
                        found = True
                        print("Thông tin chi tiết:", car)
                        break
                if not found:
                    print(f"Không tìm thấy biển số {license_plate_search} trong hệ thống!")
                break
        case "4":
            while True:
                license_plate_out = input("Nhập biển số xe cần ra: ").strip()
                if license_plate_out == "":
                    print("Biển số không được để trống!")
                    continue
                found = False
                for i, car in enumerate(parking_list):
                    if car['license_plate'] == license_plate_out:
                        found = True
                        break
                if not found:
                    print(f"Không tìm thấy biển số {license_plate_out} trong hệ thống!")
                    break
                while True:
                    end_hour = input("Nhập giờ ra: ").strip()
                    if not end_hour.isdigit():
                        print("Giờ ra phải là số nguyên!")
                        continue
                    end_hour = int(end_hour)
                    if end_hour < car['start_hour']:
                        print("[Lỗi]: Giờ ra phải sau hoặc bằng giờ vào!")
                        continue
                    break
                total_hour = end_hour - car['start_hour']
                if car['type_car'] == "1":
                    fee = total_hour * 5000
                else:
                    fee = total_hour * 10000
                print(f"Tổng phí phải trả: {fee} VNĐ")
                deleted_car = parking_list.pop(i)
                print(f"[Thành công]: Đã xóa xe ID {deleted_car['id']} thành công!")
                break
        case "5":
            print("Đã thoát chương trình")
            break
        case _:
            print("Không có lựa chọn này!")
                
        


