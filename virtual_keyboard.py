import cv2

keyboard_layout = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
    ['Space', 'Backspace', 'Enter']
]

def get_pressed_key(x, y, key_size=60, margin=10):
    for row_idx, row in enumerate(keyboard_layout):
        for col_idx, key in enumerate(row):
            key_x = margin + col_idx * (key_size + margin)
            key_y = 150 + row_idx * (key_size + margin)
            if key_x < x < key_x + key_size and key_y < y < key_y + key_size:
                return key
    return None

def draw_keyboard(img, key_size=60, margin=10):
    for row_idx, row in enumerate(keyboard_layout):
        for col_idx, key in enumerate(row):
            x = margin + col_idx * (key_size + margin)
            y = 150 + row_idx * (key_size + margin)
            cv2.rectangle(img, (x, y), (x + key_size, y + key_size), (255, 255, 255), -1)
            cv2.rectangle(img, (x, y), (x + key_size, y + key_size), (0, 0, 0), 2)
            cv2.putText(img, key, (x + 5, y + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
