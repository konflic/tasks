## OOP Tasks

### Excercise 1
Write a program that defines a shape class with a constructor that gives value to w (width) and h(height) and **not implemented** area() method. Define two sub-classes Triangle and Rectangle, implement area method, it should return area of the figure according to geometry rules (*google formulas*). Below instantiate two objects a triangle and a rectangle and call the area() function in this two varibles.

```python
...

triangle = Triangle(w=10, h=12)
rectangle = Rectangle(w=10, h=12)

print(triangle.area()) # -> 60
print(rectangle.area()) # -> 120
```

### Exercise 2
Write a probram with a mother class Animal. Inside it define a constructor with name and age parameters, and say() method that returns the name and age of Anumal. Then create two sub-classes Zebra and Dolphin. Create two objects and call say method. say method must be implemented **only** in Animal class. (Hint, use __class__ variable)

```python
...

d = Dolphin("Chuck", 20)
z = Zebra("Zelda", 30)

d.say() # -> Hi, I am Dolphin Chuck and I am 20!
z.say() # -> Hi, I am Zebra Zelda and I am 30!
```

### Req
1. Assingment should be passed as Pull-request
2. Create a separate folder in your repo called hw_oop
3. Each in separate files. ex1.py and ex2.py inside folder.
4. PR should be merged ONLY after approval.
