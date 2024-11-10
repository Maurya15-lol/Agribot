print("Please use accurate values")
print("\n")
print("Let's start off by knowing your temperature ")
avg_temp = float(input("Enter the average temperature in your area (°C): "))


if -24 <= avg_temp <= 55:
    z = int(input("Please choose your soil type: \n"
                  "(1) FOR ALLUVIAL SOIL \n"
                  "(2) FOR LOAMY SOIL \n"
                  "(3) FOR BLACK SOIL \n"
                  "(4) FOR RED SOIL \n"
                  "(5) FOR LATERITE SOIL \n"
                  "(6) FOR SILT SOIL \n"
                  "(7) FOR SANDY-LOAM SOIL\n"))
    print("\n")

   #alluvial
    if z == 1:
        print("You have chosen ALLUVIAL SOIL as your soil type.")
        avg_rainfall = float(input("Enter the average amount of rainfall in your area (in CMS): "))

        if 75 <= avg_rainfall <= 200:
            print("You can grow RICE or SUGARCANE.")
            print("RICE is usually sown between JUNE - JULY and harvested between SEPTEMBER - OCTOBER.")
            print(
                "SUGARCANE is usually sown between FEBRUARY - MARCH or SEPTEMBER - OCTOBER and harvested after 10-16 MONTHS.")


        elif 50 <= avg_rainfall <= 100:
            print("You can grow WHEAT or MAIZE.")
            print("WHEAT is usually sown between OCTOBER - NOVEMBER and harvested between MARCH - APRIL.")
            print("MAIZE can be sown almost throughout the year and harvested in OCTOBER - DECEMBER.")
        else:
            print("No suitable crops found for this rainfall range.")

    #loamy
    elif z == 2:
        print("You have chosen LOAMY SOIL as your soil type.")
        avg_rainfall = float(input("Enter the average amount of rainfall in your area (in CMS): "))

        if 60 <= avg_rainfall <= 150:
            print("You can grow RICE, WHEAT, or MAIZE.")
            print("RICE is usually sown between JUNE - JULY and harvested between SEPTEMBER - OCTOBER.")
            print("WHEAT is usually sown between OCTOBER - NOVEMBER and harvested between MARCH - APRIL.")
            print("MAIZE can be sown almost throughout the year and harvested in OCTOBER - DECEMBER.")
        else:
            print("No suitable crops found for this rainfall range.")

    # Black
    elif z == 3:
        print("You have chosen BLACK SOIL as your soil type.")
        avg_rainfall = float(input("Enter the average amount of rainfall in your area (in CMS): "))

        if 75 <= avg_rainfall <= 150:
            print("You can grow COTTON or SOYBEAN.")
            print("COTTON is usually sown in MAY - JUNE and harvested in OCTOBER - NOVEMBER.")
            print("SOYBEAN can be sown from JUNE to JULY and harvested in OCTOBER.")
        else:
            print("No suitable crops found for this rainfall range.")

    #red
    elif z == 4:
        print("You have chosen RED SOIL as your soil type.")
        avg_rainfall = float(input("Enter the average amount of rainfall in your area (in CMS): "))

        if 50 <= avg_rainfall <= 100:
            print("You can grow GROUNDNUT or SUNFLOWER.")
            print("GROUNDNUT is usually sown from MAY to JUNE and harvested in SEPTEMBER.")
            print("SUNFLOWER can be sown from MARCH to APRIL and harvested in AUGUST.")
        else:
            print("No suitable crops found for this rainfall range.")

    # Laterite
    elif z == 5:
        print("You have chosen LATERITE SOIL as your soil type.")
        avg_rainfall = float(input("Enter the average amount of rainfall in your area (in CMS): "))

        if 100 <= avg_rainfall <= 250:
            print("You can grow CASHEW or TEA.")
            print("CASHEW is usually sown from APRIL to MAY and harvested from DECEMBER to JANUARY.")
            print("TEA can be grown throughout the year with proper irrigation.")
        else:
            print("No suitable crops found for this rainfall range.")

    # Silt
    elif z == 6:
        print("You have chosen SILT SOIL as your soil type.")
        avg_rainfall = float(input("Enter the average amount of rainfall in your area (in CMS): "))

        if 80 <= avg_rainfall <= 200:
            print("You can grow RICE or POTATOES.")
            print("RICE is usually sown between JUNE - JULY and harvested between SEPTEMBER - OCTOBER.")
            print("POTATOES can be planted from JANUARY to FEBRUARY and harvested in MAY.")
        else:
            print("No suitable crops found for this rainfall range.")

    # Sandy-Loam
    elif z == 7:
        print("You have chosen SANDY-LOAM SOIL as your soil type.")
        avg_rainfall = float(input("Enter the average amount of rainfall in your area (in CMS): "))

        if 50 <= avg_rainfall <= 120:
            print("You can grow CARROTS or ONIONS.")
            print("CARROTS are usually sown from AUGUST to SEPTEMBER and harvested in DECEMBER to FEBRUARY.")
            print("ONIONS can be planted from JANUARY to MARCH and harvested by MAY to JUNE.")
        else:
            print("No suitable crops found for this rainfall range.")

    else:
        print("Invalid soil type selected. Please choose a number between 1 and 7.")
else:
    print("Sorry only works for citizens of India")

