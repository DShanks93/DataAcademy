def run():
    def area_tri(b,h):
        area=(b*h)/2
        return area
    
    print("Bienvenido a la operación área de un triángulo, indicar : ")
    base = float(input("Base: "))
    altura = float(input("Altura: "))

    print("El área del triángulo es: " + str(area_tri(base,altura)) + "und")              
    
    

if __name__ == "__main__":
    run()