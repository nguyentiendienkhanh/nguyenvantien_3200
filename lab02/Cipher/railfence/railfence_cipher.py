class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        if num_rails <= 1:
            return plain_text  # Không có rail hoặc chỉ có 1 rail thì không mã hóa

        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # Điều hướng đi xuống (+1) hoặc đi lên (-1)

        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction 
        
        # Gộp các hàng thành chuỗi mã hóa
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        if num_rails <= 1:
            return cipher_text  # Không có rail hoặc chỉ có 1 rail thì không giải mã

        # 1. Xác định độ dài của mỗi rail
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # 2. Chia chuỗi thành các phần tương ứng với rail
        rail = []
        start = 0
        for length in rail_lengths:
            rail.append(list(cipher_text[start:start + length]))  # Chuyển thành danh sách để pop()
            start += length

        # 3. Giải mã từ rail
        plain_text = []
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            if rail[rail_index]:  # Kiểm tra xem rail có rỗng không
                plain_text.append(rail[rail_index].pop(0))  # Lấy phần tử đầu tiên của mỗi rail
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return ''.join(plain_text)
