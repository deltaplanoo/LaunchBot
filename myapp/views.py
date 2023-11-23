from django.shortcuts import render
import json

def index(request):
    # Your Python code that generates JSON data
    def generate_json_data():
        # Replace this with your actual data or method to generate JSON
        data = [
            {"name": "John", "age": 30, "city": "New York"},
            {"name": "Alice", "age": 25, "city": "San Francisco"},
            # Add more data as needed
        ]
        return data

    # Get JSON data
    json_data = generate_json_data()

    # Pass the JSON data to the template
    context = {
        'json_data': json.dumps(json_data)
    }

    return render(request, 'index.html', context)

def home(request):  # note: works fine with filter(assigned_to=request.user)
        
    return render(request, 'index.html')