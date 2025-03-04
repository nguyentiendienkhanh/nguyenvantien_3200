from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("*****************************************************")
    print("**1. Thêm sinh viên                                **")
    print("**2. Cập nhật thông tin sinh viên bởi ID           **")
    print("**3. Xóa sinh viên bởi ID                          **")
    print("**4. Tìm kiếm sinh viên theo tên                   **")
    print("**5. Sắp xếp sinh viên theo điểm trung bìnhbình    **")
    print("**6. Sắp xếp sinh viên theo tên chuyên ngành       **")
    print("**7. Hiển thị danh sách sinh viên                  **")
    print("**8. Thoát                                         **")

    key = int(input("Nhập lựa chọn của bạn: "))
    if (key == 1):
        print("\n1. Thêm sinh viên")
        qlsv.nhapSinhVien() 
        print("\nDanh sách sinh viên thành công! ")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):  # Thụt lề đúng
            print("\n2. Cập nhật thông tin sinh viên bởi ID")
            print("\nNhập ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:  # Đưa else về đúng vị trí ngang với if
            print("\nDanh sách sinh viên rỗng!")

    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xóa sinh viên bởi ID")
            print("\nNhập ID: ")
            ID = int(input())
            if (qlsv.deleteByID(ID)):
                print("\nSinh viên có ID = ", ID, " đã được xóa khỏi danh sách.")
            else:
                print("\nKhông tìm thấy sinh viên có ID = ", ID)
        else:
            print("\nDanh sách sinh viên rỗng!")

    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0) :
            print("\n4. Tìm kiếm sinh viên theo tên")
            print("\nNhập tên cần tìm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sách sinh viên rỗng!")
    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sắp xếp sinh viên theo điểm trung bình(GPA)")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.listSinhVien)
        else:
            print("\nDanh sách sinh viên rỗng!")    
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sắp xếp sinh viên theo tên")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.listSinhVien)
        else:
            print("\nDanh sách sinh viên rỗng!")
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hiển thị danh sách sinh viên")
            qlsv.showSinhVien(qlsv.listSinhVien)
        else:
            print("\nDanh sách sinh viên rỗng!")
    elif (key == 0):
        print("\n. Bạn đã thoát khỏi chương trình!")
        break
    else:
        print("\nLựa chọn không hợp lệ!")
        print("\nVui lòng chọn lại!")

        