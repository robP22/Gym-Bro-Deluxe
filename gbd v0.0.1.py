'''
This is the initial requirements and design document, therefore it may contain mostly plain english or pseudocode (which also may not be fully correct, but represents a general starting idea)

Gui application (may be able to use PyQt6) #future mobile support and primary useage

user_age = integer calculated when the user confirms their birthdate?
user_BMI = get_user_input_here (weight, height, neck measurement, naval measurement, shoulder measurement) #im sure a library or function exists for this
lift_intensity = #need function that uses slider for intensity, returns estimated lift weight (integer) for lift type

#we may be able to use a sql database to record information about typical lifting weights for specific exercises in order to more accurately predict the weight_given_based_on_lift_intensity (tmp name)

# should include things for explosiveness, endurance, raw power?
# calculate relative strength (percentage based on user weight vs max?

def estimated_lift_weight(user_BMI, workout_type, list_of_1rep_max): #may not be all necessary arguments
    # here we set lift_intensity['only values for individual exercises the user provided will be iterated over'] = 100% for each workout that the user inputted information about
    # we use this to calculate lift_weight based on the lift_intensity slider. The user may update the 1 rep max on their set '1_rep_max_day' or opt to update it freely?
    # load our database
    
    
# automatically store the users routine and suggest improvements to help targeting specific muscle groups or prevent the user from overworking a specific group of muscles by suggesting routine changes (such as instead of doing squats 4 days in a row, only do legs 1-2x per week)
# provide the user some sort of logic and proof behind each suggestion explaining how it may benefit the user and allow them to accept or decline
# automatically increase training intensity based on the schedule (maybe we can have some templates and a community for downloading templates)
# automatically notifies the user when its training time and shows a list of good warmup exercises for that days training type

# need to display each workout (as an image or small video) on the main workout page, clickable links showing which muscles to activate during the exercise (which typically is the targeted muscle to train)
