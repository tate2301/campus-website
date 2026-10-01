# -*- coding: utf-8 -*-
"""The Campus mark, drawn in the illustration style: one school block with its gable roof, in the campus
projection, white on the Campus tile. Three drawings by size, so it stays crisp from the app icon to the favicon:
  >= 40px  the full school: eaves, ridge light, two windows, the door on its step, the flag, a ground shadow
  24-39px  block, roof, door and flag; no windows
  < 24px   block, roof and door only, drawn a little larger so the silhouette fills the tile"""
C30, S30 = 0.8660254, 0.5
TILE = "#7c5cff"
SHADOW = "#6644ee"
WALL_F, WALL_S = "#ffffff", "#e4dbff"
ROOF_F, ROOF_B, ROOF_E = "#c3b0ff", "#ece6ff", "#d8ccff"
DOOR, GLASS, STEP = "#6a48f0", "#d6c9ff", "#efeaff"

W_, D_, H_, RISE, EAVE = 2.6, 1.5, 1.05, 0.85, 0.12


def _pts(u, ox, oy, ps):
    return " ".join(f"{ox + (x - y) * C30 * u:.2f},{oy + (x + y) * S30 * u - z * u:.2f}" for x, y, z in ps)


def campus_mark(size=40, r=None, tile=True):
    r = round(size * 0.26) if r is None else r
    full, mid = size >= 40, size >= 24
    u = size * (0.168 if mid else 0.19)
    fx, fy = -0.35, D_ + 0.1
    xs = [(x - y) * C30 for x in ((fx if mid else -EAVE), W_ + EAVE) for y in (-EAVE, D_ + EAVE)]
    ys = [(x + y) * S30 - z for x in (-EAVE, W_ + EAVE) for y in (-EAVE, D_ + EAVE) for z in (0, H_ + RISE)]
    ox = size / 2 - (min(xs) + max(xs)) / 2 * u
    oy = size / 2 - (min(ys) + max(ys)) / 2 * u + size * 0.025
    P = lambda *ps: _pts(u, ox, oy, ps)
    ym = D_ / 2
    sw = max(0.4, size / 80)
    edge = f'stroke="rgba(40,20,110,.16)" stroke-width="{sw:.2f}" stroke-linejoin="round"'
    out = ""
    if mid:                                                                                      # ground shadow, slightly darker purple
        cx_, cy_ = _pts(u, ox, oy, [(W_ / 2 + 0.25, D_ / 2 + 0.2, 0)]).split(",")
        out += f'<ellipse cx="{cx_}" cy="{float(cy_):.2f}" rx="{(W_ + D_) * 0.5 * u * 0.95:.2f}" ry="{(W_ + D_) * 0.5 * u * 0.38:.2f}" fill="{SHADOW}" opacity=".55"/>'
    out += (f'<polygon points="{P((0, D_, 0), (W_, D_, 0), (W_, D_, H_), (0, D_, H_))}" fill="{WALL_F}" {edge}/>'                       # front wall
            f'<polygon points="{P((W_, 0, 0), (W_, D_, 0), (W_, D_, H_), (W_, ym, H_ + RISE), (W_, 0, H_))}" fill="{WALL_S}" {edge}/>')    # gable end
    e = EAVE                                                                                     # the roof, with eaves on every side
    out += (f'<polygon points="{P((-e, -e, H_ - 0.06), (W_ + e, -e, H_ - 0.06), (W_ + e, ym, H_ + RISE), (-e, ym, H_ + RISE))}" fill="{ROOF_B}" {edge}/>'
            f'<polygon points="{P((-e, ym, H_ + RISE), (W_ + e, ym, H_ + RISE), (W_ + e, D_ + e, H_ - 0.06), (-e, D_ + e, H_ - 0.06))}" fill="{ROOF_F}" {edge}/>'
            f'<polygon points="{P((W_ + e, ym, H_ + RISE), (W_ + e, D_ + e, H_ - 0.06), (W_ + e, D_ + e, H_ - 0.14), (W_ + e, ym, H_ + RISE - 0.08))}" fill="{ROOF_E}"/>')
    if full:
        out += f'<polyline points="{P((-e, ym, H_ + RISE), (W_ + e, ym, H_ + RISE))}" fill="none" stroke="#ffffff" stroke-width="{max(0.8, size / 70):.2f}" stroke-linecap="round"/>'
        out += f'<polygon points="{P((0.95, D_ + 0.0, 0.0), (1.65, D_ + 0.0, 0.0), (1.65, D_ + 0.28, 0.0), (0.95, D_ + 0.28, 0.0))}" fill="{STEP}"/>'
    out += f'<polygon points="{P((1.1, D_, 0), (1.5, D_, 0), (1.5, D_, 0.7), (1.1, D_, 0.7))}" fill="{DOOR}"/>'                          # the door
    if full:
        for x0 in (0.3, 1.85):
            out += f'<polygon points="{P((x0, D_, 0.36), (x0 + 0.45, D_, 0.36), (x0 + 0.45, D_, 0.74), (x0, D_, 0.74))}" fill="{GLASS}"/>'
    if mid:                                                                                      # the school flag
        a = _pts(u, ox, oy, [(fx, fy, 0)]).split(",")
        b = _pts(u, ox, oy, [(fx, fy, 2.2)]).split(",")
        out += f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#ffffff" stroke-width="{max(1.1, size / 44):.2f}" stroke-linecap="round"/>'
        out += f'<polygon points="{P((fx, fy, 2.2), (fx + 0.66, fy, 2.08), (fx + 0.66, fy, 1.78), (fx, fy, 1.9))}" fill="#ffffff"/>'
    svg = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" style="display:block" aria-hidden="true">{out}</svg>'
    if not tile:
        return svg
    return (f'<span style="width:{size}px;height:{size}px;border-radius:{r}px;background:{TILE};display:flex;align-items:center;justify-content:center;flex:none;overflow:hidden">'
            f'{svg}</span>')


def menu_icon(size=20, open_=False, ink="#0b0c14", accent="#2563eb"):
    """the Campus menu button: two ink bars and a short blue one, the house rule of one blue part; open, the bars cross"""
    t = max(1.6, size * 0.11)
    if open_:
        a, b = size * 0.2, size * 0.8
        return (f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" aria-hidden="true">'
                f'<line x1="{a}" y1="{a}" x2="{b}" y2="{b}" stroke="{ink}" stroke-width="{t}" stroke-linecap="round"/>'
                f'<line x1="{b}" y1="{a}" x2="{a}" y2="{b}" stroke="{accent}" stroke-width="{t}" stroke-linecap="round"/></svg>')
    y = [size * 0.28, size * 0.5, size * 0.72]
    w = [(size * 0.16, size * 0.84, ink), (size * 0.16, size * 0.84, ink), (size * 0.16, size * 0.52, accent)]
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" aria-hidden="true">'
            + "".join(f'<line x1="{x0:.1f}" y1="{yy:.1f}" x2="{x1:.1f}" y2="{yy:.1f}" stroke="{c}" stroke-width="{t:.1f}" stroke-linecap="round"/>' for (x0, x1, c), yy in zip(w, y))
            + '</svg>')
