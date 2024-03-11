game = [1,2,3,4,5,6,7,8]
n = 4

def binary_search(game, n, list_lenght, i, attempt):

    if game[i] == n:
        return attempt

    elif game[i] > n:
        list_lenght = i
        middle_down = i//2
        return binary_search(game, n, list_lenght, middle_down, attempt+1)
        
    elif game[i] < n:
        middle_up = (i + list_lenght)//2
        return binary_search(game, n, list_lenght, middle_up, attempt+1)

list_lenght = len(game)
print(binary_search(game, n, list_lenght, list_lenght//2, 1))
