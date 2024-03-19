import turtle

def draw_pifagor_tree(t, branch_length, level):
    if level == 0:
        return
    t.forward(branch_length * level)
    t.left(45)
    draw_pifagor_tree(t, branch_length, level-1)
    t.right(90)
    draw_pifagor_tree(t, branch_length, level-1)
    t.left(45)
    t.backward(branch_length * level)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    branch_length = 10

    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("green")
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    
    draw_pifagor_tree(t, branch_length, level)
    
    screen.mainloop()

if __name__ == "__main__":
    main()
