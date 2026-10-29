# Stack 초기화 함수
def init_stack(size):
    global stack, top
    stack = [None] * size
    top = -1
    return print("스택 초기화 완료! 스택 크기: " + str(size))

# Push 함수
def push(data):
    global top
    if is_stack_full():
        return print("스택이 꽉 찼습니다.")
    else:
        top += 1
        stack[top] = data
        return print("현재 top:" + str(top))

# pop 함수
def pop():
    global top
    if is_stack_empty():
        return print("스택이 비어있습니다.")
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return print("Pop된 데이터:" + str(data) + ", 현재 top:" + str(top))

#Peek 함수
def peek():
    global top
    if is_stack_empty():
        return print("스택이 비어있습니다. 삭제할 데이터가 없습니다.")
    else:
        data = stack[top]
        return print("Peek된 데이터:" + str(data) + ", 현재 top:" + str(top))

# Stack Full Check
def is_stack_full():
    global top
    if top == len(stack) - 1:
        return True
    else:
        return False

#stack Empty Check
def is_stack_empty():
    global top
    if top == -1:
        return True
    else:
        return False

# 스택 상태 출력(프린트 함수)
def print_stack():
    print("=== 스택 상태 ===")
    # range(start,end,step) : start부터 end까지 step만큼 증가/감소
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i])
    print("===============")
    
# Stack 초기화
init_stack(7)

# push
push("커피")
push("녹차")
push("꿀물")
push("레몬차")
push("오렌지주스")
push("밀크티")
push("아이스티")

push("콜라")

print_stack()

peek() #아이스티

# pop
pop()
pop()
pop()
pop()
pop()
pop()
pop()

pop()

peek() #스택이 비어있습니다.

print_stack()
