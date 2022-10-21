def afficheliste():
    liste=[1,2,3,4,5,6]
    for i in range (len(liste))  :
        print(f"{liste[i]}")

def pour():
    for i in range (1,5,2):
        print("ouusmane sinianta")

def main():
    Name= str(input('donner ton nom'))
    age= int(input('donne ton age: \t'))
    print(f"bonjour {Name.title()}")
    print(f"ton age est : {age}")

if __name__ == '__main__':
        pour()
        afficheliste()