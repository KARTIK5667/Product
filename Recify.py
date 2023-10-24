import streamlit as st

def calculate_resale_value(condition, age, original_price, market_demand):
  """Calculates the resale value of a product based on the condition, age, original price, and market demand.

  Args:
    condition: The condition of the product, as a string.
    age: The age of the product, in years or months.
    original_price: The original price of the product.
    market_demand: The market demand for the product, as a string.

  Returns:
    The resale value of the product, as a float.
  """

  # Calculate the condition weight.
  condition_weight = {
    'New': 0.9,
    'Like New': 0.8,
    'Good': 0.7,
    'Fair': 0.6,
    'Poor': 0.5
  }[condition]

  # Calculate the age weight.
  age_weight = 1 - (age / 10)

  # Calculate the market demand weight.
  market_demand_weight = {
    'High': 1.1,
    'Medium': 1.0,
    'Low': 0.9
  }[market_demand]

  # Calculate the resale value.
  resale_value = original_price * condition_weight * age_weight * market_demand_weight

  return resale_value

# Create a Streamlit app.
st.title('Product Recycle Value Calculator')

# Create a form to collect the user input.
with st.form('product_info'):
  condition = st.selectbox('Condition', ['New', 'Like New', 'Good', 'Fair', 'Poor'])
  age = st.number_input('Age (years or months)', min_value=0)
  original_price = st.number_input('Original Price')
  market_demand = st.selectbox('Market Demand', ['High', 'Medium', 'Low'])

  submit_button = st.form_submit_button('Calculate')

# Calculate the resale value if the submit button is clicked.
if submit_button:
  resale_value = calculate_resale_value(condition, age, original_price, market_demand)

  # Display the resale value to the user.
  st.write('The resale value of your product is: **$', resale_value, '**')
