# Where a pixelmatch diff image is red, in 100px bands (dev helper for reading .parity/*.diff.png)
import sys
from PIL import Image
import numpy as np
d = np.asarray(Image.open(sys.argv[1]).convert('RGB')).astype(int)
red = (d[:, :, 0] > 200) & (d[:, :, 1] < 120)
rows = red.sum(axis=1)
step = int(sys.argv[2]) if len(sys.argv) > 2 else 100
tot = red.sum()
print('total', tot, f'{tot / red.size * 100:.2f}%')
for i in range(0, len(rows), step):
    s = rows[i:i + step].sum()
    if s > tot * 0.02:
        cols = red[i:i + step].sum(axis=0).nonzero()[0]
        print(f'{i:6d} {s:7d}  x {cols.min()}-{cols.max()}')
