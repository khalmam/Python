# This problem involves a right triangle, where:

# 𝐴
# 𝐵
# AB is base (horizontal side),

# 𝐵
# 𝐶
# BC is vertical side,

# 𝐴
# 𝐶
# AC is the hypotenuse (since triangle is right-angled at 
# 𝐵
# B).

# You are given:

# 𝐴
# 𝐵
# =
# 𝑎
# AB=a

# 𝐵
# 𝐶
# =
# 𝑏
# BC=b

# You need to find angle 
# 𝜃
# =
# ∠
# 𝑀
# 𝐵
# 𝐶
# θ=∠MBC, where M is the midpoint of hypotenuse AC.

# 🧠 Concept
# In any right triangle, the midpoint of the hypotenuse is equidistant from all three vertices.
# This makes triangle 
# △
# 𝑀
# 𝐵
# 𝐶
# △MBC an isosceles triangle, and you can use trigonometry to find angle 
# ∠
# 𝑀
# 𝐵
# 𝐶
# ∠MBC.

# But instead of diving too deep into geometry, we can solve this using vector geometry
# or directly using trigonometry.

# Let’s proceed with code using Python’s math module.




import math

# Read input
a = float(input())
b = float(input())

# Midpoint logic: angle at MBC
mb = math.hypot(a / 2, b / 2)

# cos(theta) = (b / 2) / mb
cos_theta = (b / 2) / mb
theta_rad = math.acos(cos_theta)
theta_deg = math.degrees(theta_rad)

# Print with degree symbol
print(f"{theta_deg:.0f}\u00B0")  # \u00B0 is the degree symbol
