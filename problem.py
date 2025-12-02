
data_practice = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82"]

data_real = []
with open("inputdata_1.txt","r") as data:
    for line in data.readlines():
        data_real.append(line.replace("\n",""))

def solve(rotations):
    
    def move(value, currentposition):
        
        subtract = False
        direction = str(value[0])
        amount = int(value[1:])

        if direction == "L":
            subtract = True
        
        for x in range(0, amount):
            if subtract:
                currentposition-=1
            else:
                currentposition+=1
            
            if currentposition == 100:
                currentposition = 0
            
            if currentposition == -1:
                currentposition = 99

        return currentposition


    rotations = rotations.copy()

    # Starting position
    position = 50
    password = 0
    for rotation in rotations:
        print(f"Rotating {rotation}")
        position = move(rotation, position)
        print(f"New Position = {position}")
        if position == 0:
            password += 1
    return password


def main():
    print(f"password is {solve(data_real)}")


if __name__ == "__main__":
    main()
    # print(data_real)

