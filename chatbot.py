talkers = ["Chatbot", "Vous"]
current_talker = talkers[0]
frequent_questions = [
"Quels sont les horaires d’ouverture de l'administration d’Irgib Africa ?", 
"Où se trouve le campus d’Irgib Africa ?",
"Comment puis-je m’inscrire à Irgib Africa ?",
"Quels sont les frais de scolarité pour chaque programme ?",
"Quand commencent les inscriptions pour la prochaine année académique ?",
"Y a-t-il des bourses disponibles pour les étudiants ?",
"Quels documents sont à fournir ?"
]
frequent_questions_string = ""
question_index = 1

for question in frequent_questions:
    frequent_questions_string += f"{question_index}. {question}\n"
    question_index += 1

def normalize_input(input):
    input = " ".join(input.split())
    return input.lower().strip()

def check_integer(message):
    try:
        int_message = int(message)
        return True
    except ValueError:
        return False
    
def answer_frequent(message):
        if message == "1":
            response = "Nous sommes ouverts de 9h à 18h."
        elif message == "2":
            response = "Nous sommes à Akpakpa Unicomer juste apres la SOBEBRA"
        elif message == "3":
            response = "Vous pouvez utiliser notre site web ou vous inscrire directement sur place"
        elif message == "4":
            response = "500.000 FCFA pour la contribution à tous les programmes. Les frais d'inscription ou de réinscription ne sont pas incluses"
        elif message == "5":
            response = "Dès Juillet prochain"
        elif message == "6":
            response = "Oui, des bourses de mérite sont attribuées aux étudiants. Durant la formation, il auront droit à des stages"
        elif message == "7":
            response = "téléchargés la liste des documents à fournir ici : [https://benindelice.onrender.com/signup]"
        else:
            response = f"Choisissez une valeur dans la plage des suggestions données: \n{frequent_questions_string}"
        return f"{current_talker}: {response}"
        
def change_talker():
    return talkers[0] if current_talker == talkers[1] else talkers[1]
    
def check_greetings(message):
    return message in ["bonjour", "bonsoir", "salut", "coucou", "hello", "hi", "eya"]

def check_thanks(message):
    for word in ["merci", "thanks", "ok", "je vois"]:
        response = word in message
        if response:
            return True
    else:
        return False

def check_bye(message):
    for word in ["bye", "au revoir"]:
        response = word in message
        if response:
            return True
    else:
        return False

def partiular_response(message):
    # Case 1 
    for word in ["horaire", "heure", "horaires", "heures", "ouverture", "d'ouverture"]:
        if word in message:
            return f"{current_talker}: Nous sommes ouverts de 9h à 18h."
        
    # Case 2 
    for word in ["où se trouve", "quelle est la position", "la localisation d", "la position d"]:
        if word in message:
            return f"{current_talker}: Nous sommes à Akapkpa"
        
    # Case 3: Exemple : Y a-t-il plusieurs campus pour l’université Irgib Africa ?
    for word in ["plusieurs campus", "les campus", "les sites", "plusieurs sites"]:
        if word in message:
            return f"{current_talker}: Il y existe plusieurs campus dans diffrentes parties du pays et à l'intenational"
    
    else:
        return f"{current_talker}: Je ne comprends pas votre question"
    
print(f"""
{current_talker}: Bonjour ! Je suis votre assistant virtuel.
Vous pouvez poser directement une question ou alors choisir une courante: 

{frequent_questions_string}
""")

while True:
    current_talker = change_talker()
    user_message = normalize_input(input(f"{current_talker}: "))

    current_talker = change_talker()
    is_integer = check_integer(user_message)
    if is_integer:
        print(answer_frequent(user_message))

    elif check_greetings(user_message):
        print(f"{current_talker}: Bonjour ! Comment puis-je vous aider ?")
    
    elif check_thanks(user_message):
        print(f"{current_talker}: C'est un plaisir de vous aider. Avez-vous d'autres questions")

    elif check_bye(user_message):
        exit(f"{current_talker}: Au revoir ! Passez une excellente journée")

    else:
        print(partiular_response(user_message))
