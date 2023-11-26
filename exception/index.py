class NameError(Exception):
    def __init__(self, message):
        self.message = message
    
    @property
    def msg(self):
        return f"名字不允许使用 {self.message}"

name = "jerry"
try:
    if name == "jerry":
        raise NameError(name)

except NameError as ne:
    print(ne.msg)

