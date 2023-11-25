import argparse
# 执行方式  python3 6-1arg-1.py -number 100
parser = argparse.ArgumentParser(description="这个程序用来演示参数处理")
# 没有 - 表示必选 并且在执行的时候，不需要使用 -number1 100 而是直接 py 100 200
parser.add_argument( "number1",type=int, help="输入一个数字") # args.py: error: the following arguments are required: number1
parser.add_argument( "number2",type=int, help="输入一个数字") # args.py: error: the following arguments are required: number1

# -number 表示 number 参数是可选参数
parser.add_argument( "-number3", type=int,  default=20, help="输入一个数字")
args = parser.parse_args()
print(f"你输入的两数之和是 {args.number1+args.number2+args.number3} ")
