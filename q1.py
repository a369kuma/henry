def add_index(lon):
    for i in range(len(lon)):
        lon[i] += i
    return lon
        

def main():
    lon = [0,1,2]
    answer = add_index(lon)
    print(answer)


if __name__ == "__main__":
    main()