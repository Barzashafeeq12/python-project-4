def main():
    farenheit = float(input("\033[1;3m Enter the temperature in farenheit \033[0m"))
    celcius = (farenheit - 32) *5.0/9.0
    print(f"Temperature : {farenheit}F ={celcius}C")
if __name__ == '__main__':
    main()