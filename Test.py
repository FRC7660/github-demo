from __future__ import annotations
from dataclasses import dataclass
import math
from typing import Tuple
import os
import json
from pathlib import Path
from typing import Iterable

def _hitbox_to_dict(h):
    if isinstance(h, RectHitbox):
        return {"type": "rect", "x": h.x, "y": h.y, "w": h.w, "h": h.h}
    if isinstance(h, CircleHitbox):
        return {"type": "circle", "x": h.x, "y": h.y, "r": h.r}
    raise TypeError("Unsupported hitbox type")

def launch_canvas_viewer(hitboxes: Iterable[Hitbox], filename: str | Path | None = None) -> Path:
    """
    Write a small HTML + JS viewer that draws the provided hitboxes and opens it in the host browser.
    Usage:
        launch_canvas_viewer([player, projectile, enemy])
    """
    hb_list = [_hitbox_to_dict(h) for h in hitboxes]
    html = f"""
<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<title>Hitbox Viewer</title>
<style>html,body{{height:100%;margin:0}}canvas{{display:block;background:#111}}</style>
</head>
<body>
<canvas id="c"></canvas>
<script>
const hitboxes = {json.dumps(hb_list)};
const canvas = document.getElementById('c');
const ctx = canvas.getContext('2d');
function resize() {{
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  draw();
}}
window.addEventListener('resize', resize, false);
function boundsOf(h) {{
  if (h.type === 'rect') {{
    return [h.x - h.w/2, h.y - h.h/2, h.x + h.w/2, h.y + h.h/2];
  }} else {{
    return [h.x - h.r, h.y - h.r, h.x + h.r, h.y + h.r];
  }}
}}
function computeView() {{
  let minx=Infinity,miny=Infinity,maxx=-Infinity,maxy=-Infinity;
  for (const h of hitboxes) {{
    const b = boundsOf(h);
    minx = Math.min(minx, b[0]); miny = Math.min(miny, b[1]);
    maxx = Math.max(maxx, b[2]); maxy = Math.max(maxy, b[3]);
  }}
  if (!isFinite(minx)) {{ minx=miny=0; maxx=100; maxy=100; }}
  return {{minx, miny, maxx, maxy}};
}}
function toCanvasX(x, view) {{
  const pad = 20;
  const sx = (canvas.width - pad*2) / (view.maxx - view.minx || 1);
  return pad + (x - view.minx) * sx;
}}
function toCanvasY(y, view) {{
  const pad = 20;
  const sy = (canvas.height - pad*2) / (view.maxy - view.miny || 1);
  // flip Y so that increasing y goes down (keeps original coords)
  return pad + (y - view.miny) * sy;
}}

// collision helpers (same logic as Python)
function rect_vs_rect(a,b){{
  const [al,at,ar,ab] = [a.x-a.w/2,a.y-a.h/2,a.x+a.w/2,a.y+a.h/2];
  const [bl,bt,br,bb] = [b.x-b.w/2,b.y-b.h/2,b.x+b.w/2,b.y+b.h/2];
  if (ar < bl || br < al) return false;
  if (ab < bt || bb < at) return false;
  return true;
}}
function circle_vs_circle(a,b){{
  const dx = a.x - b.x, dy = a.y - b.y;
  const rs = a.r + b.r;
  return dx*dx + dy*dy <= rs*rs;
}}
function rect_vs_circle(rect,circ){{
  const left = rect.x - rect.w/2, top = rect.y - rect.h/2;
  const right = rect.x + rect.w/2, bottom = rect.y + rect.h/2;
  const closest_x = Math.max(left, Math.min(circ.x, right));
  const closest_y = Math.max(top, Math.min(circ.y, bottom));
  const dx = circ.x - closest_x, dy = circ.y - closest_y;
  return dx*dx + dy*dy <= circ.r*circ.r;
}}

function intersects(a,b){{
  if (a.type === 'rect' && b.type === 'rect') return rect_vs_rect(a,b);
  if (a.type === 'circle' && b.type === 'circle') return circle_vs_circle(a,b);
  if (a.type === 'rect' && b.type === 'circle') return rect_vs_circle(a,b);
  if (a.type === 'circle' && b.type === 'rect') return rect_vs_circle(b,a);
  return false;
}}

function draw() {{
  ctx.clearRect(0,0,canvas.width,canvas.height);
  const view = computeView();
  // draw grid
  ctx.strokeStyle = '#222'; ctx.lineWidth = 1;
  for (let i=0;i<10;i++){{
    const t = i/9;
    ctx.beginPath();
    ctx.moveTo(0, t*canvas.height);
    ctx.lineTo(canvas.width, t*canvas.height);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(t*canvas.width, 0);
    ctx.lineTo(t*canvas.width, canvas.height);
    ctx.stroke();
  }}
  // detect collisions
  const colliding = new Set();
  for (let i=0;i<hitboxes.length;i++) for (let j=i+1;j<hitboxes.length;j++) {{
    if (intersects(hitboxes[i], hitboxes[j])) {{
      colliding.add(i); colliding.add(j);
    }}
  }}

  // draw hitboxes
  for (let i=0;i<hitboxes.length;i++) {{
    const h = hitboxes[i];
    const isColl = colliding.has(i);
    if (h.type === 'rect') {{
      const cx = toCanvasX(h.x, view), cy = toCanvasY(h.y, view);
      const cw = Math.abs(toCanvasX(h.x + h.w/2, view) - toCanvasX(h.x - h.w/2, view));
      const ch = Math.abs(toCanvasY(h.y + h.h/2, view) - toCanvasY(h.y - h.h/2, view));
      ctx.fillStyle = isColl ? 'rgba(255,60,60,0.4)' : 'rgba(60,160,255,0.25)';
      ctx.strokeStyle = isColl ? 'rgba(255,60,60,0.9)' : 'rgba(60,160,255,0.9)';
      ctx.lineWidth = 2;
      ctx.fillRect(cx - cw/2, cy - ch/2, cw, ch);
      ctx.strokeRect(cx - cw/2, cy - ch/2, cw, ch);
    }} else {{
      const cx = toCanvasX(h.x, view), cy = toCanvasY(h.y, view);
      const cr = Math.abs(toCanvasX(h.x + h.r, view) - toCanvasX(h.x, view));
      ctx.beginPath();
      ctx.fillStyle = isColl ? 'rgba(255,180,60,0.35)' : 'rgba(180,255,120,0.2)';
      ctx.strokeStyle = isColl ? 'rgba(255,180,60,0.95)' : 'rgba(180,255,120,0.95)';
      ctx.lineWidth = 2;
      ctx.arc(cx, cy, cr, 0, Math.PI*2);
      ctx.fill();
      ctx.stroke();
    }}
    // label
    ctx.fillStyle = '#fff';
    ctx.font = '12px sans-serif';
    ctx.fillText(String(i), toCanvasX(h.x, view)+6, toCanvasY(h.y, view)-6);
  }}
}}

resize();
draw();
</script>
</body>
</html>
"""
    if filename is None:
        filename = Path(os.getcwd()) / "hitbox_viewer.html"
    else:
        filename = Path(filename)
    filename.write_text(html, encoding="utf-8")
    # try to open using host browser environment variable (per workspace instruction)
    try:
        os.system(f'$BROWSER "{filename}"')
    except Exception:
        pass
    return filename


