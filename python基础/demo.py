class Screen(object):



    def resolution(self):
        return self.width * self.height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution())
