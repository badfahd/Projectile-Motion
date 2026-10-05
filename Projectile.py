import vpython as vp

scene = vp.canvas(title="Projectile Simulator", width=1600, height=900,center=vp.vector(0,0,0),resizable=True)
floor = vp.box(
    pos=vp.vector(0, -5, 0),
    size=vp.vector(30, 0.2, 5),
    color=vp.color.green,
)
base = vp.box(
    pos=vp.vector(-15, -4.9, 0),
    size=vp.vector(1.5, 0.6, 1.5),
    color=vp.color.orange,
)

LAUNCH_POS = vp.vector(-15, -4.6, 0)
scene.camera.pos=vp.vector(-15,2,15)
scene.camera.axis=vp.vector(5,-2,-15)
ball = None
firing = False
launcher = None

# UI Element setup before functions call them
info = vp.wtext(text="")


def show_theory(s=None):
  theta = vp.radians(angle_slider.value)
  v = float(speed_input.text)
  R = v**2 * vp.sin(2 * theta) / 9.8
  info.text = f"Theoretical Range: {R:.2f} units"


def launch(b=None):
  global ball, firing, launcher
  theta = vp.radians(angle_slider.value)
  v = float(speed_input.text)

  if ball is not None:
    ball.visible = False
  ball = vp.sphere(
      pos=LAUNCH_POS, radius=0.3, color=vp.color.red, make_trail=True
  )
  ball.v = vp.vector(v * vp.cos(theta), v * vp.sin(theta), 0)

  if launcher is not None:
    launcher.visible = False
  launcher = vp.cylinder(
      pos=LAUNCH_POS,
      radius=0.4,
      color=vp.color.gray(0.5),
      axis=2 * vp.vector(vp.cos(theta), vp.sin(theta), 0),
  )

  firing = True


scene.append_to_caption("Angle(1-90 Degree): ")
angle_slider = vp.slider(
    min=1, max=90, value=45, step=1, length=250, bind=show_theory
)
scene.append_to_caption("\nSpeed: ")
speed_input = vp.winput(text="10", width=60, bind=show_theory)
scene.append_to_caption(" ")
launch_button = vp.button(text="Launch!", bind=launch)
scene.append_to_caption("\n")

g = vp.vector(0, -9.8, 0)
dt = 0.005

show_theory()  # Initialize theory display

while True:
  vp.rate(200)
  if firing and ball is not None:
    ball.v += g * dt
    ball.pos += ball.v * dt
    if ball.pos.y - ball.radius <= -4.9:
      firing = False
      print(f"Landed distance: {ball.pos.x - LAUNCH_POS.x:.2f} units")