def open_tests_link(target: str | Path | None = None) -> Path:
  """
  Create a small HTML page with a link to the given target file (defaults to hitbox_viewer.html),
  open it in the host browser, and return the path to the created page.
  """
  if target is None:
    target = Path(os.getcwd()) / "hitbox_viewer.html"
  else:
    target = Path(target)

  page_path = Path(os.getcwd()) / "run_tests.html"
  html = f"""<!doctype html>
<html>
<head><meta charset="utf-8"/><title>Run Tests</title></head>
<body style="font-family:sans-serif;background:#111;color:#eee;display:flex;flex-direction:column;align-items:center;justify-content:center;height:100vh">
  <h1>Run Tests</h1>
  <p><a href="{target.name}" style="color:#7fdfff;font-size:18px" target="_blank">Open Hitbox Viewer</a></p>
  <p style="font-size:12px;color:#bbb">If the link doesn't work, open the file:</p>
  <pre style="background:#000;padding:8px;border-radius:6px;color:#9f9">{target}</pre>
</body>
</html>
"""
  page_path.write_text(html, encoding="utf-8")
  try:
    os.system(f'$BROWSER "{page_path}"')
  except Exception:
    pass
  return page_path
@dataclass

class RectHitbox:
    x: float  # center x
    y: float  # center y
    w: float  # width
    h: float  # height

    def bounds(self) -> Tuple[float, float, float, float]:
        """Return (left, top, right, bottom)."""
        half_w = self.w / 2.0
        half_h = self.h / 2.0
        return (self.x - half_w, self.y - half_h, self.x + half_w, self.y + half_h)

    def move(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy

    def set_position(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def contains_point(self, px: float, py: float) -> bool:
        left, top, right, bottom = self.bounds()
        return left <= px <= right and top <= py <= bottom

    def intersects(self, other: "Hitbox") -> bool:
        if isinstance(other, RectHitbox):
            return rect_vs_rect(self, other)
        if isinstance(other, CircleHitbox):
            return rect_vs_circle(self, other)
        raise TypeError("Unsupported hitbox type")


@dataclass
class CircleHitbox:
    x: float  # center x
    y: float  # center y
    r: float  # radius

    def move(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy

    def set_position(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def contains_point(self, px: float, py: float) -> bool:
        return (px - self.x) ** 2 + (py - self.y) ** 2 <= self.r ** 2

    def intersects(self, other: "Hitbox") -> bool:
        if isinstance(other, CircleHitbox):
            return circle_vs_circle(self, other)
        if isinstance(other, RectHitbox):
            return rect_vs_circle(other, self)
        raise TypeError("Unsupported hitbox type")


# Type alias for union
Hitbox = RectHitbox | CircleHitbox


# Collision helper functions

def rect_vs_rect(a: RectHitbox, b: RectHitbox) -> bool:
    a_left, a_top, a_right, a_bottom = a.bounds()
    b_left, b_top, b_right, b_bottom = b.bounds()
    # Separating Axis Theorem for AABB
    if a_right < b_left or b_right < a_left:
        return False
    if a_bottom < b_top or b_bottom < a_top:
        return False
    return True


def circle_vs_circle(a: CircleHitbox, b: CircleHitbox) -> bool:
    dx = a.x - b.x
    dy = a.y - b.y
    radius_sum = a.r + b.r
    return dx * dx + dy * dy <= radius_sum * radius_sum


def rect_vs_circle(rect: RectHitbox, circ: CircleHitbox) -> bool:
    left, top, right, bottom = rect.bounds()
    # Clamp circle center to rectangle
    closest_x = max(left, min(circ.x, right))
    closest_y = max(top, min(circ.y, bottom))
    dx = circ.x - closest_x
    dy = circ.y - closest_y
    return dx * dx + dy * dy <= circ.r * circ.r


# Example usage and small self-test
if __name__ == "__main__":
    # Character hitbox (rect) and a circular projectile
    player = RectHitbox(x=100, y=100, w=32, h=48)   # center-based
    projectile = CircleHitbox(x=116, y=110, r=8)

    print("Player bounds:", player.bounds())
    print("Projectile at:", (projectile.x, projectile.y), "r=", projectile.r)

    print("Player contains point (100,100):", player.contains_point(100, 100))
    print("Projectile contains point (120,110):", projectile.contains_point(120, 110))

    print("Collision (player vs projectile):", player.intersects(projectile))

    # Move projectile away
    projectile.move(100, 0)
    print("Moved projectile to:", (projectile.x, projectile.y))
    print("Collision after move:", player.intersects(projectile))

    # Rect vs rect test
    enemy = RectHitbox(x=120, y=100, w=24, h=24)
    print("Player vs enemy collision:", player.intersects(enemy))

    # Basic assertions (will raise if something is wrong)
    assert player.intersects(RectHitbox(100, 100, 32, 48))
    assert circle_vs_circle(CircleHitbox(0, 0, 5), CircleHitbox(7, 0, 3)) is True
    assert rect_vs_circle(RectHitbox(0, 0, 10, 10), CircleHitbox(20, 20, 1)) is False

    # Launch the visual HTML viewer for the example hitboxes (writes file and attempts to open $BROWSER)
    try:
        viewer_path = launch_canvas_viewer([player, projectile, enemy])
        print("Viewer written to:", viewer_path)
    except Exception as e:
        print("Could not launch viewer:", e)
