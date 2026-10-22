import time
from mc_lab import Servo, Motor  # Standard MC Lab hardware module drivers

# Servo 2 connected to M5 port
servo_2 = Servo(port="M5")

# Motor 1 & 2 connected to Servo2 driver module at Port B and Port C
motor_b = Motor(port="B")
motor_c = Motor(port="C")

def run_hardware_diagnostics():
    print("--- Starting MC Lab Hardware Test ---")
    
    # --- 1. Test Servo 2 on Port M5 ---
    print("Testing Servo 2 (Port M5)...")
    try:
        print("  Moving Servo 2 to 0 degrees...")
        servo_2.set_angle(0)
        time.sleep(1)
        
        print("  Moving Servo 2 to 90 degrees...")
        servo_2.set_angle(90)
        time.sleep(1)
        
        print("  Moving Servo 2 to 180 degrees...")
        servo_2.set_angle(180)
        time.sleep(1)
        
        print("  Resetting Servo 2 to Center (90 deg)...")
        servo_2.set_angle(90)
        time.sleep(0.5)
        print("[SUCCESS] Servo 2 responsive.")
    except Exception as e:
        print(f"[ERROR] Servo 2 test failed: {e}")

    # --- 2. Test Motor B ---
    print("\nTesting Motor B (Port B)...")
    try:
        print("  Spinning Motor B FORWARD at 50% power...")
        motor_b.set_speed(50)
        time.sleep(2)
        
        print("  Spinning Motor B REVERSE at -50% power...")
        motor_b.set_speed(-50)
        time.sleep(2)
        
        print("  Stopping Motor B...")
        motor_b.set_speed(0)
        time.sleep(0.5)
        print("[SUCCESS] Motor B responsive.")
    except Exception as e:
        print(f"[ERROR] Motor B test failed: {e}")

    # --- 3. Test Motor C ---
    print("\nTesting Motor C (Port C)...")
    try:
        print("  Spinning Motor C FORWARD at 50% power...")
        motor_c.set_speed(50)
        time.sleep(2)
        
        print("  Spinning Motor C REVERSE at -50% power...")
        motor_c.set_speed(-50)
        time.sleep(2)
        
        print("  Stopping Motor C...")
        motor_c.set_speed(0)
        time.sleep(0.5)
        print("[SUCCESS] Motor C responsive.")
    except Exception as e:
        print(f"[ERROR] Motor C test failed: {e}")

    print("\n--- Diagnostic Test Completed Successfully ---")

if __name__ == "__main__":
    run_hardware_diagnostics()