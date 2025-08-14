import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Replace with the actual path to your ChromeDriver executable
webdriver_path = r"C:\\Users\\Adhvaith\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

# Create a new instance of the Chrome driver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://www.ecalc.ch/motorcalc.php")

try:
    # Wait for 5 seconds
    time.sleep(5)

    # Look for the "OK" button with the specified ID
    ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "modalConfirmOk"))
    )

    # Click the "OK" button
    ok_button.click()
    print("Clicked OK button.")
    
    # Locate and click the login link
    login_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/calcmember/login.php')]"))
    )
    login_link.click()
    print("Clicked on the login link.")

    # Wait for a moment to ensure the page updates after clicking the login link
    time.sleep(2)

    # Assuming the username is 'your_username' and password is 'your_password'
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    # Enter the username and password
    username_input.send_keys("dhruvbobbyjohnson@gmail.com")
    password_input.send_keys("auoexb3t")
    print("Entered username and password.")

    # Locate and click the submit button
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='myButton']"))
    )
    submit_button.click()
    print("Clicked submit button.")
    try:
        popup = WebDriverWait(driver, 10).until(
            EC.alert_is_present()
        )
        print("Pop-up detected.")
        # Switch to the pop-up and accept it (click OK)
        popup.accept()
        print("Clicked OK in the pop-up.")
    except Exception:
        print("No pop-up detected.")
    time.sleep(10)  # You can adjust the duration as needed

    # Input the value "16000" for the weight using JavaScript
    weight_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inGWeight"))
    )
    driver.execute_script("arguments[0].value = '16000'", weight_input)
    print("Entered weight: 16000")

    wingspan_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "inGWingSpan"))
    )
    driver.execute_script("arguments[0].value = '64'", wingspan_input)
    print("Entered wingspan: 64")

    wing_area_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "inGWingArea"))
    )
    driver.execute_script("arguments[0].value = '165'", wing_area_input)
    print("Entered wing area: 165")

    configuration_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "inBS"))
    )
    driver.execute_script("arguments[0].value = '6'", configuration_input)
    print("Entered configuration: 6s")

    # Function to scroll and select an option in the dropdown
    def select_option(dropdown_id, target_option_text):
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, dropdown_id))
        )
        dropdown.click()

        options = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, f"//select[@id='{dropdown_id}']/option"))
        )

        for option in options:
            option_text = option.text
            print(f"Checking {dropdown_id} option: {option_text}")
            if option_text == target_option_text:
                option.click()
                print(f"Selected {dropdown_id}: {target_option_text}")
                break

    # List of motor manufacturers and their corresponding motor options
    motor_manufacturer_motor_options = {
        'Hacker Motor': ['A60-5XS V4 28-Pole (420)','A-50 16L V4 (265)'],

    }
    target_battery_option_texts = ['LiPo 4000mAh - 80/120C',  
    'LiPo 4500mAh - 80/120C', 
    'LiPo 5000mAh - 80/120C', 'LiPo 6000mAh - 80/120C','LiPo 4000mAh - 65/100C', 
    'LiPo 4500mAh - 65/100C', 'LiPo 5000mAh - 65/100C', 'LiPo 6000mAh - 65/100C',
    'LiPo 4000mAh - 55/80C','LiPo 4500mAh - 55/80C', 
    'LiPo 5000mAh - 55/80C', 'LiPo 6000mAh - 55/80C','LiPo 4000mAh - 35/50C', 
    'LiPo 4500mAh - 35/50C', 'LiPo 5000mAh - 35/50C', 'LiPo 6000mAh - 35/50C', 
    'LiPo 4000mAh - 30/45C','LiPo 4500mAh - 30/45C', 
    'LiPo 5000mAh - 30/45C', 'LiPo 6000mAh - 30/45C', 'LiPo 8000mAh - 30/45C', 'LiPo 4000mAh - 25/35C', 
    'LiPo 4500mAh - 25/35C', 'LiPo 5000mAh - 25/35C', 'LiPo 6000mAh - 25/35C'
    ]
    target_controller_option_texts = ['max 80A' , 
    'max 90A' , 'max 100A' , 'max 120A',
    'APD 120F3x',
    'APD 200F3x',
    'CC Phoenix Edge 75',
    'CC Phoenix Edge 100',
    'CC Phoenix Edge 130',
    'CC Phoenix Edge HV 80',
    'CC Talon 90',
    'CC Talon 120 HV',
    ]

    csv_file_path = "ecalc_data12.csv"
    with open(csv_file_path, mode='w', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Battery", "Controller", "Motor Manufacturer", "Motor Type", "Diameter", "Pitch", "Static Thrust","Specific Thrust","RPM","Current","Voltage","Power","Thrust-weight","Efficiency","Pitch-Speed","Speed","Motor-Run-Time"])

    # Loop through each motor manufacturer
    for target_motor_manufacturer_option_text, motor_options in motor_manufacturer_motor_options.items():

        # Select the motor manufacturer option
        select_option('inMManufacturer', target_motor_manufacturer_option_text)

        # Loop through each motor option for the current motor manufacturer
        for target_motor_option_text in motor_options:

            # Select the motor option
            select_option('inMType', target_motor_option_text)

            # Loop through each battery, controller, diameter, and pitch combination
            for battery_option in target_battery_option_texts:
                for controller_option in target_controller_option_texts:
                    for diameter in range(18, 23):
                        for pitch in range(8, 14):
                            # Input the diameter value using JavaScript
                            diameter_input = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.ID, "inPDiameter"))
                            )
                            driver.execute_script(f"arguments[0].value = '{diameter}'", diameter_input)
                            print(f"Entered diameter: {diameter}")

                            # Input the pitch value using JavaScript
                            pitch_input = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.ID, "inPPitch"))
                            )
                            driver.execute_script(f"arguments[0].value = '{pitch}'", pitch_input)
                            print(f"Entered pitch: {pitch}")

                            # Select the battery option
                            select_option('inBCell', battery_option)

                            # Select the controller option
                            select_option('inEType', controller_option)

                            time.sleep(3)
                            calculate_button = WebDriverWait(driver, 30).until(
                                EC.element_to_be_clickable((By.NAME, "btnCalculate"))
                            )

                            # Click the "Calculate" button
                            calculate_button.click()
                            print("Clicked Calculate button.")
                            time.sleep(3)

                            thrust_element = driver.find_element(By.ID, "outPThrust")
                            thrust_value = thrust_element.text
                            specific_thrust_element = driver.find_element(By.ID, "outPEfficiency")
                            specific_thrust_value = specific_thrust_element.text
                            revolutions_element = driver.find_element(By.ID, "outPRpm")
                            revolutions_value = revolutions_element.text
                            current_element = driver.find_element(By.ID, "outLoggerI")
                            current_value = current_element.text
                            power_element = driver.find_element(By.ID, "outLoggerP")
                            power_value = power_element.text
                            thrust_weight_element = driver.find_element(By.ID, "outTotThrustWeight")
                            thrust_weight_value = thrust_weight_element.text
                            voltage_element = driver.find_element(By.ID, "outLoggerV")
                            voltage_value = voltage_element.text
                            efficiency_element = driver.find_element(By.ID, "outMaxEfficiency")
                            efficiency_value = efficiency_element.text
                            pitch_speed_element = driver.find_element(By.ID, "outPPitchSpeed")
                            pitch_speed_value = pitch_speed_element.text
                            speed_element = driver.find_element(By.ID, "outMLevelSpeed")
                            speed_value = speed_element.text
                            motor_run_time_element = driver.find_element(By.ID, "outBMixedFlightTime")
                            motor_run_time_value = motor_run_time_element.text

                            # Append the data to the CSV file
                            with open(csv_file_path, mode='a', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow([battery_option,controller_option,target_motor_manufacturer_option_text,target_motor_option_text,diameter,pitch,thrust_value,specific_thrust_value,revolutions_value,current_value,voltage_value,power_value,thrust_weight_value,efficiency_value,pitch_speed_value,speed_value,motor_run_time_value])
                                
                              

                            thrust_weight_range = (0.25, 0.35)
                            csv_file_path = "ecalc_data12.csv"

                            # Specify the path for the filtered CSV file
                            filtered_csv_file_path = "filtered_ecalc_data12.csv"

                            # Open the filtered CSV file for writing
                            with open(filtered_csv_file_path, mode='w', newline='') as filtered_file:
                                filtered_writer = csv.writer(filtered_file)
                                filtered_writer.writerow(["Battery", "Controller", "Motor Manufacturer", "Motor Type", "Diameter", "Pitch", "Static Thrust", "Specific Thrust", "RPM", "Current", "Voltage", "Power", "Thrust-weight", "Efficiency", "Pitch-Speed", "Speed", "Motor-Run-Time"])

                                # Loop through each row in the original CSV file
                                with open(csv_file_path, mode='r') as original_file:
                                    reader = csv.reader(original_file)
                                    next(reader)  # Skip the header row

                                    for row in reader:
                                       
                                       thrust_weight_value = float(row[12])  # Adjust the index based on the actual position of the thrust-weight ratio
                                       if thrust_weight_range[0] <= thrust_weight_value <= thrust_weight_range[1]:
                                        filtered_writer.writerow(row)
    specific_diameter_pitch_combinations = [
    (20,15),
    (20.5,13.5),
    (20.5,12),
    (21,13.5),
    (21.5,13),
    (24,12),
    ]

    # Loop through the specific diameter and pitch combinations
    for given_diameter, given_pitch in specific_diameter_pitch_combinations:
        # Input the diameter value using JavaScript
        diameter_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inPDiameter"))
        )
        driver.execute_script(f"arguments[0].value = '{given_diameter}'", diameter_input)
        print(f"Entered diameter: {given_diameter}")

        # Input the pitch value using JavaScript
        pitch_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inPPitch"))
        )
        driver.execute_script(f"arguments[0].value = '{given_pitch}'", pitch_input)
        print(f"Entered pitch: {given_pitch}")

        # Loop through each battery and controller option
        for battery_option in target_battery_option_texts:
            for controller_option in target_controller_option_texts:
                # Select the battery option
                select_option('inBCell', battery_option)

                # Select the controller option
                select_option('inEType', controller_option)

                time.sleep(3)
                calculate_button = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.NAME, "btnCalculate"))
                )

                # Click the "Calculate" button
                calculate_button.click()
                print("Clicked Calculate button.")
                time.sleep(3)

                thrust_element = driver.find_element(By.ID, "outPThrust")
                thrust_value = thrust_element.text
                specific_thrust_element = driver.find_element(By.ID, "outPEfficiency")
                specific_thrust_value = specific_thrust_element.text
                revolutions_element = driver.find_element(By.ID, "outPRpm")
                revolutions_value = revolutions_element.text
                current_element = driver.find_element(By.ID, "outLoggerI")
                current_value = current_element.text
                power_element = driver.find_element(By.ID, "outLoggerP")
                power_value = power_element.text
                thrust_weight_element = driver.find_element(By.ID, "outTotThrustWeight")
                thrust_weight_value = thrust_weight_element.text
                voltage_element = driver.find_element(By.ID, "outLoggerV")
                voltage_value = voltage_element.text
                efficiency_element = driver.find_element(By.ID, "outMaxEfficiency")
                efficiency_value = efficiency_element.text
                pitch_speed_element = driver.find_element(By.ID, "outPPitchSpeed")
                pitch_speed_value = pitch_speed_element.text
                speed_element = driver.find_element(By.ID, "outMLevelSpeed")
                speed_value = speed_element.text
                motor_run_time_element = driver.find_element(By.ID, "outBMixedFlightTime")
                motor_run_time_value = motor_run_time_element.text

            # Append the data to the CSV file
            with open(csv_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([battery_option, controller_option, target_motor_manufacturer_option_text, target_motor_option_text, given_diameter, given_pitch, thrust_value, specific_thrust_value, revolutions_value, current_value, voltage_value, power_value, thrust_weight_value, efficiency_value])

    # Optional: Wait for user input to close the browser manually
    input("Press Enter to close the browser...")

finally:
    # Note: Removed driver.quit() to keep the browser window open
    pass
