# Approximating π physically

A script I made when I was bored. It shows how π emerges from the property of
the circle: a point is inside a circle if its distance from the center is less
than or equal to the radius of the circle.

π can be approximated from a circle of radius r inscribed within a square. If
we randomly distribute points throughout a square or a circle:

```
Number of points ~ Area
```

Then, from the formulas for the area of a square or a circle:

```
Area Square = (2r)² = 4r²
Area Circle = πr²
```

Obtaining π is simple:

```
Area Circle / Area Square = πr² / 4r² = π / 4
π = Area Circle / Area Square · 4
```
