def main():
    ids_invalid = check_invalid("inputdata.txt")
    # print(f"invalid Ids: {ids_invalid}")
    print(f"answer is: {answer(ids_invalid)}")






def check_invalid(filename:str):
    """
    check for invalid product IDs 
    
    :param filename: Name of file to check
    :type filename: str
    """
    def readinput(filename:str):
        with open(filename, "r") as file:
            data = file.readline()
        return data.split(",")
    
    data = readinput(filename)
    

    def get_range(input_range):
        """
        Docstring for get_range
        
        :param input_range: range from input file ex:"11-22"

        returns it as a range ex: range(11, 23)
        """
        # print(input_range)
        ranges = input_range.split("-")
        start = int(ranges[0])
        stop = int(ranges[1]) + 1
        # print(f"start: {start}\nstop: {stop}")
        return range(start,stop)
    
    def check_duplicate(number:int):
        number = str(number)
        length = len(number)
        half = length // 2
        half_first = number[0:half]
        half_second = number[half:]
        # print(f"{half_first} and {half_second}")
        if half_first == half_second:
            # print(f"returning {half_first + half_second}")
            return half_first + half_second
        return 0


    # list of ranges from input data
    ids_invalid = []
    for entry in data:
        #test all numbers in every range
        for number in get_range(entry):
            duplicate = check_duplicate(number)
            # print(f"duplicate value is {duplicate}")
            if duplicate != 0:
                # print(f"appending {duplicate} to output")
                ids_invalid.append(duplicate)
    
    return ids_invalid
    



def answer(ids_invalid:list):
    """
    Calculate answer from list of invalid ids
    
    :param ids_invalid: List object of invalid ids
    :type ids_invalid: list
    """
    total = 0
    for id in ids_invalid:
        id = int(id)
        total += id
    return total           






if __name__ == "__main__":
    main()


