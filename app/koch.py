import turtle
import time
from loguru import logger


def draw_koch(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        draw_koch(length / 3, depth - 1)
        turtle.left(60)
        draw_koch(length / 3, depth - 1)
        turtle.right(120)
        draw_koch(length / 3, depth - 1)
        turtle.left(60)
        draw_koch(length / 3, depth - 1)


def draw_koch_snowflake(length, depth):
    for _ in range(3):
        draw_koch(length, depth)
        turtle.right(120)


def main():
    turtle.speed(0)
    starting_positions = [(x, y)
                          for x in range(-200, 201)
                          for y in range(200, -201, -200)]

    for depth, pos in enumerate(starting_positions, 1):
        turtle.penup()
        turtle.goto(pos)
        turtle.pendown()
        start_time = time.time()
        draw_koch_snowflake(100, depth)
        end_time = time.time()
        logger.info(f"Depth: {depth}, Took: {end_time - start_time:.2f}s")

    turtle.done()


if __name__ == "__main__":
    main()
