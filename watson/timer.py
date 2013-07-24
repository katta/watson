import time


class Timer():

    def start(self):
        self.begin = time.time()
        self.lapstart = self.begin

    def lap(self):
        self.lapend = time.time()
        laptime = self.lapend - self.lapstart
        self.lapstart = time.time()
        return laptime

    def end(self) :
    	return time.time() - self.begin