from functools import wraps
import time
import random

# First, let's create our decorator factory
def retry_with_delay(max_retries=3, delay_seconds=1):
    # This is our decorator function that takes the function to be wrapped
    def decorator(func):
        # This preserves the metadata of the original function
        @wraps(func)
        # This is our wrapper that adds the retry logic
        def wrapper(*args, **kwargs):
            # Keep track of attempts
            attempts = 0
            
            # Try until we succeed or run out of retries
            while attempts < max_retries:
                try:
                    # Try to execute the function
                    result = func(*args, **kwargs)
                    print(f"✅ API call successful on attempt {attempts + 1}")
                    return result
                
                except Exception as e:
                    attempts += 1
                    if attempts == max_retries:
                        print(f"❌ Failed after {max_retries} attempts")
                        raise e
                    
                    print(f"⚠️ Attempt {attempts} failed. Retrying in {delay_seconds} seconds...")
                    time.sleep(delay_seconds)
            
        return wrapper
    return decorator

# Let's create a simulated API call that sometimes fails
def simulate_api_error():
    # Randomly succeed or fail
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("API temporarily unavailable")
    return "API response data"

# Now let's use our decorator on a function that makes API calls
@retry_with_delay(max_retries=3, delay_seconds=1)
def call_external_api():
    """This function calls an external API"""
    return simulate_api_error()

# Let's test it
def test_api_call():
    print("\nMaking API call...")
    try:
        result = call_external_api()
        print(f"Final result: {result}")
    except Exception as e:
        print(f"Final error: {str(e)}")

# Run multiple tests to see different scenarios
for i in range(3):
    print(f"\n=== Test {i+1} ===")
    test_api_call()