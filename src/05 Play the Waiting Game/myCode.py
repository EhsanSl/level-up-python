import time
import random


def waiting_game(target_time):
    print(f"The target wait time is {target_time}")

    n = input(f'---press Enter to begin---')
    start = time.perf_counter()

    m = input()
    end = time.perf_counter()

    wait_time = end - start
    if wait_time > target_time:
        print(f'too slow by {wait_time - target_time :.3f}')
    elif wait_time < target_time:
        print(f'too fast by {target_time - wait_time :.3f}')
    else:
        print(f'Woa! you were not supposed to beat this game!')

    return None


if __name__ == '__main__':



    target_time = random.randint(1, 5)
    waiting_game(target_time)
