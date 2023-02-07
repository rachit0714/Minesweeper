window_width = 1040
window_height = 620
grid_size = 18
mines_count = grid_size
if grid_size > 12:
    mines_count *= 2

def in_range(n):
        return 0 <= n <= grid_size - 1
