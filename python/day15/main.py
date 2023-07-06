import sys
import time

from python.day15.Point import Point
from python.day15.Sensor import Sensor


def get_row_2m_absence_analysis(sensors: [Sensor]) -> int:
    return 0

def part_one(data):
    sensors = []
    for line in data:
        parts = line.split(":")
        position_data = parts[0][10:]
        position = extract_point(position_data)
        reading_data = parts[1][22:]
        reading = extract_point(reading_data)
        sensor = Sensor(position, reading)
        sensors.append(sensor)
        print(sensor)

    answer = get_row_2m_absence_analysis(sensors)

    print('In row 2000000 there cannot be a beacon in {} rows'.format(answer))

def extract_point(data: str) -> Point:
    xy = data.split(",")
    x = xy[0].split("=")[1]
    y = xy[1].split("=")[1]
    return Point(int(x), int(y))

def main() -> int:
    with open('../../input/day15') as file:
        data = file.readlines()

    start_time = time.time_ns()
    part_one(data)
    print("--- Part one took %d ms ---" % ((time.time_ns() - start_time) / 1000000))

    start_time = time.time_ns()
    # part_two(data)
    print("--- Part two took %d ms ---" % ((time.time_ns() - start_time) / 1000000))

    return 0


if __name__ == '__main__':
    sys.exit(main())
