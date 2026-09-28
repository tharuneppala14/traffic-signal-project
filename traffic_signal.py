import time

signals = [
    ("RED", 10, "STOP"),
    ("GREEN", 10, "GO"),
    ("YELLOW", 3, "READY")
]

while True:
    for color, duration, message in signals:

        print("\n" + "=" * 35)
        print("       TRAFFIC SIGNAL")
        print("=" * 35)

        print(f"\n        {color}")
        print(f"        {message}\n")

        for remaining in range(duration, 0, -1):
            print(f"Time remaining: {remaining} seconds", end="\r")
            time.sleep(1)

        print("\n")
