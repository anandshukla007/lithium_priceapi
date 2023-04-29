# price_api

# Price API

This project is a RESTful API built with Django that retrieves the latest price from a specific website.

## Getting Started

To run the Price API locally, follow the instructions below.

## API Endpoint

The API has a single endpoint:
    GET /price
## Response Format
    The response is returned in JSON format and has the following fields:
    {
    price: The latest price of Lithium-ion batteries as a float value.
    }
Example response:
    {"Current Price": "0.12"}
    
## Error Handling
    The API returns an error response with a status code of 400 for invalid requests.

### Prerequisites

- Python 3.x
- Django
- Requests
- BeautifulSoup

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/anandshukla007/lithium_priceapi.git
   
2. Change to the project directory:

   ```bash
   cd price_api

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   
4. Start the Django development server:

   ```bash
   python manage.py runserver
   
The API will be accessible at http://localhost:8000/price
