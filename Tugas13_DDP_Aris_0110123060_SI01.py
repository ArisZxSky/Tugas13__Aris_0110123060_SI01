class Animal:
    def __init__(self, name, food, habitat, reproduction):
        self.name = name
        self.food = food
        self.habitat = habitat
        self.reproduction = reproduction

class Rhino(Animal):
    def __init__(self, habitat):
        super().__init__("Badak", "Badak makan tumbuhan", habitat, "viviparous")
        self.size = "Badak bertubuh Besar"
        self.color = "Berwarna Abu-abu"
        self.endangered = "Badak Berkembang biak dengan melahirkan"
        self.horn_type = "Badak memiliki tanduk"

    def charge(self):
        return f"{self.name} sedang melakukan serangan!"

class Fish(Animal):
    def __init__(self, habitat):
        super().__init__("Ikan", "plankton", habitat, "oviparous")
        self.size = "ada yang kecil dan besar"
        self.color = "jenisnya Beragam"
        self.fins = "Berkembang biak dengan bertelur"
        self.scales = "Ikan kebanyakan makan ikan lain lagi"

    def swim(self):
        return f"{self.name} sedang berenang di laut."

class Snake(Animal):
    def __init__(self, habitat):
        super().__init__("Ular", "hewan kecil", habitat, "oviparous")
        self.size = "Ular memiliki tubuh yang Panjang"
        self.color = "jenisnya Bervariasi"
        self.venomous = "Ular Berkembang biak dengan memakan ikan"
        self.pattern = "Memiliki Corak unik"

    def slither(self):
        return f"{self.name} sedang merayap di tanah."

# Contoh penggunaan:
rhino = Rhino("Badak hidup diHutan Tropis")
print(rhino.charge())  
print(rhino.size)      
print(rhino.color)     
print(rhino.endangered) 
print(rhino.horn_type) 

fish = Fish("Ikan hidup di Perairan Tawar dan ada juga di laut")
print(fish.swim())     
print(fish.size)       
print(fish.color)      
print(fish.fins)       
print(fish.scales)     

snake = Snake("Kebanyakan ular hidup di Hutan Hujan Tropis")
print(snake.slither()) 
print(snake.size)      
print(snake.color)     
print(snake.venomous)  
print(snake.pattern)   
print(snake.habitat)   
