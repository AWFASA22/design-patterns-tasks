def calculate_daily_sales(sales_data):
    result = {}
    
    for day_index, daily_sales in enumerate(sales_data):
        day_total = 0
        valid_sales_count = 0
        
        for sale in daily_sales:
            if isinstance(sale, (int, float)) and not isinstance(sale, bool):
                day_total += sale
                valid_sales_count += 1
        
        if valid_sales_count > 0:
            day_average = day_total / valid_sales_count
        else:
            day_average = 0
        
        result[f'Day {day_index + 1}'] = {
            'total': day_total,
            'average': day_average
        }
    
    return result

# Example 
sales_data = [
    [100, 200, 'invalid', 300],  # Day 1
    [400, None, 500],            # Day 2
    [],                          # Day 3
    [600, 700, 800, 900],        # Day 4
    [1000],                      # Day 5
    ['error', 1100, 1200],       # Day 6
    [1300, 1400, 'nan']          # Day 7
]

print(calculate_daily_sales(sales_data))
