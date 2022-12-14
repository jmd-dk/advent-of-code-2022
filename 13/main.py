import bisect, math, re

# Read in data
class Int(int):
    for method in ['lt', 'gt', 'eq']:
        method = f'__{method}__'
        locals()[method] = lambda self, other, *, method=method: (
            getattr([self], method)(other)
            if isinstance(other, list)
            else getattr(super(), method)(other)
        )
read_packet = lambda f: eval(
    re.sub(r'\d+', lambda m: 'Int({})'.format(m.group()), f.readline())
)
packets = []
with open('input.txt') as f:
    while True:
        for _ in range(2):
            packets.append(read_packet(f))
        if not f.readline():
            break

# Part one
print(
    'part one:',
    sum(
        i
        for i, pair in enumerate(zip(packets[0::2], packets[1::2]), 1)
        if list(pair) == sorted(pair)
    )
)

# Part two
divider_packets = [[[Int(2)]], [[Int(6)]]]
for packet in divider_packets:
    packets.append(packet)
packets.sort()
print(
    'part two:',
    math.prod(
        1 + bisect.bisect_left(packets, packet)
        for packet in divider_packets
    )
)

