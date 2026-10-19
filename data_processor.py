class DataProcessor:
    @staticmethod
    def clean_data(data_list: list) -> list:
        return [item.strip() for item in data_list if isinstance(item, str) and item.strip()]

    @staticmethod
    def summarize(numbers: list) -> dict:
        if not numbers:
            return {"total": 0, "average": 0}
        total = sum(numbers)
        return {"total": total, "average": total / len(numbers)}