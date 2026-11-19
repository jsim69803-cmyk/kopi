# 클래스 선언부
class graph():
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def print_graph(graph):
    print("=== 그래프 정보 출력 ===")
    for row in range(graph.size):
        for col in range(graph.size):
            print(graph.graph[row][col], end="")
        print()

# 전역 변수 선언부
G1, G3 =None, None

G1 = graph(4)
G1.graph[0][1] = 1
G1.graph[0][2] = 1
G1.graph[0][3] = 1
G1.graph[1][0] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1
G1.graph[3][0] = 1
G1.graph[3][2] = 1
print_graph(G1)


print("=== G1 무방향 그래프 ==")
for row in range(G1.size):
    for col in range(G1.size):
        print(G1.graph[row][col], end= '')
    print()

G3 = graph(4)
G3.graph[0][1] = 1
G3.graph[0][2] = 1
G3.graph[3][0] = 1
G3.graph[3][2] = 1

print("=== G3 무방향 그래프 ===")
for row in range(G3.size):
    for col in range(G3.size):
        print(G3.graph[row][col], end='')
