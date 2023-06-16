import turtle
import time
from loguru import logger


def draw_sierpinski(length, depth):
    if depth == 0:
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        draw_sierpinski(length / 2, depth - 1)
        turtle.forward(length / 2)
        draw_sierpinski(length / 2, depth - 1)
        turtle.backward(length / 2)
        turtle.right(60)
        turtle.forward(length / 2)
        turtle.left(60)
        draw_sierpinski(length / 2, depth - 1)
        turtle.right(60)
        turtle.backward(length / 2)
        turtle.left(60)


def main():
    turtle.speed(0)
    start_positions = [(-300, 200), (0, 200), (300, 200),
                       (-300, -100), (0, -100), (300, -100)]
    for depth, start_pos in zip(range(1, 7), start_positions):
        turtle.penup()
        turtle.goto(start_pos)
        turtle.pendown()
        start_time = time.time()
        draw_sierpinski(150, depth)
        end_time = time.time()
        logger.info(f"Depth: {depth}, Took: {end_time - start_time:.2f}s")
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
