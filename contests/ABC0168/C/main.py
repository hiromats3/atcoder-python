import math

def resolve():
    A, B, H, M = map(int, input().split())

    h_rad = math.radians(30*H + M / 2)
    h_y = A * math.cos(h_rad)
    h_x = A * math.sin(h_rad)
    m_rad = math.radians(6*M)
    m_y = B * math.cos(m_rad)
    m_x = B * math.sin(m_rad)

    ans = math.sqrt((h_y - m_y)**2 + (h_x - m_x)**2)
    print(ans)

if __name__ == "__main__":
    resolve()