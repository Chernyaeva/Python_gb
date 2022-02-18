import time


class TrafficLight:
    __color: str

    def running(self):
        colors_time = {'red': 4, 'yellow': 2, 'green': 3}
        colors_revision = []
        for key in colors_time:
            colors_revision.append(key)
            if colors_revision != ['red'] and colors_revision != ['red', 'yellow'] and colors_revision != ['red',
                                                                                                           'yellow',
                                                                                                           'green']:
                raise ('wrong order')
            self.__color = key
            print(f'{self.__color} {colors_time[key]} сек')
            while colors_time[key]:
                time.sleep(1)
                colors_time[key] -= 1


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
