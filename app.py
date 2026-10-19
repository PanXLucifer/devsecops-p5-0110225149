from config import Config
from calculator import Calculator
from user_manager import UserManager
from data_processor import DataProcessor

def main():
    print(f"Menjalankan {Config.APP_NAME} v{Config.VERSION}")
    
    calc = Calculator()
    print("Hasil 5 + 3:", calc.add(5, 3))
    
    user_mgr = UserManager()
    user_mgr.register_user("admin", "admin@example.com")
    print("User terdaftar:", user_mgr.get_user("admin"))
    
    processor = DataProcessor()
    raw_data = ["  data1  ", "", "data2  "]
    print("Data bersih:", processor.clean_data(raw_data))

if __name__ == "__main__":
    main()