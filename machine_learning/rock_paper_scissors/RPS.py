# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random



def player(prev_play, opponent_history=[],
          play_order={}):
    n=5
    opponent_history.append(prev_play)
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    sub_order={}
    
    guess = 'P' # Respuesta hasta que llegue al mínimo
    
    if len(opponent_history) > n:
        last_n = "".join(opponent_history[-n:])
    
        if last_n not in play_order:
            play_order[last_n] = 1
        else:
            play_order[last_n] += 1

        potential = [
            last_n[1:] + "R",
            last_n[1:] + "P",
            last_n[1:] + "S",
        ]

        sub_order = {k: play_order[k] for k in potential if k in play_order}
        
        
        if len(sub_order) > 0: 
            prediction = max(sub_order, key=sub_order.get)[-1:]
            guess = ideal_response[prediction]
                
                
        # print('play_order:', play_order)
        # print('potential:', potential)
        # print('sub_order: ',sub_order)
        # print('opponent_history', opponent_history)

    return guess


# opponent_history=['R','R','R','R','R']
# prev_play='R'
# play_order={}


# n=5
# opponent_history.append(prev_play)

# guess = 'R' # Respuesta hasta que llegue al mínimo

# if len(opponent_history) > n:
#     last_n = "".join(opponent_history[-n:])

#     if last_n not in play_order:
#         play_order[last_n] = 1
#     else:
#         play_order[last_n] += 1

#     potential = [
#         last_n[1:] + "R",
#         last_n[1:] + "P",
#         last_n[1:] + "S",
#     ]

#     sub_order = {
#         k: play_order[k]
#         for k in potential if k in play_order
#     }

#     prediction = max(sub_order, key=sub_order.get)[-1:]

#     ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
#     guess = ideal_response[prediction]
    
# print(guess)