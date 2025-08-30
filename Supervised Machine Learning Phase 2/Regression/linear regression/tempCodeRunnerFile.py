        # user sy input ly kr prediction

        hour = float(input("Enter hours which u wanna study: "))

        prediction= model.predict([[hour]]) 


        if hour <= 2 :
            print(f"Based on your hour {hour}, you may score around {prediction} u will fail")
        else:
            print(f"Based on your hour {hour}, you may score around {prediction} u will passed")