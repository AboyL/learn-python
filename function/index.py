from functools import wraps

def time_call(times=5):
  def call(func):
    @wraps(func)
    def call2():
      for i in range(times):
        func()
        print(f"执行{i+1} 次")
    return call2
  return call
@time_call(7)
def func():
  print('func')
func()
