# สร้างกราฟที่เป็น directed graph พร้อม weight
def create_directed_graph(pairs):
    graph = {}
    edges = [pair.split() for pair in pairs.split(',')]

    for start, weight, end in edges:
        if start not in graph:
            graph[start] = []
        graph[start].append((end, int(weight)))

        # ตรวจสอบว่า end อยู่ในกราฟหรือยัง ถ้ายังให้เพิ่มเข้าไป
        if end not in graph:
            graph[end] = []

    return graph

# Dijkstra's algorithm แบบไม่ใช้ heapq
def dijkstra(graph, start, end):
    # เก็บระยะทางที่สั้นที่สุดจาก start ไปยังแต่ละ node
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    # เก็บโหนดก่อนหน้าในเส้นทาง
    previous = {node: None for node in graph}

    # ชุดของโหนดที่ถูกเข้าชมแล้ว
    visited = set()

    while len(visited) < len(graph):
        # หาโหนดที่มีค่า dist ที่น้อยที่สุดซึ่งยังไม่ถูกเข้าชม
        min_node = None
        for node in graph:
            if node not in visited and (min_node is None or dist[node] < dist[min_node]):
                min_node = node

        # ถ้าไม่พบโหนดที่ยังไม่ได้เข้าชมหรือไม่สามารถไปต่อได้
        if min_node is None:
            break

        # ทำการเยี่ยมชมโหนดนี้
        visited.add(min_node)

        # อัปเดตระยะทางสำหรับโหนดที่เชื่อมต่อ
        for neighbor, weight in graph[min_node]:
            if neighbor in visited:
                continue
            new_dist = dist[min_node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                previous[neighbor] = min_node

    # สร้างเส้นทางจาก start ไป end
    path = []
    current = end

    # ตรวจสอบว่า current อยู่ใน graph หรือไม่
    if current not in graph:
        return None

    while previous[current] is not None:
        path.insert(0, current)
        current = previous[current]

    if previous[current] is None and current != start:
        return None

    if path:
        path.insert(0, start)

    return path if path else None

# ฟังก์ชันหลักในการหาทางสั้นที่สุด
def find_shortest_paths(input_data):
    graph_data, query_data = input_data.split('/')
    graph = create_directed_graph(graph_data)

    for query in query_data.split(','):
        start, end = query.split()
        path = dijkstra(graph, start, end)

        if path:
            print(f"{start} to {end} : {'->'.join(path)}")
        else:
            print(f"Not have path : {start} to {end}")

# เรียกใช้ฟังก์ชันหลัก
if __name__ == '__main__':
    input_data = input("Enter : ")
    find_shortest_paths(input_data)
