def dijkstra(graph, start, target):
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
        for neighbor, weight in graph[min_node].items():
            if neighbor in visited:
                continue
            new_dist = dist[min_node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                previous[neighbor] = min_node

    # สร้างเส้นทางจาก start ไป target
    path = []
    current = target
    while previous[current] is not None:
        path.insert(0, current)
        current = previous[current]

    if previous[current] is None and current != start:
        return float('inf'), []

    path.insert(0, start)  # เพิ่มโหนดเริ่มต้นที่เป็น path

    return dist[target], path  # คืนค่าระยะทางและเส้นทาง


# ฟังก์ชันหลัก
if __name__ == '__main__':
    graph = {
        'A': {'B': 1, 'C': 2},
        'B': {'D': 12, 'A': 1},
        'C': {'D': 9, 'F': 3, 'A': 2},
        'D': {'C': 9, 'E': 7, 'G': 1},
        'E': {'G': 5, 'D': 7},
        'F': {'G': 4},
        'G': {'D': 1, 'E': 5, 'F': 4}
    }

    # รับค่า input
    print(" *** Dijkstra's shortest path ***")
    start_vertex, target_vertex = input("Enter start and target vertex : ").split()
    shortest_distance, path = dijkstra(graph, start_vertex, target_vertex)

    # แสดงผลลัพธ์
    if shortest_distance == float('inf'):
        print(f"No path from {start_vertex} to {target_vertex}")
    else:
        print(f"Shortest distance is {shortest_distance}")
        print(f"And the path is {path}")
